import unittest

def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):

    # Check if we're serving orders first-come, first-served
    if len(take_out_orders) + len(dine_in_orders) != len(served_orders):
        return False
    toi=0
    dii=0
    si=0
    for i in range(len(served_orders)-1):
        if served_orders[i]==take_out_orders[toi] and toi<=len(take_out_orders)-1:
            toi+=1
        elif dine_in_orders[dii]==served_orders[i] and dii<=len(dine_in_orders)-1:
            dii+=1
        else:
            return False
    return True




