- Applying DevOps principles to managing laptops
  - Rationale:
    - Speeding up onboarding
    - Making it easy to share best practices through pull requests
    - Ability to revert configurations in case they get messed up
    - Making it easier to enforce quality standards by *making the right way the easy way*.
  - What to track?
  	 - IDE configurations
    - Git config
    - Dotfiles
    - Language specific files
      - ~/pylintrc
      - /etc/pip.conf, ~/.config/pip/pip.conf, conda initialization script (link)
      - ~/m2/settings.xml (Maven), ~/.sbt/repositories
  - Machine set up script for efficient onboarding (and machine replacement)
	  + Install typically used programs
		  * If we can use a package manager (apt, homebrew, chocolatey), this is much easier!
	  + Clone all repos the user needs. (This can also help set the expectation in which standardized location a given repo is located on everyone's machine, e.g. ~/projects/, which makes it easier to reference configuration files if necessary. Alternatively, everyone might've to set an environment variable identifying the directory on their machine where Local versions of repose are located.) We can have a hierarchy of scripts: Some that are run for any company employee, and some that are specific to a given department, team, job role, etc.
		  * Clone configs repo (see above), then run scripts to create hard links where necessary.
		  * Clone engineering standards and team standards
		  *
