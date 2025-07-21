import json
import os

FILE_NAME = "todo.json"

# ==================== Logic ====================
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, encoding="utf-8") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)

def show_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📝 Danh sách trống.")
    for i, task in enumerate(tasks):
        status = "✔" if task["done"] else "✘"
        print(f"{i + 1}. [{status}] {task['title']}")

def mark_done(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        del tasks[index]
        save_tasks(tasks)

# ==================== CLI (Giao diện dòng lệnh) ====================
def menu():
    while True:
        print("\n--- TO DO APP ---")
        print("1. Hiển thị danh sách")
        print("2. Thêm công việc")
        print("3. Đánh dấu hoàn thành")
        print("4. Xoá công việc")
        print("5. Thoát")
        choice = input("Chọn: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            title = input("Nhập công việc: ")
            add_task(title)
            print("✅ Đã thêm.")
        elif choice == "3":
            show_tasks()
            idx = int(input("Chọn số thứ tự cần đánh dấu: ")) - 1
            mark_done(idx)
            print("✔ Đã đánh dấu.")
        elif choice == "4":
            show_tasks()
            idx = int(input("Chọn số thứ tự cần xoá: ")) - 1
            delete_task(idx)
            print("🗑️ Đã xoá.")
        elif choice == "5":
            break
        else:
            print("⚠️ Lựa chọn không hợp lệ.")

menu()
