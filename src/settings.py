import os

ADMIN_LOGIN = 'admin'
ADMIN_PASSWORD = 'admin'

RABBITMQ_HOST = 'rabbitmq_node_1' if 'FROM_DOCKER_COMPOSE' in os.environ else 'localhost'

FIRST_NODE_PORT = 5670
FIRST_NODE_URL = f'amqp://{ADMIN_LOGIN}:{ADMIN_PASSWORD}@{RABBITMQ_HOST}:{FIRST_NODE_PORT}'

# LOAD_BALANCER_HOST = 'haproxy' if 'FROM_DOCKER_COMPOSE' in os.environ else 'localhost'
# LOAD_BALANCER_PORT = 8000
