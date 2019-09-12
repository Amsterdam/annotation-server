# annotation-server
Annotation tool server prototype

## Class diagram
![Model class diagram](doc/class_diagram.png?raw=true "Model class diagram")

## Imports

Run all import from the project root:

* `PYTHONPATH=. python import_lib/stadsarchief/import_sa_aanvraag.py import_lib/stadsarchief/data/.../...csv`, 
don't forget to set the `IIIF_API_ROOT` env variable. The CSV files themselves are not in this repo.
