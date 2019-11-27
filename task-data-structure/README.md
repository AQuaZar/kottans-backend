# Data Structures API

This application is my solution to practice part of data-structures task during Kottans-backend online course. [Link to the task.](https://github.com/kottans/backend/blob/master/tasks/data-structures.md)

Role of this API is to provide means of interaction with two types of data-structures: stack and linked list. Client can work with data stored on the server's memory. Application accepts two types of requests PUT to change data and GET to receive full view of data-structure. To transfer data from client to server JSON format has to be used as a payload to request, response from server passed as a string.

## Available Data Parameters

### Stack

| Name        | Value              | Description                                                                                                                                       |
| ----------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Put         |
| "data_type" | "stack"            | Specifies that stack data-structure is used                                                                                                       |
| "action"    | "push", "pop"      | Push - adds value specified in "Value" property on top of the stack, pop - removes value from top of the stack and returns it in body of response |
| "value"     | alphanumeric value | Value that will be pushed to the stack                                                                                                            |
| Get         |
| "data_type" | "stack"            | Specifies that stack data is shown                                                                                                                |
| "action"    | "show"             | Full view of stack will be provided in body of server response                                                                                    |

### Linked List

| Name        | Value              | Description                                                                                                                                   |
| ----------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Put         |
| "data_type" | "linked_list"      | Specifies that data from linked-list structure is affected                                                                                    |
| "action"    | "insert", "remove" | Insert - value specified in "Value" property inserted as a head of the list and will point to successor, remove - removes value from the list |
| "successor" | alphanumeric value | Optional parameter, if member of list is provided, value specified in "Value" property will be inserted before specified successor            |
| "value"     | alphanumeric value | Value that will be inserted to the linked list                                                                                                |
| Get         |
| "data_type" | "linked_list"      | Specifies that linked-list data is shown                                                                                                      |
| "action"    | "show"             | Full view of list will be provided in body of server response                                                                                 |

## Examples

For example requests will be used 'requests' python library and 'json' library to serialize data.

    import requests
    import json

    url = "http://localhost:8000/"

    data = {"data_type": "linked_list", "action": "insert", "value": "Joske"}
    data = json.dumps(data)
    r = requests.put(url, data)

In this example the PUT request is performed. As a result of request string _"Joske"_ will be _inserted_ in _linked list_ hold in local server memory.

To check state of our linked list we can use GET request:

    data = {"data_type": "linked_list", "action": "show"}
    data = json.dumps(data)
    r = requests.get(url, data=data)
    print(r.content)

To check the body of respond, 'content' field is used, as result we get:

> 'head -> Joske -> None'
