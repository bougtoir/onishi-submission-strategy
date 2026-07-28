# ONISHI 統合論文 仕様書（Specification / Outline v1）

**手法名**: ONISHI = **O**ptimal **N**ormalization, **I**ncoherence **S**tratification, and **H**armonized **I**ntegration
**位置づけ**: LINKO・IONE・KOTHA の3手法を統合する上位フレームワーク論文（統合論文 / integration paper）
**打ち出し（確定・グランドデザイン）**: ONISHI は **エビデンス統合（evidence synthesis）の妥当性を、研究間・研究内・研究種別間の3階層で診断・調和するメタ方法論**である。LINKO（研究間）・IONE（研究内）・KOTHA（研究種別間）が各階層を担い、単一データへの逐次適用で一気通貫の評価を与える。※本文では対象を "evidence synthesis" と積極的に定義し、他手法との対比（例:「メタ解析への〜ではない」等）は用いない。
**投稿先（確定）**: American Journal of Epidemiology (AJE, IF 4.8, Oxford UP, Hybrid, Subscription 出版で APC $0)。Article type は "Practice of Epidemiology" を第一想定。
　代替（不採択時）: Epidemiology (IF 4.4) → International Journal of Epidemiology (IF 6.4, 挑戦枠) → BMC MRM 通常号
**種別**: 方法論フレームワーク論文（methodological framework / "Practice of Epidemiology" 相当）
**作成日**: 2026-07-09

> 本書は本文執筆前の設計図。各セクションの目的・骨子・語数目安・図表計画・依存する既存成果物を定義する。
> 数値・結果は3構成論文（LINKO/IONE/KOTHA）の確定値を単一のソース（後述の「数値ソース台帳」）から引用し、統合論文内で再計算はしない。

---

## 0. 前提と確定事項（P1–P5 すべて確定済み / 2026-07-09）

| # | 論点 | 状態 | 確定内容・投稿直前の残チェック |
|---|------|------|--------|
| P1 | 頭字語の確定 | **確定済み** | ONISHI = Optimal Normalization, Incoherence Stratification, and Harmonized Integration（統合セッションで確定）。IONE 正式名 = **Incoherence-Oriented Neutralisation and Extraction**（IONE 論文の最新タイトル "…for Detecting Hidden Population Structure in Observational Studies" の冒頭部分）。※ONISHI 頭字語内の "Incoherence Stratification (IS)" は IONE を指すグロスであり、IONE 自身の正式名とは別。統合論文では IONE 初出時に正式名を全記載する。 |
| P2 | 投稿先の最終決定 | **確定: AJE（American Journal of Epidemiology）**。IF 4.8, Oxford UP, Hybrid, Subscription 出版で APC $0 | Article type は **"Practice of Epidemiology"（方法論開発向け）** を第一想定。語数上限は投稿直前に AJE 最新 Author Guidelines で要確認（原著系は本文 ~3,500語・Abstract 200語程度と厳しめ。方法論枠はより長め可）。本仕様の語数目安（本文 5,500–7,000語）は上限確認後に圧縮・上書きする。 |
| P3 | 3構成論文の引用形態 | **確定: 3論文とも Research Square プレプリント DOI で引用し、本文・カバーレターに "under review" と明記**。<br>・KOTHA: https://doi.org/10.21203/rs.3.rs-9420092/v1 <br>・IONE: https://doi.org/10.21203/rs.3.rs-9271445/v1 <br>・LINKO: https://doi.org/10.21203/rs.3.rs-9338552/v1 | 採択が進んだ論文があれば投稿直前に published 引用へ更新 |
| P4 | 統合デモの方針 | **確定: 方針B（単一の公開IPDに IONE→LINKO→KOTHA を実際に逐次適用し、各段階の出力を新規生成）** | 使用データは公開IPDの **IST（International Stroke Trial, LINKO で使用実績あり）** を第一候補とする。各段階の出力（C1・部分集団ラベル → 部分集団別 ICR → Module K/T/H 統合）を Fig 6 / Table 3 として新規計算。工数大につき本文執筆と並行して解析スクリプトを準備。 |
| P5 | C1 指標の呼称統一 | **確定: IONE 最新版に完全一致**。C1 = 1 − I²（**incoherence indicator**）、層内均質性の **W 指標** を併記 | 統合論文全体で IONE プレプリントの記法・定義と一字一句合わせる（記号・呼称・式） |

---

## 1. コアメッセージ（One-sentence thesis）

> 臨床エビデンスの**統合（evidence synthesis）**は「研究間（どの研究の情報が重いか）」「研究内（集団が均質か）」「研究種別間（RCT と観察研究をどう調和させるか）」という3つの独立した階層で崩れうる。ONISHI は各階層に対応する3手法（LINKO・IONE・KOTHA）を単一のデータに逐次適用する統合パイプラインであり、個別手法では捉えられない異質性の根因特定から意思決定支援までを一気通貫で提供する、エビデンス統合の妥当性診断のためのメタ方法論である。

