# DevOps Coding Exercise

Welcome! The goal of this exercise is to highlight your skills as a DevOps Engineer, particularly with Kubernetes and Python programming.

## Required Tools

- Python 3.9+
- Kubernetes cluster (Minikube, Docker Desktop, Rancher Desktop, etc.)
- Git

## Scenario

The DevOps team has started to build a Python Web Service intended to run on Kubernetes. The application is a simple HTTP server that returns a list of pods running on a specified node or set of nodes. Your task is to pick up where your DevOps teammate left off and complete the work.

## Task 1: Python Programming

Implement the Node Pod Grouper Service:

- The class should have an `__init__` method to initialize a connection to the Kubernetes API.
- The `get_node` method should return all pods on a given node by node name.
- The `get_nodes` method should return a dictionary mapping node names to lists of pods on those nodes.

## Task 2: Docker Container Build

The Docker container is currently not building. Your tasks are to:

- Debug the issue
- Fix the issue
- Improve and enhance the Dockerfile as needed

## Task 3: Kubernetes Deployment

Create the necessary Kubernetes manifests to deploy this app to a cluster, exposing it via a ClusterIP Service.

> Note: Kubernetes resources should follow common best practices and design principles.

## Submitting Your Work

Make meaningful commits throughout your work to demonstrate how you break up and approach tasks. Once you have completed all tasks, create an archive of your local git repository and submit it via email.
