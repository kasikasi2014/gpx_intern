import web
from web import form

render = web.template.render('templates/')
db = web.database(dbn='mysql',user='root',pw='123ww213ww',db='data')

urls = ('/', 'index')
app = web.application(urls, globals())


myform = form.Form( 
    form.Textbox("stock",
	form.notnull,
	form.regexp('(\d{6}).([a-zA-Z][a-zA-Z0-9]+)', 'Must be a stockname'),
	description="stock's name like 000001.SH"),
    form.Textbox("start", 
        form.notnull,
	form.regexp('(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2})', 'Must be a timestamp'),
        description="start time like 2015-08-11 00:00:00"),
    form.Textbox("end", 
        form.notnull,
	form.regexp('(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2})', 'Must be a time'),
        description="end time like 2015-08-11 00:00:00"))

   
class index: 
    def GET(self): 
        form = myform()
        # make sure you create a copy of the form by calling it (line above)
        # Otherwise changes will appear globally
        return render.formtest(form)

    def POST(self):
	data = web.input(stock=None,start=None,end=None) 
        form = myform()
	
        if not form.validates(): 
            return render.formtest(form)
        else:
            # form.d.boe and form['boe'].value are equivalent ways of
            # extracting the validated arguments from the form.
	    todos = db.select('t_day_stock',  where="stock = $data.stock and date>=$data.start and date<=$data.end", vars=locals())
	    return render.index(todos)

if __name__=="__main__":
    web.internalerror = web.debugerror
    app.run()
