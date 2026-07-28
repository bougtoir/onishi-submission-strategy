# -*- coding: utf-8 -*-
"""Manuscript content for the ONISHI integration paper (AJE, Practice of Epidemiology).

Numbers are read from integration_analysis/results.json at build time; this module
holds prose only. Citation markers use {n} / {a-b}; they are rendered as
Word-native superscripts. Figure/table references are plain text and are
verified against the actual figures/tables by the build script.
"""

TITLE = ("ONISHI: an integrated framework for diagnosing the validity of "
         "evidence synthesis across three levels")

SHORT_TITLE = "Cross-level diagnosis of evidence synthesis"

ARTICLE_TYPE = "Practice of Epidemiology"

AUTHORS = [
    {"name": "[Author One]", "aff": 1, "corr": True,
     "email": "[corresponding.author@institution.edu]"},
    {"name": "[Author Two]", "aff": 1, "corr": False, "email": None},
]
AFFILIATIONS = {
    1: "[Department, Institution, City, Country]",
}
CORR_ADDRESS = ("[Corresponding author: Author One, Department, Institution, "
                "full postal address, City, Postcode, Country; "
                "email corresponding.author@institution.edu]")

# Title-page-only fields (identity-revealing; kept OUT of the anonymized
# manuscript to support AJE double-anonymous review).
SPECIAL_COLLECTION = "[None / to be completed by the authors, if applicable.]"
ORCID_IDS = "[Author One ORCiD: 0000-0000-0000-0000; Author Two ORCiD: 0000-0000-0000-0000]"
JOINT_AUTHORSHIP = "[Not applicable / specify dual lead authorship if applicable.]"
ACKNOWLEDGEMENTS = ("The authors thank the International Stroke Trial "
                    "Collaborative Group and Edinburgh DataShare for making the "
                    "individual patient data publicly available.")
FUNDING = "[None / to be completed by the authors, including specific grant numbers.]"
CONFLICTS = "[None declared \u2014 to be confirmed by the authors.]"
DISCLAIMER = ("The views expressed are those of the authors. [Complete or remove "
              "as applicable.]")
DATA_AVAILABILITY = ("The International Stroke Trial individual patient data are "
                     "publicly available from Edinburgh DataShare "
                     "(https://datashare.ed.ac.uk/handle/10283/124). Analysis "
                     "code that reproduces every reported number and figure is "
                     "available at [repository URL / DOI].")
AI_USE = ("An AI assistant was used to help draft and format the manuscript and "
          "to implement the analysis code; all content, analyses, and numbers "
          "were reviewed and verified by the authors, who take full "
          "responsibility for the work. See the cover letter.")

KEYWORDS = [
    "evidence synthesis", "meta-analysis", "heterogeneity",
    "effect modification", "individual patient data",
    "optimal information size", "Bayesian methods", "research methods",
]

# Highlights: each <= ~90 characters, plain statements, no over-claiming.
HIGHLIGHTS = [
    "Evidence synthesis can fail at three distinct levels that require different diagnostics.",
    "ONISHI pairs each level with one method and chains them into a single pipeline.",
    "Methods hand off subgroup labels, information weights, and power sizing on shared data.",
    "A worked example uses public data from the International Stroke Trial ({N} patients).",
    "The example trial is coherent across risk strata but information-limited, not null.",
]

# Abstract: unstructured, <= 200 words (AJE).
ABSTRACT = (
    "Evidence synthesis can fail in at least three independent ways: the studies "
    "pooled may carry unequal amounts of information (between studies), a study "
    "population may hide coherent subgroups with different behaviour (within "
    "studies), and randomized and observational evidence may disagree or an "
    "inconclusive result may be misread as showing no effect (between study "
    "types). Existing tools address these problems separately. We describe ONISHI "
    "(Optimal Normalization, Incoherence Stratification, and Harmonized "
    "Integration), a framework that assigns one previously reported method to each "
    "level\u2014LINKO between studies, IONE within studies, and KOTHA between study "
    "types\u2014and chains them into a single pipeline on shared data with defined "
    "hand-offs between methods. We specify the interfaces, describe the analytic "
    "capabilities that emerge from combining methods, and give a worked example on "
    "public individual patient data from the International Stroke Trial ({N} "
    "patients). The pipeline shows the aspirin effect on 14-day mortality to be "
    "coherent across risk strata yet informationally insufficient rather than null "
    "({INFOFRAC} of the optimal information size), and it quantifies the additional "
    "evidence needed. ONISHI offers a structured way to interrogate a synthesis "
    "before trusting it."
)

