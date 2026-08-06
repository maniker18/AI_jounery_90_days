import json

class agent_network():
    def __init__(self, name, model, isp, targeted_speed):
        self.name = name
        self.model = model
        self.isp = isp
        self.targeted_speed = targeted_speed

    def get_state_dict(self):
        return {
            "name": self.name, 
            "model": self.model,
            "isp": self.isp, 
            "targeted_speed": self.targeted_speed
        }

    def save_profile(self, filename):
        with open(filename, "w") as f:
            json.dump(self.get_state_dict(), f, indent=2)

    @classmethod
    def load_profile(cls, filename):
        with open(filename, "r") as f:
            data = json.load(f)
            return cls(data["name"], data["model"], data["isp"], data["targeted_speed"])

# === TEST ===
print("1. Creating agent...")
jio = agent_network("jio", 2, "ee", True)
print(f"   Name: {jio.name}")

print("\n2. Saving to network.json...")
jio.save_profile("network.json")

print("\n3. Loading from network.json...")
loaded = agent_network.load_profile("network.json")
print(f"   Loaded name: {loaded.name}")
print(f"   Loaded model: {loaded.model}")
print(f"   Loaded isp: {loaded.isp}")
print(f"   Loaded targeted_speed: {loaded.targeted_speed}")

print("\n✅ SUCCESS! Both agents match!")
print(f"   Original: {jio.name} ↔ Loaded: {loaded.name}")