Certainly! To set up a RabbitMQ queue that delivers messages from one pod to another in Kubernetes, you'll need to create a RabbitMQ deployment, services for communication, and deploy two pods as message producers and consumers. Below is a basic example using YAML manifests.

RabbitMQ Deployment YAML (rabbitmq-deployment.yaml):
yaml
 
apiVersion: apps/v1
kind: Deployment
metadata:
  name: rabbitmq
spec:
  replicas: 1
  selector:
    matchLabels:
      app: rabbitmq
  template:
    metadata:
      labels:
        app: rabbitmq
    spec:
      containers:
        - name: rabbitmq
          image: rabbitmq:3.8
          ports:
            - containerPort: 5672  # RabbitMQ default port
---
apiVersion: v1
kind: Service
metadata:
  name: rabbitmq-service
spec:
  selector:
    app: rabbitmq
  ports:
    - protocol: TCP
      port: 5672
      targetPort: 5672
Producer Pod YAML (producer-pod.yaml):
yaml
 
apiVersion: v1
kind: Pod
metadata:
  name: producer-pod
spec:
  containers:
    - name: producer-container
      image: your-producer-image:tag  # Replace with your actual producer image
      env:
        - name: RABBITMQ_HOST
          value: "rabbitmq-service"
Consumer Pod YAML (consumer-pod.yaml):
yaml
 
apiVersion: v1
kind: Pod
metadata:
  name: consumer-pod
spec:
  containers:
    - name: consumer-container
      image: your-consumer-image:tag  # Replace with your actual consumer image
      env:
        - name: RABBITMQ_HOST
          value: "rabbitmq-service"
In the producer and consumer applications, you need to use the RabbitMQ connection details provided in the RABBITMQ_HOST environment variable.

Here is a basic Python example for a producer and consumer using the pika library:

Python Producer Example:
python
 
# producer.py
import pika
import os

connection = pika.BlockingConnection(pika.ConnectionParameters(host=os.environ["RABBITMQ_HOST"]))
channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello, RabbitMQ!')

print(" [x] Sent 'Hello, RabbitMQ!'")

connection.close()
Python Consumer Example:
python
 
# consumer.py
import pika
import os

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

connection = pika.BlockingConnection(pika.ConnectionParameters(host=os.environ["RABBITMQ_HOST"]))
channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True)

print(" [*] Waiting for messages. To exit, press Ctrl+C")
channel.start_consuming()
Remember to replace the placeholder your-producer-image:tag and your-consumer-image:tag with the actual names and versions of your Docker images.

Note: This is a basic setup, and for production use, you might need to consider security, persistence, and other configuration options based on your requirements.