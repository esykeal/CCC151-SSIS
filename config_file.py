database_name = "ssis_db"

student_fieldnames = ["id_number", "first_name", "last_name", "gender", "year_level", "program_code"]
program_fieldnames = ["program_code", "program_name", "college_code"]
college_fieldnames = ["college_code", "college_name"]

#TODO: FIND OUT IF BELOW ARE STILL USEFUL
header_names = {
    "STUDENTS": [
        ("id_number", "ID Number"),
        ("first_name", "First Name"),
        ("last_name", "Last Name"),
        ("gender", "Gender"),
        ("year_level", "Year Level"),
        ("program_code", "Program Code"),
    ],
    "PROGRAMS": [
        ("program_code", "Program Code"),
        ("program_name", "Program Name"),
        ("college_code", "College Code"),
    ],
    "COLLEGES": [
        ("college_code", "College Code"),
        ("college_name", "College Name"),
    ],
}