# ONISHI manuscript — draft sections (§6 Illustrative Application, §7 Discussion)

> Draft for review. English text for AJE ("Practice of Epidemiology").
> All numbers are taken from `integration_analysis/results.json` (single source of
> truth; regenerated and authenticity-verified in PR #249). Figure/Table references
> follow the spec numbering (Fig 6, Table 3).

---

## 6. Illustrative Application

To show how the three components act as one pipeline rather than three separate
tools, we applied ONISHI sequentially—IONE → LINKO → KOTHA—to a single
publicly available individual-patient dataset, the International Stroke Trial
(IST; open access, Edinburgh DataShare). We analysed the effect of randomised
aspirin allocation on 14-day death among 18,451 patients (25 baseline variables;
event rate 22.5%). Pooled across the whole trial, the effect is close to null and
inconclusive (odds ratio [OR] 0.94, 95% CI crossing 1), the type of "flat" result
that is routinely filed as showing no benefit. ONISHI turns this single result
into a layered, decision-grade read-out (Fig 6; Table 3).

**Phase 1 — IONE (within-study coherence).** We stratified patients into four
latent risk groups by their predicted outcome probability. The 14-day mortality
rose from 4.4% in stratum 0 to 50.9% in stratum 3, confirming strong latent
population structure. Crucially, the aspirin *effect* was coherent across these
strata: the incoherence indicator C1(effect) = 1.00 (between-stratum I² = 0%) and
the within-stratum homogeneity W = 0.18. In other words, IONE finds no hidden
effect modification—the treatment effect itself does not differ by risk group
(Fig 6, panel 1A).

**Phase 2 — LINKO (between-study information weight).** For each IONE stratum we
recomputed the endpoint information contribution ratio (ICR) via the PCA-based
estimator. The ICR increased monotonically with baseline risk
(stratum 0 → 3: 2.3×10⁻⁵, 3.2×10⁻⁵, 1.8×10⁻⁴, 7.4×10⁻⁴; median 1.1×10⁻⁴),
showing that the outcome carries very different amounts of information across
subgroups even though the effect is homogeneous. Thus the two diagnostics are
complementary and dissociable: a coherent effect (IONE) coexists with a strongly
risk-dependent information contribution (LINKO) (Fig 6, panel 1B).

We also used LINKO at the between-study level, treating the 13 IST national
sub-studies as studies (Fig 6, panel 2). Random-effects meta-analysis gave a
pooled OR of 0.93 (SE 0.056; I² = 37%). Re-weighting each country by its ICR left
the point estimate unchanged (OR 0.93). We note explicitly that the accompanying
change in the standard error (0.056 → 0.037) is *not* an effect of information
weighting: an equal-weight estimator yields the same SE (0.037), so the reduction
reflects the removal of the random-effects between-country variance (τ²), not the
ICR weights, whose values were near-uniform here (0.001–0.002). The correct
reading of this step is therefore *robustness*: the harmonised point estimate is
insensitive to information weighting.

**Phase 3 — KOTHA (integration and information sizing).** We passed the IONE
risk profiles into KOTHA's counterfactual-power module (Fig 6, panel 3). Holding
the trial size and the pooled effect fixed, statistical power at the observed
effect ranged from 14% in the lowest-risk stratum to 86% in the highest-risk
stratum, quantifying how event scarcity—not absence of effect—drives the flat
result. Module H formalised this: against an optimal information size (OIS) of
7,880 events, the trial accrued 4,159 (information fraction 53%), and trial
sequential analysis gave a cumulative Z of −1.73, inside the ±1.96 monitoring
boundary. Finally, the ICR-guided power-prior integration harmonised the strata
into OR ≈ 0.93–0.95, revising the naïve probability of benefit downward from 0.96
to 0.85 (Fig 6, panel 4C–D).

**Integrated read-out.** Read together, the pipeline yields a single conclusion
that no component gives alone: the aspirin effect is coherent across the
population (no effect modification; IONE C1 = 1.00), but the current evidence is
*informationally insufficient* rather than null (information fraction 53%;
Z = −1.73). Converting the shortfall to a design target, reaching the OIS would
require 3,721 additional events—about 16,500 additional patients at the trial's
overall event rate (roughly doubling enrolment), and IONE's risk profiles show
this is reached far more efficiently by enriching for higher-risk patients
(~7,300 additional stratum-3-like patients versus ~83,700 stratum-0-like). ONISHI
thus reframes a filed-away "negative" trial as an interim result and outputs the
sample size the next study would need—an output available only when the three
methods are chained (Table 3).

---

## 7. Discussion

We have described ONISHI, a framework that diagnoses the validity of evidence
synthesis across three independent levels—between studies (which studies carry
the informative signal; LINKO), within studies (whether a population hides
coherent subgroups; IONE), and between study types (how to harmonise randomised
and observational evidence, and distinguish "no effect" from "no information";
KOTHA)—and chains the three into a single pipeline on shared data. The IST
application shows the practical payoff: individually, each method stops at a
partial statement ("the effect is homogeneous", "the pooled estimate is robust",
"low-risk strata are underpowered"), whereas the sequential pipeline delivers one
actionable verdict—coherent effect, insufficient information, and the additional
sample size required for resolution.

**Relation to existing frameworks.** ONISHI is complementary to, not a
replacement for, established tools. Heterogeneity statistics (I², τ²) quantify
inconsistency but do not attribute it to a level or a mechanism; ONISHI separates
effect incoherence (IONE) from information weight (LINKO). GRADE codifies
certainty judgements, and KOTHA's Module H connects directly to the GRADE
imprecision domain by supplying OIS/TSA and an explicit information fraction.
Target-trial emulation and IPD meta-analysis address the between-study-type and
between-study levels respectively, but neither provides the within-study
coherence diagnosis that IONE contributes. The framework's novelty is thus the
cross-level integration and the defined hand-offs between methods
(C1/subgroup labels → counterfactual power; ICR → integration weights and the
GRADE report), not any single component.

**Limitations.** First, ONISHI inherits the limitations of its components: IONE's
stratification is exploratory and model-dependent, the PCA-based ICR requires
individual-patient data and is sensitive to the variable set, and KOTHA's
Bayesian integration is sensitive to prior and discount specification. Second,
the fullest pipeline is data-hungry, requiring IPD; combinations that rely only
on published summaries are correspondingly more limited. Third, the IST
illustration is deliberately a single, coherent case rather than a validation
study: the national ICRs were near-uniform, so the information-weighting step
demonstrated robustness rather than a change in estimate—information weighting is
expected to matter more when studies differ markedly in information content, an
effect we illustrate separately (Supplement). Finally, the "additional patients"
figure is an information-size projection under the observed event rate and effect,
intended as a design heuristic, not a formal sample-size calculation for a
specific future protocol.

**Implications and future work.** For applied evidence synthesis, ONISHI offers a
structured way to interrogate a synthesis before trusting it—and, importantly, a
way to rescue inconclusive but coherent trials by characterising them as
information-limited and quantifying what further evidence would resolve them.
Priorities for future work are a unified software implementation of the pipeline,
prospective evaluation on synthesis problems with known ground truth, and
extension of the hand-off interfaces to time-to-event and network-meta-analytic
settings.
