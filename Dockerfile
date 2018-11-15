FROM python:3.6
WORKDIR /edx/app/messaging/messaging
ADD requirements.txt /edx/app/messaging/messaging
ADD requirements /edx/app/messaging/messaging/requirements
ADD Makefile /edx/app/messaging/messaging
WORKDIR /edx/app/messaging/messaging
RUN make requirements
ADD . /edx/app/messaging/messaging
EXPOSE 8765
