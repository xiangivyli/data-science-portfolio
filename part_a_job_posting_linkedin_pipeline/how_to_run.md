### Virtual Machine, GCP (Optional)
 - Step 1: Generate SSH key [docs](https://cloud.google.com/compute/docs/connect/create-ssh-keys) 
 - Step 2: Add public key to Metadata in Compute Engine
 - Step 3: Create Instance, choose vCPU, memory, Boot disk, etc
 - Step 4: Create **config** file, **Host**, **HostName** (External IP), **User**, **IndentityFile** (PATH/TO/PRIVATEKEY FILE)
 - Step 5: `ssh` + *the host name* to log in 
 - Step 6: VS code adds **Remote - SSH** to control the remote VM

### Prerequisites
1. **Anaconda** [site](https://www.anaconda.com/download)
  - `wget https://repo.anaconda.com/archive/Anaconda3-2024.02-1-Linux-x86_64.sh`
  - `bash Anaconda3-2024.02-1-Linux-x86_64.sh`
  - `yes` 

2. **Docker** (install with *apt-get* under Linux)
  - `sudo apt-get update`
  - `sudo apt-get install docker.io`

  get permission, [reference](https://github.com/sindresorhus/guides/blob/main/docker-without-sudo.md)
  - `sudo groupadd docker`
  - `sudo gpasswd -a $USER docker`
  - log in and log back
  - `sudo service docker restart`
3. **Docker Compose** [site](https://github.com/docker/compose/releases)
  - `mkdir bin`
  - `cd bin/`
  - `wget https://github.com/docker/compose/releases/download/v2.27.0/docker-compose-linux-x86_64 -O docker-compose`
  - `chmod +x docker-compose` #executable mode
  - `nano .bashrc` #run commands file
  - add `export PATH="${HOME}/bin:${PATH}"` #add bin directory to the existing `PATH`
  - `source .bashrc`
4. **Terraform** [site](https://releases.hashicorp.com/terraform)
  - `wget https://releases.hashicorp.com/terraform/1.8.2/terraform_1.8.2_linux_amd64.zip`
  - `sudo apt-get install unzip`
  - `unzip terraform_1.8.2_linux_amd64.zip`
  - `rm terraform_1.8.2_linux_amd64.zip` #remove zip file
5. **Astro Cli** [site](https://docs.astronomer.io/astro/cli/install-cli)
 - `curl -sSL install.astronomer.io | sudo bash -s`



