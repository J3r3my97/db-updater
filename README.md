# db-updater
helloworld for db-updater app



# Spin up locally

cd src
uvicorn main:app --reload

# In a seperate terminal
 ./cloud-sql-proxy calcium-backup-338422:us-central1:dental-analytic-db

 # In Web browser
http://127.0.0.1:8000/docs#