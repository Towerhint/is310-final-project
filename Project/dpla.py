import requests

api_key_dpla = "be74c4fbc809777371970ca172113645"

# Trying boolean search for "Berlin magazine page"
url = 'https://api.dp.la/v2/items?q=kittens&api_key='


def dpla(tosearch='', url_head='https://api.dp.la/v2/items?q=', url_end='&api_key=', api_key='be74c4fbc809777371970ca172113645'):
    result = list()
    response = requests.get(url_head + tosearch + url_end + api_key)
    file = response.json()

    for item in file['docs']:
        temp = dict()

        if 'object' in item and 'description' in item['sourceResource']:
            temp['Url of where it comes from'] = item['isShownAt']
            temp['Data provider'] = item['dataProvider']
            temp['Image'] = item['object']
            temp['More info'] = item['sourceResource']['description']

            result.append(temp)

    return result

# def get_content(url='', keyword=''):
#     content = scrape_webpage(url)
#     links = soup.find_all('a')

# dpla_data = dpla(tosearch='yodeling')
# for item in dpla_data:
#     print(item)

# It is a 350x350 small image to be shown

# print(dpla_data['docs'][0]['object'])

# It slices the first item!!
# print(dpla_data['docs'][1])

# We need to get some information:
# 1. Url of where it comes from: isShownAt
# 2. Data provider: dataProvider
# 3. Image: object
# 4. More info: subject

# print(dpla_data['docs'][2]['isShownAt'])
# print("---------")
#
# print(dpla_data['docs'][2]['dataProvider'])
# print("---------")
#
# print(dpla_data['docs'][2]['object'])
# print("---------")
#
# print(dpla_data['docs'][2]['sourceResource'])
# print("---------")

# for key,value in dpla_data['docs'][0].items():
#     print(key)
#     print(value)
#     print("---------")
