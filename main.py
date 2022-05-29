# must be imported requests-html
from requests_html import HTMLSession

urllist = ["https://www.amazon.com/Oculus-Quest-Advanced-All-One-Virtual/dp/B099VMT8VZ/?_encoding=UTF8&pf_rd_p=a6eed03c-49da-47d6-ac11-598532cc753a&pd_rd_wg=fAqjb&pf_rd_r=Z3AAB4JD5QXEYBVWZ7GE&content-id=amzn1.sym.a6eed03c-49da-47d6-ac11-598532cc753a&pd_rd_w=GcD8z&pd_rd_r=a0d1c6b1-36a5-4afb-9763-b62ce368762c&ref_=pd_gw_exports_top_sellers_unrec",
           "https://www.amazon.com/Oculus-Quest-Advanced-All-One-Virtual/dp/B09B8DQ26F/ref=lp_21479456011_1_2",
           "https://www.amazon.com/Oculus-Quest-All-Gaming-System-PC/dp/B07HNW68ZC/ref=lp_21479456011_1_5"]


def get_price(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)

    product = {
        'title': r.html.xpath('//*[@id="productTitle"]', first=True).text,
        'price': r.html.xpath('//*[@id="priceblock_ourprice"]', first=True).text
    }
    print(product)
    return product


# url = "https://www.amazon.com/Oculus-Quest-Advanced-All-One-Virtual/dp/B099VMT8VZ/?_encoding=UTF8&pf_rd_p=a6eed03c-49da-47d6-ac11-598532cc753a&pd_rd_wg=fAqjb&pf_rd_r=Z3AAB4JD5QXEYBVWZ7GE&content-id=amzn1.sym.a6eed03c-49da-47d6-ac11-598532cc753a&pd_rd_w=GcD8z&pd_rd_r=a0d1c6b1-36a5-4afb-9763-b62ce368762c&ref_=pd_gw_exports_top_sellers_unrec"
for url in urllist:
    get_price(url=url)

