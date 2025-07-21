import json
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("TO DO APP")
root.geometry("600x700")
root.configure(bg="#93d5d9")  # nền dịu mắt

# 🎨 Style dịu mắt + bo góc
style = ttk.Style()
style.theme_use("clam")

# Màu chính
main_color = "#dbc0e0"   # xanh pastel dịu
hover_color = "#93d5d9"
text_color = "#333"
bg_color = "#93d5d9"

# Nút
style.configure("Rounded.TButton",
                font=("Segoe UI", 11),
                padding=6,
                relief="flat",
                background=main_color,
                foreground=text_color,
                borderwidth=0)
style.map("Rounded.TButton",
          background=[("active", hover_color)])

# Checkbox
style.configure("TCheckbutton",
                background=bg_color,
                font=("Segoe UI", 11),
                foreground=text_color,
                focuscolor=bg_color)

# Entry
style.configure("TEntry",
                font=("Segoe UI", 11),
                padding=6,
                relief="flat")

# Label
style.configure("TLabel",
                font=("Segoe UI", 13),
                background=bg_color,
                foreground=text_color)

frame_task = ttk.Frame(root, style="TFrame")
frame_task.grid(row=1, column=0, padx=10, sticky="w")

check_vars = []

def save(files,need_save):
    with open(files,"w", encoding="utf-8") as f:
        json.dump(need_save, f, indent=2, ensure_ascii= False)


def get_list():
    try:
        with open("todo.json", encoding="utf-8") as file:
            task = json.load(file)
    except:
        task = []
    return task

def show(tasks):
    for widget in frame_task.winfo_children():
        widget.destroy()
    check_vars.clear()
    for index, i in enumerate(tasks):
        var = tk.IntVar(value=i["done"])
        check_vars.append(var)
        ttk.Checkbutton(frame_task, text=i["title"], variable=var, style="TCheckbutton").grid(row=index, column=0, sticky="w", pady=2)

def write_file_and_check(mission):
    danh_sach = get_list()
    for index, i in enumerate(danh_sach):
        i["done"] = bool(check_vars[index].get())
    if mission.strip() != "":
        new = {"title": mission.strip(), "done": False}
        danh_sach.append(new)
    save("todo.json",danh_sach)
    show(danh_sach)

def set_up_delete(tasks):
    global part_time_vars
    part_time_vars = []
    for widget in frame_task.winfo_children():
        widget.destroy()
    for index, i in enumerate(tasks):
        var = tk.IntVar()
        part_time_vars.append(var)
        ttk.Checkbutton(frame_task, text=i["title"], variable=var, style="TCheckbutton").grid(row=index, column=0, sticky="w", pady=2)
    ttk.Button(frame_task, text="Xác nhận xóa", style="Rounded.TButton", command=lambda: delete(tasks)).grid(row=len(tasks)+1, column=0, pady=10)

def delete(tasks):
    new_tasks = [i for index, i in enumerate(tasks) if part_time_vars[index].get() == 0]
    for widget in frame_task.winfo_children():
        widget.destroy()
    save("todo.json",new_tasks)
    show(new_tasks)

def start():
    ttk.Label(root, text="Đây là todo list của bạn:").grid(row=0, column=0, pady=10)
    user_inp = ttk.Entry(root, width=40)
    user_inp.grid(row=3, column=0, pady=10)

    button_frame = ttk.Frame(root, style="TFrame")
    button_frame.grid(row=2, column=0, pady=10)

    ttk.Button(button_frame, text="Lưu thay đổi", style="Rounded.TButton", command=lambda: write_file_and_check(user_inp.get())).grid(row=0, column=0, padx=5)
    ttk.Button(button_frame, text="Xóa công việc", style="Rounded.TButton", command=lambda: set_up_delete(get_list())).grid(row=0, column=1, padx=5)

    show(get_list())

start()
root.mainloop()
