yf_list = [1,2,3,4,5,6,7,80,9,10,11,12,13,14,15,16,17,18,19,20]
# yuu = max(yf_list)
# y_val = yf_list.index(yuu)
# print yuu, y_val

i = 1
while i<=5:
    print i
    if i == 1:
        addingList = yf_list
        # print i, addingList
    else:
        # print i
        for j in range(len(yf_list)):
            addingList[j] += yf_list[j]
            # print "hi"
        if i == 5: 
            
            yuu = max(yf_list[5:])
            y_val = yf_list.index(yuu)
            print "done"
            print yf_list, yuu, y_val
            i=0
            addingList = []
            break
        # print i, addingList
    # print "ok"
    i += 1