# annotation-server
Annotation tool server prototype

Related **front-end:** https://github.com/Amsterdam/stadsarchief-annotation-tool

## Class diagram
![Model class diagram](doc/class_diagram.png?raw=true "Model class diagram")

## Install

```
pip install -r requirements.txt
```

## Start

```docker-compose up database```

Start the Django server
```python manage.py runserver```


## Imports

Run all import from the project root:

* `PYTHONPATH=. python import_lib/stadsarchief/import_sa_aanvraag.py import_lib/stadsarchief/data/.../...csv`, 
don't forget to set the `IIIF_API_ROOT` env variable. The CSV files themselves are not in this repo.
