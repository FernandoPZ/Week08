import web

urls = (
    '/', 'page.controllers.index.Index',
    '/list', 'page.controllers.list.List',
    '/insert', 'page.controllers.insert.Insert',
    '/delete', 'page.controllers.delete.Delete',
    '/view', 'page.controllers.view.View',
    '/update', 'page.controllers.update.Update',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
