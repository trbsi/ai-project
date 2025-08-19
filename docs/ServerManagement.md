# ✅ Deploy an Existing Django Project (from Git) on Ubuntu VPS with Domain, SSL & Poetry

This guide explains how to deploy an **existing Django project from Git** on an Ubuntu VPS **from scratch**, including:

- Cloning your Git repository
- Poetry for dependency management
- Gunicorn (WSGI)
- Nginx (reverse proxy)
- Let’s Encrypt SSL
- Systemd service for auto-start

---

## **0. Prerequisites**
- Ubuntu VPS (20.04 or 22.04)
- A sudo user (non-root)
- A domain (e.g., `example.com`)
- SSH access
- Existing Django project in **GitHub/GitLab/other**

---

## **1. Point Domain to VPS**
At your domain registrar, create **A records**:

| Host | Type | Value (IP)     |
|------|------|----------------|
| @    | A    | YOUR.SERVER.IP |
| www  | A    | YOUR.SERVER.IP |

Check DNS:
```bash
dig example.com
```

---

## **2. Update Server & Install Required Packages**
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-venv python3-pip nginx git ufw
sudo apt install -y certbot python3-certbot-nginx curl
```

Enable firewall:
```bash
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw --force enable
```

---

## **3. Install Poetry**
Install Poetry:
```bash
curl -sSL https://install.python-poetry.org | python3 -
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

Verify:
```bash
poetry --version
```

---

## **4. Clone Your Django Project**
Create project directory and clone the repo:
```bash
cd /home/youruser/
git clone https://github.com/yourusername/your-django-project.git mydjangoapp
cd mydjangoapp
```

---

## **5. Install Dependencies with Poetry**
Configure Poetry to create venv inside the project:
```bash
poetry config virtualenvs.in-project true
```

Install dependencies from `pyproject.toml`:
```bash
poetry install --no-dev
```

Activate the virtual environment:
```bash
poetry shell
```

---

## **6. Django Setup**
Apply migrations and collect static files:
```bash
poetry run python manage.py migrate
poetry run python manage.py collectstatic --noinput
```

Test locally (optional):
```bash
poetry run python manage.py runserver 0.0.0.0:8000
```

Edit `settings.py`:
```python
ALLOWED_HOSTS = ['example.com', 'www.example.com']
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'
```

---

## **7. Create Gunicorn Systemd Service**
Create `/etc/systemd/system/mydjangoapp.service`:
```ini
[Unit]
Description=Gunicorn instance to serve Django app
After=network.target

[Service]
User=youruser
Group=www-data
WorkingDirectory=/home/youruser/mydjangoapp
ExecStart=/home/youruser/mydjangoapp/.venv/bin/gunicorn --workers 3 --bind 127.0.0.1:8000 myproject.wsgi:application
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable & start service:
```bash
sudo systemctl daemon-reload
sudo systemctl enable mydjangoapp
sudo systemctl start mydjangoapp
```

Check status:
```bash
sudo systemctl status mydjangoapp
```

---

## **8. Configure Nginx**
Create `/etc/nginx/sites-available/mydjangoapp`:
```nginx
server {
    listen 80;
    server_name example.com www.example.com;

    location /static/ {
        alias /home/youruser/mydjangoapp/static/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Enable site:
```bash
sudo ln -s /etc/nginx/sites-available/mydjangoapp /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

---

## **9. Enable HTTPS with Let’s Encrypt**
Install SSL:
```bash
sudo certbot --nginx -d example.com -d www.example.com
```

Auto-renew check:
```bash
sudo certbot renew --dry-run
```

---

## **10. Deployment Workflow (Updating Code from Git)**
When pushing new updates:
```bash
cd /home/youruser/mydjangoapp
git pull
poetry install --no-dev
poetry run python manage.py migrate
poetry run python manage.py collectstatic --noinput
sudo systemctl restart mydjangoapp
```

---

## **11. Troubleshooting**
- **502 Bad Gateway** → check `sudo systemctl status mydjangoapp`
- **Static files missing** → run `poetry run python manage.py collectstatic`
- **Permission issues** → ensure files are readable by `www-data`
- **Renew SSL manually** → `sudo certbot renew`

---

### ✅ Done!
Your Django app from **Git repository** is now:
- Running on **Gunicorn**
- Behind **Nginx**
- Managed with **Poetry**
- Served via **HTTPS (Let’s Encrypt)**
- Auto-started with **systemd**
