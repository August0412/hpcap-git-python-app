from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    name = "Atharv Ganer" 
    pnr = "240840141004" 
    # List of technologies
    technologies = ['Python', 'Flask', 'JavaScript', 'HTML', 'CSS', 'SQL', 'Docker']
    
    # Print technologies using a for loop in Python
    print("Technologies:")
    for tech in technologies:
        print(tech)

    # List of Students
    students = ['Chaitali', 'Atharv', 'Apurva', 'Anirudh']

    # Print technologies using a for loop in Python
    print("Students:")
    for stud in students:
        print(stud)

    return render_template('index.html', name=name, pnr=pnr)

print "This is used for git"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  
