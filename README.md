<h3>Step 1: Download and it contains four files:</h3>
    <li>  requirements.txt
    <li>  email_process.py
    <li>  Dockerfile
    <li>  emailprocess.yaml

<h3>Step 2: Build docker image </h3>
        	docker build -f Dockerfile -t emailprocess:latest .
    

<h3>Step 3: Deploy the service</h3>
    kubectl apply -f emailprocess.yaml
