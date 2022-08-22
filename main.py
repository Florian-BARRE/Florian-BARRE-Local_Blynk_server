"""
Attention ne fonctionne que sur une distribution Linux !
"""

# Librairie(s)
import os
import sys

# Variables / Constantes globles
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
server_path = os.path.join(BASE_DIR, "server-0.41.16.jar")
storage_path = os.path.join(BASE_DIR, "Blynk")

# Main
if "win" in sys.platform:
      cmd = f"cmd /K " \
            f"java -jar {server_path} -dataFolder {storage_path}" 
  
elif "linux" in sys.platform:
      cmd = f"lxterminal -e '" \
            f"cd {BASE_DIR}; " \
            f"echo Run Blynk local server; " \
            f"java -jar {server_path} -dataFolder {storage_path}" \
            f"'"

os.system(cmd)