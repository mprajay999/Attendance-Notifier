from Module import getattendance,sendmail,gettime

users={'Prajay':['160117735101','160117735101','mprajay999@gmail.com']}


if __name__=='__main__':
    for name in users:
        try:
            attendance = getattendance(users[name][0], users[name][1])
            print(attendance)
            sendmail(users[name][2], name, attendance,gettime())

        except:
            print('Server Error')
            break

