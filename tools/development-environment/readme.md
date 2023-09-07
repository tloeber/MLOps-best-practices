# Python dependency management
Note: **The problem of dependency management is entangled with the problem of separating environments**. This is complicated by the fact that there are two main ways of separating environments, virtual environments and containers, and each of these two choices have somewhat different implications for dependency management. Nevertheless, the challenges are similar enough that I decided it is best to discuss the topics of dependency management and separating environments together.

## Goals
### Must-haves
- Reproducibility
- Easy and quick install/project setup:
  - Easy to set up the project on a _new machine_ (exact replication): It should be easy for new engineers to set up and run the project themselves (by running only a few commands), so that we can easily onboard new team members. In addition, this also makes it much easier for other teams to contribute or take over the project when necessary.
  - Easy to _update_ dependencies: It should be easy to *update* the dependencies, so that can make sure our packages have the latest security patches.
  - Easy to add _new dependencies_: it should be easy to install *additional* packages without running into dependency conflicts with existing packages.

### Should-haves
- Allow creation of different dependency *groups* (most importantly prod versus non-prod). Reason: By not having to install unnecessary packages in prod, we:
  - reduce the size of the deployment package/container, which in turn makes security scans and auto-scaling faster;
  - increase security by reducing the attack surface.

## How to achieve these goals?
### Environment separation
This can either be achieved by using [**containers**, which I discuss in a separate section](../../best-practices/DevSecOps/containers/readme.md) or by leveraging **virtual environments**.

