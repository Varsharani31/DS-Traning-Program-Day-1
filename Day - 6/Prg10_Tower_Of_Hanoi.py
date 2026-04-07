# TOWER OF HONOI

# here we have 3 pipe and n disk
# we can move only one disk at a time
# we can move only 1 dist from any one pipe
# we can move only top most plate
# we cannot move bigger disk on top of smaller plate
# we can move only smaller disk on bigger disk

class TowerOfHonoi:
    def __init__(self,n):
        self.n = n
        self.a = list(range(n, 0, -1))
        self.b = []
        self.c = []
        self.step = 0

    def print_state(self, disk_moved):
        self.step += 1
        print(f"Step {self.step}: Moved disk {disk_moved}")
        print(f"  Pipe A: {self.a}")
        print(f"  Pipe B: {self.b}")
        print(f"  Pipe C: {self.c}\n")

    def move(self,n,a,b,c):
        if n == 1:
            disk = a.pop()
            c.append(disk)
            self.print_state(disk)
            return
        self.move(n-1,a,c,b)
        disk = a.pop()
        c.append(disk)
        self.print_state(disk)
        self.move(n-1,b,a,c)

    def start(self):
        print("Initial state:")
        print("Pipe A:", self.a)
        print("Pipe B:", self.b)
        print("Pipe C:", self.c)
        print("\nMoving disks...")
        
        self.move(self.n,self.a,self.b,self.c)
        
        print("\nFinal state:")
        print("Pipe A:", self.a)
        print("Pipe B:", self.b)
        print("Pipe C:", self.c)

# Example usage:
n = int(input("Enter Size Of Disk : "))
hanoi = TowerOfHonoi(n)
hanoi.start()




# Output =
# Enter Size Of Disk : 3
# Initial state:
# Pipe A: [3, 2, 1]
# Pipe B: []
# Pipe C: []

# Moving disks...
# Step 1: Moved disk 1
#   Pipe A: [3, 2]
#   Pipe B: []
#   Pipe C: [1]

# Step 2: Moved disk 2
#   Pipe A: [3]
#   Pipe B: [2]
#   Pipe C: [1]

# Step 3: Moved disk 1
#   Pipe A: [3]
#   Pipe B: [2, 1]
#   Pipe C: []

# Step 4: Moved disk 3
#   Pipe A: []
#   Pipe B: [2, 1]
#   Pipe C: [3]

# Step 5: Moved disk 1
#   Pipe A: [1]
#   Pipe B: [2]
#   Pipe C: [3]

# Step 6: Moved disk 2
#   Pipe A: [1]
#   Pipe B: []
#   Pipe C: [3, 2]

# Step 7: Moved disk 1
#   Pipe A: []
#   Pipe B: []
#   Pipe C: [3, 2, 1]


# Final state:
# Pipe A: []
# Pipe B: []
# Pipe C: [3, 2, 1]