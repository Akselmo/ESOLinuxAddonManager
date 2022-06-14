#!/bin/bash
nuitka3 main.py --onefile --enable-plugin=gi -o ESOLinuxAddonManager --output-dir="./dist" --linux-onefile-icon="./esotux.png"
