import requests
import datetime
from newsapi import NewsApiClient
import urllib.request
import urllib.parse

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
SMS_ENDPOINT = "https://api.textlocal.in/"
NEWS_API_KEY = "0d5419315b4545eea5d58606c6fa3428"
STOCKS_API_KEY = "P8U5BQF0WWT7SXZQ"
SMS_API_KEY = "NDU0NDcwN2E0ZTU3MzM3MTU5Njc0NTY0NmY2OTMwNDc="
print(datetime.date.today() - datetime.timedelta(1))
date_y = "2023-05-19"
date_y_y = "2023-05-18"

stocks_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCKS_API_KEY,
}
news_parameters = {
    "q": COMPANY_NAME,
    "from_param": datetime.date.today(),
    "to": date_y_y,
    "sortBy": "popularity",
    # "language":
}
# text_params = {
#     "username": "ayushrajput1708@gmail.com",
#     "apiKey": SMS_API_KEY,
#     "numbers": {"917889440379"},
#     "message": {'Hi, This is a Sample message'},
#
# }

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
# HINT 2: Work out the value of 5% of yerstday's closing stock price.

def calculate_percent(a, b):
    x = a - b
    return (a - x) / 100


def price_change():
    request_stock = requests.get(STOCK_ENDPOINT, params=stocks_parameters)
    request_stock.raise_for_status()
    stocks_data = request_stock.json()
    yesterday_price = float(stocks_data["Time Series (Daily)"].get(date_y).get("4. close"))
    day_before_yesterday_price = float(stocks_data["Time Series (Daily)"].get(date_y_y).get("4. close"))
    print(yesterday_price, day_before_yesterday_price)
    percentage_change = calculate_percent(yesterday_price, day_before_yesterday_price)
    print(percentage_change)
    if percentage_change > 5:
        get_news()


price_change()


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
# HINT 1: Think about using the Python Slice Operator
def get_news():
    newsapi = NewsApiClient(api_key=NEWS_API_KEY)
    top_headlines = newsapi.get_everything(q=COMPANY_NAME,
                                           language='en',
                                           from_param=datetime.date.today(),
                                           to=date_y_y,
                                           sort_by="popularity")
    top10_articles = top_headlines["articles"][:2]
    main_message = ""
    for i in top10_articles:
        main_message += i["title"]

    print(main_message)
    print(top10_articles)


get_news()

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
# HINT 1: Consider using a List Comprehension.


# sms_response = requests.post(SMS_ENDPOINT,params=text_params)
# print(sms_response.json())
# text_params = {
#     "apiKey": SMS_API_KEY,
#     "numbers": "917889440379",
#     "message": "hello 789",
#     "sender": "Ayush",
#     "text": "true",
# }
# f = urllib.request.urlopen('https://api.textlocal.in/send/?' + urllib.parse.urlencode(text_params))
# print(f.read(), f.code)


# def sendSMS(numbers, sender, message):
#     params = {'apikey': SMS_API_KEY, 'numbers': numbers, 'message': message, 'sender': sender, "test": "true"}
#     f = urllib.request.urlopen('https://api.textlocal.in/send/?'
#                                + urllib.parse.urlencode(params))
#     return (f.read(), f.code)
#
#
# resp, code = sendSMS('917889440379',
#                      'Jims Autos', 'Test with ')
# print(resp)

# import requests
url = 'https://api.textlocal.in/send/'
params = {
    "username": "ayushrajput1708@gmail.com",
    "apiKey": SMS_API_KEY,
    "message": "hi 890",
    "numbers": "917889440379",
    "test": "true",
}
sms_response = requests.post(url, params)
print(sms_response.content)

# def send_sms(url,params):
#     url = url+'send'
#     #Phone numbers inside braces {} in commas
#     numbers={'917889440379'}
#     message = {'Hi, This is a Sample message'}
#     params['numbers'] = numbers
#     params['message'] = message
#     response = requests.post(url,params=params)
#     return response.json()
#
# print(send_sms(url, params))



# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
