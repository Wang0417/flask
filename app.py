from flask import Flask,render_template,request
import json
import train

app=Flask(__name__)

@app.route("/")
def hi():
    return 'hi'
@app.route("/show_add_user")
def show_add_user():
    return render_template("show_add_user.html")


@app.route("/do_add_user",methods=['POST'])
def do_add_user():
    print(request.form)
    student_id=request.form.get("student_id")
    name=request.form.get("name")
    major=request.form.get("major")
    sql=f"""
    insert into `student` (student_id,name,major)
    values ({student_id},'{name}','{major}')
    """
    print(sql)
    train.insert_or_update_data(sql)
    return 'success'
if __name__=='__main__':
    app.run()