"""
This module defines the HTTP endpoint that a server can route messages to.
That endpoint is then in charge of sending data along to channel groups.
"""
import json

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.http import HttpResponse
from django.shortcuts import render

from .consumers import group_name


CHANNEL_LAYER = get_channel_layer()


def group_send(group_name, message):
    async_to_sync(CHANNEL_LAYER.group_send)(group_name, message)


def task_completed(request, course_id):
    """
    You can set up a websocket client as follows, to check that a GET request
    against this endpoint triggers a message being sent to the client.
    In devtools, open up the console and do:
    var socket = new WebSocket('ws://localhost:8765/ws/gradebook/course-v1:edX+DemoX+Demo_Course/');
    socket.onmessage = function(event) {var data = JSON.parse(event.data); var msg = data['message']; console.log(msg);};

    In a diferent browser tab, make a request to 'http://localhost:8765/gradebook/task_completed/course-v1:edX+DemoX+Demo_Course/'
    You should see 'foobar' logged to the console in your websocket client tab.
    """
    data = json.loads(request.body)
    data['type'] = 'task_message'
    group_send(group_name(course_id), data)
    return HttpResponse(content='ok')
