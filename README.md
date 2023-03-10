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

Run `main.py` file

```
python main.py
```

Visit: http://localhost:4000/firestore/data

You should see the `users` collection with a newly created document.
