import tika
tika.initVM()
from tika import parser

raw = parser.from_file('coi-4March2016.pdf')
with open('COI.txt', 'w', encoding='utf-8') as f:
    print(raw['content'], file=f)

