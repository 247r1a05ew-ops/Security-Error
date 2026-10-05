# Intentional demonstration security issue.
# Never use real credentials like this.

API_KEY = "DEMO_SECRET_12345"


def get_status():
    return "API configured"


print(get_status())
