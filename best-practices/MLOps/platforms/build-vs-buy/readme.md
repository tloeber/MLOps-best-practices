# Build vs. Buy (vs. Open-Source)

## Beyond ML: The old Build vs. Buy Discussion

Build versus Buy is of course an old question that has been discussed for many other types of software
systems. I think the general answer is clear: **Companies should concentrate on the core of their
business, and offload all other *generic* problems to specialized providers *as much as
possible*.**

Note an important qualifications I'm making: A problem must be *generic* -
otherwise there won't be an industry around providing solutions
for it.
(We can think of *consulting* as offloading non-generic problems to a third party-provider. This can still be beneficial in order to
take advantage of *specialized knowledge and an outside perspective*, but - amost by definition -
you do not really get any economies of scale).

It also follows that we should try to turn our
problems *outside of our core business* from specific into generic ones as much as possible, so
that we can benefit from the efficiency increase we get from offloading them to a specialized provider.
While this may seem obvious, it is often not a priority in practice. It's easy to
end up with a cobbled-together mess of hacks if you are overly focused on solving
immediate problems and never get the time to think about the system architecture as a whole (or
if you're not willing to invest into the future by paying down technical debt).
Furthermore, over the last decade the mainstream adoption of the
cloud has made it easy to offload much more than we previously thought possible, so non-generic
systems have become a larger drag than originally anticipated.

Let's now dive into the reasons why buying is generally better than building:

- It's a pretty safe assumption that **the core of a company's business is where its competitive
  advantage lies** - otherwise it would not be profitable (or receive continued
  investment in order to get over the hump to become profitable, in the case of a startup). Most
  companies fail, so if a company made it far enough to survive for a number of years, it likely
  must be doing something right.
- By contrast, for many tasks businesses face that are outside of their core area of expertise,
  many other specialized companies are already competing to own this niche. They
  have learned valuable lessons along the way, and the best ones have survived. So why reinvent
  the wheel, rather than picking the winner? (Michael Dell has a good quote around that, but
  couldn't find it anymore.)
- In addition, specialized providers enjoy **economies of scale** that give them a huge cost
  advantage. (However, if you forget to factor in the cost of your own teams's labor,
  building-yourself may wrongly seem cheaper). These **economies of scale are particularly large
  for digital goods such as software, because most of the cost associated with their production is
  fixed cost, whereas their marginal cost is near zero** (i.e., they can be shared at virtually
  zero cost). While we need to also remember that much of the lifetime cost of software systems is
  in their maintenance - not their initial creation - these economies of scale also extend to the
  ongoing maintenance, albeit to a lesser extent: Firstly, some of the maintenance is generic, and
  thus many different
  users can benefit from it (e.g., staying up-to-date with security vulnerabilities, or adding new
  features). Secondly, even for maintenance tasks isolated to a specific client - such as
  production support for infrastructure issues - there are still some economies of scale
  because of the *specialized knowledge* required.
- The previous two points imply that buying is generally more *efficient* than building. (Even if
  you factor in [transaction costs](https://en.wikipedia.org/wiki/Transaction_cost), the
  advantage of buying is generally so big that transaction costs are negligible.) However,
  *just because managed solutions are more efficient does not mean that they are automatically
  better and cheaper.* What it does imply, though, is that it is generally *possible* to provide
  better solutions at a lower price, and in a competitive market economy these business
  opportunities will not remain unfilled for very long.
  Still, particularly in the short term,
  suboptimal pricing strategies that don't make a solution attractive to all different kinds of
  customers can persist for surprisingly long times. (E.g., pricing may not sufficiently vary with scale, and thus only
  makes sense for large customers). *Therefore, we will still have to do the math ourselves to
  figure out if it is worth it - but if we arrive at the solution that it's cheaper to build it
  ourselves, we should be skeptical and double-check our numbers and assumptions* (e.g., did we
  account for the risk from the well-known fact that most software projects take much longer and
  are much more expensive than initially estimated?
  Did we factor in the cost associated with the fact that the business will only be able to draw
  value from our homegrown solution a lot later than if we bought a prebuilt solution, because it
  takes longer to build than to buy?)
- Finally, managing the core business is already hard enough – in fact, a common reason why
  established companies fail in the face of disruptive innovations is because they don't focus
  enough on the core business they are in (such as Blockbuster failing to go through with purchasing Netflix,
  because they thought they were in the business of *renting out* movies, rather than in the more
  general business of letting customers watch movies). Thus, since it's already hard enough to
  make the right strategic decisions in the area of your own core expertise, it's best to limit
  the complexity of all the strategic decisions you have to make by offloading everything else
  as much as possible.
- A risk with buying  that needs to be managed as a vendor lock-in. This goes both for the
  risk of price
  hikes and the vendor going out of business. This risk is higher the longer it takes to
  migrate the solution to a different vendor, and the more critical the process is to our core
  business.
  - I think the price hike argument is often overstated: While it is true that we worsen
    our bargaining position the more dependent we are, this may at their worst result in less
    discounts, but as long as there is still some competition between providers, they do not
    have an incentive to make general pricing less favorable. They still need to remain attractive
    to new customers and be mindful of their reputation as a partner, and make sure their
    customers stay in business.
  - However, the risk of a service provider going out of business is real, and is higher for
    smaller and younger companies. Thus, if you go with a less established company, we better be able to
    easily migrate elsewhere (or to do the task ourselves, such as if we are just buying support).
    On the other hand, while it would be hard to migrate away from something like AWS Lambda or
    even Step Functions, the risk of AWS going out of business (or discontinuing these popular
    services) is very low. On the other hand, the cost of avoiding the risk by instead replicating
    the same functionality in
    a cloud-provider agnostic way (probably using Kubernetes) is orders of magnitudes higher -
    so accepting the risk of vendor lock-in is clearly a risk worth taking.

Most companies tend to under-rely on managed services because:
    - They systematically under-estimate the relative cost of building versus buying, because they:
      - are overly focused on the additional out-of-pocket *expenses* of managed services, while not sufficiently taking into account the value of engineers' time that this frees up;
      - don't sufficiently account for the risk of "unknown unknowns" of implementing a solution themselves (["planning fallacy"](https://en.wikipedia.org/wiki/Planning_fallacy));
    - If there is already an internal team currently providing these services in-house, these internal stakeholders - who now risk loosing their project - often have disproportionate influence on decision-making. This is
      - because of [loss aversion](https://en.wikipedia.org/wiki/Loss_aversion), i.e. people tend to be more sensitive to losses compared to gains;
      - because the losses are *concentrated* while the gains are *spread out*, making it easier for the would-be losers to organize and lobby for their interests.

## What about free and open-source software?

A third option is to leverage free and open-source software (FOSS) options, if any are available.
In some ways, these are
similar to buying a prebuilt solution: You have less ability implement customization, but it's much
quicker, easier, and cheaper to get started. In other ways, though, leveraging FOSS is more
similar to building-yourself: You may still have to put in a lot of work yourself, whether it is to
do some customization for specific needs, or to add additional features that are not supported.
Overall, I think it really depends on the specifics of the use case whether relying on FOSS
solutions makes sense:

- Some solutions are FOSS first (e.g., Linux), others are a company's product first (e.g.,
  MLFlow or BentoML). The latter often
  lack critical features that are a must-have for enterprise customer, such as role-based access
  control, audit logging, etc. If the only viable open-source solution is of this kind, it
  only makes sense to adopt it if:
  - you're sure you can add the missing features yourself, or
  - you're willing to live without them for a while (remember: a re-architecture is generally
    necessary after a few years anyway), or
  - you are willing and able to pay for the commercial offering once needed.
- But even if a FOSS solution gives you everything you need, it may still make sense to
  pay for the commercial offering: Like the "buy" solution discussed above, a commercial version
  can help companies offload the undifferentiated heavy lifting (e.g., implementing access
  control or management of the underlying infrastructure), which a specialized provide can
  generally provide at a lower cost. In addition, it also reduces the complexity for the
  buyer, as they only need to worry about a smaller subset of problems (namely the ones that are
  specific to their core business).
  - By the way, I know it feels like you're losing out if you're not taking advantage of a free
    open-source version, but - if the license also allows using the software for commercial use -
    it is cheaper for other companies to build a business on top of it. In fact, there will be more
    competition than if every company was starting from scratch, so the cost savings will get
    passed down to the purchaser more quickly. Thus, *you're basically still getting the
    open-source core of the software for free, and you're just paying for the additional
    features and support if you go with the managed offering!*

## ML-specific considerations

- There is a plethora of both commercial and open source solutions available for the vast
  majority of use cases. Even for specialized use cases, there are flexible solutions such as
  Sagemaker's Bring Your Own Container or Metaflow's ability to integrate with a wide variety of
  specialized tools. Thus, just because you need to use your own algorithms doesn't mean you
  need to build a custom ML platform yourself!
- There are only few companies (large tech companies) that have  the resources,
  expertise, and custom requirements to compete with AWS's or Google's offerings - almost
  everyone else is mainly going to be reinventing the wheel.

# Conclusion

- **Try to find a *managed* service*** - having to deal with lower levels problems such as managing the infrastructure and having to deal with the problems that come with distributed systems (e.g., partial failure) adds unnecessary complexity. While leveraging a managed service costs extra,
  once you factor in the cost of engineers' time, managed services are often much cheaper.
  Remember: Successful companies focus on their business's *core* expertise, and try to offload
  everything else!
-
