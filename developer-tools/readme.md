- Standardize which IDE we use?
	+ Pro:
		- easier to manage common settings in version control, In particular to make sure everybody is using productivity-enhancing features (e.g., static code analysis plugins to get instant feedback while writing the code - and not just on commit or even merge - to get instant feedback).
		- Can commit project-specific IDE configurations, e.g. whether to initialize Anaconda in integrated terminal; debug configuration (launch.json in VSCode).
		- The best IDEs offer a lot of powerful productivity features, but it takes quite a bit of initial time investment in order to be able to leverage those features. Likewise, it requires an initial upfront investment to get used to configure those settings as code, and to find an efficient process to It's already a lot of investment to master one of them, so it's already hard to invest enough time.
	+ Con: it's not great to force people to do something against their will, either because they don't like it, or because they already have invested a lot of time learning a different productivity tool.
	+ Decision:
		- Try to convince and give incentives to standardize, but don't force anyone. If somebody really wants to use a different tool, they will be responsible for managing configurations (general and project specific settings, setup scripts) as code. The goal is that it lives up to the same quality standards as the main/original tool.
		- Doing this extra work is not for everyone – it requires a certain kind of personality (e.g., being passionate about process improvement, and thinking a lot about how certain features make coding more productive, rather than just focusing on delivering tangible features in the short term). If we do have such a personality on the team who is interested in exploring other options, it actually might be beneficial to have someone stay up to date with the potentials of competing tools. This helps reduce the risk that we may miss it if a tool that initially was inferior gradually catches up, and may at some point offer compelling reasons to switch over (like Visual Studio code has over the last couple of years, compared to PyCharm).
		- Be careful to **not manage settings in IDE-specific files if they could also be managed in a more general way**.
			+ In particular, environment variables should be managed in a .env file!

# VSCode vs PyCharm:
- PyCharm exclusive features:
  - Pytest: Pick only a single test to run, using GUI (clickable arrow)

- PyCharm features were I haven't found an equivalent yet but need to do more research:
  - Run configurations (in particular, for a test file I want to be able to press control enter to run it quickly. Quick iterations are essential for TDD.)

- Features free in VSCode but paid in PyCharm
  - Jupyter notebook support
  - [Remote development](https://www.jetbrains.com/help/pycharm/configuring-remote-interpreters-via-ssh.html)
  - [Docker support](https://www.jetbrains.com/help/pycharm/using-docker-as-a-remote-interpreter.html)

- VSCode advantages
  - Free - whereas PyCharm usually requires paid subscription.
  - Easier to manage IDE configurations as code, which [brings a host of other advantages](../DevSecOps/readme.md#Applying DevOps principles to managing laptops)
    - Configurations are more readable because they use JSON rather than XML
    - Configurations are not spread out across as many files
    - Configuration is code is much better documented, and is considered a standard way to set 
	  configurations.
  - More favorable trend: VSCode has been improving more rapidly than PyCharm over the 
	last few years. While the two are roughly equal now, it makes it likely that VSCode will 
	surpass 
	PyCharm over the coming years.

- Decision:
  - VSCode wins, because it offers roughly the same features, but all of them for free. In 
	addition, it makes it easy to manage its configurations as code, which [I think is essential.
	](../DevSecOps/readme.md#Applying DevOps principles to managing laptops)