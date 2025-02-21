class School:
    school_name="ABC school"
    
    @staticmethod
    def claculate_grade(mark):
        if mark>=90:
            return 'A+'
        else:
            return 'F'

print(School.claculate_grade(96))