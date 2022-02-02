import requests


url = "https://api.pwnedpasswords.com/range/" + "CBFDA"

res = requests.get(url)
print(res)


def request_api_date(query_char):
    pass
