# Essential Docker Commands Cheat Sheet

---

## **General Commands**

1. **Check Docker Version:**
   ```bash
   docker --version
   ```

2. **Show System-Wide Docker Information:**
   ```bash
   docker info
   ```

---

## **Container Lifecycle**

1. **List Running Containers:**
   ```bash
   docker ps
   ```

2. **List All Containers (Running and Stopped):**
   ```bash
   docker ps -a
   ```

3. **Restart a Stopped Container:**
   ```bash
   docker start <container_id>
   ```

4. **Stop a Running Container:**
   ```bash
   docker stop <container_id>
   ```

5. **Access a Running Container (Interactive Mode):**
   ```bash
   docker exec -it <container_id> bash
   ```

6. **Remove a Specific Container:**
   ```bash
   docker rm <container_id>
   ```

---

## **Advanced Commands**

1. **Run a Container in Detached Mode:**
   ```bash
   docker run -d <image_name>
   ```

2. **Remove All Stopped Containers, Unused Images, and Volumes:**
   ```bash
   docker system prune -a --volumes
   ```

3. **Run a Container with Resource Limits:**
   ```bash
   docker run --memory="512m" --cpus="1" <image_name>
   ```

---

## **Image Management**

1. **List All Docker Images:**
   ```bash
   docker images
   ```

2. **Pull a Specific Image from Docker Hub:**
   ```bash
   docker pull <image_name>:<tag>
   ```
   Example:
   ```bash
   docker pull ubuntu:20.04
   ```

3. **Export an Image to a `.tar` File:**
   ```bash
   docker save -o my_image.tar <image_name>:<tag>
   ```

4. **Load an Image from a `.tar` File:**
   ```bash
   docker load -i my_image.tar
   ```

5. **Tag an Image:**
   ```bash
   docker tag <image_id> <new_image_name>:<tag>
   ```

6. **Push an Image to a Docker Registry:**
   ```bash
   docker push <image_name>:<tag>
   ```

7. **Remove a Specific Image:**
   ```bash
   docker rmi <image_id>
   ```

8. **Remove All Unused Images:**
   ```bash
   docker image prune -a
   ```

---

## **Saving, Importing, and Exporting**

1. **Save a Docker Image to a `.tar` File:**
   ```bash
   docker save -o my_image.tar <image_name>:<tag>
   ```

2. **Load a Docker Image from a `.tar` File:**
   ```bash
   docker load -i my_image.tar
   ```

3. **Export a Container to a `.tar` File:**
   ```bash
   docker export -o my_container.tar <container_id>
   ```

4. **Import a Container's Filesystem from a `.tar` File:**
   ```bash
   cat my_container.tar | docker import - my_container
   ```

---

## **Volume Management**

1. **List All Volumes:**
   ```bash
   docker volume ls
   ```

2. **Create a Named Volume:**
   ```bash
   docker volume create <volume_name>
   ```

3. **Inspect a Volume:**
   ```bash
   docker volume inspect <volume_name>
   ```

4. **Remove a Volume:**
   ```bash
   docker volume rm <volume_name>
   ```

---

## **Networking**

1. **List Docker Networks:**
   ```bash
   docker network ls
   ```

2. **Create a Docker Network:**
   ```bash
   docker network create <network_name>
   ```

3. **Connect a Container to a Network:**
   ```bash
   docker network connect <network_name> <container_id>
   ```

4. **Disconnect a Container from a Network:**
   ```bash
   docker network disconnect <network_name> <container_id>
   ```

---

## **Debugging and Troubleshooting**

1. **View Container Logs:**
   ```bash
   docker logs <container_id>
   ```

2. **Inspect Container Details:**
   ```bash
   docker inspect <container_id>
   ```

3. **Check Resource Usage of Containers:**
   ```bash
   docker stats
   ```

4. **Check Disk Usage of Docker Resources:**
   ```bash
   docker system df
   ```

---


## **Commands for Docker Compose**

1. **Start Services Defined in `docker-compose.yml`:**
   ```bash
   docker-compose up
   ```

2. **Stop Services:**
   ```bash
   docker-compose down
   ```

3. **Rebuild and Start Services:**
   ```bash
   docker-compose up --build
   ```

4. **Check Logs of Services:**
   ```bash
   docker-compose logs
   ```

---


## **Key Cleanup Commands**

1. **Stop All Running Containers:**
   ```bash
   docker stop $(docker ps -q)
   ```

2. **Remove All Containers (Stopped or Running):**
   ```bash
   docker rm $(docker ps -aq)
   ```

3. **Remove All Unused Images:**
   ```bash
   docker image prune -a
   ```

4. **Remove All Docker Resources (DANGEROUS):**
   ```bash
   docker system prune -a --volumes
   ```
