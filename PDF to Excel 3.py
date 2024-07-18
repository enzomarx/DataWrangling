import requests
from bs4 import BeautifulSoup
import fpdf
import xlsxwriter
lis = []
lis = [item for item in input("What RFC should we scrape?(space separated)(example: 1918 1997): ").split()]
frmt = input('What format should we export as? (PDF, Excel): ')
frmt = frmt.lower()
if frmt == 'pdf':
    pdf = fpdf.FPDF(format='letter')
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for rfcs in lis: 
        url='https://datatracker.ietf.org/doc/html/rfc' + rfcs
        print(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find(id="content")
        pdf.write(5,str(content.text))
        pdf.ln()
        pdf.output('rfc' + rfcs + ".pdf")
elif frmt == 'excel':
    for rfcs in lis: 
        url='https://datatracker.ietf.org/doc/html/rfc' + rfcs
        print(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find(id="content")
        workbook = xlsxwriter.Workbook('rfc' + rfcs + '.xls')
        worksheet = workbook.add_worksheet()
        worksheet.write(0, 0, str(content.text))
        workbook.close()
else:
    print('Please enter a valid format')