# Body blocks: ("H1", text) heading; ("P", text) paragraph; ("FIG", n)/("TBL", n)
# inline-placement markers (used only by the review copy). Citation markers {n}.
BODY = [
    ("H1", "INTRODUCTION"),
    ("P",
     "Evidence synthesis\u2014combining results across studies to estimate an "
     "effect\u2014underlies much of clinical epidemiology and guideline "
     "development. It usually proceeds by pooling a small number of summary "
     "quantities under the assumption that those summaries are commensurable and "
     "that a single pooled estimate is meaningful. That assumption can break in "
     "more than one way, and the ways are not interchangeable."),
    ("P",
     "We distinguish three levels at which a synthesis can be compromised. Between "
     "studies, the outcome measured in each study may carry unequal amounts of "
     "information about the effect, so that nominally comparable studies "
     "contribute unequally; the LINKO method (Latent Information Normalization for "
     "Key Outcomes) quantifies this through an information contribution ratio "
     "(ICR).{1} Within a study, an apparently homogeneous population may contain "
     "coherent subgroups whose effects differ, so that a single average "
     "misrepresents every subgroup; the IONE method (Incoherence-Oriented "
     "Neutralisation and Extraction) detects such structure through an incoherence "
     "indicator, C1, and a within-stratum homogeneity measure, W.{2} Between study "
     "types, randomized and observational evidence may diverge and an inconclusive "
     "result may be mistaken for evidence of no effect; the KOTHA method "
     "(Knowledge-driven Observational-Trial Harmonisation Approach) addresses this "
     "with counterfactual power analysis and Bayesian harmonization.{3}"),
    ("P",
     "Each level already has established tools. Heterogeneity statistics such as "
     "the I\u00b2 statistic and the between-study variance \u03c4\u00b2 quantify "
     "inconsistency between studies but do not attribute it to a level or a "
     "mechanism.{4} Propensity-score methods adjust observational comparisons for "
     "measured confounding.{5} The Grading of Recommendations Assessment, "
     "Development and Evaluation (GRADE) approach codifies how certainty in a body "
     "of evidence should be rated.{6} Target-trial emulation disciplines "
     "observational analyses by specifying the randomized trial they "
     "approximate.{7} These tools are powerful within their domains, but each "
     "targets one level, and none provides a way to move systematically across "
     "levels on the same data."),
    ("P",
     "We describe ONISHI (Optimal Normalization, Incoherence Stratification, and "
     "Harmonized Integration), a framework that pairs each level with one of the "
     "three methods above and connects them into a single pipeline. Our "
     "contribution is threefold: a conceptual account of why the three methods are "
     "complementary rather than redundant; the analytic capabilities that arise "
     "from combining them; and explicit hand-off interfaces that let the output of "
     "one method parameterize the next. We give an overview of the framework, "
     "summarize the component methods, describe their pairwise and joint "
     "combinations, specify the integrated pipeline, and illustrate the whole "
     "pipeline on a single public dataset."),

    ("H1", "THE ONISHI FRAMEWORK"),
    ("P",
     "ONISHI is organized around a simple correspondence: three levels of "
     "potential failure, three methods, and one shared data basis (Figure 1). "
     "LINKO operates between studies, IONE within studies, and KOTHA between study "
     "types (Table 1). The three components map onto the framework name\u2014"
     "Normalization (LINKO), Incoherence Stratification (IONE), and Harmonized "
     "Integration (KOTHA)."),
    ("FIG", 1),
    ("P",
     "The methods draw on a common set of inputs rather than incompatible data "
     "structures. LINKO can operate on published trial summaries or on individual "
     "patient data (IPD); IONE requires IPD or an observational cohort; KOTHA "
     "combines randomized and observational effect estimates and, where available, "
     "IPD. Because these inputs overlap, a single dataset with IPD can feed all "
     "three methods, which is what makes a sequential pipeline possible."),
    ("P",
     "Each method is reported in full in a separate manuscript;{1-3} here we treat "
     "them as components with defined inputs and outputs and focus on their "
     "integration. Table 1 summarizes each method's target level, core metric, "
     "primary input, and what it verifies."),
    ("TBL", 1),

    ("H1", "COMPONENT METHODS"),
    ("P",
     "LINKO quantifies how much information each study or endpoint contributes to "
     "a pooled estimate through the ICR, computed either from a variance "
     "decomposition or from a principal-component-analysis (PCA)-based "
     "estimator.{1} A low ICR flags a study or endpoint whose nominal weight in "
     "the synthesis is not matched by its informational content, so that it can be "
     "down-weighted or reported explicitly rather than pooled uncritically."),
    ("P",
     "IONE asks whether a single population conceals coherent subgroups with "
     "distinct behaviour.{2} It proceeds in two steps: the incoherence indicator "
     "C1, defined as one minus the I\u00b2 statistic on the relevant partition, "
     "detects departure from a single coherent effect, and coherent subgroups are "
     "then extracted, with within-stratum homogeneity summarized by W. IONE is "
     "explicitly an exploratory, model-dependent diagnostic, in keeping with the "
     "distinction between risk-based and effect-based approaches to "
     "treatment-effect heterogeneity.{8}"),
    ("P",
     "KOTHA harmonizes randomized and observational evidence and separates "
     "\u201cevidence of no effect\u201d from \u201cno evidence of effect\u201d.{3} "
     "It comprises three modules: Module K (counterfactual power simulation), "
     "Module T (hierarchical Bayesian integration), and Module H, which links the "
     "analysis to reporting standards by supplying an optimal information size "
     "(OIS), trial sequential analysis (TSA),{9} and the GRADE imprecision "
     "domain.{10} Detailed derivations and validation of each method are given in "
     "the respective reports;{1-3} we summarize only what the pipeline consumes."),

    ("H1", "COMBINATIONS AND SYNERGIES"),
    ("P",
     "Because the three methods target non-overlapping levels, pairing them yields "
     "capabilities that none has alone. We describe the three pairwise "
     "combinations and the full triple, illustrating each on the shared dataset "
     "introduced below."),
    ("P",
     "LINKO with IONE separates two sources of apparent heterogeneity that are "
     "easily confused: differences in information content (LINKO) and genuine "
     "subgroup incoherence (IONE). Applying LINKO within IONE-defined subgroups "
     "shows that a subgroup can carry little information yet a coherent effect, or "
     "a large information share yet a divergent effect; the pair distinguishes "
     "these cases and thereby supports root-cause identification of heterogeneity "
     "rather than its mere quantification."),
    ("P",
     "LINKO with KOTHA makes the information content of the evidence explicit in "
     "both pooling and certainty assessment. The ICR enters KOTHA directly: as an "
     "input to the Module K power calculation and as a prior weight in the Module "
     "T Bayesian integration, while Module H reports the ICR alongside the OIS and "
     "TSA."),
    ("P",
     "IONE with KOTHA links population structure to external validity. IONE's "
     "subgroup risk profiles feed KOTHA's counterfactual power module, so that "
     "power is evaluated per risk stratum rather than for an undifferentiated "
     "population, and the C1 indicator informs how representative the evidence is "
     "judged to be."),
    ("P",
     "Chaining all three methods\u2014incoherence detection, information "
     "quantification, and harmonized integration\u2014produces a comprehensive "
     "assessment in which heterogeneity is first localized, then weighted by "
     "information, then integrated into a single decision-grade read-out. The "
     "next section specifies this pipeline."),

    ("H1", "INTEGRATED PIPELINE"),
    ("P",
     "The pipeline runs IONE \u2192 LINKO \u2192 KOTHA on shared data (Figure 2). "
     "Phase 1 (IONE) decomposes the population into coherent subgroups and "
     "computes C1 and W. Phase 2 (LINKO) recomputes the ICR within each subgroup "
     "and generates the information-weighted summaries. Phase 3 (KOTHA) integrates "
     "the evidence and produces the decision-support output."),
    ("FIG", 2),
    ("P",
     "The value of the pipeline lies in the defined hand-offs between phases "
     "(Table 2). IONE passes its subgroup labels to LINKO, which recomputes the "
     "ICR within each subgroup, and its subgroup risk profiles to KOTHA Module K, "
     "which uses them to parameterize per-stratum power. LINKO passes the ICR to "
     "KOTHA Module T, where it scales the information borrowed in the hierarchical "
     "(power-prior) integration,{11} and, together with C1, to Module H as "
     "reporting items."),
    ("TBL", 2),
    ("P",
     "Two cross-phase hand-offs (dashed arrows, Figure 2) bypass the strict "
     "sequence: IONE risk profiles reach Module K directly, and LINKO's ICR "
     "reaches Module T directly. These interfaces are what turn three methods into "
     "one analysis rather than three analyses reported side by side."),

    ("H1", "ILLUSTRATIVE APPLICATION"),
    ("P",
     "To show how the three components act as one pipeline rather than three "
     "separate tools, we applied ONISHI sequentially\u2014IONE \u2192 LINKO \u2192 "
     "KOTHA\u2014to a single publicly available individual-patient dataset, the "
     "International Stroke Trial (IST; open access, Edinburgh DataShare).{12,13} We "
     "analysed the effect of randomized aspirin allocation on 14-day death among "
     "the {N} of {N_RAND} randomized patients with complete baseline covariates "
     "(complete-case analysis; 25 baseline variables; event rate {ER}). Pooled "
     "across the "
     "whole trial, the effect is close to null and inconclusive (odds ratio [OR] "
     "{OR_overall}, 95% confidence interval [CI] {CI_overall}), the kind of "
     "\u201cflat\u201d result that is routinely filed as showing no benefit. "
     "ONISHI turns this single result into a layered, decision-grade read-out "
     "(Figures 3\u20136; Table 3)."),
    ("FIG", 3),
    ("P",
     "Phase 1\u2014IONE (within-study coherence). We stratified patients into four "
     "latent risk groups by their predicted outcome probability. The 14-day "
     "mortality rose from {ER_s0} in stratum 0 to {ER_s3} in stratum 3, confirming "
     "strong latent population structure. Crucially, the aspirin effect was "
     "coherent across these strata: the incoherence indicator C1 (effect) = "
     "{C1} (between-stratum I\u00b2 = 0%) and the within-stratum homogeneity W = "
     "{W}. In other words, IONE finds no hidden effect modification\u2014the "
     "treatment effect itself does not differ by risk group (Figure 3A)."),
    ("P",
     "Phase 2\u2014LINKO (information weight). For each IONE stratum we recomputed "
     "the endpoint ICR via the PCA-based estimator. The ICR increased "
     "monotonically with baseline risk (stratum 0 \u2192 3: {ICR_s0}, {ICR_s1}, "
     "{ICR_s2}, {ICR_s3}; median {ICR_med}), showing that the outcome carries very "
     "different amounts of information across subgroups even though the effect is "
     "homogeneous. The two diagnostics are therefore complementary and "
     "dissociable: a coherent effect (IONE) coexists with a strongly risk-"
     "dependent information contribution (LINKO) (Figure 3B)."),
    ("P",
     "We also applied LINKO at the between-study level, treating the 13 IST "
     "national sub-studies as studies (Figure 4). Random-effects "
     "meta-analysis{14} gave a pooled OR of {OR_iv} (standard error [SE] {SE_iv}; "
     "I\u00b2 = {I2_p2}). Re-weighting each country by its ICR left the point "
     "estimate unchanged (OR {OR_icr}). We note explicitly that the accompanying "
     "change in the standard error ({SE_iv} \u2192 {SE_icr}) is not an effect of "
     "information weighting: an equal-weight estimator yields the same standard "
     "error ({SE_unit}), so the reduction reflects the removal of the "
     "random-effects between-country variance (\u03c4\u00b2), not the ICR weights, "
     "whose values were near-uniform here ({ICR_BS_LO}\u2013{ICR_BS_HI}). The "
     "correct reading "
     "of this step is therefore robustness: the harmonized point estimate is "
     "insensitive to information weighting."),
    ("FIG", 4),
    ("P",
     "Phase 3\u2014KOTHA (integration and information sizing). We passed the IONE "
     "risk profiles into KOTHA's counterfactual-power module (Figure 5). "
     "Holding the trial size and the pooled effect fixed, statistical power at the "
     "observed effect ranged from {pow_s0} in the lowest-risk stratum to {pow_s3} "
     "in the highest-risk stratum, quantifying how event scarcity\u2014not absence "
     "of effect\u2014drives the flat result. Module H formalized this: against an "
     "optimal information size of {OIS} events, the trial accrued {OBS} "
     "(information fraction {INFOFRAC}), and trial sequential analysis gave a "
     "cumulative Z of {TSAZ}, inside the \u00b11.96 monitoring boundary. Finally, "
     "the ICR-guided power-prior integration harmonized the strata into an OR of "
     "{OR_pp_lo}\u2013{OR_pp_hi}, revising the naive probability of benefit "
     "downward from {PB_naive} to {PB_icr} (Figure 6)."),
    ("FIG", 5),
    ("FIG", 6),
    ("P",
     "Integrated read-out. Read together, the pipeline yields a single conclusion "
     "that no component gives alone: the aspirin effect is coherent across the "
     "population (no effect modification; C1 = {C1}), but the current evidence is "
     "informationally insufficient rather than null (information fraction "
     "{INFOFRAC}; cumulative Z = {TSAZ}). Converting the shortfall into a design "
     "target, reaching the optimal information size would require {ADD_EV} "
     "additional events\u2014about {ADD_N} additional patients at the trial's "
     "overall event rate (roughly doubling enrolment). IONE's risk profiles show "
     "this target is reached far more efficiently by enriching for higher-risk "
     "patients (about {ADD_N_S3} additional stratum-3-like patients versus about "
     "{ADD_N_S0} stratum-0-like). ONISHI thus reframes a filed-away "
     "\u201cnegative\u201d trial "
     "as an interim result and outputs the sample size a future study would "
     "need\u2014an output available only when the three methods are chained "
     "(Table 3)."),
    ("TBL", 3),

    ("H1", "DISCUSSION"),
    ("P",
     "We have described ONISHI, a framework that diagnoses the validity of "
     "evidence synthesis across three independent levels\u2014between studies "
     "(which studies carry the informative signal; LINKO), within studies (whether "
     "a population hides coherent subgroups; IONE), and between study types (how to "
     "harmonize randomized and observational evidence, and how to distinguish "
     "\u201cno effect\u201d from \u201cno information\u201d; KOTHA)\u2014and chains "
     "the three into a single pipeline on shared data. The IST application shows "
     "the practical payoff: individually, each method stops at a partial statement "
     "(\u201cthe effect is homogeneous\u201d, \u201cthe pooled estimate is "
     "robust\u201d, \u201clow-risk strata are underpowered\u201d), whereas the "
     "sequential pipeline delivers one actionable verdict\u2014coherent effect, "
     "insufficient information, and the additional sample size required for "
     "resolution."),
    ("P",
     "ONISHI is complementary to, not a replacement for, established tools. "
     "Heterogeneity statistics quantify inconsistency but do not attribute it to a "
     "level or a mechanism;{4} ONISHI separates effect incoherence (IONE) from "
     "information weight (LINKO). GRADE codifies certainty judgements, and KOTHA's "
     "Module H connects directly to the GRADE imprecision domain by supplying the "
     "OIS, trial sequential analysis, and an explicit information fraction.{6,10} "
     "Target-trial emulation and individual-patient-data meta-analysis address the "
     "between-study-type and between-study levels respectively,{7,15} but neither "
     "provides the within-study coherence diagnosis that IONE contributes, which "
     "is aligned with predictive approaches to treatment-effect heterogeneity.{8} "
     "The framework's novelty is thus the cross-level integration and the defined "
     "hand-offs between methods (subgroup labels \u2192 counterfactual power; ICR "
     "\u2192 integration weights and the GRADE report), not any single component."),
    ("P",
     "Several limitations follow. First, ONISHI inherits the limitations of its "
     "components: IONE's stratification is exploratory and model-dependent, the "
     "PCA-based ICR requires individual patient data and is sensitive to the "
     "variable set, and KOTHA's Bayesian integration is sensitive to prior and "
     "discount specification. Second, the fullest pipeline is data-hungry, "
     "requiring IPD; combinations that rely only on published summaries are "
     "correspondingly more limited. Third, the IST illustration is deliberately a "
     "single, coherent case rather than a validation study: the national ICRs were "
     "near-uniform, so the information-weighting step demonstrated robustness "
     "rather than a change in estimate\u2014information weighting is expected to "
     "matter more when studies differ markedly in information content. Fourth, the "
     "IST analysis was complete-case ({N} of {N_RAND} randomized patients with "
     "complete baseline covariates), so informative missingness could bias the "
     "illustration, and the between-study step treats the trial's national "
     "sub-studies as if they were independent studies\u2014an illustrative device, "
     "since they share a single protocol rather than being separate trials. Fifth, "
     "the per-stratum coherence, power, and information analyses are exploratory "
     "and not adjusted for multiple comparisons. Finally, the "
     "\u201cadditional patients\u201d figure is an information-size projection "
     "under the observed event rate and effect, intended as a design heuristic, "
     "not a formal sample-size calculation for a specific future protocol."),
    ("P",
     "For applied evidence synthesis, ONISHI offers a structured way to interrogate "
     "a synthesis before trusting it and, importantly, a way to characterize "
     "inconclusive but coherent trials as information-limited while quantifying "
     "what further evidence would resolve them. Priorities for future work are a "
     "unified software implementation of the pipeline, prospective evaluation on "
     "synthesis problems with known ground truth, and extension of the hand-off "
     "interfaces to time-to-event and network-meta-analytic settings."),

    ("H1", "CONCLUSION"),
    ("P",
     "Evidence synthesis can be compromised at three distinct levels, and "
     "diagnosing one does not diagnose the others. ONISHI pairs each level with a "
     "dedicated method and chains the three into a single, reproducible pipeline "
     "with explicit interfaces, so that a body of evidence can be interrogated "
     "across levels on shared data. Applied to a large public trial, the pipeline "
     "reframed an inconclusive result as coherent but information-limited and "
     "quantified the evidence needed to resolve it. The framework is complementary "
     "to existing appraisal tools and is intended to make the validity of a "
     "synthesis an explicit, inspectable property rather than an assumption."),
]

