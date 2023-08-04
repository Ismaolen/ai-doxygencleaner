#!/bin/bash

docker build -t doxycleaner .
docker tag doxycleaner registry.gitlab.com/ismsh/ai-doxygencleaner/doxycleaner:latest
docker login registry.gitlab.com
docker push registry.gitlab.com/ismsh/ai-doxygencleaner/doxycleaner:latest
