Step 1: Download and it contains four files:
        * requirements.txt
        * email_process.py
        * Dockerfile
        * emailprocess.yaml

Step 2: Build docker image
    docker build -f Dockerfile -t emailprocess:latest .

Step 3: Deploy the service
    kubectl apply -f emailprocess.yaml
    
For example:
