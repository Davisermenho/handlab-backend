import importlib

modules = ['app.main','app.models','app.schemas','config.config']
for m in modules:
    try:
        importlib.import_module(m)
        print(m, 'OK')
    except Exception as e:
        print(m, 'ERROR', e)
