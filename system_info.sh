#!/bin/bash

echo "====== SYSTEM INFO ======"

echo "User:"
whoami

echo ""

echo "Hostname:"
hostname

echo ""

echo "Kernel:"
uname -a

echo ""

echo "Disk:"
df -h

echo ""

echo "Memory:"
free -h
