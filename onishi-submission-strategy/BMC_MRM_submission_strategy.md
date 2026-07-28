# BMC Medical Research Methodology 特集号 "Causal inference and observational data vol. 2" 適合性分析・投稿戦略

## 1. 特集号のスコープ

**締切：2026年7月30日** ｜ IF 3.4 (2024) ｜ 5yr IF 5.2 ｜ OA

特集号が歓迎するトピック（公式ページより抜粋）：

| # | トピック | 備考 |
|---|---------|------|
| 1 | 因果推論フレームワークの方法論的進歩（ポテンシャルアウトカム、構造的因果モデル、グラフィカルモデル） | |
| 2 | バイアス軽減技術（交絡制御、選択バイアス、測定誤差） | |
| 3 | 観察データの因果発見アルゴリズム・ML手法 | |
| 4 | 傾向スコア法の実装・比較 | |
| 5 | 操作変数法・自然実験 | |
| 6 | 感度分析・定量的バイアス分析 | |
| 7 | リアルワールドデータによる比較効果研究 | |
| 8 | 疫学・医療サービス研究・臨床意思決定への応用 | |
| 9 | 因果推論研究のための報告基準・透明性ツール | |

**Guest Editors**: Rishi J Desai (Harvard), Ivan Olier (LJMU), Joy Shi (MGH)
— 全員、観察研究×因果推論の方法論者。RCT-観察研究の橋渡しに関心あり。

---

## 2. 各論文の適合性評価

### 2.1 KOTHA — ★★★★★ 最適合

| 項目 | 評価 |
|------|------|
| **内容** | RCTと観察研究のエビデンス乖離を診断・解決する3モジュールフレームワーク（反実仮想パワーシミュレーション、階層ベイズ統合、解釈的ガイドライン） |
| **該当トピック** | #1（因果推論フレームワーク）、#2（バイアス軽減）、#6（感度分析）、#7（RWDによる比較効果研究）、#8（臨床意思決定） |
| **適合理由** | 特集号の中核テーマそのもの。「観察研究から因果的結論を引き出す際の課題」に正面から取り組み、RCTとの調和を方法論として提案。Module KのCounterfactual Power Simulationは観察データからのpower推定、Module Tは階層ベイズによるRCT-観察統合、Module HはGRADE拡張。いずれも特集号エディターの関心と直接合致 |
| **懸念点** | なし。最も自然な投稿先 |

### 2.2 IONE — ★★★★☆ 高適合

| 項目 | 評価 |
|------|------|
| **内容** | 観察研究における隠れた部分集団構造（インコヒーレンス）を検出し、シンプソンのパラドックスを解決するフレームワーク。C1コヒーレンス指標による定量化 |
| **該当トピック** | #2（交絡制御）、#3（データからの因果発見・ML手法）、#8（疫学・臨床応用） |
| **適合理由** | シンプソンのパラドックスは因果推論の古典的問題であり、「観察データから正しい因果効果を推定する」ための前処理として位置づけ可能。PCA+クラスタリングによる部分集団検出はML手法に該当。交絡バイアス・効果修飾の見落とし・生態学的誤謬への対処はトピック#2に直結 |
| **懸念点** | IONEの中核は「集団構造の検出」であり、因果推論そのものの方法論とは一歩距離がある。**フレーミングが鍵**：「観察研究から因果推論を行う前提条件としての集団均質性の確保」と位置づければ適合度が上がる |

### 2.3 LINKO — ★★★☆☆ 中適合

| 項目 | 評価 |
|------|------|
| **内容** | メタ解析におけるICR（情報寄与率）を定量化し、エンドポイントの情報代表性を診断。Prism Forest Plot可視化 |
| **該当トピック** | #6（定量的バイアス分析）、#9（報告基準・透明性ツール） |
| **適合理由** | メタ解析の方法論として、情報構造の偏りを「バイアスの一形態」として位置づけることが可能。Prism Forest Plotは透明性ツールに該当 |
| **懸念点** | LINKOの主対象はメタ解析であり、「観察データからの因果推論」というスコープとはやや焦点がずれる。メタ解析はRCTの統合が主であり、特集号の「observational data」の文脈とは異なる。**ただし**、メタ解析に観察研究を含む場合や、観察研究のIPDメタ解析であればスコープ内 |

### 2.4 ONISHI（統合論文）— ★★★★☆ 高適合