**打ち出しの範囲（執筆方針・内部メモ）**: 本論文は evidence synthesis 全般を対象に据える。ただし「メタ解析は一部に過ぎない」という但し書きを本文で繰り返さない——3階層（研究間／研究内／研究種別間）を素直に提示すれば、IONE・KOTHA を知らない読者にも守備範囲が自然に伝わるため。冒頭で対象を "evidence synthesis" と一度定義するに留め、防御的な言い換えは避ける。

**新規性の主張（統合論文が個別3論文に上乗せする価値）**
1. 3手法が相補的（対象階層が重複しない）であることの概念的整理と、共通データ基盤上での接続仕様の提示。
2. 逐次適用パイプライン（IONE → LINKO → KOTHA）による、単独では不可能な4つの新能力（§4）。
3. 手法間のデータ受け渡し（C1 → Module K、ICR → Module T 等）のインターフェース定義。

---

## 2. 論文構成（AJE 想定 / IMRaD + 方法論拡張）

| セクション | 目的 | 語数目安 | 主な図表 |
|-----------|------|---------|---------|
| Title / Abstract | 統合フレームワークの提示 | Abstract 200–250語（構造化） | — |
| 1. Introduction | 3階層の問題設定と既存手法の限界、統合の必要性 | 600–800 | — |
| 2. The ONISHI Framework (Overview) | 3手法の役割分担と共通データ基盤 | 500–700 | **Fig 1**（概要） |
| 3. Component Methods (要約) | LINKO/IONE/KOTHA を各1段落で要約（詳細は各論文へ委譲） | 700–900 | **Table 1**（3手法比較） |
| 4. Combinations & Synergies | 4通りの組み合わせと新能力 | 900–1,100 | **Fig 2**（4組合せ）, **Fig 3**（シナジー行列）, **Fig 5**（レーダー） |
| 5. Integrated Pipeline | IONE→LINKO→KOTHA の逐次適用仕様とインターフェース | 700–900 | **Fig 4**（パイプライン）, **Table 2**（インターフェース定義） |
| 6. Illustrative Application | 統合デモ（1ケースを3手法逐次適用） | 800–1,000 | **Fig 6**（新規: 統合デモ結果）, **Table 3**（各段階の出力） |
| 7. Discussion | 位置づけ、限界、既存フレームワーク（GRADE, target trial emulation 等）との関係 | 700–900 | — |
| 8. Conclusion | まとめと今後 | 150–200 | — |
| Declarations / References | AJE 規定準拠 | — | — |

**合計本文目安**: 約 5,500–7,000 語（AJE の該当 Article type 上限確認後に調整＝P2）

---

## 3. 各セクション骨子（Section skeletons）

### Abstract（構造化 200–250語）
- **Background**: エビデンス統合（evidence synthesis）が崩れる3階層。
- **Methods**: ONISHI = LINKO(N) + IONE(IS) + KOTHA(HI) の統合パイプライン。共通データ基盤と手法間インターフェース。
- **Results**: 4組合せの新能力、統合デモ1ケースでの一気通貫解析結果。
- **Conclusions**: 階層横断的なエビデンス評価の実務的枠組み。

### 1. Introduction
- 段落1: エビデンス統合（evidence synthesis）が「低次元データの持ち寄り」で成立する前提への問い。対象を evidence synthesis と一度定義するに留め、「メタ解析は一部に過ぎない」等の防御的言い換えは繰り返さない。
- 段落2: 3つの独立した失敗モード ——
  - 研究間: 各研究のアウトカムが担う情報的重みが不均一（→ LINKO/ICR）。
  - 研究内: 集団に隠れたサブグループ構造（incoherence）（→ IONE/C1）。
  - 研究種別間: RCT と観察研究の乖離、情報量不足と「効果なし」の混同（→ KOTHA/Module K,T,H）。
- 段落3: 既存手法（I²/τ²、傾向スコア、GRADE、target trial emulation）は各階層を個別に扱うが、階層横断の統合枠組みがない。
- 段落4: 本論文の貢献（§1 コアメッセージの3点）と論文構成。

### 2. The ONISHI Framework (Overview)
- 3手法と対象階層の対応表を文章化（Table 1 と Fig 1 を引用）。
- 「共通データ基盤」の定義: 公表 RCT の Table 1、個票データ(IPD)、観察コホート、RCT/観察の効果推定値。
- 頭字語の定義（N=LINKO, IS=IONE, HI=KOTHA）。

