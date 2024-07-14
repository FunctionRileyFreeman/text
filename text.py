class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def add_item(self, item):
        self.items.append(item)

    def __str__(self):
        return self.name


class Player:
    def __init__(self, current_room):
        self.current_room = current_room
        self.inventory = []

    def move(self, direction):
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
            print(f"You are now in the {self.current_room}.")
            print(self.current_room.description)
        else:
            print("You cannot go that way.")

    def take_item(self, item_name):
        for item in self.current_room.items:
            if item.name.lower() == item_name.lower():
                self.inventory.append(item)
                self.current_room.items.remove(item)
                print(f"You have taken the {item.name}.")
                return
        print("Item not found in this room.")

    def check_inventory(self):
        if not self.inventory:
            print("Your inventory is empty.")
        else:
            print("Inventory:")
            for item in self.inventory:
                print(item.name)


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description


# Create rooms
kitchen = Room("Kitchen", "A room with a stove and sink.")
living_room = Room("Living Room", "A spacious room with a TV and sofa.")
bedroom = Room("Bedroom", "A cozy room with a bed and wardrobe.")

# Create items
knife = Item("Knife", "A sharp kitchen knife.")
remote = Item("Remote", "A TV remote control.")

# Add items to rooms
kitchen.add_item(knife)
living_room.add_item(remote)

# Define room exits
kitchen.add_exit("north", living_room)
living_room.add_exit("south", kitchen)
living_room.add_exit("east", bedroom)
bedroom.add_exit("west", living_room)

# Initialize player
player = Player(kitchen)

# Game loop
while True:
    print()
    print("You are in the", player.current_room)
    print(player.current_room.description)
    command = input("What would you like to do? ").strip().lower()

    if command.startswith("go "):
        direction = command[3:]
        player.move(direction)
    elif command.startswith("take "):
        item_name = command[5:]
        player.take_item(item_name)
    elif command == "inventory":
        player.check_inventory()
    elif command == "quit":
        print("Goodbye!")
        break
    else:
        print("Invalid command. Type 'go direction', 'take item', 'inventory', or 'quit'.")
