import datetime
import calendar

def amortize(amount, startDate, endDate):
    actualEndDate = calendar.monthrange(endDate.year, endDate.month)
    if actualEndDate[1] != endDate.day:
    if isLastDateOfMonth(endDate.year, endDate.month):
        return "heheheh"
    return "no  heheheh"



def isLastDateOfMonth(year, month):
    return calendar.monthrange(year, month)
    
startDate = datetime.date(2020, 1, 1)
endDate = datetime.date(2020, 12, 31)
print amortize(1200, startDate, endDate)
