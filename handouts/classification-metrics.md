<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<style>
@import url('https://fonts.googleapis.com/css?family=EB+Garamond&display=swap');
body { padding: 0; }
section#classification-metrics {
    padding: 12pt 36pt;
    font-family: 'EB Garamond', serif;
    align-items: middle;
    display: flex; flex-wrap: wrap; box-sizing: border-box; }
h1, h2 { font-family: 'Gill Sans', sans-serif; font-weight: normal; }
h1 { text-align: center; }
h1, #confusion-matrix, #sklearn-confusion-matrix { width: 100%; }
#accuracy { width: 100%; }
#recall, #precision { width: 49.5%; }
table { width: 100%; border-collapse: collapse; }
td, th { padding: 1em 1em; text-align: left; }
.underline { text-decoration: underline; }
tr:nth-child(2) td:nth-child(2) { border-top: 1px solid black; border-right: 1px solid black; }
tr:nth-child(1) td:nth-child(3) { border-bottom: 1px solid black; border-left: 1px solid black; }
em { text-decoration: underline; font-style: normal; }
#sklearn-confusion-matrix td, th { padding: 0; text-align: center; }
#sklearn-confusion-matrix table { width: 50%; }
#f1-score p { margin: 0; }
</style>
# Classification Metrics

Classifcation metrics are derived from a *confusion matrix*.

|                        | Actual Positive    | Actual Negative    |                     |
| -------------------    | ------------------ | ------------------ | ------------------- |
| **Predicted Positive** | TP                 | FP (Type I Err)    | *Precision*         |
| **Predicted Negative** | FN (Type II Err)   | TN                 |                     |
|                        | *Recall*           |                    |                     |

## Accuracy

(TP + TN) / (FP + FN + TP + TN)

- total # correct / total

## Recall

TP / (TP + FN)

- % of actually positive cases that were predicted as positive
- optimize for this when missing actual positive cases is expensive
- Optimizing for recall avoids false negatives
- "doesn't care" about false positives
- Use this when false negatives are more costly than false positives
- e.g. we might want to be on the safe side when predicting the presence of
  cancer

## Precision

TP / (TP + FP)

- % of of positive predictions that are correct
- Optimize for this when we want to be really sure, i.e. when false
  positives are expensive
- Optimizing for precision avoids false positives
- Use this when false positives are more costly than false negatives
- "doesn't care" about "missing out", predicting negative when it's actually
  positive i.e. false negatives
- e.g. Google's interview / hiring process

## `sklearn` confusion matrix

|              | Pred - | Pred + |
| ---          | ------ | ------ |
| **Actual -** | TN     | FP     |
| **Actual +** | FN     | TP     |
