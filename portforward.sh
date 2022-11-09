#!/bin/bash

killall -9 kubectl
kubectl port-forward --namespace asu $(kubectl get po -n asu | grep pubchem-db | \awk '{print $1;}') 5432:5432 &