# ---------------------------------------------------------------------------
# References, in order of first appearance in BODY.
# ---------------------------------------------------------------------------
REFERENCES = [
    # 1 LINKO
    "[Author One], [Author Two]. LINKO: Latent Information Normalization for Key "
    "Outcomes\u2014quantifying endpoint information contribution in evidence "
    "synthesis. Research Square. Preprint (under review). "
    "doi:10.21203/rs.3.rs-9338552/v1.",
    # 2 IONE
    "[Author One], [Author Two]. IONE: Incoherence-Oriented Neutralisation and "
    "Extraction for detecting hidden population structure in observational "
    "studies. Research Square. Preprint (under review). "
    "doi:10.21203/rs.3.rs-9271445/v1.",
    # 3 KOTHA
    "[Author One], [Author Two]. KOTHA: a Knowledge-driven Observational-Trial "
    "Harmonisation Approach for evidence integration. Research Square. Preprint "
    "(under review). doi:10.21203/rs.3.rs-9420092/v1.",
    # 4 Higgins Thompson
    "Higgins JPT, Thompson SG. Quantifying heterogeneity in a meta-analysis. Stat "
    "Med. 2002;21(11):1539-1558. doi:10.1002/sim.1186.",
    # 5 Rosenbaum Rubin
    "Rosenbaum PR, Rubin DB. The central role of the propensity score in "
    "observational studies for causal effects. Biometrika. 1983;70(1):41-55. "
    "doi:10.1093/biomet/70.1.41.",
    # 6 GRADE BMJ 2008
    "Guyatt GH, Oxman AD, Vist GE, et al. GRADE: an emerging consensus on rating "
    "quality of evidence and strength of recommendations. BMJ. "
    "2008;336(7650):924-926. doi:10.1136/bmj.39489.470347.AD.",
    # 7 Hernan Robins target trial
    "Hern\u00e1n MA, Robins JM. Using big data to emulate a target trial when a "
    "randomized trial is not available. Am J Epidemiol. 2016;183(8):758-764. "
    "doi:10.1093/aje/kwv254.",
    # 8 Kent PATH
    "Kent DM, Paulus JK, van Klaveren D, et al. The Predictive Approaches to "
    "Treatment effect Heterogeneity (PATH) Statement. Ann Intern Med. "
    "2020;172(1):35-45. doi:10.7326/M18-3667.",
    # 9 Wetterslev TSA
    "Wetterslev J, Thorlund K, Brok J, Gluud C. Trial sequential analysis may "
    "establish when firm evidence is reached in cumulative meta-analysis. J Clin "
    "Epidemiol. 2008;61(1):64-75. doi:10.1016/j.jclinepi.2007.03.013.",
    # 10 GRADE imprecision
    "Guyatt GH, Oxman AD, Kunz R, et al. GRADE guidelines 6. Rating the quality of "
    "evidence\u2014imprecision. J Clin Epidemiol. 2011;64(12):1283-1293. "
    "doi:10.1016/j.jclinepi.2011.01.012.",
    # 11 Ibrahim Chen power prior
    "Ibrahim JG, Chen MH. Power prior distributions for regression models. Stat "
    "Sci. 2000;15(1):46-60. doi:10.1214/ss/1009212673.",
    # 12 Sandercock 2011 database
    "Sandercock PA, Niewada M, Cz\u0142onkowska A; International Stroke Trial "
    "Collaborative Group. The International Stroke Trial database. Trials. "
    "2011;12:101. doi:10.1186/1745-6215-12-101.",
    # 13 IST 1997 Lancet
    "International Stroke Trial Collaborative Group. The International Stroke Trial "
    "(IST): a randomised trial of aspirin, subcutaneous heparin, both, or neither "
    "among 19435 patients with acute ischaemic stroke. Lancet. "
    "1997;349(9065):1569-1581. doi:10.1016/S0140-6736(97)04011-7.",
    # 14 DerSimonian Laird
    "DerSimonian R, Laird N. Meta-analysis in clinical trials. Control Clin Trials. "
    "1986;7(3):177-188. doi:10.1016/0197-2456(86)90046-2.",
    # 15 Riley IPD
    "Riley RD, Lambert PC, Abo-Zaid G. Meta-analysis of individual participant "
    "data: rationale, conduct, and reporting. BMJ. 2010;340:c221. "
    "doi:10.1136/bmj.c221.",
]

