release: export BOKEH_SECRET_KEY=dp4UM8aLpYIgxkai7GQF8J6IYWNLNZGM2bwZHpQcK5LJ
release: export BOKEH_SIGN_SESSIONS=True
web: bokeh serve --address="0.0.0.0" --port=$PORT iris_kmeans.py --allow-websocket-origin=heroku-panel-test.herokuapp.com --session-ids external-signed
