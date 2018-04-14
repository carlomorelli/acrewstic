from flask import Flask, jsonify, abort, request, make_response
from repository import Repository

app = Flask(__name__)

repository = Repository(host='localhost', port=6379)


"""
Starting collection
"""
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

"""
Rest implementations
"""


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/acrewstic/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/acrewstic/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


@app.route('/acrewstic/tasks', methods=['POST'])
def create_task():
    if not request.json() or 'title' not in request.json():
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json()['title'],
        'description': request.json().get('description', default=''),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


@app.route('/acrewstic/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json():
        abort(400)
    if 'title' in request.json():
        if type(request.json()['title']) is not str:
            abort(400)
    if 'description' in request.json():
        if type(request.json()['description']) is not str:
            abort(400)
    if 'done' in request.json():
        if type(request.json()['done']) is not bool:
            abort(400)
    task[0]['title'] = request.json().get('title', default=task[0]['title'])
    task[0]['description'] = request.json().get('description', default=task[0]['description'])
    task[0]['done'] = request.json().get('done', default=task[0]['done'])
    return jsonify({'task': task[0]})


@app.route('/acrewstic/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})


@app.route('/acrewstic/version', methods=['GET'])
def get_version():
    app_info = {
        'name': 'Acrewstic',
        'version': '0.1'
    }
    flask_info = {
        'version': '0.11.1'
    }
    try:
        redis_info = repository.info()
    except:
        redis_info = '<<<Unable to connect to database>>>'
    return jsonify({
        'app_info': app_info,
        'flask_info': flask_info,
        'redis_info': redis_info
    })


"""
Main loop
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