# Figure legends (main figures). Keys are figure numbers.
FIGURE_LEGENDS = {
    1: ("Figure 1. Overview of the ONISHI framework. Three levels at which an "
        "evidence synthesis can be compromised are matched to three component "
        "methods operating on a common data basis: LINKO between studies, IONE "
        "within studies, and KOTHA between study types. ICR, information "
        "contribution ratio; IPD, individual patient data; OIS, optimal "
        "information size; TSA, trial sequential analysis; GRADE, Grading of "
        "Recommendations Assessment, Development and Evaluation."),
    2: ("Figure 2. The integrated ONISHI pipeline. Data flow runs IONE \u2192 "
        "LINKO \u2192 KOTHA, with two cross-phase hand-offs shown as dashed arrows: "
        "IONE subgroup risk profiles parameterize the KOTHA Module K power "
        "simulation, and the LINKO information contribution ratio (ICR) enters the "
        "KOTHA Module T Bayesian integration as a prior weight."),
    3: ("Figure 3. LINKO + IONE on the International Stroke Trial ({N} "
        "patients; randomized aspirin allocation, 14-day death). A) aspirin odds "
        "ratios are coherent across four latent risk strata (C1 [effect] = {C1}, "
        "W = {W}); B) the per-stratum information contribution ratio (ICR) "
        "increases with baseline risk, so a coherent effect coexists with a "
        "risk-dependent information contribution. OR, odds ratio; ICR, "
        "information contribution ratio; ER, event rate."),
    4: ("Figure 4. LINKO + KOTHA on the International Stroke Trial: pooling "
        "across 13 national sub-studies by inverse-variance random effects, ICR "
        "weighting, and equal weighting. The ICR-weighted and equal-weight point "
        "estimates coincide, so information weighting demonstrates robustness "
        "rather than a change in estimate. OR, odds ratio; ICR, information "
        "contribution ratio."),
    5: ("Figure 5. IONE + KOTHA on the International Stroke Trial: A) statistical "
        "power at the observed effect against the assumed true odds ratio for "
        "each risk stratum; B) power at the trial-wide pooled odds ratio per "
        "stratum, quantifying how event scarcity\u2014not absence of "
        "effect\u2014drives the flat result. OIS, optimal information size."),
    6: ("Figure 6. Full ONISHI pipeline on the International Stroke Trial: A) "
        "IONE subgroup aspirin odds ratios by stratum; B) LINKO per-stratum "
        "information weights; C) KOTHA ICR-guided power-prior harmonization "
        "(harmonized odds ratio with 95% credible band across the discount on "
        "low-ICR strata); D) trial sequential analysis (cumulative Z = {TSAZ}, "
        "within the \u00b11.96 boundary; information fraction {INFOFRAC}). "
        "OR, odds ratio; ICR, information contribution ratio."),
}

