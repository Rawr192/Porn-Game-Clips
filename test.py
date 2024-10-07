import requests

# Define the base URL for the GitHub repository
base_url = "https://api.github.com/repos/Methusan105/Torrents/actions/workflows/"

# List of workflow names
workflow_names = [
    "torrenttools2.yaml",
    # Add more workflow names as needed
]

# Function to run workflow
def run_workflow(workflow_name, file_number):
    url = base_url + workflow_name + "/dispatches"
    headers = {
        "Authorization": "Bearer token",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "ref": "main",
        "inputs": {
            "name": f"Cyberpunk-{file_number:01d}.bin",
            "comment": f"test{file_number:01d}",
            "url": f"https://github.com/Methusan105/Games-and-Programs/releases/download/CP/Cyberpunk-{file_number:01d}.bin",
            "file_name": f"Cyberpunk-{file_number:01d}.bin",
            "piece_size": "auto",  # Piece size set to auto
            "protocol_version": "hybrid",  # Protocol version set to hybrid
            "maximize_disk_space": "true"  # Assuming you want to maximize disk space
        }
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 204:
        print(f"{workflow_name} triggered successfully for file {file_number:03d}!")
    else:
        print("Failed to trigger workflow.")
        print(response.text)

# Run each workflow for each file
for workflow_name in workflow_names:
    for file_number in range(1, 50):
        print(f"Running {workflow_name} for file {file_number:01d}")
        run_workflow(workflow_name, file_number)
