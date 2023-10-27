# Tips and tricks
- May need plug-ins to work better with some third party packages, e.g. Pydantic, NumPy
- Keep project-specific configuration in version control

# Troubleshooting
- I've had trouble with the config file not being picked up properly. The easiest way to detect that was to explicitly specify the config file to use in the CLI command, using the --config-file flag.  (This may seem obvious in retrospect, but in this case, what I was trying to debug is whether a certain plug-in is enabled or not. I didn't find a direct way of debugging which plug-ins are used, but the indirect way of explicitly specifying the config file proved the easiest solution to showing that the plugin was not used because the config file had not been not read.)
