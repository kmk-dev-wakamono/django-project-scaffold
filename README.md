# Django hello skeleton

## 環境構築について

必要なもの

- Python (>= 3.13.2)

### Python

Python の実行環境のインストールについては、scoopやchocolateyなどのパッケージマネージャを利用するか、PythonのホームページからPythonの実行可能ファイルをダウンロード・インストールしてください。

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

