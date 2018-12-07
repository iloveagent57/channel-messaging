import json
import logging

from asgiref.sync import async_to_sync as _sync
from channels.generic.websocket import WebsocketConsumer


log = logging.getLogger(__name__)


def group_name(course_id):
    cleaned_course_id = course_id.replace(':', '--').replace('+', '--').replace('_', '--')
    return 'gradebook_group_{}'.format(cleaned_course_id)


class GradebookConsumer(WebsocketConsumer):
    def connect(self):
        self.course_id = self.scope['url_route']['kwargs']['course_id']
        self.course_id_group = group_name(self.course_id)

        _sync(self.channel_layer.group_add)(
            self.course_id_group,
            self.channel_name,
        )

        self.accept()

    def disconnect(self, close_code):
        _sync(self.channel_layer.group_discard)(
            self.course_id_group,
            self.channel_name,
        )

    def task_message(self, event):
        self.send(text_data=json.dumps(event))
