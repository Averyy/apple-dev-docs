# Filter.Value

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The comparison operand supplied for the filter condition.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object Filter.Value
```

#### Discussion

For single-value operators (`EQUALS`, `NOT_EQUALS`, `GREATER_THAN`, and similar), pass either a bare string or a single-element array. For multi-value operators (`IN`, `BETWEEN`, `CONTAINS_ANY`, `CONTAINS_ALL`), pass an array. The server enforces the operator-specific cardinality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/filter/value-data.dictionary)*