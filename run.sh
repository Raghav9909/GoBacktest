#!/bin/bash

# Command to run in the first new terminal window
COMMAND1="echo Running first command; cd /Users/karman/Desktop/projects/GoBacktest/fastAPI ; uvicorn app:app --reload --port 5000"

# Command to run in the second new terminal window
COMMAND2="echo Running second command; cd /Users/karman/Desktop/projects/GoBacktest/frontend ; npm install;npm start "

# AppleScript to open a new terminal window and run COMMAND1
osascript <<END
tell application "Terminal"
    do script "$COMMAND1"
    activate
end tell
END

# AppleScript to open another new terminal window and run COMMAND2
osascript <<END
tell application "Terminal"
    do script "$COMMAND2"
    activate
end tell
END
