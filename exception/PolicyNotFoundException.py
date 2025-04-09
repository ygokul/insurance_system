class PolicyNotFoundException(Exception):
    def __init__(self, policy_id):
        super().__init__(f"Policy with ID {policy_id} not found")
        self.policy_id = policy_id