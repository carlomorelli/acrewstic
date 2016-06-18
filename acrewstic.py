from flask import Flask, jsonify, abort, request, make_response
from redis import StrictRedis

app = Flask(__name__)
redis = StrictRedis(host='redis', port=6379)

# store dictionary
#    redis.hmset(hkey, dict_to_store)
# retrieve dictionary
#    redis.hmget(hkey)
# lists
#    redis.lappend(hkey, string)
#    redis.llen


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
    if not request.get_json() or 'title' not in request.get_json():
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.get_json()['title'],
        'description': request.get_json().get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


@app.route('/acrewstic/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.get_json():
        abort(400)
    if 'title' in request.get_json():
        if type(request.get_json()['title']) is not unicode:
            abort(400)
    if 'description' in request.get_json():
        if type(request.get_json()['description']) is not unicode:
            abort(400)
    if 'done' in request.get_json():
        if type(request.get_json()['done']) is not bool:
            abort(400)
    task[0]['title'] = request.get_json().get('title', task[0]['title'])
    task[0]['description'] = request.get_json().get(
        'description', task[0]['description'])
    task[0]['done'] = request.get_json().get('done', task[0]['done'])
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
        redis_info = redis.info()
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
