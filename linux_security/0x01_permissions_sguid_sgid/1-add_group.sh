#!/bin/bash
addgroup "$1"
chgrp "$1" "$2"
chown g+rx "$2"
