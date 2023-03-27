#flaskr/__init__.py

import os
from flask import Flask

def create_app(test_config=None):
    #creating and configuring the app 
    app= Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        secret_key='carl',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    if test_config is None:
        #load instance config, if it exist, when not testing
        app.config.from_pyfile('hello.py', silent=True)
    else:
            #load test config if passed in
            app.config.from_mapping(test_config)

        #ensure the instance folder exist
    try:
        os.makedirs(app.instance_path) 
    except OSError:
        pass
    @app.route('/')
    def hello():
        return 'hello carline'
    app.run()   
