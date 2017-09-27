# Openshift docker build exercise

Testing how to do OpenShift builds using the Docker strategy.

Create the build configuration:
```
$ cat docker/Dockerfile | oc new-build . --name="hello-openshift" -D -
```

Deploy the application:
```
$ oc new-app --image-stream=hello-openshift
```
