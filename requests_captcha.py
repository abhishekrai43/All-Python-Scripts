import xlrd
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
file_location = "link_download_sample.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36" ,
    'referer':'http://buscatextual.cnpq.br/buscatextual/download.do?metodo=apresentar&idcnpq=8681074107208059',
    'Host': 'buscatextual.cnpq.br',
    'Origin': 'http://buscatextual.cnpq.br'
}
i = 1
def get_data(row):
    global i
    i += 1
    with requests.Session() as s:
        s.headers.update(header)
        r = s.get(row)
        with open(f'file{i}.xml', 'wb') as f:
            f.write(r.content)
            print(f"Downloaded file no {i}")

processes = []
with ThreadPoolExecutor(max_workers=10) as executor:
    for row in range(1,sheet.nrows):
        processes.append(executor.submit(get_data, sheet.cell_value(row,0)))

for task in as_completed(processes):
    print(task.result())




