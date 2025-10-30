import time

class HashTableLinked:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)

        if self.table[index] is None:
            self.table[index] = self.Node(key, value)
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next

            new_node = self.Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

    def search(self, key):
        index = self._hash(key)

        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def __len__(self):
        return self.size

    def print_table(self):
        for i, bucket in enumerate(self.table):
            print(f"{i}:", end="")
            current = self.table[i]
            while current:
                print(f"[{current.key}={current.value}]", end="")
                current = current.next
            print()


class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"[{self.product_id}] {self.name} - RM{self.price:.2f} (Qty: {self.quantity})"


def main():
    inventory = HashTableLinked(20)

    # Sample initial products
    products = [
        Product("P001", "Baby Milk", 45.50, 20),
        Product("P002", "Diapers", 30.00, 50),
        Product("P003", "Baby Lotion", 18.90, 35),
        Product("P004", "Baby Stroller", 399.00, 5),
    ]

    for product in products:
        inventory.insert(product.product_id, product)

    while True:
        print("\n==== Baby Shop Inventory System ====")
        print("1. Insert Product")
        print("2. Search Product")
        print("3. Show Hash Table")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            pid = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            price = float(input("Enter Price: "))
            qty = int(input("Enter Quantity: "))
            product = Product(pid, name, price, qty)
            inventory.insert(pid, product)
            print("Product inserted successfully!")

        elif choice == "2":
            pid = input("Enter Product ID to search: ")
            result = inventory.search(pid)
            if result:
                print("Found:", result)
            else:
                print("Product not found.")

        elif choice == "3":
            print("\nCurrent Hash Table:")
            inventory.print_table()

        elif choice == "4":
            print("Exiting... Bye!")
            break

        else:
            print("⚠Invalid choice. Try again.")


def performance_test():
    print("\n==== Performance Test ====")
    records = [Product(f"P{i:03}", f"Product{i}", i * 10, i * 5) for i in range(1, 5000)]

    ht = HashTableLinked(1000)
    for p in records:
        ht.insert(p.product_id, p)

    arr = records[:]
    search_key = "P2500"

    start = time.time()
    result_ht = ht.search(search_key)
    ht_time = time.time() - start

    start = time.time()
    result_arr = None
    for p in arr:
        if p.product_id == search_key:
            result_arr = p
            break
    arr_time = time.time() - start

    print(f"Hash Table Search Time: {ht_time:.8f} sec -> {result_ht}")
    print(f"Array Search Time: {arr_time:.8f} sec -> {result_arr}")

    if ht_time < arr_time:
        print("\nHash Table is faster — O(1) average search time.")
    else:
        print("\nArray was faster (possibly due to Python overhead).")


if __name__ == "__main__":
    main()
    performance_test()
