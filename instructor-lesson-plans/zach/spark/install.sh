#!/usr/bin/env bash

brew tap adoptopenjdk/openjdk
brew cask install adoptopenjdk11

java -version
# should see v11

# modify rc?
# export JAVA_HOME=$(/usr/libexec/java_home)

python -m pip install pyspark

pyspark

>>> spark.range(5).show()
