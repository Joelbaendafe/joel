#!/bin/bash

# Script to build APK using Buildozer for MDT 97 application

# Set the environment variables
export WORKSPACE=$(pwd)
export BUILD_DIR="$WORKSPACE/.buildozer"
export KIVY_HOME="$WORKSPACE/.kivy"

# Check for Buildozer installation
if ! command -v buildozer &> /dev/null
then
    echo "Buildozer could not be found. Please install Buildozer."
    exit
fi

# Change to the application directory
cd $WORKSPACE/MDT97

# Build the APK
buildozer android debug

# Check the exit status and notify the user
if [ $? -eq 0 ]; then
    echo "APK Build Successful!"
else
    echo "APK Build Failed! Check the logs for errors."
fi
