# firebase-emulator-python

Guide on how to setup firebase emulator locally using docker and how to use it with Python

Start the Docker container:

```
docker compose up -d
```

Install dependencies

```
pip install -r requirements.txt
```

Set environment variables by creating a `.env` file with the following contents

```
FIRESTORE_EMULATOR_HOST=localhost:8000
FIREBASE_AUTH_EMULATOR_HOST=localhost:9099
PUBSUB_EMULATOR_HOST=localhost:8085
```

Run `main.py` file

```
python main.py
```

Visit: http://localhost:4000/firestore/data

You should see the `users` collection with a newly created document.
