#waiting for a certain number of pods to be ready in a Kubernetes deployment. 

import subprocess
import time
import json

def get_ready_replicas(deployment_name, namespace='default'):
    try:
        # Execute the kubectl command and capture the output in JSON format
        result = subprocess.run(['kubectl', 'get', 'deployment', deployment_name, '-n', namespace, '-o', 'json'],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        
        # Parse the JSON output
        deployment_info = json.loads(result.stdout)
        
        # Extract the number of ready replicas
        ready_replicas = deployment_info['status'].get('readyReplicas', 0)
        desired_replicas = deployment_info['spec']['replicas']
        
        return ready_replicas, desired_replicas
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e.stderr}")
        return 0, 0

def wait_for_pods_ready(deployment_name, namespace='default'):
    while True:
        ready_replicas, desired_replicas = get_ready_replicas(deployment_name, namespace)
        if ready_replicas == desired_replicas:
            print(f"All {desired_replicas} pods are ready.")
            break
        else:
            print(f"Waiting for pods to be ready... {ready_replicas}/{desired_replicas} are ready.")
            time.sleep(10)

# Example usage
deployment_name = 'myapp'
namespace = 'default'  # Change this to the appropriate namespace if needed
wait_for_pods_ready(deployment_name, namespace)