# Alt text (accessibility) for each main figure, required by AJE beneath the
# figure legend. Describes the visual content for readers using screen readers.
FIGURE_ALT_TEXT = {
    1: ("Schematic with three coloured boxes labelled LINKO, IONE, and KOTHA "
        "sitting above a single box labelled Common Data Sources, with arrows "
        "from the data box to each method; each method box lists its outputs and "
        "the level of synthesis it addresses (between studies, within studies, "
        "and between study types)."),
    2: ("Left-to-right flow diagram with four boxes: IONE, LINKO, KOTHA, and "
        "Output, connected by solid arrows, drawing on a shared input-data box "
        "at the bottom; two dashed arrows indicate cross-phase hand-offs from "
        "IONE to KOTHA Module K and from LINKO to KOTHA Module T."),
    3: ("Two-panel figure. A) forest plot of aspirin odds ratios across four risk "
        "strata, all confidence intervals crossing an odds ratio of 1; B) bar "
        "chart of the information contribution ratio rising across the four "
        "strata."),
    4: ("Forest plot of aspirin odds ratios across 13 national sub-studies with "
        "three overlaid pooled estimates (inverse-variance random effects, "
        "ICR-weighted, and equal-weight) that nearly coincide near an odds ratio "
        "of 0.93, plotted on a logarithmic axis."),
    5: ("Two-panel figure. A) power curves of statistical power against the "
        "assumed true odds ratio for each of four risk strata; B) bar chart of "
        "power at the pooled odds ratio by stratum, increasing with baseline "
        "risk."),
    6: ("Four-panel figure. A) forest plot of subgroup aspirin odds ratios by "
        "stratum; B) bar chart of information contribution ratio by stratum; C) "
        "harmonized odds ratio with a 95% credible band as a function of the "
        "discount applied to low-ICR strata; D) trial-sequential-analysis "
        "cumulative-Z curve within the \u00b11.96 monitoring boundaries."),
}

