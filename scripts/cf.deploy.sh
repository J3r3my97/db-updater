#!/usr/bin/env bash
set -e
# Set the project ID and region
read -e -n 1 -p "Continue? [Y/n] " confirm
confirm=${confirm:-N}
if [[ $confirm =~ ^[Yy]$ ]]; then
    echo "Starting deployment..."
    PROJECT_ID="calcium-backup-338422"
    REGION="us-central1"

    # Deploy the Cloud Function
    gcloud functions deploy data_loader \
        --project=$PROJECT_ID \
        --region=$REGION \
        --runtime=python39 \
        --trigger-topic=trigger_data_load \
        --memory=256MB \
        --entry-point=handle_triggering_events \
        --max-instances=1 \

else
    echo "Exiting..."
    exit 1
fi