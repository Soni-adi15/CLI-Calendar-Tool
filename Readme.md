# 📅 Smart Calendar & Reminder App (CLI)

A powerful console-based Calendar and Reminder Manager built using Python.
This application allows users to view calendars, manage reminders, and organize tasks with categories — all within the terminal.

---

## 🚀 Features

* 📆 View monthly calendar
* 🎯 Highlight current date
* 🟢 Mark reminder dates with `*`
* ➕ Add reminders with categories
* 📋 View all reminders
* 📌 View today's reminders
* ✏️ Edit existing reminders
* ❌ Delete reminders
* 💾 Persistent storage using JSON
* 🎨 Colored terminal output (using colorama)

---

## 🛠️ Tech Stack

* Python
* colorama (for colored terminal output)
* JSON (for data storage)

---

## 📂 Project Structure

```id="h7q1cw"
calendar-app/
 ├── Calendar_app.py
 └── reminders.json
```

---

## ▶️ How to Run

1. Clone the repository:

```id="6wksz8"
git clone https://github.com/Soni-adi15/CLI-Calendar-Tool.git
```

2. Navigate to the folder:

```id="ngq24f"
cd calendar-app
```

3. Install dependencies:

```id="c0cwcs"
pip install colorama
```

4. Run the app:

```id="l31ez3"
python Calendar_app.py
```

---

## 🧠 How It Works

* The app uses Python's built-in `calendar` module to display monthly calendars
* Reminders are stored in a `reminders.json` file
* Each reminder includes:

  * 📌 Date
  * 📝 Text
  * 🏷️ Category (Work, Personal, Birthday, Other)

---

## 📸 Preview

<p align = "center">   
    <img src = "Screenshots\Screenshot 2026-04-16 200751.png" width = "80%" />
</p>

---

## 💡 Future Improvements

* 🔔 Desktop notifications
* 🖥️ GUI version (Tkinter / PyQt)
* 🌐 Web version (Flask / Django)
* 🔐 User authentication system

---

## 👨‍💻 Author

Aditya Soni

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
