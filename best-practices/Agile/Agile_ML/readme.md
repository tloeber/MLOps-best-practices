# What does Agile look like for production ML systems?

As Agile principles have shown success beyond their software origins and are being generalized to a wider array of work, it is crucial not to overlook the domain-specific practices vital for building Agile software products. These technical practices ensure our applications remain Agile in the face of ongoing pressures to make changes and add new features.
Building on these insights from traditional software, let’s explore the implications for the domain of ML systems. We will discuss how to:

- balance the focus on quick delivery of value with the need to manage technical debt.
- make the internal quality of an ML application visible through the right KPIs.
- identify those decisions that require some amount of planning ahead in order to avoid getting stuck on suboptimal trajectories.
- enable rapid experimentation and feedback cycles by leveraging the right kinds of tests and prioritizing observability.
- avoid pitfalls common in ML when creating cross-functional teams.

## Challenges

This is far from a complete list, but simply a few things that are underappreciated:

### incentive mismatch

- general problem to software: Incentives are skewed towards the short term, since technical debt is not visible (but tangible features, as well as finances are easily visible)
- ML specific: MVP is much bigger than in most other applications of software engineering (at least if we are talking about productionization, rather than thinking of a data science notebook as an MVP). Therefore, we need to take a more long-term perspective. Similarly, more stars need to align, because even a problem in one area of the system (e.g., data reliability), can invalidate the whole product. Also, stakes are often much higher.

### Gap between POC and production

- General problem in software: it’s easy to create a simple POC, but it’s orders of magnitude harder to scale this process to multiple developers, growing functional requirements, and production-grade quality requirements. Even worse, the quickest way to the former does not automatically scale to the latter.
- ML specific: even greater divide between data science POC and the engineering approach required for productionization.

## Solutions

### Agile architecture

Creating a process for collaboration – though with a clear division of labor - between the product owner and the technical lead to find the right trade-off between, on the one hand, moving fast towards business value, but on the other hand avoid compromising our ability to keep doing so in the future.

- Tech lead communicates trade-offs about quality attributes of the system (reliability, availability, maintainability, changeability, security, etc.) in a way understandable by the business side (e.g., what an SLA expressed in percentage means in terms of hours of downtime per year, etc.)
- product owner decides on relative importance of these criteria
- based on this, tech lead makes architectural decisions to achieve the right trade-offs
- dev team strives to make quality attributes of the system visible through KPIs, so that we see if we are on track, and to make it easier for the non-technical side to understand what work needs to be done beyond tangible features. Examples: DevOps metrics (change failure rate, mean time to resolution, time from commit to production,…), ML specific metrics (accuracy etc. over time and by subset), data quality metrics (_), error budgets that trigger feature freeze if violated (Google’s SRE approach). We should also track code quality (which exactly?), though the measures we have are more indirect and imperfect (e.g., can easily distinguish between accidental and inherent complexity).
- (requires periodic reevaluation as new information comes in)

### Identify decisions that constitute critical junctures, and thus require medium to a longer-term planning

In particular, this requires devoting technical expertise to create a software architecture that:

- supports Agility in general (rather than letting the architecture emerge from the various low-level decisions on which user stories to prioritize). Note that this is most important at the beginning of a project but requires ongoing reevaluation.
- Makes the right trade-offs between achieving the various quality attributes of the system, as described above

### Managing technical debt

Balancing the focus on quick delivery of value (meeting functional requirements) with the need to manage technical debt. This is essential not only for staying on track to keep meeting the quality attributes of the system, but also that we are not pressured into short-term decisions that are detrimental to the medium-and long-term interest of the business side.

- technical excellence, which may require some investments

### how do cross-functional teams look like in ML?

