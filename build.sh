#!/bin/bash
nuitka3 main.py --onefile -o ESOLinuxAddonManager --include-package="certifi" --output-dir="./dist" --linux-onefile-icon="./esotux.png"