from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)  # Use double underscores for "__name__" instead of single underscores

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    contact_info = request.form['contact_info']
    hobbies = request.form['hobbies']
    education = request.form['education']
    experience = request.form['experience']
    major = request.form['major']
    university = request.form['university']
    city = request.form['city']
    state = request.form['state']

    # Retrieve other form inputs here

    resume_content = f"""
    [Your Name]
    {name}

    Contact Information:
    {contact_info}

    Hobbies:
    {hobbies}

    Education:
    {education}

    Experience:
    {experience}

    Objective:
    Seeking a challenging position or internship opportunity in the field of {major} to apply and enhance my technical skills, while contributing to innovative projects.

    Education:
    Bachelor of Technology (B.Tech) in {major}
    {university}, {city}, {state}

    Relevant Coursework:
    - {request.form['course1']}
    - {request.form['course2']}
    - {request.form['course3']}
    - {request.form['course4']}
    - {request.form['course5']}

    Technical Skills:
    - {request.form['skill1']}
    - {request.form['skill2']}
    - {request.form['skill3']}

    Internships:
    1. {request.form['internship1']}
    2. {request.form['internship2']}

    Extracurricular Activities:
    - {request.form['activity1']}
    - {request.form['activity2']}

    Awards and Achievements:
    - {request.form['award1']}
    - {request.form['award2']}

    Certifications:
    - {request.form['certification1']}
    - {request.form['certification2']}

    Languages:
    - {request.form['language1']}
    - {request.form['language2']}

    References:
    Available upon request.
    """

    return render_template('result.html', resume_content=resume_content)

if __name__ == '__main__':  # Use double underscores for "__main__" instead of single underscores
    app.run(debug=True)
