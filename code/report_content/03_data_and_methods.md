ACLED's *Data Export Tool* covers Western Africa (2018-01-01 to 2025-04-25). AES filtering yields {n_events_aes} events; {n_civ_events_aes} carry the civilian-targeting flag, accounting for {n_civ_fatalities_aes} fatalities [Raleigh et al. 2010]. When sources disagree, ACLED records the lower number, undercounting deaths. Eck's critique is addressed below [Eck 2012].



Country-year merges add the Powell-Thyne coup dataset [Powell & Thyne 2011] and V-Dem v16 for regime indicators. Cleaning derives four actor-role categories (state, non-state armed group, external force, civilian/other) and three breakpoints: first coup, French withdrawal, Russian arrival.



Pre/post ratios use a month-level bootstrap (2,000 replications, 95% CIs). A negative-binomial regression with country fixed effects, an event-volume control, and a linear time trend yields the headline incidence-rate ratio (IRR): post-Wagner counts as a multiple of pre-Wagner. The same specification is repeated on 13 non-AES countries as a placebo (null expected if Wagner-specific). Burkina Faso ({bf_civ_n_post_months}-month) and Niger ({niger_civ_n_post_months}-month) have shorter post-windows than Mali ({mali_civ_n_post_months}); we flag this rather than averaging through it.
