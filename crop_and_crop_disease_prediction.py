from flask import Flask,render_template,request,redirect,session
from DBConnection import Db
import random

app = Flask(__name__)
app.secret_key="789"
@app.route('/adminhome')
def adminhome():
    return render_template("admin/index.html")
@app.route('/weatherhome')
def weatherhome():
    return render_template("weather/index.html")



@app.route('/')
def abc():
    return render_template("index.html")

@app.route('/login',methods=['get','post'])
def login():
    if request.method=="POST":
        username=request.form['textfield']
        password=request.form['textfield2']
        db=Db()
        res=db.selectOne("select * from login where user_name='"+username+"'and password='"+password+"' ")
        if res is not None:
            if res['user_type']=='admin':
                session['lg']="lo"
                return redirect('/adminhome')
            elif res['user_type']=='weather':
                session['lid']=res['login_id']
                session['lg'] = "lo"
                return redirect('/weatherhome')
            else:
                return "invalid user"
        else:
            return "user not exsist"
    else:
        return render_template("LOGIN.html")


@app.route('/add_weather',methods=['get','post'])
def add_weather():
    if session['lg']=="lo":
        if request.method=="POST":
            name=request.form['textfield1']
            email=request.form['textfield2']
            phone=request.form['textfield3']
            ps=random.randint(0000,9999)
            db=Db()
            res=db.insert("insert into login values ('','"+email+"','"+str(ps)+"','weather')")
            db.insert("insert into weather_dept values ('"+str(res)+"','"+name+"','"+email+"','"+phone+"')")
            return '''<script>alert('success');window.location='/adminhome'</script>'''
        else:
            return render_template('admin/Add weather.html')
    else:
        return redirect('/')


@app.route('/AO_management',methods=['get','post'])
def AO_management():
    if session['lg'] == "lo":
         if request.method=="POST":
            name=request.form['textfield1']
            email=request.form['textfield2']
            phone=request.form['textfield3']
            db = Db()
            db.insert("insert into agriculture_office VALUES ('','"+name+"','"+email+"','"+phone+"')")

            return '''<script>alert('success');window.location='/adminhome'</script>'''
         else:


            return render_template('admin/AO Management.html')
    else:
        return redirect('/')

@app.route('/crop_management',methods=['get','post'])
def crop_management():
    if session['lg'] == "lo":
        if request.method=="POST":
            name=request.form['textfield']
            rate=request.form['textfield1']
            db=Db()
            db.insert("insert into crop VALUES ('','"+name+"','"+rate+"')")
            return '''<script>alert('success');window.location='/adminhome'</script>'''
        else:

            return render_template('admin/crop management.html')
    else:
        return redirect('/')

@app.route('/farmer',methods=['get','post'])
def farmer():
    if session['lg'] == "lo":
        if request.method=="POST":
            name=request.form['textfield']
            email=request.form['textfield1']
            phone=request.form['textfield2']
            db=Db()
            db.insert("insert into farmer VALUES ('','"+name+"','"+email+"','"+phone+"')")
            return '''<script>alert('success');window.location='/adminhome'</script>'''
        else:
            return render_template('admin/view farmer.html')
    else:
        return redirect('/')

@app.route('/fertilizer',methods=['get','post'])
def fertilizer():
    if session['lg'] == "lo":
        if request.method=="POST":
            name=request.form['textfield']
            rate=request.form['textfield1']
            comment=request.form['textfield2']
            db=Db()
            db.insert("insert into fertilizers VALUES ('','"+name+"','"+rate+"','"+comment+"')")
            return '''<script>alert('success');window.location='/adminhome'</script>'''
        else:
            return render_template('admin/fertilizer.html')
    else:
        return redirect('/')

@app.route('/pesticide',methods=['get','post'])
def pesticide():
    if session['lg'] == "lo":
        if request.method=="POST":
            name = request.form['textfield']
            rate = request.form['textfield1']
            comment = request.form['textfield2']
            db=Db()
            db.insert("insert into pesticide values('','"+name+"','"+rate+"','"+comment+"')")
            return '''<script>alert('success');window.location='/adminhome'</script>'''
        else:

            return render_template('admin/pesticide.html')
    else:
        return redirect('/')

@app.route('/view_AO')
def view_AO():
    if session['lg'] == "lo":
        db=Db()
        qry=db.select("select * from agriculture_office")
        return render_template('admin/view A O.html',data=qry)
    else:
        return redirect('/')

@app.route('/delete_AO/<aid>')
def delete_A0(aid):
    if session['lg'] == "lo":
        db=Db()
        db.delete("delete from agriculture_office where agri_id='"+aid+"' ")
        return redirect('/view_AO')
    else:
        return redirect('/')



