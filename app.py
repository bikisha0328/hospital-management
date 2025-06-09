from flask import Flask, render_template, request, redirect
from models import db, Patient, Doctor, Appointment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

@app.route('/')
def home():
    return render_template('index.html')

# Patients
@app.route('/patients')
def view_patients():
    patients = Patient.query.all()
    return render_template('patients.html', patients=patients)

@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        db.session.add(Patient(name=name, age=age, gender=gender))
        db.session.commit()
        return redirect('/patients')
    return render_template('add_patient.html')

# Doctors
@app.route('/doctors')
def view_doctors():
    doctors = Doctor.query.all()
    return render_template('doctors.html', doctors=doctors)

@app.route('/add_doctor', methods=['GET', 'POST'])
def add_doctor():
    if request.method == 'POST':
        name = request.form['name']
        specialty = request.form['specialty']
        db.session.add(Doctor(name=name, specialty=specialty))
        db.session.commit()
        return redirect('/doctors')
    return render_template('add_doctor.html')

# Appointments
@app.route('/appointments')
def view_appointments():
    appointments = Appointment.query.all()
    return render_template('appointments.html', appointments=appointments)

@app.route('/book_appointment', methods=['GET', 'POST'])
def book_appointment():
    if request.method == 'POST':
        patient_id = request.form['patient_id']
        doctor_id = request.form['doctor_id']
        date = request.form['date']
        db.session.add(Appointment(patient_id=patient_id, doctor_id=doctor_id, date=date))
        db.session.commit()
        return redirect('/appointments')
    patients = Patient.query.all()
    doctors = Doctor.query.all()
    return render_template('book_appointment.html', patients=patients, doctors=doctors)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
