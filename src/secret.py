import json

import google.cloud.secretmanager as secretmanager

# Create a Secret Manager client
client = secretmanager.SecretManagerServiceClient()


def get_secret(project_id, secret_id, version="latest"):
    name = client.secret_version_path(project_id, secret_id, version)
    response = client.access_secret_version(name=name)
    secret_payload = json.loads(response.payload.data.decode("UTF-8"))
    return secret_payload
