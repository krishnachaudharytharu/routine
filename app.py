from flask import Flask, request, render_template, redirect, session, url_for, flash

app=Flask(__name__)
app.secret_key="super_secret_key"

morning_list=[]

personal_list=[]
study_list=[]
evening_list=[]
night_list=[]

@app.route("/")
def home():
    return render_template("index.html", morning_list=morning_list, study_list=study_list, personal_list=personal_list, evening_list=evening_list, night_list=night_list )

@app.route("/add_1", methods=["POST"])
def add_1():
    if request.method=="POST":
        wake_of_time =request.form["wake_of_time"]
        freshen_up=request.form["freshen_up"]
        exercise=request.form["exercise"]
        breakfast=request.form["breakfast"]
        
        morning_list.append({
            "wake_of_time":wake_of_time,
            "freshen_up":freshen_up,
            "exercise":exercise,
            "breakfast":breakfast
        })
        flash("Added your Morning routine", "success")
        return redirect("/")

    
    
    

@app.route("/add_2", methods=["POST"])
def add_2():
    if request.method=="POST":
        classes =request.form["classes"]
        python_practice=request.form["python_practice"]
            
        java_practice=request.form["java_practice"]
        dsa_practice=request.form["dsa_practice"]
        assignment_completion=request.form["assignment_completion"]
        
        study_list.append({
            "classes":classes,
            "python_practice": python_practice,
            "java_practice":java_practice,
            "dsa_practice":dsa_practice,
            "assignment_completion":assignment_completion
        
        })
        flash("Added your Study routine", "success")
        return redirect("/")

    
    
    

@app.route("/add_3", methods=["POST"])
def add_3():
    if request.method=="POST":
        lunch=request.form["lunch"]
        rest_time=request.form["rest_time"]
        family_time=request.form["family_time"]
        friends_time=request.form["friends_time"]
        
        personal_list.append({
            "lunch":lunch,
            "rest_time":rest_time,
            "family_time":family_time,
            "friends_time":friends_time
        
        
        
        
        })
        flash("Added your Personal routine")
        return redirect("/")
    

@app.route("/add_4", methods=["POST"])
def add_4():
    if request.method=="POST":
        coding_practice=request.form["coding_practice"]
        ai_ml_learning=request.form["ai_ml_learning"]
        project_dev=request.form["project_dev"]
        revision=request.form["revision"]
        
        evening_list.append({
            "coding_practice":coding_practice,
            "ai_ml_learning":ai_ml_learning,
            "project_dev":project_dev,
            "revision":revision
        
        
        
        
        })
        flash("Added your evening route")
        return redirect("/")
    

@app.route("/add_5", methods=["POST"])
def add_5():
    if request.method=="POST":
        dinner=request.form["dinner"]
        next_day_planing=request.form["next_day_planing"]
        reading=request.form["reading"]
        sleep_time=request.form["sleep_time"]
        
        night_list.append({
            "dinner":dinner,
            "next_day_planing":next_day_planing,
            "reading":reading,
            "sleep_time":sleep_time
        
        
        
        
        })
        flash("Added your night routine")
        return redirect("/")


         
    

if __name__=="__main__":
    app.run(debug=True)







