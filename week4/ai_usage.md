This code is a simple appointment-booking example that stores appointments in a list and displays them to the user.

1. What the code does
a) Creates an empty list
Python
appointments = []
Show more lines

This list will hold all appointment records.

b) Defines add_appointment()
Python
def add_appointment(patient, practitioner, time):
Show more lines

This function:

Receives a patient's name, a practitioner's name, and a time.
Creates a dictionary containing those values.
Adds the dictionary to the appointments list.

Example appointment stored:

Python
{
"patient": "Liam Brown",
"practitioner": "Dr. Patel",
"time": "2024-08-01 9:00 AM"
}
Show more lines
c) Defines show_appointments()
Python
def show_appointments():
Show more lines

This function checks whether any appointments exist.

If the list is empty, it prints:

Python
No appointments yet.
Show more lines

Otherwise, it loops through every appointment and prints details such as:

Python
Liam Brown with Dr. Patel at 2024-08-01 9:00 AM
Show more lines
d) Adds two appointments
Python
add_appointment("Liam Brown", "Dr. Patel", "2024-08-01 9:00 AM")
add_appointment("Sarah Lee", "Dr. Nguyen", "2024-08-01 9:30 AM")
Show more lines

These calls create two appointment records and store them in the list.

e) Displays all appointments
Python
show_appointments()
Show more lines

Output:

Plain Text
Liam Brown with Dr. Patel at 2024-08-01 9:00 AM
Sarah Lee with Dr. Nguyen at 2024-08-01 9:30 AM
Show more lines
2. Three limitations
1. No validation of input data

The program accepts any values.

For example:

Python
add_appointment("", "", "banana")
Show more lines

would still be stored, even though the information is invalid.

2. No check for scheduling conflicts

Two patients could be booked with the same practitioner at the same time:

Python
add_appointment("John", "Dr. Patel", "9:00 AM")
add_appointment("Mary", "Dr. Patel", "9:00 AM")
Show more lines

The program would allow both appointments.

3. Data is not permanently saved

Appointments exist only while the program is running.

When the program stops, all information in the appointments list is lost.

3. Suggested improvements

Without rewriting the whole application, you could:

Add input validation

Check that:

patient names are not empty
practitioner names are not empty
appointment times follow a valid format
Prevent double-bookings

Before adding an appointment, search the list to ensure the practitioner is not already booked for that time.

Store dates and times properly

Instead of plain text strings, use Python's datetime module. This makes sorting, comparison, and validation easier.

Improve appointment display

You could number the appointments:

Plain Text
1. Liam Brown with Dr. Patel at 9:00 AM
2. Sarah Lee with Dr. Nguyen at 9:30 AM
Show more lines
Save data to a file

Store appointments in a file (such as JSON) so they remain available after the program closes.

4. Two questions to test your understanding

Why is a dictionary used to represent each appointment instead of storing the patient, practitioner, and time as three separate values in the list?

What will happen if show_appointments() is called before any appointments are added, and which part of the code causes that behavior?

Explanation of the analysis

I explained the role of the list, functions, dictionaries, function calls, and output. I then identified three practical limitations (validation, conflict checking, persistence) and suggested targeted improvements without rewriting the entire application. The two questions check understanding of data structures and program flow.


Part D:
Python
appointments = []
 
def add_appointment(patient_name, practitioner_name, appointment_time):
appointment = {
"patient": patient_name,
"practitioner": practitioner_name,
"time": appointment_time
}
appointments.append(appointment)
 
# Example usage
add_appointment("Liam Brown", "Dr. Patel", "9:00 AM")
add_appointment("Sarah Lee", "Dr. Nguyen", "9:30 AM")
 
print(appointments)
Show less
How it works
appointments is a list that stores appointment records.
add_appointment() takes three pieces of information:
patient name
practitioner name
appointment time
A dictionary is created for each appointment.
The dictionary is added to the appointments list.
The final print() statement displays all stored appointments.

This approach is suitable for introductory programming because it uses only basic concepts: lists, dictionaries, functions, and variables.