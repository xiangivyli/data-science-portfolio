### Virtual Machine, GCP (Optional)
Step 1: Generate SSH key [docs](https://cloud.google.com/compute/docs/connect/create-ssh-keys) 
Step 2: Add public key to Metadata in Compute Engine
Step 3: Create Instance, choose vCPU, memory, Boot disk, etc
Step 4: Create **config** file, **Host**, **HostName** (External IP), **User**, **IndentityFile** (PATH/TO/PRIVATEKEY FILE)

### Prerequisites
1. Anaconda [site](https://www.anaconda.com/download)
1. Docker and Docker Compose