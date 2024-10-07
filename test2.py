import requests

# Define the base URL for the GitHub repository
base_url = "https://api.github.com/repos/Methusan105/Torrents/actions"

# Set the headers with your GitHub personal access token
headers = {
    "Authorization": "Bearer token",
    "Accept": "application/vnd.github.v3+json"
}

# Step 1: Get the list of workflow runs
runs_url = f"{base_url}/runs"
response = requests.get(runs_url, headers=headers)

if response.status_code == 200:
    # Get the list of workflow runs from the response
    workflow_runs = response.json()["workflow_runs"]

    # Step 2: Download Artifacts for Each Workflow Run
    for run in workflow_runs:
        workflow_run_id = run["id"]
        artifacts_url = f"{base_url}/runs/{workflow_run_id}/artifacts"
        artifacts_response = requests.get(artifacts_url, headers=headers)

        if artifacts_response.status_code == 200:
            # Get the list of artifacts from the response
            artifacts = artifacts_response.json()["artifacts"]

            # Print the artifact names before sorting
            print("Artifact names before sorting:")
            for artifact in artifacts:
                print(artifact["name"])

            # Sort the artifacts by name in ascending order
            sorted_artifacts = sorted(artifacts, key=lambda x: x["name"])

            # Download each artifact
            for artifact in sorted_artifacts:
                artifact_id = artifact["id"]
                artifact_name = artifact["name"]
                download_url = artifact["archive_download_url"]

                # Make the GET request to download the artifact
                artifact_response = requests.get(download_url, headers=headers)

                # Save the artifact to a file
                with open(f"{artifact_name}.zip", "wb") as file:
                    file.write(artifact_response.content)

                print(f"Downloaded artifact: {artifact_name}")
        else:
            print(f"Failed to retrieve artifacts for workflow run {workflow_run_id}.")
            print(artifacts_response.text)
else:
    print("Failed to retrieve workflow runs.")
    print(response.text)