TABLE_TITLES = {
    1: "Table 1. The three component methods of the ONISHI framework.",
    2: "Table 2. Hand-off interfaces in the integrated ONISHI pipeline.",
    3: ("Table 3. Stratum-wise outputs of the ONISHI pipeline applied to the "
        "International Stroke Trial."),
}

TABLE_FOOTNOTES = {
    1: ("ICR, information contribution ratio; IPD, individual patient data; OIS, "
        "optimal information size; TSA, trial sequential analysis; I\u00b2, "
        "heterogeneity statistic; C1, incoherence indicator (one minus I\u00b2); "
        "W, within-stratum homogeneity."),
    2: ("ICR, information contribution ratio; C1, incoherence indicator; OIS, "
        "optimal information size; TSA, trial sequential analysis; GRADE, Grading "
        "of Recommendations Assessment, Development and Evaluation."),
    3: ("Strata are latent risk groups defined by predicted outcome probability. "
        "Odds ratios are for randomized aspirin allocation on 14-day death; "
        "confidence intervals are computed on the log-odds scale. The ICR is the "
        "principal-component-analysis-based estimate. Power is computed at the "
        "trial-wide pooled odds ratio. \u201cAdditional patients to OIS\u201d is "
        "the number of further patients, at each stratum's event rate, projected "
        "to reach the optimal information size; it is a design heuristic, not a "
        "formal sample-size calculation. CI, confidence interval; ICR, information "
        "contribution ratio; OIS, optimal information size."),
}
