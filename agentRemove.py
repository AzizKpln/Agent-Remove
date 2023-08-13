import subprocess

agentList=open("agents.txt","r",encoding="utf-8")
readAgent=agentList.readlines()

for agent in readAgent:
  agent=agent.strip()
  subprocess.call(f"/var/ossec/bin/manage_agents -r {str(agent)}",shell=True)
