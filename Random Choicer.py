import random, json

class RandomChoicer:
    while True:
        try:
            money = int(input("""
    Please, enter the amount you want to split: """))
            break
        except ValueError:
            print("""         
    ENTER A INTEGER VALUEE!!!""")

    def __init__(self) -> None:
        self.working = True

    def Program(self):
        choice = self.Menu()

        if choice == 1:
            self.AddStudent()
        elif choice == 2:
            self.DeleteStudent()
        elif choice == 3:
            self.ShowStudent()
        elif choice == 4:
            self.RandomStudent()
        else:
            self.Exit()

    def Menu(self):
        while True:    
            try:
                choice = int(input("""
---------------- WELCOME TO THE RANDOM CHOICER ----------------\n
                ADD STUDENT
                DELETE STUDENT
                SHOW STUDENT
                RANDOM STUDENTS
                EXIT
                
                Enter your choice(1-5): """))
                break
            except ValueError:
                print("""         
                ENTER A INTEGER VALUE!!!""")

        while choice < 1 or choice > 5:
            choice = int(input(
"""     Seçimi yanliş daxil edirsiz!!
        Yenidən daxil edin(1-5): """))

        return choice

    def AddStudent(self):
        print("""
---------------- WELCOME TO THE RANDOM CHOICER ----------------\n""")
        
        student_id = 0
        name = input(
"""     Student name:""")
        lname = input(
"""     Student last name: """)
        class_st = input(
"""     Student class: """)

        with open('data.json', 'r') as doc:
            data = json.loads(doc.read())
            student_id = len(data)+1
       
        student_data = {'id': student_id, 'name':name, 'lname':lname, 'class':class_st}

        with open('data.json', 'r') as doc:
            data = doc.read()
            data = json.loads(data)
            data.append(student_data)
            data = json.dumps(data)
            with open('data.json', 'w') as doc:
                doc.write(data)
        
    def DeleteStudent(self):
        print("""
---------------- WELCOME TO THE RANDOM CHOICER ----------------\n""")
        
        with open('data.json', 'r') as doc:
            data = json.loads(doc.read())
            max_id = data[0]['id']
            for i in data:
                print(
f"""    {i['id']}. {i['lname']} {i['name']} {i['class']}""")
                if max_id < i['id']:
                    max_id = i['id']
        
            delete_id = int(input(f"""
        Choice ID which you want to delete student(1-{max_id}): """))

            data.remove(data[delete_id-1])

            with open('data.json', 'w') as doc:
                doc.write(json.dumps(data))
    

    def ShowStudent(self):
        print("""
---------------- WELCOME TO THE RANDOM CHOICER ----------------\n""")

        with open('data.json', 'r') as doc:
            data = json.loads(doc.read())
            max_id = data[0]['id']
            for i in data:
                print(
f"""    {i['id']}. {i['lname']} {i['name']} {i['class']}""")

    def RandomStudent(self):
        print("""
---------------- WELCOME TO THE RANDOM CHOICER ----------------\n""")
        
        count_of_random = int(input("""
        Please, enter count of random students: """))
        print()
        
        new_data = [1, 2, 1, 1]
        new_data2 = []
        new_str = """Random Characters:\n\n"""

        with open('data.json', 'r') as doc:
            data = json.loads(doc.read())
            
            while True:
                if len(new_data) == len(set(new_data)):
                    break
                else:
                    new_data = []
                    for i in range(count_of_random):
                        new_data.append(random.randint(1, len(data)))
            
            for i in new_data:
                new_data2.append(data[i-1])
            
            count = 1
            for i in new_data2:
                print(
f"""    {count}. {i['lname']} {i['name']} {i['class']}""")
                new_str += f"""    {count}. {i['lname']} {i['name']} {i['class']} ==> {self.money/len(new_data2)}""" + '\n'
                count += 1 
            
            while True:
                try:
                    file_name = input("""
            Please enter your file name: """)
                    
                    with open(f'DATA/{file_name}.txt', 'x') as doc:
                        doc.write(new_str)
                    break
                except FileExistsError:
                    print("""         
            THIS FILE IS EXISTS!!!""")

            
    
    def Exit(self):
        print("""
---------------- OUR PROGRAM STOPPED ----------------   
    """)
        self.working = False

random_choicer = RandomChoicer()

while random_choicer.working:
    random_choicer.Program()