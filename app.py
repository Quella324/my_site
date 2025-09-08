from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 简单的数据存储（实际应用中应使用数据库）
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task_content = request.form['content']
    tasks.append({'content': task_content, 'complete': False})
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['complete'] = True
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
