from datetime import datetime
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    time = db.Column(db.DateTime, default=datetime.utcnow)


def __repr__(self) -> str:
    return f'{self.sno} - {self.title}'


@app.route('/' ,methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        title = (request.form['title'])
        description = (request.form['description'])
        todo = Todo(title= title, description= description)
        db.session.add(todo)
        db.session.commit()
        
    allTodo = Todo.query.all()
    return render_template('index.html',allTodo = allTodo)

@app.route('/delete/<int:sno>')
def delete(sno):
    ToDelete = Todo.query.filter_by(sno = sno).first()
    db.session.delete(ToDelete)
    db.session.commit()
    return redirect('/')


@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method == 'POST':
        ToUpdate = Todo.query.filter_by(sno=sno).first()
        title = request.form['title']
        description = request.form['description']
        ToUpdate.title = title
        ToUpdate.description = description
        db.session.commit()
        return redirect('/')
    ToUpdate = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', ToUpdate=ToUpdate)


if __name__ == '__main__':
    app.run(debug=True)
 