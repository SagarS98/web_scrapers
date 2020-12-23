from requests_html import HTMLSession
import pandas as pd

urls = ['https://www.amazon.in/Notebook-Horizon-i5-10210U-Graphics-XMA1904-AR/dp/B089F5JGM1?ref_=ast_sto_dp',
        'https://www.amazon.in/Redmi-Note-Shadow-Black-Storage/dp/B089MTR9JB/ref=zg_bs_electronics_2?_encoding=UTF8&psc=1&refRID=R4TFDF2WHPF3M6VWR7W7',
        'https://www.amazon.in/OnePlus-Nord-Gray-256GB-Storage/dp/B08697WT6D/ref=zg_bs_electronics_11?_encoding=UTF8&psc=1&refRID=R4TFDF2WHPF3M6VWR7W7',
        'https://www.amazon.in/gp/product/B08L8DV7BX/ref=s9_acss_bw_cg_Offers_4a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-8&pf_rd_r=9KYFXWPAV6SNSH2J9AGR&pf_rd_t=101&pf_rd_p=973916f9-f587-4014-9c31-3810c8f3293d&pf_rd_i=1389401031']

def getPrice(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)
    try:
        product = {
            'title': r.html.xpath('//*[@id="productTitle"]', first=True).text,
            'price': r.html.xpath('//*[@id="priceblock_ourprice"]', first=True).text
               }
        print(product)
    except:
        product = {
            'title': r.html.xpath('//*[@id="productTitle"]', first=True).text,
            'price': 'item unavailable'
        }
        print(product)
    return product

products = []
for url in urls:
    products.append(getPrice(url))

print(len(products))

detailsdf = pd.DataFrame(products)
detailsdf.to_excel('products.xlsx', index=False)