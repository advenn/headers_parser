sample_headers = """accept: text/html,application/xhtml+xml...
accept-encoding: gzip, deflate, br
accept-language: en-GB,en-US;q=0.9,en;q=0.8,uz;q=0.7
cache-control: max-age=0
cookie: <cookie>
sec-ch-ua: "Not_A Brand";v="99",...
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: none
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: <user-agent>"""


def parse_headers(hdrs: str):
    headers = {}
    for line in hdrs.splitlines():
        headers[line.split(':')[0].strip()] = line.split(':')[1].strip()
    return headers
  
 output: 
  {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
 'accept-encoding': 'gzip, deflate, br',
 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,uz;q=0.7',
 'cache-control': 'max-age=0',
 'cookie': '<cookie>',
 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", '
              '"Chromium";v="109"',
 'sec-ch-ua-mobile': '?0',
 'sec-ch-ua-platform': '"Windows"',
 'sec-fetch-dest': 'document',
 'sec-fetch-mode': 'navigate',
 'sec-fetch-site': 'none',
 'sec-fetch-user': '?1',
 'upgrade-insecure-requests': '1',
 'user-agent': '<user-agent>'}
