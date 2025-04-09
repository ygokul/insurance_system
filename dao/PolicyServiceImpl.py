from dao.IPolicyService import IPolicyService
from entity.policy import Policy
from exception.PolicyNotFoundException import PolicyNotFoundException
from util.DBConnUtil import DBConnUtil

class PolicyServiceImpl(IPolicyService):
    def __init__(self):
        self.connection = DBConnUtil.get_connection()
    
    def create_policy(self, policy):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO Policy (policyName, coverageDetails, premium) VALUES (%s, %s, %s)"
            values = (policy.getPolicyName(), policy.getCoverageDetails(), policy.getPremium())
            cursor.execute(query, values)
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error creating policy: {e}")
            return False
    
    def get_policy(self, policy_id):
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM Policy WHERE policyId = %s"
            cursor.execute(query, (policy_id,))
            policy_data = cursor.fetchone()
            
            if not policy_data:
                raise PolicyNotFoundException(policy_id)
                
            policy = Policy()
            policy.setPolicyId(policy_data['policyId'])
            policy.setPolicyName(policy_data['policyName'])
            policy.setCoverageDetails(policy_data['coverageDetails'])
            policy.setPremium(policy_data['premium'])
            
            return policy
        except PolicyNotFoundException as e:
            raise e
        except Exception as e:
            print(f"Error retrieving policy: {e}")
            raise
    
    def get_all_policies(self):
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM Policy"
            cursor.execute(query)
            policies_data = cursor.fetchall()
            
            policies = []
            for policy_data in policies_data:
                policy = Policy()
                policy.setPolicyId(policy_data['policyId'])
                policy.setPolicyName(policy_data['policyName'])
                policy.setCoverageDetails(policy_data['coverageDetails'])
                policy.setPremium(policy_data['premium'])
                policies.append(policy)
            
            return policies
        except Exception as e:
            print(f"Error retrieving all policies: {e}")
            raise
    
    def update_policy(self, policy):
        try:
            cursor = self.connection.cursor()
            query = "UPDATE Policy SET policyName = %s, coverageDetails = %s, premium = %s WHERE policyId = %s"
            values = (policy.getPolicyName(), policy.getCoverageDetails(), policy.getPremium(), policy.getPolicyId())
            cursor.execute(query, values)
            self.connection.commit()
            
            if cursor.rowcount == 0:
                raise PolicyNotFoundException(policy.getPolicyId())
                
            return True
        except PolicyNotFoundException as e:
            raise e
        except Exception as e:
            print(f"Error updating policy: {e}")
            return False
    
    def delete_policy(self, policy_id):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM Policy WHERE policyId = %s"
            cursor.execute(query, (policy_id,))
            self.connection.commit()
            
            if cursor.rowcount == 0:
                raise PolicyNotFoundException(policy_id)
                
            return True
        except PolicyNotFoundException as e:
            raise e
        except Exception as e:
            print(f"Error deleting policy: {e}")
            return False
    
    def __del__(self):
        if self.connection:
            self.connection.close()