# 🔐 Flask GitHub OAuth 2.0 Authentication

This project demonstrates how to implement GitHub OAuth 2.0 login in a Flask web application using the Flask-Dance library.

---

## 📘 Table of Contents

1. [What is OAuth 2.0?](#what-is-oauth-20)
2. [Project Overview](#project-overview)
3. [Prerequisites](#prerequisites)
4. [Step-by-Step Guide](#step-by-step-guide)
    - [1. Create GitHub OAuth App](#1-create-github-oauth-app)
    - [2. Clone the Project](#2-clone-the-project)
    - [3. Set Environment Variables](#3-set-environment-variables)
    - [4. Install Dependencies](#4-install-dependencies)
    - [5. Run the Application](#5-run-the-application)
5. [Folder Structure](#folder-structure)

---

## 🤔 What is OAuth 2.0?

OAuth 2.0 is a secure authorization framework that allows third-party applications to access user resources without exposing their credentials (like passwords). 

In this project:
- The user logs in using their **GitHub account**.
- The app gets authorized to access **basic profile information** like username and avatar.
- The app does **not** access any sensitive data or password.

---

## 🚀 Project Overview

We use:
- [Flask](https://flask.palletsprojects.com/)
- [Flask-Dance](https://flask-dance.readthedocs.io/) for handling OAuth 2.0
- GitHub as the OAuth Provider

After login, the app displays:
- GitHub username
- Profile image
- Link to GitHub profile

---

## 🧰 Prerequisites

- Python 3.7+
- GitHub account

---

## 🛠 Step-by-Step Guide

### ✅ 1. Create GitHub OAuth App

1. Go to: https://github.com/settings/developers
2. Click **"OAuth Apps"** → **"New OAuth App"**
3. Fill in:
    - **Application Name**: `Flask GitHub OAuth Demo`
    - **Homepage URL**: `http://localhost:5000`
    - **Authorization Callback URL**: `http://localhost:5000/login/github/authorized`
4. Save, and copy:
    - `Client ID`
    - `Client Secret`

---

### ✅ 2. Clone the Project

```bash
git clone https://github.com/yourusername/flask-github-oauth.git
cd flask-github-oauth
```

---

### ✅ 3. Set Environment Variables

Create a `.env` file in the root of the project:

```
FLASK_SECRET_KEY=your_secret_key
GITHUB_OAUTH_CLIENT_ID=your_client_id
GITHUB_OAUTH_CLIENT_SECRET=your_client_secret
```

---

### ✅ 4. Install Dependencies

Use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate

pip install -r requirements.txt
```

If you don’t have `requirements.txt`, install manually:

```bash
pip install Flask Flask-Dance python-dotenv
```

---

### ✅ 5. Run the Application

```bash
flask run
```

Visit: [http://localhost:5000](http://localhost:5000)

---

## 🗂 Folder Structure

```
flask-github-oauth/
│
├── app.py                 # Main Flask application
├── .env                  # Environment variables (not tracked by Git)
├── templates/
│   ├── home.html         # Home page template with login button
│   └── profile.html      # User profile page after login
├── venv/                 # Virtual environment (optional)
└── README.md             # Project documentation
```
