Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Welcome to SmartCare Appointment Recorder")
...
... # First appointment
... patient1 = "Liam Brown"
... practitioner1 = "Dr. Patel"
... time1 = "2024-08-01 9:00 AM"
... print("Patient:", patient1, "| Practitioner:", practitioner1, "| Time:", time1)
...
... # Second appointment
... patient2 = "Sarah Lee"
... practitioner2 = "Dr. Nguyen"
... time2 = "2024-08-01 9:30 AM"
... print("Patient:", patient2, "| Practitioner:", practitioner2, "| Time:", time2)
...
Welcome to SmartCare Appointment Recorder
Patient: Liam Brown | Practitioner: Dr. Patel | Time: 2024-08-01 9:00 AM
Patient: Sarah Lee | Practitioner: Dr. Nguyen | Time: 2024-08-01 9:30 AM
>>> print("Welcome to SmartCare Appointment Recorder (Enhanced Version)")
... appointments = []
...
... def add_appointment(patient, practitioner, time):
...     appointment = {
...         "patient": patient,
...         "practitioner": practitioner,
...         "time": time
...     }
...     appointments.append(appointment)
...
... def show_appointments():
...     if len(appointments) == 0:
...         print("No appointments yet.")
...     else:
...         for a in appointments:
...             print(f"{a['patient']} with {a['practitioner']} at {a['time']}")
...
... # Add two appointments
... add_appointment("Liam Brown", "Dr. Patel", "2024-08-01 9:00 AM")
... add_appointment("Sarah Lee", "Dr. Nguyen", "2024-08-01 9:30 AM")
...
... # Display them
... show_appointments()
...
Welcome to SmartCare Appointment Recorder (Enhanced Version)
Liam Brown with Dr. Patel at 2024-08-01 9:00 AM
Sarah Lee with Dr. Nguyen at 2024-08-01 9:30 AM
>>>
