if __name__ == '__main__':
    import manager
    import user.views
    import file.views
    import project_test.views
    app = manager.create_app(
        blueprints=[
            user.views.bp,
            file.views.bp,
            project_test.views.bp, # 生产环境下去掉这个, 里面是一些生产测试用户和测试session是否工作的接口
        ],
        recreate_tables=True
    )
    app.run(
        host='localhost',
        port=5000
    )