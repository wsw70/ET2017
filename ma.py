import arrow

vacances = [
    arrow.Arrow.range('day', arrow.get('21/10/2017', 'DD/MM/YYYY'), arrow.get('06/11/2017', 'DD/MM/YYYY')),
    arrow.Arrow.range('day', arrow.get('23/12/2017', 'DD/MM/YYYY'), arrow.get('08/01/2018', 'DD/MM/YYYY')),
    arrow.Arrow.range('day', arrow.get('17/02/2018', 'DD/MM/YYYY'), arrow.get('05/03/2018', 'DD/MM/YYYY')),
    arrow.Arrow.range('day', arrow.get('14/04/2018', 'DD/MM/YYYY'), arrow.get('30/04/2018', 'DD/MM/YYYY')),
]

with open('ma.txt', 'w') as f:
    for date in arrow.Arrow.range('day', arrow.get('06/09/2017', 'DD/MM/YYYY'), arrow.get('06/07/2018', 'DD/MM/YYYY')):
        is_vacation = False
        is_weekend = False
        for vac in vacances:
            if date in vac:
                is_vacation = True
        _, weeknr, weekday = date.isocalendar()
        if weekday in [6, 7]:
            is_weekend = True
        #print(date, weeknr, is_weekend, is_vacation)
        if not (is_vacation or is_weekend):
            if weekday == 1:
                s = "8"
                e = "17"
            if weekday == 2:
                s = "8"
                e = "17"
            if weekday == 3:
                s = "8"
                e = "12:20"
            if weekday == 4:
                s = "8"
                e = "17"
            if weekday == 5:
                if weeknr % 2 == 0:  # semaine A
                    s = "9"
                else:
                    s = "8"
                e = "17"

            try:
                sh = int(s.split(':')[0])
                smin = int(s.split(':')[1])
            except IndexError:
                sh = int(s)
                smin = 0
            s = date.replace(hour=sh, minute=smin)

            try:
                eh = int(e.split(':')[0])
                emin = int(e.split(':')[1])
            except IndexError:
                eh = int(e)
                emin = 0
            e = date.replace(hour=eh, minute=emin)

            f.write("{0} {1}\n".format(s, e))
