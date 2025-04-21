from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo_app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class TodoDatabase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200))
    done = db.Column(db.Boolean)

@app.route("/")
def home():
    todo_list = TodoDatabase.query.all() 
    return render_template("home.html", todo_list=todo_list)

@app.route("/add", methods=["POST"])
def add():
    add_task = request.form["add_task"]
    new_task = TodoDatabase(task=add_task, done=False)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for("home"))
       
@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit(task_id):
    edit_task = db.session.get(TodoDatabase, task_id)
    if request.method == "POST":
        edit_task.task = request.form["edited_task"]
        db.session.commit()
        return redirect(url_for("home"))
    else:
        return render_template("edit.html", edit_task=edit_task, task_id=task_id)

@app.route("/check/<int:task_id>")
def check(task_id):
    check_task = db.session.get(TodoDatabase, task_id)
    check_task.done = not check_task.done
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/delete/<int:task_id>")
def delete(task_id):
    delete_task = db.session.get(TodoDatabase, task_id)
    db.session.delete(delete_task)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
