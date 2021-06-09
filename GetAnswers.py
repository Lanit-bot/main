injson = input()
meow = injson.replace('[','').replace('{','').replace(']','').replace('}','').replace('"','').replace('answer','').replace('questionId:','').replace(':',',').replace(',,',',')
end = ['','','','','','']
ans = meow.split(',')
for i in range(len(ans)):
    try:
        if int(ans[i]) > 5:
            end[0] = ans[i]
        else:
            end[int(ans[i])+1] = ans[i+1]
    except ValueError:
        pass
    #print(end)
#в end хранится список сортированный
