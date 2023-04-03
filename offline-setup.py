with open('launch.py', 'r') as file :
  filedata = file.read()

filedata = filedata.replace('run_pip(f\"install -r {requirements_file}\", \"requirements for Web UI\")', '#run_pip(f\"install -r {requirements_file}\", \"requirements for Web UI\")')
filedata = filedata.replace('run_pip(f\"install -r \\\"{requirements_file}\\\"\", \"requirements for Web UI\")', '#run_pip(f\"install -r \\\"{requirements_file}\\\"\", \"requirements for Web UI\")')

with open('launch-offline.py', 'w') as file:
  file.write(filedata)


with open('webui.bat', 'r') as file :
  filedata = file.read()

filedata = filedata.replace('launch.py', 'launch-offline.py')

with open('webui-offline.bat', 'w') as file:
  file.write(filedata)
