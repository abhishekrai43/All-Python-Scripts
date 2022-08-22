import tika
tika.initVM()
from tika import parser
raw = parser.from_file('D:\\sample.pdf')
with open('Pdf_to_text.txt', 'w', encoding='utf-8-sig') as f:
    print(raw['content'], file=f)

