from dao.PolicyServiceImpl import PolicyServiceImpl
from entity.policy import Policy
from exception.PolicyNotFoundException import PolicyNotFoundException

def display_menu():
    print("\nInsurance Management System")
    print("1. Create Policy")
    print("2. Get Policy")
    print("3. Get All Policies")
    print("4. Update Policy")
    print("5. Delete Policy")
    print("6. Exit")

def main():
    policy_service = PolicyServiceImpl()
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        try:
            if choice == '1':
                # Create Policy
                policy = Policy()
                policy.setPolicyName(input("Enter policy name: "))
                policy.setCoverageDetails(input("Enter coverage details: "))
                policy.setPremium(float(input("Enter premium amount: ")))
                
                if policy_service.create_policy(policy):
                    print("Policy created successfully!")
                else:
                    print("Failed to create policy.")
            
            elif choice == '2':
                # Get Policy
                policy_id = int(input("Enter policy ID: "))
                policy = policy_service.get_policy(policy_id)
                print("\nPolicy Details:")
                print(policy)
            
            elif choice == '3':
                # Get All Policies
                policies = policy_service.get_all_policies()
                print("\nAll Policies:")
                for policy in policies:
                    print(policy)
                    print("-" * 50)
            
            elif choice == '4':
                # Update Policy
                policy_id = int(input("Enter policy ID to update: "))
                policy = policy_service.get_policy(policy_id)
                
                print("\nCurrent Policy Details:")
                print(policy)
                
                policy.setPolicyName(input("Enter new policy name (leave blank to keep current): ") or policy.getPolicyName())
                policy.setCoverageDetails(input("Enter new coverage details (leave blank to keep current): ") or policy.getCoverageDetails())
                new_premium = input("Enter new premium (leave blank to keep current): ")
                if new_premium:
                    policy.setPremium(float(new_premium))
                
                if policy_service.update_policy(policy):
                    print("Policy updated successfully!")
                else:
                    print("Failed to update policy.")
            
            elif choice == '5':
                # Delete Policy
                policy_id = int(input("Enter policy ID to delete: "))
                if policy_service.delete_policy(policy_id):
                    print("Policy deleted successfully!")
                else:
                    print("Failed to delete policy.")
            
            elif choice == '6':
                print("Exiting the system...")
                break
            
            else:
                print("Invalid choice. Please try again.")
        
        except PolicyNotFoundException as e:
            print(f"Error: {e}")
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()