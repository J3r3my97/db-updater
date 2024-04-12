# db-updater
helloworld for db-updater app


# Env vars for app
export PROJECT_ID=calcium-backup-338422

export APP=db-updater

export PORT=1234

export REGION="us-central1"

export TAG="gcr.io/$PROJECT_ID/$APP"

# Set Default Project (all later commands will use it) 
gcloud config set project $PROJECT_ID

# Create and push docker image
docker build -t $TAG .
gcloud builds submit --tag $TAG

# Spin up locally
open docker app in the background and run in terminal

"docker run -dp $PORT:$PORT -e PORT=$PORT $TAG"

uvicorn main:app --reload