### 3. Component Methods（各1段落・詳細は各論文へ）
- **LINKO**: ICR（ICR_v 分散ベース / ICR_pca 主成分ベース）、Prism Forest Plot、ICR 加重統合。1–2文で主要検証結果（スタチン=安定 / 血糖=異質、IST の PCA で r=0.90）。引用: LINKO 論文。
- **IONE**（Incoherence-Oriented Neutralisation and Extraction）: 2段階（C1 incoherence 指標で検出 → コヒーレント部分集団抽出）、W 指標（層内均質性）、探索的診断ツールとしての位置づけ。1–2文で検証（シミュレーション + semi-synthetic）。引用: IONE 論文。初出時に正式名を全記載。
- **KOTHA**: Module K（反実仮想パワー）/ T（階層ベイズ統合）/ H（OIS・TSA・GRADE 連携）。「evidence of no effect vs no evidence of effect」の区別。1–2文で検証（Mg in AMI, Statins in HF）。引用: KOTHA 論文。

### 4. Combinations & Synergies（4通り）
各組合せを「概要 / 新能力 / 具体シナリオ」の3点セットで（既存 combinations_report の内容を圧縮・統合論文向けに再編）。
- **4.1 LINKO + IONE — ICR誘導型部分集団解析**: 部分集団レベル ICR、異質性の根因特定（変数次元差 vs 集団 incoherence の切り分け）、C1–ICR 複合診断。シナリオ: 厳格血糖コントロール（UKPDS vs ACCORD）。
- **4.2 LINKO + KOTHA — 情報量を考慮したエビデンス統合**: ICR を Module K のパワー計算・Module T のベイズ事前重みに投入、Module H が ICR を OIS/TSA と併記。
- **4.3 IONE + KOTHA — 集団構造を反映した統合評価**: IONE の部分集団リスクプロファイルを Module K に、C1 を代表性評価に活用。
- **4.4 三手法統合（ONISHI）— 包括的エビデンス評価パイプライン**: incoherence 検出 → 情報定量化 → 統合調和の一気通貫。
- Fig 3（シナジー行列）と Fig 5（能力レーダー: 異質性診断/集団分解/情報定量化/エビデンス統合/ガイドライン有用性/外的妥当性の6軸）で相補性を可視化。

### 5. Integrated Pipeline（インターフェース仕様）
- Phase 1 IONE（集団分解・C1 算出）→ Phase 2 LINKO（部分集団別 ICR・Prism Forest Plot）→ Phase 3 KOTHA（K/T/H 統合）→ Output（意思決定支援）。
- **Table 2（インターフェース定義）**: 各接続について「上流の出力 → 下流の入力 → 変換」を明記。
  - IONE.C1 / 部分集団ラベル → KOTHA.Module K（部分集団リスクプロファイル）
  - IONE 部分集団 → LINKO（部分集団ごとの ICR 再算出）
  - LINKO.ICR → KOTHA.Module T（ベイズ事前重み）
  - LINKO.ICR / IONE.C1 → KOTHA.Module H（OIS/TSA と併記する報告項目）
- フィードバック経路（Fig 4 の破線矢印）を文章化。

### 6. Illustrative Application（統合デモ）— **方針B 確定**
- 単一の公開 IPD データ（第一候補 **IST: International Stroke Trial**, LINKO で使用実績あり）に **IONE→LINKO→KOTHA を実際に逐次適用**し、各段階の出力を Fig 6 / Table 3 として新規生成する。
- ストーリー: Phase1 IONE で C1・隠れ部分集団を検出 → Phase2 LINKO で部分集団別 ICR/ICRD を算出 → Phase3 KOTHA の Module K/T/H で統合し、GRADE 差分・意思決定含意まで。
- 実装: 本文執筆と並行して `generate_demo.py`（仮）を用意し、各段階の中間出力（C1・W、部分集団別 ICRD、Module T 統合効果）を再現可能な形で保存。数値は §5 台帳と矛盾しないよう単一ソース化。
- 代替データ: IST の IPD 利用に制約がある場合は他の公開 IPD（例: GUSTO, SPRINT 公開版）へ切替可能（要ライセンス確認）。

### 7. Discussion
- 統合の意義: 単独手法では「異質性がある」までしか言えないが、ONISHI は「なぜ・どの階層で・どう対処するか」を提供。
- 既存枠組みとの関係: GRADE（Module H が接続）、target trial emulation、IPD メタ解析。
- 限界: 各手法の限界の継承（IONE の探索的性格、ICR_pca の IPD 依存、KOTHA のベイズ事前設定感度）。データ要件が重い組合せ（IPD 必須）。
- 今後: ソフトウェア実装（統合パッケージ）、前向き検証。

### 8. Conclusion
- 3階層・3手法・1パイプラインの要約と実務への含意。

