# Deployment of Meteorite Landings Application to Kubernetes

Now that we have created the Meteorite Landings Data Application found [here](https://github.com/ianwood314/homeworks/tree/main/homework05),
we can to deploy the application to Kubernetes to improve the usability and scalability of the application.

## Deploy the Software System to Kubernetes

### Deploy Redis Server to Kubernetes
1. Deploy the Redis Deployment
    - `kubectl apply -f ianwood-test-redis-deployment.yml`
2. Deploy the Redis Persistant Volume Claim
    - `kubectl apply -f `ianwood-test-redis-pvc.yml`
3. Deploy the Redis Service
    - `kubectl apply -f `ianwood-test-redis-service.yml`

### Deploy Flask App to Kubernetes
1. Deploy the Flask Deployment
    - `kubectl apply -f ianwood-test-flask-deployment.yml`
2. Deploy the Flask Service
    - `kubectl apply -f ianwood-test-flask-service.yml`

To see a list of all of the deployments and the pods created from those deployments, type 
`kubectl get all` in the terminal.
