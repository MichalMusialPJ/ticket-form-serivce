# ticket-form-serivce

Create **venv**
```bash
python3 -m venv venv
source venv/bin/activate
```


Install dependencies
```bash
pip3 install -r requirements.txt
```

Make migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

Run server

```bash
python manage.py runserver
```

Here is your form page :)

`http://127.0.0.1:8000/ticket/form/`
