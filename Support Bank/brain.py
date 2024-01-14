
class Brain:

    def __init__(self, object):
        self.object = object
    

    def csv_loop(self):
        # If all data is valid, continue into main loop
        flag = True
        while flag:
            user_input = input("\n Choose one of the two options:\n\
                        * list all              - List all employees and total amounts\n\
                        * list <employee name>  - List all transactions for the employee\n\
                        * exit\
                        \nChoice: ")

            if user_input.lower() == "list all":
                print(self.object.list_all())
            elif user_input.lower().startswith("list "):
                split_input = user_input.split()
                name = " ".join(split_input[1:])
                print(name)
                
                if name.lower() in [employee.lower() for employee in self.object.unique_names()]:

                    print(self.object.list_user_details(name))
                else:
                    print("No matching lines found for the specified user.")
            elif user_input.lower() == "exit":
                break
            else:
                print("Incorrect choice, choose again")


    def json_loop(self):
            # If all data is valid, continue into main loop
            flag = True
            while flag:
                user_input = input("\n Choose one of the two options:\n\
                            * list all              - List all employees and total amounts\n\
                            * list <employee name>  - List all transactions for the employee\n\
                            * exit\
                            \nChoice: ")

                if user_input.lower() == "list all":
                    print(self.object.list_all())
                elif user_input.lower().startswith("list "):
                    split_input = user_input.split()
                    name = " ".join(split_input[1:])
                    print(name)
                    
                    if name.lower() in [employee.lower() for employee in self.object.unique_names()]:

                        print(self.object.list_user_details(name))
                    else:
                        print("No matching lines found for the specified user.")
                elif user_input.lower() == "exit":
                    break
                else:
                    print("Incorrect choice, choose again")
