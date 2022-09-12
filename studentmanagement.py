import sys
Students_Data = []
# restart = False
{
# def check():
#     x = int(input("Enter ID of student "))
#     for searchid in Students_Data:
#         # print(searchid)
#         if x == searchid["Id"]:
#             print("xxxx Id already exist xxxx")
#             # sys.exit()
#         if x != searchid["Id"]:
#             pass
#     return x

# def rollback():
#ShowOptions = 5
}
class info:
    def __init__(self,count):
        self.count=count
        
    def Detail(self):
        # student["Id"].append(check())
        student = {
            "Id": self.count,
            "Name": input("Enter name "),
            "Contact": int(input("Enter contact no ")),
            "Course": input("Enter course name "),
            "Paid fees":int(input("Enter fee amount ")),
            "Total Fees": 10000,
            "Balance": 0,
        }
        Students_Data.append(student)
        
# -----START-----
try:
    def start():
        ShowOptions = 0
        executioncount = 1
        while ShowOptions !=5:
            ShowOptions = int(input("****Select Task****\n1. Add new student detail.\n2. Show details of all students.\n3. Delete student detail.\n4. Fee management.\n5. exit()\n\nSelect your choice option !!!\n"))
            i = 4
            
            if ShowOptions == 1:
                ob1 = info(executioncount)
                ob1.Detail()
                executioncount = executioncount+1
            for balance in Students_Data:
                for k,v in balance.items():
                    balance["Balance"] = balance["Total Fees"] - balance["Paid fees"]
            
            if ShowOptions == 2:
                for std_list in Students_Data:
                    print(std_list,"\n")
                ask = int(input("For continue press 9\n"))
                if ask == 9:
                    pass
            
            if ShowOptions ==3:
                for showtable in Students_Data:
                    print(showtable,"\n")
                    
                delete_std_detail = input("Enter name for delete ")
                for delete in Students_Data:
                    for j,d in delete.items():
                        if delete_std_detail == delete["Name"]:
                            Students_Data.remove(delete)
                            print("Details have been deleted !!")
                            break
                            
            
            if ShowOptions == 4:
                print("****FEES DETAIL****")
                fees_option = int(input("1. Want to show student fee detail.\n2.Update student fee.\n"))
                if fees_option == 1:
                    ask_std_name = input("Enter student name & get fees detail\n")
                    for search in Students_Data:
                        for key,value in search.items():
                            # print(key,value)
                            if ask_std_name == search["Name"]:
                                print("Paid fees of ",ask_std_name," is ",search["Paid fees"])
                                break
                if fees_option == 2:
                    update_std_fees = input("Enter student name ")
                    for find in Students_Data:
                        for key,value in find.items():
                            # print(key,value)
                            if update_std_fees == find["Name"]:
                                newfee = int(input("Enter new fees"))
                                x = find["Paid fees"] + newfee
                                find["Paid fees"] = x
                                ask = int(input("For continue press 9\n"))
                                if ask == 9:
                                    break   
                        
    start()
except:
    print("\n**YOU ENTERED A WRONG KEY**\n")

    
