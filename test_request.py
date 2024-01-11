import requests
 
#API path setting
check_url = "http://127.0.0.1:5000/CheckServerStatus"
exit_url = "http://127.0.0.1:5000/PythonShutdown"
test_url = "http://127.0.0.1:5000/TestPassingData"
 
# region Check server status if it still running
#Create response and checking time elapsed between request and response
response = requests.post(check_url)
print(response)
print(response.json())
print("Request - Response time = " + str(response.elapsed.total_seconds()) + "sec")
# endregion

# region Check passing data from requester to server
#Mock up data in JSON format
data = {
        "text" : "Hello world!!!",
        "intnum" : 25,
        "floatnum" : -2.5325235,
        "boolean" : True
        }

#Create response and checking time elapsed between request and response 
data_response = requests.post(test_url, json=data)
print(data_response)
print(data_response.json())
print("Request - Response time = " + str(data_response.elapsed.total_seconds()) + "sec")
# endregion

#Create killing server and assume local server is closed
exit_response = requests.post(exit_url)
