from flask import Flask, render_template
from flask_socketio import SocketIO
from threading import Lock
import boto3
from kafka import KafkaConsumer
import json
import sys

async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

if len(sys.argv) > 1:
    topic_name = sys.argv[1]
else:
    raise ValueError("need param for topic name")


BootStrap_Servers = [
    'b-3.demo-cluster-1.9z77lu.c4.kafka.cn-northwest-1.amazonaws.com.cn:9092',
    'b-1.demo-cluster-1.9z77lu.c4.kafka.cn-northwest-1.amazonaws.com.cn:9092',
    'b-2.demo-cluster-1.9z77lu.c4.kafka.cn-northwest-1.amazonaws.com.cn:9092'
]


def background_thread():
    print(f"begin read {topic_name}")
    consumer = KafkaConsumer(topic_name, bootstrap_servers=BootStrap_Servers)

    for record in consumer:
        data = record[6]
        print(data)
        record_data_str = data.decode("utf-8")
        # print(record_data_str)
        t = json.loads(record_data_str)
        socketio.emit('push', t)


@socketio.on('connect')
def handle_my_custom_event(json):
    print('received json: ' + str(json))
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)


@app.route("/js")
def js():
    return render_template('socket.io.js')


@app.route("/")
def hello():
    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=8086)
