Contacts = {
    "Amit": "9876543210",
    "Neha": "9123456780",
    "Rahul": "9988776655"
}

contacts["Simran"] = "9012345678"
contacts["Amit"] = "9999999999"

print("Lookup Neha:", contacts.get("Neha"))


print("Lookup Karan:", contacts.get("Karan", "Contact not found"))
print("\nContact List:")
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")
