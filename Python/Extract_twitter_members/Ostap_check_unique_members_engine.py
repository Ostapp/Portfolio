import Ostap_unique_members

def check_unique_members1(item):
   
    with open (item, 'r', encoding = 'utf-8') as text:
                read_item = text.readlines()

    print(item[19:] + " is now being processed")

        
    for name in read_item:
        if name not in Ostap_unique_members.list_:
            Ostap_unique_members.list_ = Ostap_unique_members.list_ + name
            Ostap_unique_members.counter_ = Ostap_unique_members.counter_ + 1
            Ostap_unique_members.list1 = Ostap_unique_members.list1 + name
            Ostap_unique_members.counter1 = Ostap_unique_members.counter1 + 1
        else:
            Ostap_unique_members.list1 = Ostap_unique_members.list1 + name
            Ostap_unique_members.counter1 = Ostap_unique_members.counter1 + 1
