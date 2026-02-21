# Django hello skeleton

This repository contains a minimal Django project and a `hello` app with two pages:

- `/` -> "hello, world"
- `/hello/{user}/` -> "hello, {user}"

Environment setup (Windows - venv)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

If you'd like to use the `uv` Python package manager instead of `venv`, replace the virtualenv and `pip install` steps with your `uv` workflow. I'm happy to update these instructions with exact `uv` commands if you tell me which `uv` variant/version you use.
