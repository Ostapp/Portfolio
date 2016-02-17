import Ostap_check_unique_members_engine
import glob
import Ostap_unique_members

list_of_files = glob.glob('H:\Twitter_members\*.txt')

for item in list_of_files:
        Ostap_check_unique_members_engine.check_unique_members1(item)


print("There are " + str(Ostap_unique_members.counter1) + " members in total")    
print("Among them there are " + str(Ostap_unique_members.counter_) + " unique members")   
        
new_file = open ('H:/Twitter_members/unique_members.txt', 'w')
        new_file.write(Ostap_unique_members.list_)
        new_file.close()
