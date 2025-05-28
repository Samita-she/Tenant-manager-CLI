from data_manager import load_data, save_data
from models import Tenant, Payment
from datetime import datetime
import uuid

MONTHLY_RENT = 10500


data = {
    "tenants": load_data("tenants.json"),
    "payments": load_data("payments.json")
}

def show_menu():
    print("\nTenant Manager CLI")
    print("1. Add Tenant")
    print("2. Record Rent Payment")
    print("3. View Rent Status")
    print("4. Mark Tenant as Moved Out")
    print("5. Exit")



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

    payment = Payment(tenant["tenant_id"], amount, date)
    data["payments"].append(payment.to_dict())
    save_data(data["payments"], "payments.json")
    print("✅ Payment recorded.")
 

def calculate_months_between(start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    months = (end.year - start.year) * 12 + end.month - start.month + 1
    return max(months, 0)

def view_rent_status():
    today = datetime.today().strftime("%Y-%m-%d")
    
    for tenant in data["tenants"]:
        tenant_id = tenant["tenant_id"]
        name = tenant["name"]
        move_in = tenant["move_in_date"]
        move_out = tenant.get("move_out_date")
        end_date = move_out if move_out else today

        months_occupied = calculate_months_between(move_in, end_date)
        expected_rent = months_occupied * MONTHLY_RENT

        total_paid = sum(
            p["amount"] for p in data["payments"] if p["tenant_id"] == tenant_id
        )

        status = "✅ Paid"
        if total_paid < expected_rent:
            status = "⚠️ Partial" if total_paid > 0 else "❌ Unpaid"

        print(f"\nTenant: {name}")
        print(f"Unit: {tenant['unit_number']}")
        print(f"Months Occupied: {months_occupied}")
        print(f"Total Due: {expected_rent}")
        print(f"Total Paid: {total_paid}")
        print(f"Status: {status}")

def mark_moved_out():
    name = input("Enter tenant name to mark as moved out: ")
    tenant = next((t for t in data["tenants"] if t["name"].lower() == name.lower()), None)

    if not tenant:
        print("❌ Tenant not found.")
        return

    if tenant.get("move_out_date"):
        print("⚠️ Tenant already marked as moved out.")
        return

    date = input("Enter move-out date (YYYY-MM-DD), or press Enter for today: ")
    if not date:
        date = datetime.today().strftime("%Y-%m-%d")

    tenant["move_out_date"] = date
    save_data(data["tenants"], "tenants.json")
    print(f"✅ {tenant['name']} marked as moved out on {date}.")


def main_menu():
    while True:
        show_menu()
        choice = input("Select an option: ")
        if choice == "1":
            add_tenant()
        elif choice == "2":
            record_payment()
        elif choice == "3":
            view_rent_status()
        elif choice == "4":
            mark_moved_out()
        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main_menu()