| 項目 | 評価 |
|------|------|
| **内容** | LINKO+IONE+KOTHAの統合パイプライン。4通りの組み合わせによる包括的エビデンス評価 |
| **該当トピック** | #1（方法論的進歩）、#2（バイアス軽減）、#7（RWDによる比較効果研究）、#8（臨床意思決定）、#9（透明性ツール） |
| **適合理由** | 「集団構造検出→情報定量化→エビデンス調和」の全段階をカバーする統合的方法論は、"interdisciplinary solutions bridging statistics, computer science, and biomedical sciences"（特集号が特に歓迎と明記）に該当 |
| **懸念点** | 前提3論文の参照が必要。プレプリントでの先行公開が望ましい |

---

## 3. 適合性の総合判断

**結論：KOTHAとIONEは高い適合性、ONISHIも条件付きで適合。LINKOは単独ではスコープとのずれがあるが、フレーミング次第で可能。**

```
適合度ランキング:
  KOTHA  ★★★★★  — 特集号の中核テーマそのもの
  IONE   ★★★★☆  — 因果推論の前提条件として位置づけ可能
  ONISHI ★★★★☆  — 統合論文として高い付加価値（前提論文の公開が条件）
  LINKO  ★★★☆☆  — メタ解析焦点。観察研究IPDメタ解析に寄せれば可能
```

---

## 4. 投稿戦略

### 4.1 推奨戦略：段階的アプローチ

4論文全てを特集号に投稿するのは**リスクが高い**（エディターが「まとめて出しすぎ」と判断する可能性、査読者リソースの集中、LINKOのスコープ問題）。

#### **推奨案：特集号にはKOTHA + IONE（+ ONISHI）、LINKOは別ルート**

```
┌──────────────────────────────────────────────────────────────────┐
│ Timeline                                                        │
├──────────────┬───────────────────────────────────────────────────┤
│ 2026年4月    │ ① LINKO → arXiv/medRxiv プレプリント登録         │
│              │ ② IONE  → arXiv/medRxiv プレプリント登録         │
│              │ ③ KOTHA → arXiv/medRxiv プレプリント登録         │
├──────────────┼───────────────────────────────────────────────────┤
│ 2026年4月末  │ ④ LINKO → BMC MRM 通常投稿（特集号外）          │
│              │    またはStats in Medicine / Res Synth Methods    │
├──────────────┼───────────────────────────────────────────────────┤
│ 2026年5月    │ ⑤ KOTHA → BMC MRM 特集号投稿                    │
│              │ ⑥ IONE  → BMC MRM 特集号投稿                    │
├──────────────┼───────────────────────────────────────────────────┤
│ 2026年6月    │ ⑦ ONISHI統合論文 → BMC MRM 特集号投稿           │
│              │    (①②③のプレプリントをciteして先行性を確保)     │
├──────────────┼───────────────────────────────────────────────────┤
│ 2026年7月30日│ 特集号締切                                        │
└──────────────┴───────────────────────────────────────────────────┘
```

### 4.2 各ステップの根拠

#### ① アーカイブ先行登録（4月・3論文同時）

- **目的**：先行性の確保＋ONISHI統合論文からの参照を可能にする
- **推奨先**：**medRxiv**（医学研究方法論に最適）またはarXiv (stat.ME)
- **注意**：BMC (Springer Nature) はmedRxiv/arXivプレプリントを許容
- **3論文同時登録**により、「一連の研究プログラム」としての可視性を確保
- DOIが付与されるため、ONISHI論文からの正式引用が可能

#### ② LINKO → 通常投稿（特集号外）

- LINKOはメタ解析の方法論であり、特集号のスコープ（観察データ×因果推論）との適合度がやや低い
- **代替投稿先候補**：
  - **BMC MRM 通常号**（同じジャーナルなので、特集号エディターにもvisible）
  - **Research Synthesis Methods**（IF 9.8、メタ解析方法論の専門誌）
  - **Statistics in Medicine**（IF 2.0だが方法論に強い）
  - **Systematic Reviews**（BMC系列、メタ解析の可視化ツールに好意的）
- 特集号外への投稿を4月末に行い、KOTHA/IONEに先行させることで、特集号論文から「同著者のcompanion paper」として参照可能

#### ③ KOTHA → 特集号（5月投稿）

- 最も適合度が高いので**最優先で投稿**
- 締切まで約3ヶ月の余裕があり、査読対応の時間を確保
- Module K（反実仮想シミュレーション）のRWD×因果推論の側面を強調
- マグネシウム療法・スタチンの実データ検証は具体的応用例として強い

