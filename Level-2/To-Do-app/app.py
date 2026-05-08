from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

FILE_NAME = 'tasks.json'

# Load tasks
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return[]

# Save tasks
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)
        
# Home page
@app.route("/")
def index():
    tasks = load_tasks()
    return render_template("index.html", tasks=tasks)

# Add Tasks
@app.route("/add", methods=["POST"])
def add_task():
    task_name = request.form.get("task")
    if task_name:
        tasks = load_tasks()
        new_task = {
            "task": task_name,
            "done": False
        } 
        
        tasks.append(new_task)
        save_tasks(tasks)
        
    return redirect("/")

# Delete task
@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        save_tasks(tasks)
    return redirect("/")

# Mark done
@app.route("/done/<int:task_id>")
def mark_done(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id]["done"] = True
        save_tasks(tasks)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
