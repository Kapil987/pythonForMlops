### 🐳 Basic Docker Commands

#### 🔧 **Container Management**

* `docker run hello-world` – Run a test container
* `docker run -it ubuntu /bin/bash` – Run container interactively
* `docker ps` – List running containers
* `docker ps -a` – List all containers
* `docker stop <container_id>` – Stop running container
* `docker start <container_id>` – Start a stopped container
* `docker restart <container_id>` – Restart container
* `docker rm <container_id>` – Remove container
* `docker logs <container_id>` – View container logs
* `docker exec -it <container_id> bash` – Run command inside container

#### 📦 **Image Management**

* `docker images` – List images
* `docker pull <image>` – Download image
* `docker build -t myimage .` – Build image from Dockerfile
* `docker rmi <image_id>` – Remove image
* `docker tag <image_id> myrepo/myimage:tag` – Tag image
* `docker push myrepo/myimage:tag` – Push image to registry

#### 📁 **Volumes & Files**

* `docker volume ls` – List volumes
* `docker volume create <name>` – Create volume
* `docker run -v myvol:/data ubuntu` – Mount volume
* `docker cp <container_id>:/file/path ./host` – Copy file from container
* `docker cp ./host <container_id>:/file/path` – Copy file to container

#### 🧰 **Others**

* `docker network ls` – List networks
* `docker inspect <container/image>` – View detailed metadata
* `docker stats` – Live container resource usage
* `docker system prune` – Remove unused data

### 📦 Docker Compose Commands

#### ⚙️ **Setup & Build**

* `docker compose up` – Start services defined in `docker-compose.yml`
* `docker compose up -d` – Start in detached mode
* `docker compose build` – Build or rebuild services
* `docker compose build --no-cache` – Build without using cache

#### 🧹 **Cleanup**

* `docker compose down` – Stop and remove containers, networks, etc.
* `docker compose down -v` – Also remove volumes
* `docker compose rm` – Remove stopped containers

#### 🔄 **Restart / Stop**

* `docker compose stop` – Stop running containers
* `docker compose start` – Start stopped containers
* `docker compose restart` – Restart all services

#### 📋 **Info & Debug**

* `docker compose ps` – List containers
* `docker compose logs` – View logs
* `docker compose logs -f` – Follow logs
* `docker compose exec <service> <cmd>` – Run command in running container
* `docker compose run <service> <cmd>` – Run one-off command

#### 📂 **File-specific**

* `docker compose -f custom.yml up` – Use specific YAML file

