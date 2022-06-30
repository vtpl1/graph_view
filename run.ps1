# gunicorn -k eventlet 'graph_view:create_app()'

$env:FLASK_APP = "graph_view:main"
$env:FLASK_ENV = "development"
flask run