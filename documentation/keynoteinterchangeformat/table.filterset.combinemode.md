# Table.FilterSet.CombineMode

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The rule for combining the per-column filters in a filter set to decide whether a row passes.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
string Table.FilterSet.CombineMode
```

## Discussion

This value takes one of the following forms:

- `and`: Logical AND: a row passes only if it passes every column’s filter.
- `or`: Logical OR: a row passes if it passes any column’s filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.filterset.combinemode)*