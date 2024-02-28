
#https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL
#crearse cuenta en postman
from zeep import Client
client = Client(
    "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"
)
result = client.service.NumberToWords(5)
#my homework!
result_NumberToDollars = client.service.NumberToDollars(12)
print(result)
#print my result
print(result_NumberToDollars)