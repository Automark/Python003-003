import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
cookie = '__mta=220446631.1597994730833.1597995869673.1597995955033.5; uuid_n_v=v1; uuid=7D7D0B00E37F11EAB90FBBC3BB80078A73B73AF3924844A0997E5775F4CB4193; _csrf=62775efabca3d945bdbfde0217efad354c2c1d5e387201295f9515ac24e3914f; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1597994730; _lxsdk_cuid=1740fe880d982-03d9b23cfb61c8-31627405-13c680-1740fe880dac8; _lxsdk=7D7D0B00E37F11EAB90FBBC3BB80078A73B73AF3924844A0997E5775F4CB4193; mojo-uuid=f9bb7d4ba559a3d06b8e4fc0849ac327; __mta=220446631.1597994730833.1597994791085.1597995857201.4; mojo-session-id={"id":"d26e93ddbfc6805c4f35a1ec45d85769","time":1597999690417}; mojo-trace-id=1; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1597999690; _lxsdk_s=17410342cc6-95e-d4f-71%7C%7C3'

header = {'user-agent': user_agent, 'Cookie': cookie}

myurl = "https://maoyan.com/films?showType=3"

response = requests.get(myurl,headers=header)

bs_info = bs(response.text, 'html.parser')

result = []

for tag in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}, limit=10):
    # 电影名称
    name = tag.find('span', attrs={'class': 'name'}).text
    # 电影类型
    category = tag.find('span', text='类型:').parent.text.split('\n')[-2].strip()
    # 上映时间
    show_time = tag.find('span', text='上映时间:').parent.text.split('\n')[-2].strip()

    result.append(tuple([name, category, show_time]))

movie1 = pd.DataFrame(data = result)
movie1.to_csv('./top10_movie.csv', encoding='utf8', index=False, header=False)

