import requests

url = "http://localhost:8000/"

for i in range(1, 10):
    requests.put(url, data={"data_type": "stack", "action": "push", "value": str(i)})
for i in range(1, 3):
    r = requests.put(url, data={"data_type": "stack", "action": "pop"})
    print(r.content)
r = requests.get(url, data={"data_type": "stack", "action": "show"})
print(r)

for i in range(1, 10):
    requests.put(
        url, data={"data_type": "linked_list", "action": "insert", "value": str(i)}
    )

requests.put(
    url,
    data={
        "data_type": "linked_list",
        "action": "insert",
        "value": "A4",
        "successor": "4",
    },
)
requests.put(
    url,
    data={
        "data_type": "linked_list",
        "action": "insert",
        "value": "B8",
        "successor": "8",
    },
)
for i in range(1, 3):
    r = requests.put(
        url, data={"data_type": "linked_list", "action": "remove", "value": str(i)}
    )
r = requests.get(url, data={"data_type": "linked_list", "action": "show"})

print(r.content)