#### ④ IONE → 特集号（5月投稿、KOTHAと同時または1-2週遅れ）

- フレーミングの調整が必要：**「観察研究コホートにおける因果推論の前提条件としてのpopulation coherenceの検証」**
- タイトル案："Detecting Incoherent Populations in Observational Studies: A Framework for Ensuring Valid Causal Inference" — 因果推論を前面に出す
- シンプソンのパラドックス5事例の応用は、観察データの因果推論の典型的落とし穴として特集号に響く

#### ⑤ ONISHI統合論文 → 特集号（6月投稿）

- KOTHA/IONEの投稿から1ヶ月遅らせ、プレプリント引用で先行性を確保
- 「KOTHA and IONE are companion papers submitted to this collection（別途投稿中）, while LINKO has been submitted to [journal name]」とカバーレターで明記
- 統合論文としての付加価値を強調：4通りの組み合わせの実証が主題
- **リスク**：前提論文がまだ出版されていない段階での統合論文は、査読者が評価しにくい可能性
  - **対策**：プレプリントのリンクをSupplementary Materialとして提供

### 4.3 フレーミング戦略（カバーレター用）

#### KOTHA カバーレター要旨案

> "We present KOTHA, a three-module framework for diagnosing and resolving evidence discordance between randomized controlled trials and observational studies — a core challenge in drawing causal conclusions from real-world data. Module K employs counterfactual power simulation using observational risk distributions; Module T integrates trial and observational evidence via hierarchical Bayesian models with bias discounting; Module H provides structured interpretation guidelines for low-information meta-analyses. We believe KOTHA directly addresses your Collection's focus on 'improving transparency, reproducibility, and robustness' in causal inference from observational data."

#### IONE カバーレター要旨案

> "We present IONE, a framework for detecting hidden population incoherence in observational cohorts — a prerequisite for valid causal inference. When observational populations comprise latent subgroups with opposing causal structures, aggregate analyses may yield paradoxical conclusions (Simpson's paradox). IONE provides a quantitative coherence index (C1) and decomposition algorithm to ensure that causal inference is conducted within genuinely homogeneous populations. This directly contributes to your Collection's focus on 'bias mitigation techniques' and 'causal discovery algorithms.'"

---

## 5. リスクと代替案

### 5.1 リスク

| リスク | 確率 | 対策 |
|--------|------|------|
| LINKO特集号スコープ外と判定 | 中 | 通常号またはRes Synth Methodsに投稿（推奨案で対応済み） |
| ONISHI統合論文が「前提論文未出版」で査読困難 | 中 | プレプリント提供＋Supplementary Materialに全フレームワーク概要を添付 |
| 特集号に同一著者から3本は多すぎると判断される | 低〜中 | 投稿前にGuest Editorに非公式に打診（pre-submission inquiry） |
| 締切（7/30）までに全論文の準備が間に合わない | 中 | KOTHA単独投稿を最低限の目標とし、残りは通常号へ |

### 5.2 代替戦略：2論文に絞る

もし3-4論文の同時準備が現実的でない場合：

```
最小戦略：
  特集号 → KOTHA のみ（5月投稿）
  medRxiv → IONE, LINKO（4月プレプリント）
  後日   → ONISHI統合論文（KOTHA出版後）
```

```
中間戦略：
  特集号 → KOTHA + IONE（5月投稿）
  通常号 → LINKO（別ジャーナル）
  後日   → ONISHI統合論文
```

### 5.3 Pre-submission Inquiry の推奨

**特集号に複数論文を投稿する前に、Guest Editorへの事前問い合わせを強く推奨。**

BMC MRMでは editorial inquiries が可能。以下のようなメールを送付：

> "Dear Editors, We have developed a series of complementary methodological frameworks addressing different aspects of causal inference from observational data: (1) KOTHA for RCT-observational harmonization, (2) IONE for population coherence assessment, and (3) an integrating framework (ONISHI). Would you welcome 2-3 related submissions to the Collection, given that each addresses distinct methodological challenges? We would be happy to provide abstracts for your consideration."

---

## 6. まとめ

| 項目 | 推奨 |
|------|------|
| **最優先** | KOTHAを特集号に投稿（5月、スコープ完全合致） |
| **次点** | IONEを特集号に投稿（フレーミング調整して因果推論の前提条件として位置づけ） |
| **条件付き** | ONISHI統合論文を特集号に（前提3論文のプレプリント公開後） |
| **別ルート** | LINKOはRes Synth MethodsまたはBMC MRM通常号 |
| **先行措置** | 4月に3論文をmedRxivに同時登録 |
| **事前措置** | Guest Editorにpre-submission inquiry |

