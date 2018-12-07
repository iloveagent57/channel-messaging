from django.conf.urls import url

from . import consumers


COURSE_KEY_PATTERN = r'(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)'
COURSE_ID_PATTERN = COURSE_KEY_PATTERN.replace('course_key_string', 'course_id')

websocket_urlpatterns = [
    url(r'^ws/gradebook/{course_id}/$'.format(course_id=COURSE_ID_PATTERN), consumers.GradebookConsumer),
]