@app.route('/view_crop_management')
def view_crop_management():
    if session['lg'] == "lo":
        db=Db()
        qry=db.select("select * from crop")
        return render_template('admin/view crop management.html',data=qry)
    else:
        return redirect('/')
@app.route('/delete_crop_management/<cid>')
def delete_crop_management(cid):
    if session['lg'] == "lo":

        db=Db()
        db.delete("delete from crop where crop_id='"+cid+"' ")
        return redirect('/view_crop_management')
    else:
        return redirect('/')

@app.route('/view_farmer')
def view_farmer():
    if session['lg'] == "lo":
        db=Db()
        qry = db.select("select * from farmer")
        return render_template('admin/view farmer.html',data=qry)
    else:
        return redirect('/')
@app.route('/view_weather')
def view_weather():
    if session['lg'] == "lo":
        db=Db()
        qry = db.select("select * from weather_dept")

        return render_template('admin/view weather.html',data=qry)
    else:
        return redirect('/')

@app.route('/delete_weather/<did>')
def delete_weather(did):
    if session['lg'] == "lo":
        db=Db()
        db.delete("delete from weather_dept where dept_id='"+did+"' ")
        return redirect('/view_weather')
    else:
        return redirect('/')


@app.route('/view_fertilizer')
def view_fertilizer():
    if session['lg'] == "lo":

        db=Db()
        qry = db.select("select * from fertilizers")
        return render_template('admin/viewfertilizer.html',data=qry)
    else:
        return redirect('/')
@app.route('/delete_fertilizer/<fid>')
def delete_fertilizer(fid):
    if session['lg'] == "lo":
        db=Db()
        db.delete("delete from fertilizers where fertilizer_id='"+fid+"' ")
        return redirect('/view_fertilizer')
    else:
        return redirect('/')

@app.route('/view_pesticides')
def view_pesticides():
    if session['lg'] == "lo":
        db = Db()
        qry = db.select("select * from pesticide")

        return render_template('admin/viewpesticide.html',data=qry)
    else:
        return redirect('/')
@app.route('/delete_pesticide/<pid>')
def delete_pesticide(pid):
    if session['lg'] == "lo":

        db=Db()
        db.delete("delete from pesticide where pest_id='"+pid+"' ")
        return redirect('/view_pesticides')
    else:
        return redirect('/')



@app.route('/log_out')
def log_out():
    session.clear()
    session['lg']=""
    return redirect('/')



#########################################    WEATHER          ################################################
#########################################    WEATHER          ################################################



@app.route('/view_Profile')
def view_profile():
    if session['lg'] == "lo":
        db=Db()
        qry = db.selectOne("select * from weather_dept where dept_id='"+str(session['lid'])+"'")
        return render_template('weather/view profile.html',data=qry)
    else:
        return redirect('/')

@app.route('/add_weather2',methods=['get','post'])
def add_weather2():
    if session['lg']=="lo":
        if request.method=="POST":
            weather=request.form['textarea']
            db=Db()
            db.insert("insert into weather values ('','"+str(session['lid'])+"',curdate(),'"+weather+"')")
            return '''<script>alert('success');window.location='/weatherhome'</script>'''
        else:
            return render_template('weather/addweather.html')
    else:
        return redirect('/')

@app.route('/view_weather1')
def view_weather1():
    if session['lg'] == "lo":
        db=Db()
        qry = db.select("select * from weather where weather_dept_id='"+str(session['lid'])+"'")
        return render_template('weather/viewweather.html',data=qry)
    else:
        return redirect('/')

@app.route('/delete_weather1/<wid>')
def delete_weather1(wid):
    if session['lg'] == "lo":
        db=Db()
        db.delete("delete from weather where weather_ID='"+wid+"' ")
        return redirect('/view_weather1')
    else:
        return redirect('/')



@app.route('/view_doubt')
def view_doubt():
    if session['lg'] == "lo":
        db=Db()
        qry = db.select("select * from doubt,farmer where doubt.farmer_id=farmer.farmer_id")
        return render_template('weather/doubtsweather.html',data=qry)
    else:
        return redirect('/')




@app.route('/sendreply/<did>',methods=['get','post'])
def send_reply(did):
    if session['lg']=="lo":
        if request.method=="POST":
            Reply=request.form['textarea']

            db=Db()
            db.update("update doubt set reply='"+Reply+"',reply_date=curdate() where doubt_id='"+did+"'")
            return '''<script>alert('success');window.location='/weatherhome'</script>'''
        else:
            return render_template('weather/sendreply.html')
    else:
        return redirect('/')




########################################### AO  ###########################################################


@app.route('/view_Profile_AO')
def view_profile_AO():
    if session['lg'] == "lo":
        db=Db()
        qry = db.selectOne("select * from agriculture_office where agri_id='"+str(session['lid'])+"'")
        return render_template('AO/AOview.html',data=qry)
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run()
