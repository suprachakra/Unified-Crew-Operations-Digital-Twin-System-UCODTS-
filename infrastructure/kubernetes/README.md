## Kubernetes Manifests

### Overview
This directory contains Kubernetes manifests used to deploy UCODTS services on a Kubernetes cluster. These manifests include definitions for deployments, services, and ingress resources.

### Files
- **deployment.yaml**: Sample Deployment manifest for a generic service.
- **service.yaml**: Sample Service manifest to expose the deployment.
- **ingress.yaml**: Sample Ingress resource for routing external traffic.
  
### Usage
- Customize these manifests according to your service specifics.
- Use `kubectl apply -f <filename>` to deploy the resources.
- Refer to this documentation for best practices on scaling and security.
