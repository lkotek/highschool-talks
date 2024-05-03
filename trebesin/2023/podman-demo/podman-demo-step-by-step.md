# Simple podman demo step by step

1. Ensure podman is installed:
`sude dnf install podman`

2. Prepare Dockerfile in directory containing your app (dir app)

3. Change directory into `app` directory

4. Build image:
`podman build .`

5. Check image is build:
`podman images`

6. Tag your image in human-readable way :)
`podman tag <IMAGE ID> bottle`

7. Run your image:
`podman run -p 8084:8081 bottle`

8. Check details about image you built:
`podman inspect bottle`

9. Learn more abour podman and docker: https://podman.io/getting-started/

10. Check existing images in registers:
   - https://hub.docker.com/
   - https://registry.fedoraproject.org/
