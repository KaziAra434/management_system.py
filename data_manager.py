print("📱 Welcome to Smart Contact & Inventory Manager")
print("="*40)

contacts = {}
num_of_contacts = int(input("How many contacts you want to add: "))

for i in range(num_of_contacts):
    print(f"\nEnter Contact details for {i+1}")

    name = input("Enter contact name: ").lower()
    phone = int(input("Enter phone number: "))
    contacts[name] = phone
    
print("\n" + "=" * 10  + " Contact List " + "=" * 10)

for name, phone in contacts.items():
    print(name, "-", phone)
print("="*34)

while True:
    
    update_name = input("\nEnter contact name to update: ").lower()

    if update_name in contacts:
        new_phone = input("Enter new phone number: ")
        contacts[update_name] = new_phone
        print("🟢 Contact updated successfully!")
        break
    else: 
        print("❌ Contact not found!")

while True:

    delete_name = input("\nEnter contact name to delete: ").lower()

    if delete_name in contacts:
        del contacts[delete_name]
        print("✅ Contact deleted successfully!")
        break
    else: 
        print("Contact not found!")

print("\n" + "#"*20 + " Updated Contact List " + "#"*20)

for name, phone in contacts.items():
    print(name, "-", phone)

sample_categories = {"electronics", "food", "sports"}

union_result = categories.union(sample_categories)
difference_result = categories.difference(sample_categories)

print("\n 🛍 Sample Categories:")
print(sample_categories)

print("\nUnion Result:")
print(union_result)

print("\nDifference Result:")
print(difference_result)

inventory = {
    "💻 Laptop": {"price": 50000, "stock": 10},
    "📱 Phone": {"price": 30000, "stock": 20}
}
print("\n" + "^"*20 + " Inventory Details " + "^"*20)

for product, details in inventory.items():
    print("\nProduct:", product)
    print("Price:", details["price"])
    print("Stock:", details["stock"])

    