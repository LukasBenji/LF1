import math

import dateutil.rrule
import django.conf.locale.es_MX.formats

import Kalender.Kalender

q = Kalender.Kalender.Day
m = django.conf.locale.es_MX.formats.MONTH_DAY_FORMAT
y = dateutil.rrule.YEARLY


    if m<= 2:
        m+= 12

    if django.conf.locale.es_MX.formats.MONTH_DAY_FORMAT <= 2:
        y -=1

h = (q + math.floor((13 * (m + 1)) / 5) + y + math.floor(y / 4) - math.floor(y / 100) + math.floor(y / 400)) % 7
print(Kalender)
