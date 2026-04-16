import calendar
from colorama import init, Fore, Back, Style
import json
import os
from datetime import datetime, date
import locale

# Init colorama
init(autoreset=True)

REMINDER_FILE = "reminders.json"
CATEGORIES = ['Work', 'Personal', 'Birthday', 'Other']

# ---------------- UTIL ----------------
def today_str():
    return date.today().strftime("%Y-%m-%d")

# ---------------- FILE ----------------
def load_reminders():
    if os.path.exists(REMINDER_FILE):
        with open(REMINDER_FILE, 'r') as f:
            try:
                return json.load(f)
            except:
                return {}
    return {}

def save_reminders(reminders):
    with open(REMINDER_FILE, 'w') as f:
        json.dump(reminders, f, indent=4)

reminders = load_reminders()

# ---------------- MIGRATE OLD DATA ----------------
changed = False
for date_key in list(reminders):
    new_entries = []
    for entry in reminders[date_key]:
        if isinstance(entry, str):
            new_entries.append({'text': entry, 'category': 'Other'})
            changed = True
        else:
            new_entries.append(entry)
    reminders[date_key] = new_entries

if changed:
    save_reminders(reminders)

# ---------------- REMINDER FUNCTIONS ----------------
def add_reminder(date_str, text, category):
    entry = {'text': text, 'category': category}
    reminders.setdefault(date_str, []).append(entry)
    save_reminders(reminders)

def view_reminders():
    if not reminders:
        print(Fore.YELLOW + "No reminders set.")
        return

    print(Fore.CYAN + "All reminders:")
    for d in sorted(reminders):
        for entry in reminders[d]:
            color = Fore.GREEN
            if d == today_str():
                color = Fore.MAGENTA + Style.BRIGHT
            print(color + f"{d} [{entry['category']}] {entry['text']}")

def view_today():
    t = today_str()
    if t in reminders:
        print(Fore.MAGENTA + Style.BRIGHT + "Today's Reminders:")
        for e in reminders[t]:
            print(f"- [{e['category']}] {e['text']}")
    else:
        print(Fore.YELLOW + "No reminders for today.")

def delete_reminder(date_str):
    if date_str not in reminders:
        print(Fore.YELLOW + "No reminders found.")
        return

    for i, e in enumerate(reminders[date_str], 1):
        print(f"{i}. [{e['category']}] {e['text']}")

    try:
        nums = sorted(map(int, input("Enter numbers to delete: ").split()), reverse=True)
        for n in nums:
            if 1 <= n <= len(reminders[date_str]):
                deleted = reminders[date_str].pop(n - 1)
                print(Fore.RED + f"Deleted: {deleted['text']}")
        if not reminders[date_str]:
            del reminders[date_str]
        save_reminders(reminders)
    except:
        print(Fore.RED + "Invalid input.")

def edit_reminder(date_str):
    if date_str not in reminders:
        print(Fore.YELLOW + "No reminders found.")
        return

    for i, e in enumerate(reminders[date_str], 1):
        print(f"{i}. [{e['category']}] {e['text']}")

    try:
        num = int(input("Enter number to edit: "))
        if 1 <= num <= len(reminders[date_str]):
            entry = reminders[date_str][num - 1]

            new_text = input(f"New text (Enter to keep '{entry['text']}'): ")
            print("Categories:", ", ".join(CATEGORIES))
            new_cat = input(f"New category (Enter to keep '{entry['category']}'): ")

            if new_text.strip():
                entry['text'] = new_text

            if new_cat.strip() and new_cat in CATEGORIES:
                entry['category'] = new_cat

            save_reminders(reminders)
            print(Fore.GREEN + "Updated.")
    except:
        print(Fore.RED + "Invalid input.")

# ---------------- CALENDAR ----------------
def show_calendar(year, month):
    cal = calendar.monthcalendar(year, month)

    print(Fore.CYAN + Style.BRIGHT + f"\n{calendar.month_name[month]} {year}")
    print(Fore.YELLOW + "Mo Tu We Th Fr Sa Su")

    today = date.today()

    for week in cal:
        line = ""
        for day in week:
            if day == 0:
                line += "   "
            else:
                d_str = f"{year}-{month:02d}-{day:02d}"

                if day == today.day and month == today.month and year == today.year:
                    line += Back.MAGENTA + Fore.WHITE + f"{day:2}" + Style.RESET_ALL + " "
                elif d_str in reminders:
                    line += Fore.GREEN + Style.BRIGHT + f"{day:2}*" + Style.RESET_ALL + " "
                else:
                    line += f"{day:2} "
        print(line)

# ---------------- CATEGORY INPUT ----------------
def prompt_category():
    print("Categories:", ", ".join(CATEGORIES))
    cat = input("Enter category: ")
    if cat not in CATEGORIES:
        print("Using 'Other'")
        return "Other"
    return cat

# ---------------- START ----------------
try:
    locale.setlocale(locale.LC_TIME, '')
except:
    pass

now = datetime.now()
print(Fore.GREEN + Style.BRIGHT + now.strftime("\nCurrent date: %A, %B %d, %Y"))
show_calendar(now.year, now.month)

# ---------------- MAIN LOOP ----------------
while True:
    print(Fore.CYAN + Style.BRIGHT + "\n=== Calendar & Reminder App ===")
    print("1. Show Calendar")
    print("2. Add Reminder")
    print("3. View All Reminders")
    print("4. View Today's Reminders")
    print("5. Delete Reminder")
    print("6. Edit Reminder")
    print("7. Exit")

    choice = input("Choose (1-7): ")

    if choice == "1":
        try:
            y = int(input("Year: "))
            m = int(input("Month: "))
            show_calendar(y, m)
        except:
            print("Invalid input.")

    elif choice == "2":
        d = input("Date (YYYY-MM-DD): ")
        text = input("Reminder: ")
        cat = prompt_category()
        add_reminder(d, text, cat)

    elif choice == "3":
        view_reminders()

    elif choice == "4":
        view_today()

    elif choice == "5":
        d = input("Date: ")
        delete_reminder(d)

    elif choice == "6":
        d = input("Date: ")
        edit_reminder(d)

    elif choice == "7":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice.")