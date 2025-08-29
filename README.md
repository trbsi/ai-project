# Docs

- [ServerManagement](./docs/ServerManagement.md)

# Local Setup

1. Install Poetry for package managing - https://python-poetry.org/docs/#installing-with-the-official-installer
2. Run `poetry install`
3. Activate virtual environment `poetry env activate`
4. Run server `poetry run python manage.py runserver`
5. Open http://127.0.0.1:8000/

# Layouts

Used - https://themewagon.com/themes/softui-tailwind/

Other - https://themewagon.com/theme-framework/tailwind-css/?swoof=1&pa_price=free&paged=1&orderby=relevance&really_curr_tax=400-pa_frameworks

# Chat GPT

https://platform.openai.com/docs/overview

Sample code

```
from openai import OpenAI

client = OpenAI(
api_key="my_key"
)

response = client.responses.create(
model="gpt-4o-mini",
input="write a haiku about ai",
store=True,
)

print(response.output_text);
```