---

## 4. 図表計画（Figure / Table plan）

**既存流用可能（`ONISHI_figures_EN.pptx` / `generate_report.py` に生成コードあり）**

| 図表 | 内容 | 出典 | 統合論文での扱い |
|------|------|------|-----------------|
| Fig 1 | 3手法の概要と対象階層（概念図） | generate_report fig1_overview | 流用（編集可能シェイプ） |
| Fig 2 | 4通りの組合せとステップ | fig2_four_combinations | 流用 |
| Fig 3 | シナジー行列 | fig3_synergy_matrix | 流用 |
| Fig 4 | 統合パイプライン（フィードバック経路つき） | fig4_pipeline | 流用（インターフェース仕様と整合させ更新） |
| Fig 5 | 能力レーダーチャート（6軸×4組合せ） | fig5_radar | 流用（コード出力そのまま） |

**新規作成が必要**

| 図表 | 内容 | 必要作業 |
|------|------|---------|
| Fig 6 | 統合デモ結果（方針B: IST に IONE→LINKO→KOTHA 逐次適用した各段階の出力を1枚に） | **要新規生成**（`generate_demo.py`, IST IPD） |
| Table 1 | 3手法比較（対象階層/中核指標/入力データ/主要検証/引用先） | 新規（本仕様の内容から作表） |
| Table 2 | 手法間インターフェース定義（上流出力→下流入力→変換） | 新規（§5 の内容から作表） |
| Table 3 | 統合デモ各段階の数値出力（C1・W → 部分集団別 ICRD → Module T 統合効果・GRADE 差分） | **要新規生成**（方針B, IST） |

**図表ルール（Knowledge 準拠）**
- 本文 docx に各図表を初出パラグラフ直後にインライン配置し、かつ英語編集可能 pptx を別途提供。
- 引用は出現順・番号連番（Vancouver）。図表も出現順ナンバリング。孤児図表・幻の引用を作らない。
- EN 版は図表内テキストも全て英語、JA 版は全て日本語（言語一貫性ルール）。
- 図は **SVG または PNG** で提供（`.dot`/Graphviz 生ファイルは禁止。内部で使う場合も最終成果物は SVG/PNG に変換）。
- **投稿用の図提出形態**: AJE は図を原稿に埋め込まず**個別ファイル（PNG/TIFF/EPS 等）で別途提出**する方式のため、投稿版は Figure legends を本文末にまとめ、各図を個別ファイルで用意する。一方、社内レビュー・共有用には Knowledge 準拠でインライン配置 docx も別途生成（2形態を用意）。投稿規定の図表数上限は投稿直前に確認し統合・削減（P2）。

---

## 5. 数値ソース台帳（Single source of truth）

統合論文で引用する確定数値は下記リポの最終版から取得し、本文で再計算しない。

| 手法 | リポ / PR | 主要数値（引用候補） |
|------|-----------|--------------------|
| LINKO | `bougtoir/wip` PR #10 (`icr_paper/`)。プレプリント DOI: 10.21203/rs.3.rs-9338552/v1（under review） | スタチン ICRD=0.009 / I²=0%、血糖 ICRD=0.048 / I²=17%、IST PCA r=0.90 |
| IONE | `bougtoir/ione-stratification-framework` PR #1–#4。プレプリント DOI: 10.21203/rs.3.rs-9271445/v1（under review） | Method 1B ARI（comparator 比較値）、C1・W 指標、非線形ロバスト性（Table 8/9）、109,350 評価 |
| KOTHA | `bougtoir/wip` PR #9 (`kotha_*`)。プレプリント DOI: 10.21203/rs.3.rs-9420092/v1（under review） | Mg in AMI（12試験）event rate ratio、Statins in HF（0.53 等）、GRADE 差分 |

> 3論文は Research Square プレプリント DOI で引用し "under review" と明記（P3）。各値は投稿直前に各論文の最終確定版と再照合し、採択が進めば published 引用へ更新。

---

## 6. 執筆タスク分解（本仕様承認後の次工程）

1. Table 1・Table 2 を確定（本仕様の内容から作表）。
2. §P1–P5 の未決事項を確定（特に投稿先の語数上限・IONE 正式名・統合デモ方針A/B）。
3. Introduction → Overview → Combinations の本文ドラフト（既存 combinations_report を圧縮再利用）。
4. Integrated Pipeline + Illustrative Application（方針決定後）。
5. Discussion / Conclusion / Abstract。
6. 図表インライン配置 docx（EN/JA）+ 図表 pptx（EN）生成、引用・図表ナンバリング自動検証。
7. AJE 投稿規定チェックリスト照合、カバーレター（既存 `cover_letters_ONISHI_4papers.docx` の ONISHI 分を更新）。
