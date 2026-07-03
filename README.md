# CHECK • LIST ☑

A full-stack task management web app built with Python, Flask, and SQLite. Users can register, log in, manage their personal checklist, and track their progress in real time — all wrapped in a clean dark-themed UI.

---

## 🚀 Features

- **Secure Authentication** — Register and login with bcrypt password hashing
- **Password Complexity Rules** — Must contain uppercase, number, and symbol
- **Persistent Storage** — Tasks and users saved to SQLite database
- **Personal Checklist** — Add, complete, and delete tasks
- **Real-time Progress Ring** — Updates without page refresh using Fetch API
- **Task Summary** — Live count of total, completed, and remaining tasks
- **Session Protection** — Dashboard only accessible when logged in
- **Account Management** — Delete account and all associated tasks
- **Dark UI** — Clean glassmorphism design with Clash Grotesk typography

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Database | SQLite |
| Authentication | bcrypt, Flask Sessions |
| Frontend | HTML, CSS, JavaScript |
| API Communication | Fetch API |
| Font | Clash Grotesk (Fontshare) |

---

## 📁 Project Structure

```
python-login-system/
├── app.py              ← Flask app and all routes
├── database.py         ← All SQLite database functions
├── requirements.txt    ← Python dependencies
├── .env                ← Secret key (not pushed to GitHub)
├── .gitignore
├── templates/
│   ├── Login.html
│   ├── Signup.html
│   └── dashboard.html
└── static/
    ├── Styling/
    │   ├── style.css
    │   └── dashboard.css
    └── img/
```

---

## ⚙️ Installation & Setup

**1. Clone the repository**
```bash
git clone https://github.com/godwink12/python-login-system.git
cd python-login-system
```

**2. Create a virtual environment**
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Create your `.env` file**
```
SECRET_KEY=your_secret_key_here
```

**5. Run the app**
```bash
python app.py
```

**6. Open in browser**
```
http://127.0.0.1:5000
```

---

## 🔐 Password Requirements

When registering, passwords must:
- Be at least 6 characters long
- Contain at least one uppercase letter
- Contain at least one number
- Contain at least one symbol

---

## 📸 Pages

| Page | Route | Description |
|---|---|---|
| Login | `/` | Landing page with login form |
| Register | `/register` | Create a new account |
| Dashboard | `/dashboard` | Personal checklist and progress |
| Logout | `/logout` | Clears session and redirects |
| Delete Account | `/delete_account` | Removes user and all tasks |

---

## 🗄️ Database Tables

**users**
| Column | Type | Description |
|---|---|---|
| username | TEXT | Unique username |
| password | TEXT | bcrypt hashed password |

**tasks**
| Column | Type | Description |
|---|---|---|
| id | INTEGER | Auto-increment primary key |
| username | TEXT | Owner of the task |
| task | TEXT | Task description |
| done | INTEGER | 0 = pending, 1 = completed |

---

## 📚 What I Learned

This project was a full learning journey covering:

- Flask routes, sessions, and templates
- Jinja2 templating for dynamic HTML
- SQLite database design and queries
- bcrypt password hashing and security
- Fetch API for real-time UI updates without page refresh
- Git version control and GitHub deployment
- Virtual environments and dependency management

---

## 👤 Author

**Godwin Kadima**
- GitHub: [@godwink12](https://github.com/godwink12)

---

> *Built as a learning project — every bug was a lesson.* 💪
