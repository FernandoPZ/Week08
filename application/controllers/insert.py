import web 

render=web.template.render('page/views/')

class Insert():
    def GET(self):
      try:
        return render.insert()
      except Exception as e:
        return "--E-R-R-R-R--" + str(e.args)
