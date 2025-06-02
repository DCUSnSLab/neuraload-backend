neuraload-backend/
├── manage.py
├── requirements.txt
├── .env
├── neuraload/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── __init__.py
│   ├── users/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   └── urls.py
│   ├── devices/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   └── urls.py
│   ├── trips/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   └── urls.py
│   └── sensors/
│       ├── __init__.py
│       ├── models.py
│       ├── views.py
│       ├── serializers.py
│       └── urls.py
└── utils/
    ├── __init__.py
    ├── response.py
    └── permissions.py
