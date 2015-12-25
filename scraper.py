import scraperwiki
from scrapemark import scrape
import scraperwiki

URLList = [
  "a0L3000000OvSOEEA3" #Sales
  ,"a0L3000000OvSOFEA3" #Customer Service
  ,"a0L3000000OvSOGEA3" #Marketing
  ,"a0L3000000OvSOHEA3" #IT & Admin
  ,"a0L3000000OvSOIEA3" #HR
  ,"a0L3000000OvSOJEA3" #Finance
  ,"a0L3000000OvSOKEA3" #ERP
  ,"a0L3000000OvSOLEA3" #Collabration
  ,"a0L3000000OvrgaEAB" #Analytics
  ]
   #"https://appexchange.salesforce.com/category/analytics" #Analytics
URLRoot = "https://appexchange.salesforce.com/results?pageNo={0}&filter="
for URL0 in URLList:
  for page in range(1,49):
    URLPath = URLRoot.format(str(page))
    URL = URLPath+URL0
    print URL
    html = scraperwiki.scrape(URL)
    scrape_data = scrape("""
     {*
     
     <a class="tile-title" href="{{ [mobile].[link] }}" id="{{ [mobile].[id] }}" title="{{ [mobile].[title1] }}"></a>
     
     *}
     """, html=html);
  
    data = [{'Title':p['title1'][0], 'URL':p['link'][0], 'ID':p['id'][0], 'Format':'Managed'} for p in scrape_data['mobile']]
  
    scraperwiki.sqlite.save(unique_keys=["URL"], data=data)