---

# English Translation

---

# BMC Medical Research Methodology Special Issue "Causal inference and observational data vol. 2" Suitability analysis and submission strategy

## 1. Scope of the special issue

**Deadline: July 30, 2026** | IF 3.4 (2024) | 5yr IF 5.2 | OA

Topics welcomed by the special issue (excerpted from the official page):

| # | Topic | Notes |
|---|---------|------|
| 1 | Methodological advances in causal inference frameworks (potential outcomes, structural causal models, graphical models) | |
| 2 | Bias reduction techniques (confounding control, selection bias, measurement error) | |
| 3 | Causal discovery algorithm/ML method for observed data | |
| 4 | Implementation and comparison of propensity score methods | |
| 5 | Instrumental Variable Method/Natural Experiment | |
| 6 | Sensitivity analysis/quantitative bias analysis | |
| 7 | Comparative effectiveness research using real-world data | |
| 8 | Applications to epidemiology, health services research, and clinical decision making | |
| 9 | Reporting standards and transparency tools for causal inference research | |
**Guest Editors**: Rishi J Desai (Harvard), Ivan Olier (LJMU), Joy Shi (MGH)
— All of them are methodologists of observational research and causal inference. Interested in bridging RCT-observational research.

---

## 2. Suitability assessment of each paper

### 2.1 KOTHA — ★★★★★ Optimal fit

| Item | Rating |
|------|------|
| **Contents** | A three-module framework for diagnosing and resolving evidence gaps between RCTs and observational studies (counterfactual virtual power simulation, hierarchical Bayesian integration, interpretive guidelines) |
| **Applicable topics** | #1 (causal inference framework), #2 (bias reduction), #6 (sensitivity analysis), #7 (comparative effectiveness research using RWD), #8 (clinical decision making) |
| **Reason for suitability** | The core theme of the special issue itself. He tackles head-on the issue of drawing causal conclusions from observational studies and proposes a methodology that is compatible with RCT. Module K's Counterfactual Power Simulation is power estimation from observational data, Module T is RCT-observation integration using hierarchical Bayes, and Module H is GRADE extension. All directly align with the interests of the special issue editor |
| **Concerns** | None. Most natural place to post |
### 2.2 IONE — ★★★★☆ Highly compatible

| Item | Rating |
|------|------|
| **Contents** | A framework to detect hidden subpopulation structures (incoherence) in observational studies and resolve Simpson's paradox. Quantification by C1 coherence index |
| **Applicable topics** | #2 (confounding control), #3 (causal discovery from data/ML methods), #8 (epidemiology/clinical application) |
| **Reason for suitability** | Simpson's paradox is a classic problem in causal inference, and can be positioned as preprocessing for ``estimating correct causal effects from observed data.'' Subpopulation detection using PCA+clustering falls under the ML method. Dealing with confounding bias, oversight of effect modification, and ecological fallacy is directly linked to Topic #2 |
| **Concerns** | The core of IONE is "detection of group structure," which is one step away from the methodology of causal inference itself. **Framing is the key**: The goodness of fit will increase if it is positioned as "ensuring group homogeneity as a prerequisite for making causal inferences from observational studies" |

### 2.3 LINKO — ★★★☆☆ Medium compatibility

| Item | Rating |
|------|------|
| **Content** | Quantify ICR (information contribution ratio) in meta-analysis and diagnose the information representativeness of endpoints. Prism Forest Plot visualization |
| **Applicable topics** | #6 (Quantitative bias analysis), #9 (Reporting standards/transparency tools) |
| **Reason for suitability** | As a meta-analysis methodology, it is possible to position bias in information structure as a "form of bias." Prism Forest Plot is a transparency tool |
| **Points of Concern** | LINKO's main target is meta-analysis, and its focus is slightly different from the scope of "causal inference from observational data." Meta-analysis is mainly a synthesis of RCTs, which is different from the context of the special issue's ``observational data.'' **However**, if the meta-analysis includes observational studies, or if it is an IPD meta-analysis of observational studies, it is within the scope |

### 2.4 ONISHI (integrated paper) — ★★★★☆ Highly relevant