- Slicing by value stream/End to end ownership: Data/ML scientists in the same team as ML/MLOps engineers
  - due to the large number of personas involved, it’s challenging to prevent team size from getting too large. Pods may offer a good solution.
  - Due to the wide range of knowledge involved in the value chain, it’s challenging to create a team of “generalizing specialists”. This is especially so since the cost of suboptimal decisions can be very high, so are most use cases we need to have at least one expert for each of the major areas (data science, data engineering, MLOps) to ensure sound architectural decisions. Thus, while we definitely need to avoid having a single point of failure, a more realistic focus is to ensure that we have at least two or ideally three people who are able to perform common daily tasks. By contrast, we may have to wait for the main expert to be back from vacation or sick leave for architectural decisions (which tend to be less urgent), and to have access to shared resources outside the team for urgent troubleshooting that is more complex than the typical daily work that can be performed by a non-specialist.
 Another way to think about this is as a trade-off between: 1) more breadth in skills, which reduces the risk of bottlenecks; and 2) ensuring sufficient depth in skills to avoid the cost of inferior decisions (and to make troubleshooting quicker and easier). From this perspective, it becomes clear why this is a more challenging problem in most applications of ML: ensuring sufficient depth is already harder (for a given team size), because of the wider array of knowledge involved in the different domains that make up the value stream. This is compounded by the fact that for each given domain, making the right decisions tends to be harder because there is less of an established body of knowledge about best practices, and the landscape of tools and frameworks is evolving rapidly. In other words, we are faced with an even harder trade-off, because even in the best case we can achieve less of either value. Thus, arguing that for most ML use cases we can’t achieve the ideal state where every team member will be able to work on anything does not necessarily mean that we value this goal less, as this would only be achievable by completely sacrificing depth. Thus, keeping one of the two goals the same when both have become more expensive constitutes an argument for a different trade-off, not the same. (Of course, one may make an argument for why this would be the case, but I have not seen one, nor can I imagine a plausible one.)

### Trying out new things: Culture and infrastructure to enable rapid experimentation in ML

- access to, and ability to quickly set up, various tools and platforms
  - higher-level frameworks that take away some of the undifferentiated heavy lifting. e.g., Databricks; managed MLOps tools (whether SaaS or company-internal)
  - especially in order for data scientists to adopt productivity tools standard in engineering (e.g., linting, static code analysis, visual UI for git), they need help with research/decisions and set up. Ideally there are company-wide resources to help with this, and/or ML engineers on the same team can jump in. While we want to give individuals ownership over how exactly they like to do their work, tech lead in particular should keep an eye out for inefficient practices that simply persist because it’s the way it’s always been done.
- Trying out new things should be safe and easy. This is not just about a culture of psychological safety (which would be a general principle of agile), but specific to ML, data scientists and ML engineers need to have an easy way to experiment by spinning up new cloud resources, etc. in a dev environment, without having to go through a bureaucratic process, having to worry about data security, cost, or breaking their team member’s work, or simply needing to go through them a complicated list of steps they have to do so. In other words, the right way to do something should be the default and easy way; conversely, unsafe or undesirable practices should be impossible (or at least hard). This simply follows from the general agile principle of blaming processes, not people, if any failures do occur.

### Rapid feedback in ML

- Leverage the test pyramid:
  - the quickest tests are the ones you don’t have to write -> leverage static code analysis, especially type checking! This goes for all of software development, but this advice is especially important in ML because of two things: ML usually uses Python, where static code analysis is optional rather than mandatory (like in a compiled language); running the application to discover bugs is generally orders of magnitude more inefficient than for most other kinds of software application because of the expense of compute requirements and because it takes much longer, thereby considerably prolonging the feedback cycle.
  - Unit tests: like the former (maybe to a somewhat lesser extent?), it is more common for this to be neglected in ML, even though the payoff is generally much greater. In addition, another challenge is that unit testing is harder, e.g. it is most efficiently done by leveraging proper design patterns in the code to decrease coupling between components, which in turn makes writing unit tests is much easier and less error-prone than having to mark and patch everywhere.
  - Integration and acceptance tests. The reason this is especially important in ML is because failures are much more likely to be silent, i.e. don’t raise an error. The challenge is that there tends to be less knowledge in ML teams how best to do these (e.g., it is common to simply use pytest because nobody is familiar with dedicated frameworks such as behave + Gherkin).
  - ML-specific testing?
- Prioritize observability, so that be know if something went wrong, and can resolve it quickly
  - code (traditional observability)
  - model performance
  - data observability (data quality, data lineage)
- Ability to quickly do local runs for quick development of as much of the functionality as possible. This is complementary to testing effort, which also relies on running as much as possible locally not just for isolation but also for speed.
- Other insights from CI/CD
  - we can build on the dev ops revolution, but we face the problem of version control in additional dimensions (versioning data, joint versioning of model artifacts and associated code)
