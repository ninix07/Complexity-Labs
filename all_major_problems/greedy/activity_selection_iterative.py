def activity_selection(activities):
    num= len(activities)
    activities.sort(key= lambda x:x[0])
    indexes=[0]
    next=0
    for i in range(1,num):
        if activities[i][0] >= activities[next][1]:
            indexes.append(i)
            next=i
    return indexes



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
    indexes= activity_selection(activities)

    print(indexes)  #adding zero index cause it is directly selected
   