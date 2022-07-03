# gunicorn -k eventlet 'graph_view:create_app()'

$env:FLASK_APP = "graph_view"
$env:FLASK_ENV = "development"
flask run
# flask init-db
# pytest
# coverage run -m pytest
# coverage report -m
# pip install -e .
# python setup.py bdist_wheel
# waitress-serve --call 'graph_view:create_app'