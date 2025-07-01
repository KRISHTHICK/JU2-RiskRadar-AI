import subprocess

def get_risk_agent_response(prompt):
    command = f"A user asks a finance/investment question: {prompt}"
    result = subprocess.run(["ollama", "run", "tinyllama", command], capture_output=True, text=True)
    return result.stdout.strip()
