from data_manager import load_data, save_data
from models import Tenant, Payment
import uuid

data = {
    "tenants": load_data("tenants.json"),
    "payments": load_data("payments.json")
}

def show_menu():
    print("\nTenant Manager CLI")
    print("1. Add Tenant")
    print("2. Record Rent Payment")
    print("3. Exit")

def add_tenant():
    name = input("Tenant name: ")
    unit = input("Unit number: ")
    move_in = input("Move-in date (YYYY-MM-DD): ")
    tenant_id = str(uuid.uuid4())
    tenant = Tenant(tenant_id, name, unit, move_in)
    tenants.append(tenant.to_dict())
    save_data(tenants, "tenants.json")
    print("Tenant added.")

def record_payment():
    tenant_name = input("Enter tenant name: ")
    matching_tenants = [t for t in data["tenants"] if t["name"].lower() == tenant_name.lower()]

    if not matching_tenants:
        print("❌ No tenant found with that name.")
        return

    tenant = matching_tenants[0]
    amount = float(input("Enter payment amount: "))
    date = input("Enter payment date (YYYY-MM-DD): ")

    payment = Payment(tenant["id"], amount, date)
    data["payments"].append(payment.to_dict())
    save_data(data)
    print("✅ Payment recorded.")
 

def main_menu():
    while True:
        show_menu()
        choice = input("Select an option: ")
        if choice == "1":
            add_tenant()
        elif choice == "2":
            record_payment()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main_menu()
