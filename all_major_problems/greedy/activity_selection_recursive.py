def activity_selection(activities,curr, end):
        temp= curr+1                                                            #only check from index 1 as 0 is automatically selected
        while temp <= end and activities[temp][0] < activities[curr][1]:        # check if start< precious finish
                temp=temp+1                                                   
        if temp<=end:
            return [temp] + activity_selection(activities, temp, end)           #recursive call
        else:
               return []
        
if __name__== "__main__":
    activities = [
        [1, 3],
        [3, 4],
        [2, 5],
        [4, 7],
        [8, 9],
        [7, 10],
        [9, 11],
        [11, 12],
        [9, 13],
        [12, 14],
    ]
    curr = 0
    end = len(activities) - 1
    activities.sort(key= lambda x:x[0])
    indexes= activity_selection(activities,curr, end)
    print([0]+indexes)  #adding zero index cause it is directly selected
   

    