| Item | Rating |
|------|------|
| **Contents** | LINKO+IONE+KOTHA integrated pipeline. Comprehensive evidence evaluation using four combinations |
| **Applicable topics** | #1 (Methodological advances), #2 (Bias reduction), #7 (Comparative effectiveness research with RWD), #8 (Clinical decision making), #9 (Transparency tools) |
| **Reason for Relevance** | An integrated methodology that covers all stages of "population structure detection → information quantification → evidence harmonization" falls under "interdisciplinary solutions bridging statistics, computer science, and biomedical sciences" (Special issue is particularly welcome) |
| **Concerns** | Reference to Premise 3 papers is required. Advance publication as a preprint is preferable |

---

## 3. Comprehensive judgment of suitability

**Conclusion: KOTHA and IONE are highly compatible, ONISHI is also conditionally compatible. LINKO has some misalignment with the scope when used alone, but it can be done depending on the framing. **

````
Relevance ranking:
  KOTHA ★★★★★ — The core theme of the special issue itself
  IONE ★★★★☆ — Can be positioned as a precondition for causal inference
  ONISHI ★★★★☆ — High added value as an integrated paper (required publication of prerequisite paper)
  LINKO ★★★☆☆ — Meta-analysis focus. Possible by submitting observational research IPD meta-analysis
````

---

## 4. Posting strategy

### 4.1 Recommended Strategy: Phased Approach

