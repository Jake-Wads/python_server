---
title: Cross Validation
---
<style>
table { width: 100%; }
th { border: 1px solid black; padding: .5em 0; }
em { text-decoration: underline; }
dt { font-weight: bold; }
</style>

K-fold Cross Validation

:   Split the data into $k$ sections. The model is fit on $k - 1$ sections, and
    tested on the remaining one. This process repeats $k$ times.

Leave-one-out Cross Validation

:   K-fold cross validation where $k = n - 1$

---

## Train-Test Split

- Test data is reserved for an estimate of *out of sample* performance.

```python
train, test = train_test_split(df)
```

<table>
    <tr>
        <th>Train</th>
        <th width='20%'>Test</th>
    </tr>
</table>

## Train-Test-Validate

```python
train, test = train_test_split(df)
train, validate = train_test_split(train)
```

- Validate split is used for *model selection*.

<table>
    <tr>
        <th>Train</th>
        <th width='26.333%'>Validate</th>
        <th width='20%'>Test</th>
    </tr>
</table>

## K-fold Cross Validation ($k = 3$)

- Each of the k folds is treated as the validate split in turn.
- Model performance is averaged over the splits.

<table>
    <tr>
        <th>1</th>
        <th>2</th>
        <th>3</th>
        <th width='20%'>Test</th>
    </tr>
</table>
