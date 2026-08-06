import os
from pathlib import Path



class Agent:
    total_agents = 0  # Class variable to track total instances
    
    def __init__(self, first_name, last_name, model):
        self.first_name = first_name
        self.last_name = last_name
        self.model = model
        self._email = f"{first_name.lower()}.{last_name.lower()}@ai.com"
        Agent.total_agents += 1
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, new_email):
        self._email = new_email
    
    @staticmethod
    def is_supported_model(model_name):
        supported_models = ["gpt-4", "gpt-4o", "claude-3", "claude-3-5-sonnet", "llama-3"]
        return model_name in supported_models
    
    @classmethod
    def from_config(cls, config_string):
        # Parse config string like "Alpha-claude-3-5-sonnet"
        parts = config_string.split("-", 1)
        first_name = parts[0]
        model = parts[1].replace("-", " ")  # Clean up model name
        return cls(first_name, "Default", model)

class WorkspaceAgent(Agent):
    def __init__(self, first_name, last_name, model, workspace_dir):
        super().__init__(first_name, last_name, model)
        self.workspace_dir = workspace_dir
    
    def sync_workspace(self):
        if os.path.exists(self.workspace_dir):
            return f"Directory already exists: {self.workspace_dir}"
        else:
            os.makedirs(self.workspace_dir, exist_ok=True)
            return f"Created directory: {self.workspace_dir}"

# ===== YOUR TASKS =====

# 1. Use Agent.is_supported_model("gpt-4o") and print the result
print("=== Task 1: Check supported model ===")
result = Agent.is_supported_model("gpt-4o")
print(f"Is 'gpt-4o' supported? {result}")

# 2. Create an Agent using Agent.from_config("Alpha-claude-3-5-sonnet") and print its email
print("\n=== Task 2: Create Agent from config and print email ===")
alpha_agent = Agent.from_config("Alpha-claude-3-5-sonnet")
print(f"Alpha agent email: {alpha_agent.email}")

# 3. Create a WorkspaceAgent named "Beta" "Core", using model "llama-3", with workspace path "agent_workspace"
print("\n=== Task 3: Create WorkspaceAgent ===")
beta_agent = WorkspaceAgent("Beta", "Core", "llama-3", "agent_workspace")
print(f"Created WorkspaceAgent: {beta_agent.first_name} {beta_agent.last_name}")
print(f"Model: {beta_agent.model}")
print(f"Workspace: {beta_agent.workspace_dir}")
print(f"Initial email: {beta_agent.email}")

# 4. Update the WorkspaceAgent email using the setter to "gamma.ray@aicore.com" 
#    and print first_name to verify it updated
print("\n=== Task 4: Update email and verify ===")
print(f"Before update - First name: {beta_agent.first_name}, Email: {beta_agent.email}")
beta_agent.email = "gamma.ray@aicore.com"
print(f"After update - First name: {beta_agent.first_name}, Email: {beta_agent.email}")

# 5. Call sync_workspace() twice on the WorkspaceAgent and print both output strings
print("\n=== Task 5: Sync workspace twice ===")
first_sync = beta_agent.sync_workspace()
print(f"First sync: {first_sync}")

second_sync = beta_agent.sync_workspace()
print(f"Second sync: {second_sync}")

# 6. Print Agent.total_agents to verify the count accurately reflects all instances created
print("\n=== Task 6: Verify total agents count ===")
print(f"Total agents created: {Agent.total_agents}")
print(f"Expected: 2 (Alpha agent + Beta WorkspaceAgent)")