# Running infrastructure on Kubernetes?

TLDR: **Only makes sense in a limited set of use cases:**

- Need: Off-the-shelf infra is not enough, because ML is at the business's core, so it makes sense
  to invest 10X in order to get a 1% improvement.
- Technical ability: Able to attract superior talent (because everything becomes much harder)
- Financial ability: Able to pay for a dedicated DevOps team focused on Kubernetes

# Should data scientists know Kubernetes?

Surprisingly, this is still a question where you hear arguments for both sides. However, I think
the right answer is a resounding **no!: If data scientists need to know Kubernetes to be
productive, there is something seriously wrong with the design of their ML platform** (or they
might not have access to one at all).

I think the main reason goes back to the general insight that to solve complex engineering
problems, **we need to decompose problems in a way that we can divide labor amongst people who
specialize in different parts of the problem**. To enable the specialization, we come up with
stable interfaces that provide contracts for how the different parts of the system interact. While
we might have to revise these interfaces occasionally, for most of the time, most engineers can then
focus only on their respective domain - which is already hard enough if we're pushing boundaries.

The best example I can think of is how we make something as complex as the Internet work: As a software
engineer, I mainly have to understand the application layer (e.g., http protocol) and to a
lesser extent the transport layer (e.g., TCP). However, I don't
have to worry about how packages will be routed to the right address, and I
definitely don't have to know anything about how this communication works at the physical level
(e.g.,how the signal is transmitted through fiber-optic cables).

Similarly, if we are faced with building something as complex as a machine learning system, we need to find a way of
slicing this domain into specialties that can be fulfilled by different people.
**I do think it is essential that data scientists learn more about software
engineering** as the field is transformed from a research done in Jupyter notebooks
to an engineering discipline that deals with production code. However, it already takes a
lot of time to master data science and machine learning (and to keep one's knowledge up to date
in the face of rapid innovation). Thus,
expecting data scientists to master all (or even most) of software engineering and DevOps is
clearly unrealistic, and would go at the expense of their core domain knowledge.
Instead, the question is not just which parts of the traditional engineering knowledge we need to
have involved in the data science process, but also **which of these roles can be performed by
specialists, and which aspects are so basic and intertwined with the core data science work that
every member of the team is expected to master them.**

One natural division of specializations that has emerged is between software engineers writing code
on the one side, and infrastructure-, security- and DevOps engineers (or in earlier times, system admins)
focusing on different aspects of the infrastructure side. While the discussions around DevOps
and DevSecOps have shown that there often is still a need for collaboration between the
different sides, and that everyone still needs to have an understanding of the basics of the
whole lifecycle, it's clear that each of these fields is complex enough to warrant
deep specialists.

But what about a small startup that can't afford to have dedicated specialists for each of these
fields, you may ask? As I argued in the previous section, the answer is simple: In that case,
you probably shouldn't run your infrastructure on Kubernetes at all! If you have a small team,
you don't want your engineers to spend most of their time on something like setting up and
managing infrastructure that doesn't create any immediate business value. In the exceptional case
where Kubernetes is still needed to manage special use cases, you probably want at least one DevOps engineer specializing in it - it would be a mistake to think it's lean to skimp on specialists, because it will take non-specialists much longer to do the same task (and the hourly cost is approximately the same).

By contrast, which are the **basics of software engineering should data scientists learn**?

- writing ***clean* code** (an understanding the importance of *maintainability*)
- automatic **testing**
- object-oriented **design patterns**, etc.
- DevOps (high-level)
**These are things everyone on the team needs to know, because they can't easily be outsourced to specialists.**
We don't want to have *separate* software
engineers who constantly rewrite data scientists' throw-away code and fix bad design, etc.

# Should *ML engineers* know Kubernetes?

There is obviously more of a case to be made that *machine learning engineers* need to know
Kubernetes (K8s). However, I would still argue that:

- not all ML engineers need to know K8s, because K8s only makes sense as an infrastructure
  solution for a small subset of companies (as argued above), and
- even for ML engineers who do work with ML platforms that are deployed on K8s, they don't need to
  be K8s *experts*. K8s is a complex beast, and it requires dedicated DevOps engineers to tame.
  It's a long way from understanding its basic architecture and being able to
  deploy to it, to troubleshooting complex networking issue (which unfortunately is not a rare
  occurrence).
  The latter problems require experts that work with K8s full-time - having ML engineers
  solve these problems themselves detracts from their core function. If a company doesn't have
  the resources to employ a fleet of dedicated DevOps engineers to work on these problems, it
  should not be on K8s.
