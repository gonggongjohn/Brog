from flask import Flask


if __name__ == '__main__':
    import manager
    import user.views
    import read.views
    app = manager.create_app(
        blueprints=[
            user.views.bp,
            read.views.bp
        ],
        recreate_tables=True
    )    
    app.run(
        host='localhost',
        port=5000
    )