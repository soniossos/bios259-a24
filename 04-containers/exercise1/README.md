# Docker hands-on exercise 1

## Introduction

This exercise will guide you through modifying a Dockerfile and pushing the resulting Docker image to Docker Hub. The Dockerfile contains a simple Python application that takes a ``--name`` argument with a default value. Your task is to replace the default name with your first name and then rebuild and push the modified Docker image to Docker Hub.

## Instructions
Please follow the step-by-step instructions to complete this hands-on-excercise.

#### 1. **Fork the repository**:
First go to the GitHub repo **https://github.com/asntech/bios259-a24** and click the **Fork** button in the top-right corner to create a copy of the repository under your GitHub account.

#### 2. **Clone the Forked Repository**: 
Next, clone the repository containing the `Dockerfile` and the Python application `app.py` in the `04-containers/exercise1` directory.

Use the following command to clone the forked repository to your local machine:
    
```bash
git clone https://github.com/<your-github-id>/bios259-a24.git   
```

Replace `<your-github-id>` with your GitHub username.


#### 3. **Create a Branch**:

First navigate into the repository directory using `cd`

```bash
cd bios259-a24
```
Create a new branch and name it with your SUNetID:
```bash
git checkout -b <your-SUNet-id>
```

#### 4. Create a Solution Directory
Create a folder named as your SUNet ID in the solutions directory:
Replace `<your-SUNet-id>` with your SUNet ID.

```bash
mkdir -p 04-containers/solutions/<your-SUNet-id>/exercise1
```

#### 5. Copy the excerise files and work on your solutions
Inside the directory you just created, write your solution to the exercise 1.

```bash
cp 04-containers/exercise1/Dockerfile 04-containers/solutions/<your-SUNet-id>/exercise1/
cp 04-containers/exercise1/app.py 04-containers/solutions/<your-SUNet-id>/exercise1/
```
Optionally, you can create a `README.md` file in the directory with your name and some details.


#### 6. **Modify the Dockerfile**:

Now move to the solutions directory and start editing the files.

```bash
cd 04-containers/solutions/<your-SUNet-id>/exercise1/
```
Try to `ls` and you should see `Dockerfile` and `app.py`.

Open the `app.py` in a text editor or use vim/nano. Find the line that sets the default value for the `--name` argument. Replace the default name with your first name. And also update the version to `1.1.0`


#### 7. **Build the Docker image**:
Once you have modified the `app.py`, build the Docker image using the `docker build` command. Replace `<image_name>` with a `bios259` name for your Docker image.

```bash
docker build -t <image_name> .
```

#### 8. **Run the Docker container**:
After the image is built successfully, you can run a container from the image to ensure it works as expected.

```bash
docker run <image_name>
```
Ensure that your first name is displayed as expected in the application output.

#### 9. **Push the Docker image to Docker Hub**:

Now, it's time to push your modified Docker image to Docker Hub. First, log in to Docker Hub using the `docker login` command.

```bash
docker login
```

Enter your DockerHub login credentials when prompted.

#### 10. Tag your Docker image
Next tag your image with your DockerHub username and the desired repository name.

Use `bios259` as image name and `a24` as version.

```bash
docker tag <image_name> <docker-hub-username>/<image_name>:<version>
```

#### 11. Push the image to DockerHub
Finally, you can now push the tagged Docker image to your Docker Hub.

```bash
docker push <docker-hub-username>/<image_name>:<version>
```

#### 12. Verify on DockerHub:
Visit your DockerHub (https://hub.docker.com/) profile on the web and confirm that your Docker image has been pushed successfully.

#### 13. Push changes to GitHub
Let's brush up your Git skills now! :-)

Because you may want to commit and push the changes you made to the forked Github repo. This does happend in the real world.

Can you figure out yourself, how you can add these change, commit and then push to the remote branch?
Note: Make you're in the main course repo, not still in the solutions direcotry.

```bash
git push origin <your-SUNet-id>
```

#### 14. Make a Pull Request
- Go to the original repository: asntech/bios259-a24.
- Click on Pull Requests and then New Pull Request. 
- Select your branch as the source branch and submit the pull request.

> ***True happiness is when your PR gets accepted! I don't mean permanent residence—I mean pull request!*** 😄

## Conclusion

Congratulations! You have successfully modified the code in a Docker image `app.py`, built a Docker image with your changes, and pushed it to DockerHub. The pushed the changes to GitHub and made your first Pull Request. This exercise demonstrates a basic workflow for Docker image modification, distribution and Github contribution.
