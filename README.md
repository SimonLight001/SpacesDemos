# SpacesDemos

This is a repo used to house a few demos that can be used with the DNA Spaces Partner Firehose API

## Dependencies

Python3 (as well as pip of course)

Python packages:

These are all shown in the import list for each use case (I usually do this at the top of each file)

- requests
- pyjwt
- cryptography (a dependency of pyjwt)

## How to run

Firstly, clone/download the git repo.

Then install Python 3 (if not done already).

Then we need to install the dependencies - `pip3 install requests pyjwt cryptography`

This may require admin permissions - `sudo pip3 install requests pyjwt cryptography`

Then navigate to the correct folder - `cd Location_COVID`

Then simply run the application with `python 3 index.py`

You will be asked to enter a token. This is done by adding a partner app to a spaces dashboard (can be added to the sandbox dashboard found on the partner site).

When creating a new application, its key that the application sends Device Count information, as well as simulation data is turned on if using a sandbox.

When the app is added to the dashboard, you will be asked to generate a token, this token can then be copied and pasted into the terminal.

Once this is done, the demo will validate the app (meaning it will now show as Active in the spaces dashboard).

The demo will then begin to send data around a location, showing how many users are in that spaces as well as if the space is safe to enter (current limit is hard set at 630, but looking to improve this).