def restock_inventory(available_items, inventory_records, current_day):
    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the stock/restock for a given day.
---------------
Function Input:
---------------
available_items: (integer) Available Tshirts from the previous day.
inventory_records: (List) A list of inventory records until the previous day. Each row contains (day, sales, restocked items, available items)
current_day: (integer) Day number which you want to add as the current day. 

----------------
Function Output:
----------------
available_items:(integer) This function returns this integer which updates the available items at the current day.


The function will also update the inventory_records (For restocking) for a  given current day. It will also return "available_items".
    '''

    #Checks to see if it is day 0
    if current_day == 0:
        #Sets the sales to 0 and the restock and available items to 2000
        inventory_records.append((current_day, 0, 2000, 2000))

    #Checks to see if the current day is divisible by 7
    elif current_day % 7 == 0:
        #Calculates the amount to restock
        restocked_items = 2000 - available_items
        #Sets the available items to 2000
        available_items = 2000
        #Appends the restock levels
        inventory_records.append((current_day, 0, restocked_items, available_items))
    
    return available_items


