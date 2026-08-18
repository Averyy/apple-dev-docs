# QueryFilter.Value

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The comparison value or values for a `QueryFilter` condition.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object QueryFilter.Value
```

#### Discussion

`QueryFilter.value` accepts a scalar, an array, or no value at all, depending on the `operator`. Pass an array for operators that accept multiple values (`IN`, `NOT_IN`, `CONTAINS_ANY`, `CONTAINS_ALL`, `NOT_CONTAINS_ANY`, `NOT_CONTAINS_ALL`, `BETWEEN`), a scalar for operators that accept a single value (`EQUALS`, `STARTS_WITH`), or omit it entirely for the null-check operators `IS_NULL` and `IS_NOT_NULL`. See [`QueryFilterOperator`](queryfilteroperator.md) for the full operator reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/queryfilter/value-data.dictionary)*