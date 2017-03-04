import requests
from bs4 import BeautifulSoup as bs
payload = {
   'revAvailabilitySearch.SearchInfo.AdultCount':'1',
'revAvailabilitySearch.SearchInfo.ChildrenCount':'0',
'revAvailabilitySearch.SearchInfo.InfantCount':'0',
'revAvailabilitySearch.SearchInfo.Direction':'Return',
'revAvailabilitySearch.SearchInfo.PromoCode':'',
'revAvailabilitySearch.SearchInfo.SalesCode':'',
'revAvailabilitySearch.SearchInfo.SearchStations[0].DepartureStationCode':'TPE',
'revAvailabilitySearch.SearchInfo.SearchStations[0].ArrivalStationCode':'MLE',
'revAvailabilitySearch.SearchInfo.SearchStations[0].DepartureDate':'03/04/2017',
'revAvailabilitySearch.SearchInfo.SearchStations[1].DepartureStationCode':'MLE',
'revAvailabilitySearch.SearchInfo.SearchStations[1].ArrivalStationCode':'TPE',
'revAvailabilitySearch.SearchInfo.SearchStations[1].DepartureDate':'07/31/2017',
'Name':'', 
}
rs = requests.session()

res = rs.post('http://makeabooking.flyscoot.com/Book/?culture=zh-tw', data=payload)
res2 = rs.get('http://makeabooking.flyscoot.com/Book/Flight')
soup = bs(res2.text)
for a in soup.select('.flight-date a'):
    print a.select('span')[0].text, a.select('strong')[0].text 