def main():
    date = input('Date: ').strip()
    send(date)


def send(ate):
    fix = ''
    d = ''
    try:
        month = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"]

        z = 0
        s = 0
        for t in ate:
            if t != ',':
                fix += t
            else:
                s = 1
            if t != '/':
                d = d + t
            else:
                d = d + ' ' + '/' + ' '
        d.strip()
        a_1 = fix.split(' ')
        a_3 = d.split(' ')
        for w in month:
            if w == a_1[0] or a_3[1] == '/':
                z = 1
        if a_3[1] == '/':
            s = 1
        if z == 0 or s == 0:
            main()
        mon = month.index(a_1[0])
        if int(a_1[1]) > 22:
            main()
        if mon + 1 < 10:
            o = '0' + str(mon + 1)
        else:
            o = str(mon + 1)
        if int(a_1[1]) < 10:
            q = '0' + a_1[1]
        else:
            q = a_1[1]
        print(f"{a_1[2]}-{o}-{q}", end='')

    except ValueError:

        month = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"]
        a_2 = ate.split('/')
        for w in month:
            if w == a_2[0]:
                main()
        if int(a_2[0]) > 13 or int(a_2[1]) > 31:
            main()
        if int(a_2[0]) < 10:
            t = '0' + a_2[0]
        else:
            t = a_2[0]
        if int(a_2[1]) < 10:
            u = '0' + a_2[1]
        else:
            u = a_2[1]
        print(f"{a_2[2]}-{t}-{u}", end='')


main()