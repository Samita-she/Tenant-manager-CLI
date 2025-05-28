from data_manager import load_data, save_data
from models import Tenant, Payment
import uuid

tenants = load_data("tenants.json")
payments = load_data("payments.json")

def add_tenant():
    name = input("Tenant name: ")
    unit = input("Unit number: ")
    move_in = input("Move-in date (YYYY-MM-DD): ")
    tenant_id = str(uuid.uuid4())
    tenant = Tenant(tenant_id, name, unit, move_in)
    tenants.append(tenant.to_dict())
    save_data(tenants, "tenants.json")
    print("Tenant added.")

def main_menu():
    while True:
        print("\nTenant Manager CLI")
        print("1. Add Tenant")
        print("2. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_tenant()
        elif choice == "2":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main_menu()
