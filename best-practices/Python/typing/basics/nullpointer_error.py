import requests

def make_api_request(endpoint: str):
    try:
        response = requests.get(endpoint, timeout=5)
        return response
    except Exception as e:
        return None

response_1 = make_api_request(endpoint='https://httpbin.org/get')
response_2 = make_api_request(endpoint='https://httpbin.orgg/get')

response_1.json()
response_2.json() 
