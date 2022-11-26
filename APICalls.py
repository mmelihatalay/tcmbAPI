import requests
import xmltodict


class BaseAPICall():
    def __init__(self):
        pass
    
    def getAllCurrencies(self):
        return self._currencyDict

    def getCurrentExchange(self, target):
        
        return self._currencyDict[target]
        


class TCMBAPICall(BaseAPICall):
    source = 'https://www.tcmb.gov.tr/kurlar/today.xml'

    def __init__(self):
        BaseAPICall.__init__(self)
        self._rearrangeData()
        
    def _rearrangeData(self):
        response = requests.get(self.source)
        responseList = xmltodict.parse(response.text)['Tarih_Date']['Currency']
        self._currencyDict = {}
        for e in responseList:
            self._currencyDict[e['@CurrencyCode']] = {'Buy': e['BanknoteBuying'],
                                                'Sell': e['BanknoteSelling']}




if __name__ == '__main__':
    tcmb = TCMBAPICall()
    print(tcmb.getCurrentExchange('USD'))
