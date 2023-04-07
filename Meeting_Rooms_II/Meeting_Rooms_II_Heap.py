
def minMeetingRoom(intervals):
    rooms = []  #Initialize rooms as an empty array, which acts as a heap
    
    intervals.sort(key = lambda x: x[0])    #Sort the intervals using key parameter with the start time of the meeting
    
    heappush(rooms, intervals[0][1])    #Push the first interval into the rooms using heappush

    for room in intervals[1:]:  #Continue from the second interval to the end
        if rooms[0] <= room[0]: #If the top element in the rooms is less than the starting time of the room
            heappop(rooms)  #Pop the element in the rooms
            
            heappush(rooms, room[1])    #And push the end time of the incoming interval
            
    return len(rooms)   #Return the length of the rooms which will give the number of meeting rooms required

print(minMeetingRoom([(0,30),(5,10),(15,20)]))