Submitting all four papers to a special issue is **risky** (the editor may decide that it's too much to submit all at once, concentration of reviewer resources, LINKO scope issues).
#### **Recommended idea: KOTHA + IONE (+ ONISHI) for special issue, separate route for LINKO**

````
┌──────────────────────────────────────────────────────────────┐
│ Timeline │
├──────────────┬────────────────────────────────────────────────────┤
│ April 2026 │ ① LINKO → arXiv/medRxiv preprint registration │
│ │ ② IONE → arXiv/medRxiv preprint registration │
│ │ ③ KOTHA → arXiv/medRxiv preprint registration │
├──────────────┼────────────────────────────────────────────────────┤
│ End of April 2026 │ ④ LINKO → BMC MRM Regular posting (outside special issue) │
│ │ or Stats in Medicine / Res Synth Methods │
├──────────────┼────────────────────────────────────────────────────┤
│ May 2026 │ ⑤ KOTHA → BMC MRM special issue submission │
│ │ ⑥ IONE → BMC MRM special issue submission │
├──────────────┼────────────────────────────────────────────────────┤
│ June 2026 │ ⑦ ONISHI integrated paper → BMC MRM special issue submission │
│ │ (Cite the preprints of ①②③ to ensure advance notice) │
├──────────────┼────────────────────────────────────────────────────┤
│ July 30, 2026 │ Special issue deadline │
└──────────────┴──────────────────────────────────────────────────┘
````

### 4.2 Rationale for each step

#### ① Archive advance registration (April, 3 papers simultaneously)

- **Purpose**: Ensure precedence + enable reference from ONISHI integrated papers
- **Recommended destination**: **medRxiv** (best suited for medical research methodologies) or arXiv (stat.ME)
- **Note**: BMC (Springer Nature) accepts medRxiv/arXiv preprints
- **Simultaneous registration of 3 papers** ensures visibility as a "series of research programs"
- Since a DOI is assigned, official citations from ONISHI papers are possible.

#### ② LINKO → Regular post (outside special issue)

- LINKO is a meta-analysis methodology, and its fit with the scope of the special issue (observational data x causal inference) is somewhat low.
- **Alternative post destination candidates**:
  - **BMC MRM regular issue** (visible to the special issue editor as it is the same journal)
  - **Research Synthesis Methods** (IF 9.8, specialized journal for meta-analysis methodologies)
  - **Statistics in Medicine** (IF 2.0 but strong in methodology)
- **Systematic Reviews** (BMC series favors meta-analysis visualization tools)
- By posting outside of the special issue at the end of April and prior to KOTHA/IONE, it can be referenced as a "companion paper by the same author" from the special issue papers.

#### ③ KOTHA → Special issue (posted in May)

- Since it has the highest relevance, **post with top priority**
- We have about 3 months left before the deadline, so we have enough time to respond to peer reviews.
- Emphasizes the RWD x causal inference aspects of Module K (counterfactual virtual simulation)
- Validation of actual data on magnesium therapy and statins is strong as a concrete application example

#### ④ IONE → Special issue (Posted in May, at the same time as KOTHA or 1-2 weeks later)

- Framing needs adjustment: **"Verifying population coherence as a prerequisite for causal inference in observational study cohorts"**
- Proposed title: "Detecting Incoherent Populations in Observational Studies: A Framework for Ensuring Valid Causal Inference" — Bringing causal inference to the forefront
- The application of the five cases of Simpson's paradox resonates in the special issue as a typical pitfall of causal inference from observational data.
#### ⑤ ONISHI integrated paper → Special issue (posted in June)

- Delayed posting of KOTHA/IONE by one month to ensure precedence by citing preprint
- Specify in the cover letter that "KOTHA and IONE are companion papers submitted to this collection (separately submitted), while LINKO has been submitted to [journal name]"
- Emphasizes added value as an integrated paper: Demonstration of four combinations is the subject
- **Risk**: It may be difficult for reviewers to evaluate a synthesis paper when the underlying papers have not yet been published.
  - **Countermeasure**: Provide preprint link as Supplementary Material

### 4.3 Framing strategy (for cover letter)

#### KOTHA Cover Letter Abstract Draft
> "We present KOTHA, a three-module framework for diagnosing and resolving evidence discordance between randomized controlled trials and observational studies — a core challenge in drawing causal conclusions from real-world data. Module K employs counterfactual power simulation using observational risk distributions; Module T integrates trial and observational evidence via hierarchical Bayesian models with bias discounting; Module H provides structured interpretation guidelines for low-information meta-analyses. We believe KOTHA directly addresses your Collection's focus on 'improving transparency, reproducibility, and robustness' in causal inference from observational data."
#### IONE Cover Letter Summary Draft
> "We present IONE, a framework for detecting hidden population incoherence in observational cohorts — a prerequisite for valid causal inference. When observational populations comprise latent subgroups with opposing causal structures, aggregate analyses may yield paradoxical conclusions (Simpson's paradox). IONE provides a quantitative coherence index (C1) and decomposition algorithm to ensure that causal inference is conducted within genuinely homogeneous populations. This directly contributes to your Collection's focus on 'bias mitigation techniques' and 'causal discovery algorithms.'"

---

## 5. Risks and alternatives

### 5.1 Risk

| Risk | Probability | Countermeasures |
|--------|------|------|
| Determined to be outside the scope of the LINKO special issue | Medium | Posted in the regular issue or Res Synth Methods (already addressed with the recommended proposal) |
| ONISHI integrated paper is difficult to peer review because “prerequisite paper has not been published” | Medium | Preprint provided + complete framework summary attached in Supplementary Material |
| Three books from the same author in a special issue is judged to be too many | Low to Medium | Informally consult the Guest Editor before submission (pre-submission inquiry) |
| Unable to prepare all papers by the deadline (7/30) | Medium | The minimum goal is to submit a single submission to KOTHA, and the rest will be submitted to the regular issue |

### 5.2 Alternative strategy: narrow down to 2 papers

If preparing 3-4 papers at the same time is not practical:

````
Minimal strategy:
  Special issue → KOTHA only (posted in May)
  medRxiv → IONE, LINKO (April preprint)
  Later → ONISHI integrated paper (after KOTHA publication)
````

````
Intermediate strategy:
  Special issue → KOTHA + IONE (posted in May)
  Regular issue → LINKO (separate journal)
  Later → ONISHI integrated paper
````
### 5.3 Pre-submission Inquiry Recommendation

**We strongly recommend contacting the Guest Editor before submitting multiple papers to the special issue. **

BMC MRM allows editorial inquiries. Send an email like this:
> "Dear Editors, We have developed a series of complementary methodological frameworks addressing different aspects of causal inference from observational data: (1) KOTHA for RCT-observational harmonization, (2) IONE for population coherence assessment, and (3) an integrating framework (ONISHI). Would you welcome 2-3 related submissions to the Collection, given that each addresses distinct methodological challenges? We would be happy to provide abstracts for your consideration."

---

## 6. Summary

| Item | Recommendation |
|------|------|
| **Top priority** | Submit KOTHA to special issue (May, scope perfectly matched) |
| **Runner** | Submitted IONE to the special issue (adjusted the framing and positioned it as a precondition for causal inference) |
| **Conditional** | ONISHI integrated paper in special issue (after preprints of 3 prerequisite papers are published) |
| **Alternative route** | LINKO is Res Synth Methods or BMC MRM regular issue |
| **Preliminary measures** | Simultaneously register 3 papers on medRxiv in April |
| **Pre-measures** | pre-submission inquiry to Guest Editor |
