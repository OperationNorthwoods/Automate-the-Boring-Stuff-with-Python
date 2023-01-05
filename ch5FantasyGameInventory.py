# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(f"{v} {k}")
        item_total +=v 
    print(f"Total number of items: {item_total}")

displayInventory(stuff)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory:
            inventory[i]+= 1
        else:
            inventory[i] = 1

addToInventory(stuff, dragonLoot)
displayInventory(stuff)