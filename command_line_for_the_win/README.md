# Command line for the win Challenge.

## Overview
This guide outlines the steps to upload completed level screenshots to a sandbox environment using SFTP and later push them to GitHub.

### Steps

1. **Take Screenshots:**
   Capture screenshots of the completed levels as per the general requirements.

2. **Open Terminal/Command Prompt:**
   Launch the terminal or command prompt on your local machine.

3. **Connect to Sandbox Environment:**
   Use the SFTP command-line tool to connect to the sandbox environment. Replace "hostname," "username," and "password" with the provided credentials.
   ```bash
   sftp username@hostname
   ```

4. **Navigate to Destination Directory:**
   Once connected, navigate to the directory on the sandbox where you want to upload the screenshots.
   ```bash
   cd /path/to/sandbox/directory
   ```

5. **Upload Screenshots:**
   Use the `put` command to upload the screenshots from your local machine to the sandbox.
   ```bash
   put screenshot1.png
   put screenshot2.png
   put screenshot3.png
   ```

6. **Confirm Transfer:**
   Ensure that the screenshots have been successfully transferred by checking the sandbox directory.
   ```bash
   ls
   ```

7. **Push to GitHub:**
   After confirming the transfer, proceed to push the screenshots to GitHub as per the initial requirements.
