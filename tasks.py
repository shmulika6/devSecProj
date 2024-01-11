from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


tasks = [
    
]

counter = 0


@app.route('/')
def index():
    return render_template('index_tasks.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    global counter 
    counter = counter + 1
    new_task = {
        'id': counter,
        'title': request.form['title'],
        'completed': False
    }
    tasks.append(new_task)
    return redirect(url_for('index'))

@app.route('/complete_task/<int:task_id>')
def complete_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        task['completed'] = True
    return redirect(url_for('index'))

@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)