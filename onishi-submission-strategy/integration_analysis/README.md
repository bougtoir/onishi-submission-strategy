# ONISHI 統合デモ解析（方針B: 単一公開IPD = IST）

3手法（LINKO / IONE / KOTHA）の4通りの統合パターンを、共通データ
**International Stroke Trial (IST, 公開IPD)** に実際に適用したデモ解析。
仕様書 §4 の Fig6 / Table3 の根拠となる。

## データ
- **出典**: International Stroke Trial database (Sandercock et al. 2011,
  *Trials* 12:101; https://datashare.ed.ac.uk/handle/10283/124, open access)
- **N** = 18,451（欠測除外後）、**変数** = 25、**14日死亡率** = 22.5%
- **介入** = aspirin 割付 (`RXASP`)、**アウトカム** = 14日死亡 (`DIED`)
- **全体効果**: aspirin OR = **0.939** (logOR −0.063, se 0.035)

## 3階層と役割
| 手法 | 階層 | このデモでの役割 |
|---|---|---|
| IONE | 研究内（研究内集団） | 予測確率（decision power）で4層に潜在層別化 → 効果の非整合性 C1・層内均質性 W |
| LINKO | 研究間（情報的重み） | エンドポイントの情報寄与率 ICR_pca（層別・国別）|
| KOTHA | 研究種別間（統合） | 反実仮想パワー（Module K）・ベイズ調和（Module T）・OIS/TSA（Module H）|

## 4パターンと主な所見

### Pattern 1: LINKO + IONE（部分集団ごとの情報診断）
- IONE が予測リスクで4層（ER 4.4%→50.9%）に層別化。層間の **aspirin 効果は整合的**
  （**C1(effect)=1.00**, I²=0%）＝効果修飾なし。
- LINKO の ICR_pca（**regression ベース**。Pattern 4 と定義統一）は高リスク層ほど大きく
  （s0<s1<s2<s3）、エンドポイントの情報寄与が集団リスク構造に依存することを示す。
  ※以前 loading ベースを併用し層順位が逆転していた不整合を解消。
- **含意**: 「効果は均質だが、エンドポイントの情報寄与は集団構造に強く依存」を分離提示。
- 図: `figures/pattern1_linko_ione.png`

### Pattern 2: LINKO + KOTHA（ICR 重み付き統合）
- IST 13か国を sub-study として国別 aspirin 効果を統合（I²=37%）。
- LINKO の国別 ICR を情報的重みに用いた **ICR-weighted 統合**（KOTHA）。
- **点推定は IV-RE と同じ OR≈0.93 で不変＝頑健**。これが主たる所見。
- SE は IV-RE 0.056 → ICR-weighted 0.037 だが、この縮小は**ICR 重み付けの効果ではない**：
  重みを全て等値にした equal-weight でも SE=0.037、fixed-effect でも 0.037 で、
  差はランダム効果の τ²（層間異質 I²=37%）を落としたことに起因する。
  → 主張は「ICR 重みでも点推定は動かない（頑健）」に留め、「情報重みで精度向上」とは書かない。
- 図: `figures/pattern2_linko_kotha.png`（IV-RE / ICR-weighted / equal-weight の3線を SE 付きで併記）

### Pattern 3: IONE + KOTHA（リスク層 → 反実仮想パワー）
- IONE のリスク層プロファイル（ER）を KOTHA Module K の反実仮想パワーに投入。
- 同一 N・同一効果でも **低リスク層は著しく低パワー**（s0 ER4.4%→14%, s3 ER50.9%→86%）。
- Module H: OIS=7,880 events に対し観測 4,159 events（**情報充足率 53%**）、
  リスク比 11.5＝**深刻な indirectness**。
- **必要追加症例数**: 決着（OIS 到達）には **+3,721 events**＝全体死亡率換算で
  **追加 約16,500例**（総計 ≈35,000例, 現状の約1.9倍）。IONE 層別により
  組み入れ効率も提示（低リスク s0 のみだと +約83,700例／高リスク s3 中心なら +約7,300例）。
- **含意**: 「効果なし」ではなく「情報不足」を集団リスク構造から定量化し、
  次試験に必要な人数まで出力。
- 図: `figures/pattern3_ione_kotha.png`

### Pattern 4: ONISHI（3手法逐次: IONE → LINKO → KOTHA）
- IONE（層別化・C1=1.00・W=0.18）→ LINKO（ICR で s2,s3 を anchor、s0,s1 を discount）
  → KOTHA（ICR 誘導 power-prior 統合＋Module H TSA）。
- 調和推定 **OR≈0.93–0.95**、p(benefit) は naive 0.96 → ICR-weighted 0.85 に補正。
- **TSA 累積 Z=−1.73**（±1.96 未達）＋情報充足率 53% ＝
  **「効果を示すには情報不足（interim 相当）。決着には追加 約16,500例が必要」**
  という GRADE 整合的・意思決定レベルの結論。
- 図: `figures/pattern4_onishi_full.png`（4パネル一気通貫ダッシュボード）

## 統合所見（ONISHI の付加価値）
単独手法では「aspirin 効果は概ね中立（OR 0.94, CI が 1 をまたぐ）」で止まる。
ONISHI は 3階層を分離診断し、**(i) 効果修飾は無い（IONE: C1=1）**、
**(ii) しかし情報寄与と検出力は集団リスク構造に強く依存する（LINKO×KOTHA）**、
**(iii) 現エビデンスは情報的に不足（TSA/OIS: info fraction 53%, 決着には追加約16,500例）** という
**多層的な妥当性診断**を一気通貫で与える。とりわけ、CI が 1 をまたぐ"空振り"で終わった
中立的 RCT を捨てずに、**「効果なし」ではなく「情報不足」と判定し、決着に必要な追加症例数
（次試験の設計値）まで出力する**点が、ペア組合せにはない ONISHI の意思決定レベルの付加価値。

## 再現方法
```bash
cd onishi-submission-strategy/integration_analysis
python3 run_integration.py   # 約17秒。figures/ と results.json を再生成
```
- `linko_icr.py` / `linko_pca.py` … LINKO（ICR、PCA-ICR、IST loader）
- `ione_core.py` … IONE（層別化・C1/W・層別効果）
- `kotha_core.py` … KOTHA（Module K/T/H の中核関数）
- 各関数は3手法リポジトリ（icr-paper / ione-stratification-framework /
  rct-decomposition）から**逐語コピー**（vendoring）し、自己完結・再現可能にした。

## 注記
- 図は投稿規定に合わせ後工程で個別 PNG/TIFF 化・凡例英語化する（AJE は図を本文非埋込）。
- `.dot` は不使用。すべて PNG。