### Separately tracking abstract and concrete dependencies
- Track both [*abstract* and *concrete* dependencies](https://martin-thoma.com/python-requirements/#abstract-dependencies) in version control.
  - **Concrete dependencies** specify the precise version of each package (including the repository used) used, and  they also include all *indirect* dependencies. This is what you get by using `pip list` or `pip freeze > requirements.txt`. Thus, it becomes straightforward to:
    - re-create an identical environment on another machine (as long as it uses the same operating system and CPU architecture).
    - revert to a previous working state in case an upgrade breaks the installation. 
    - check how versions of specific packages have changed, which can provide essential information for troubleshooting new dependency conflicts.
    - Finally, we don't have to worry that the behavior of our code changes between different installs (e.g., if we ended up using an older version of a package, it may not have the functionality we depend on implemented yet).

  - **Abstract dependencies** do not define a *specific* version of all packages (though they may specify a version _range_ for some or all dependencies, or even require a specific version for a few packages). Likewise, abstract dependencies exclude _transitive_ dependencies (i.e., they do not hardcode which other packages the explicitly installed packages depend on *indirectly*). Therefore, tracking abstract dependencies in version control is vital because:
      - It becomes possible to replicate the environment on a machine with a _different operating system or CPU architecture_ (since this would require installing different versions of packages that have _compiled_ dependencies).
      - Installing _additional_ package becomes safer, because refraining from imposing _arbitrary_ constraints:
        - makes it far less likely that dependency resolution fails;
        - allows us to _intentionally_ specify exact versions or version ranges _where we have a reason to do so_. Thus, it becomes less likely that adding new packages breaks the _application behavior_, because we can intentionally set version ranges (e.g. by locking to minor versions of direct dependencies to make sure we don't accidentally upgrade major versions; see below).
      - _Updating existing_ packages becomes much easier, which in the medium-term is essential for security.
  - Unfortunately, since any update to our packages may need to change existing packages, there is a chance this will change the behavior of our code. Ultimately, this is simply a reflection of the well-known fact that application changes always pose some risk, but refraining from changes is even worse in the medium- to long-term. Thus, we should instead focus to do what's in our control to minimize this risk by:
    - Invest in a trusted test suite. (We should have this anyway, because otherwise engineers will be scared not just to upgrade packages, but to keep the codebase clean in general.)
    - Leverage the information from semantic versioning:
      - Finding the right cadence for this upgrade, so we don't take this risk more often than we have to. Ideally, this choice is informed by comparing our package versions to a vulnerability database. 
      - It should definitely be safe to upgrade the _patch_ version, because this should only add bug fixes and security patches. We can do this by using the idea of [compatible releases](https://peps.python.org/pep-0440/#compatible-release), and locking the *minor* version using `mypackage ~= 2.3.6`, which specifies that we want at least patch version 6, but it can be higher.
      - It should be safe to upgrade _minor_ versions, because this should only *add* but not change functionality. We can do this by using the idea of [compatible releases](https://peps.python.org/pep-0440/#compatible-release), and locking the *major* version, like `mypackage ~= 2.3`. This will make sure we have at least version 2.3 installed, and we can use any newer version as long as it's below 3.0.
      - When upgrading major versions, we have to rely on our tests to catch changes in behavior. Often this will result in run-time errors (e.g., because a method we try to use is not available yet an older package version), so even in the absence of tests it can be caught by a trial run.
      - Note that updating patch and minor versions *is only safe if our dependencies properly follow semantic versioning - and while many do, some don't*. This is why there is still some residual risk remaining for any package upgrade - just like for any other change to application - and we have to be able to rely on our test suite as an additional  safeguard.
  - Note that **these points are especially important for packages that will be installed by other projects, but it is still important to track these dependencies even for application code: While the easiest way to get a working install is to use the concrete dependencies, there are still enough situations where we need to use the abstract dependencies**.


## Recommended Tools
### Libraries or non-containerized applications
The reason that we lump in libraries with non-containerized applications is this: Whether a library will end up being installed inside a container or outside of one, the point is that **we don't usually distribute libraries as a container image**.

There are two main tools that offer an easy wrapper around both virtual environments as well as package management: Pipenv and Poetry. In other words, they replace both venv and pip. Both are easy to use, and do what they promise to do, so I can recommend them both. While I know most engineers aren't  in the mood to read documentation and learn yet another tool, it does not require much time to get familiar with, and will save you from a lot of headaches down the line. So it is definitely worth it!

### Pipenv
- See https://pipenv.pypa.io/en/latest/
- Tracks abstract dependency in the Pipfile, and concrete dependencies in the Pipfile.lock. 

### Poetry

### Containerized applications
- The _environment_ management aspect of tools such as Pipenv becomes redundant when using containers (since there will only be a single-environment in a container anyway). However, it doesn't really hurt performance either (as far as I know).
- For _dependency_ management, both tools clearly become less essential, because containers solve the problem of easily running the application on another machine (and keep track of _concrete_  dependencies by their very nature). **This frees up the requirements.txt (or environment.yml) to track only _abstract_ dependencies**. As a result, it becomes easier to update existing dependencies or add additional dependencies (because abstract dependencies impose much fewer constraints).
- Benefits of still using Pipenv or Poetry:
  - The main advantage they bring in a containerized setting is that they make it **easy to also re-create a maximally-similar environment *outside* of containers**. For example, this allows the data science team to get started with development without having to know containers, while it is still easy for ML engineers to containerize their models downstream. I'm not sure if this division of labor should actually be the goal, and what sort of unexpected problems this workflow will produce. Nevertheless, there are some organizational settings where leaving data scientists out from containerization is the best compromise we can achieve. In these cases, using Pipenv or Poetry together with containers is a worthwhile strategy.
  - A secondary advantage of these tools is that they **allow separating prod from non-prod dependencies**. Thus, they allow us to have prod and non-prod versions of a given container image, which are identical except in the additional non-prod dependencies. Usually this will not be an important enough consideration, especially because this is slightly more risky because it introduces another point of failure. However, we can conceive of situations where this may push us towards using one of these tools instead (e.g., if we want to minimize latency of autoscaling at any costs).
- Disadvantages:
  - Since there should not be any performance impact (which we should verify though!), the only cost is that engineers need to be familiar with yet another tool. This is usually not a big deal, because they are not complicated, and many Python developers already know them anyway. Even if they don't, it is good to know Poetry in any case, since it is a great tool for _packaging_ Python projects (which is something that remains important for libraries, even when all _applications_ are containerized).
- Preliminary conclusion: If using containers, these tools generally become **optional**. Even though the costs of using these tools are small or nonexistent, their benefits generally are small or nonexistent as well. Thus, my preliminary recommendation is to only use these where there is a tangible benefit:
    - If it is beneficial to retain the ability to run the same application outside of containers as well; 
    - If we want to be able to create multiple versions of container images with the same set of core dependencies but different groups of additional dependencies.


## Other tools for niche purposes

### venv + pip + requirements.txt
- Easy way to create a virtual environment
- Does not offer a good way to replicate environment on other machines.
  - **Does not allow to easily track abstract dependencies**. This is because there is no command similar to `pip freeze`that allows exporting abstract dependencies. Thus, the only solution is to adhere to a manual process of always installing new packages by:
    - manually adding new packages to a requirements_abstract.txt file (potentially using a version range);
    - Update environment from abstract requirements file ( by running `pip install -r requirements_abstract.txt`)
    - Updating the concrete requirements after environment update (by running `pip freeze > requirements_concrete.txt`)
    - -> The problem with this process is not just that it's tedious, but also that it is hard to enforce in an organization. Thus, it is likely to break down in some point, because the right way is not the easy way.
- Does not allow to easily track concrete dependencies if we have separate dependency *groups*, such as an additional set of packages that is required for non-prod (e.g., to run tests). 
  - A natural solution is to have one requirements file with the common dependencies, and an extra file with the additional dependencies. However, this only works if we use the tedious process outlined above to manually separate abstract and concrete dependencies. However, even in the best case in which we are able to enforce this process, we will still end up with different packages being used in prod and non-prod. This is because even if we install from concrete dependencies, installing additional dependencies may update the versions of already installed packages.
  - Thus, the only solution is to go backwards from the concrete requirements of the more encompassing requirement: We already know that the set of packages works together, and we can simply remove direct dependencies and their indirect dependencies (as long as they are not indirect dependencies for other dependencies) from this file. This is what the Pipfile.lock keeps track of for as if we use Pipenv, but as should have become clear it is not feasible to do ourselves manually.
- Recommendation: Not suitable for collaboration, but can use it when we just quickly need a virtual environment that will be discarded soon.

### conda
- Like Pipenv and Poetry, serves both as a virtual environment and package manager.
- **Conda used to be an essential tool to install ML packages before the pip ecosystem offered a good way to handle binaries. However, as wheels have become commonplace over the last years, this is no longer a big concern.**
- Disadvantages:
  - No functionality to separately track abstract and concrete dependencies. (Can't export abstract dependencies.)
  - Much slower than pip for installing dependencies.
  - If set as default Python interpreter, it causes a number of problems when trying to use standard virtual environments such as venv. This often leads to hard-to-debug problems for people not familiar with the details of Python environments. See my recommendation for how to deal with this challenge in VSCode [here](https://github.com/tloeber/utils_and_configs/blob/ea23f341d494f1ba552e0c36b5bf26a35a7c56af/IDEs/VSCode/settings/settings.json#L25-L59).
  - Using pip to install packages into a conda environment, which is a common practice, can lead to dependency conflicts because *pip and conda can't coordinate versions between each other*. Even if using the best practice of using conda for package installation wherever possible, some packages will still need to be installed using pip because they are not available as conda packages.
- Conclusion: 
  - Only use if you really need to (because you verified pip can't do the job).
  - If you do need to use conda, research and follow [best practices](https://www.anaconda.com/blog/using-pip-in-a-conda-environment) (e.g., don't be lazy and install a package using pip unless it is not available for conda).

## Tools to avoid
### virtualenv
- Replaced by venv. 

### mamba
- Much faster than conda.
- I experienced a number of major bugs when I tried it, which made it basically unusable. (This was in late 2022 or early 2023.)
- Even if these usability challenges are resolved, it may be a good replacement for conda. However, since it only solves one of the multiple pain points of conda, it is by no means a replacement for Poetry or Pipenv.

