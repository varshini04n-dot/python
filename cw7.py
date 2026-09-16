items = ["milk", "bread", "eggs"]

def add_item(item):
    items.append(item)

def remove_last_item():
    items.pop()

add_item("Sugar")
remove_last_item()

display = lambda item: print("Item:", item)

for item in items:
    display(item)

def count_characters(items, i=0):
    if i == len(items):
        return 0
    
    return len(items[i]) + count_characters(items, i + 1)

print("Total characters:", count_characters(items))