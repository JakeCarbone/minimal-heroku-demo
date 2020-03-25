release: export BOKEH_SECRET_KEY=iFObNc3skYa6qZJSjutYrwRHNmM7uxuok4IYiBZNS9nk
release: export BOKEH_SIGN_SESSIONS=yes
web: BOKEH_SIGN_SESSIONS=yes bokeh serve --address="0.0.0.0" --port=$PORT iris_kmeans.py --allow-websocket-origin=heroku-panel-test.herokuapp.com --session-ids external-signed
