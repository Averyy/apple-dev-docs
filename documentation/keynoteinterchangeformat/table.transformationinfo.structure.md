# Table.TransformationInfo.Structure

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The structural transformation of a table.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
(Table.TransformationInfo.Structure.categorized | Table.TransformationInfo.Structure.pivot) Table.TransformationInfo.Structure
```



**Allowed Types**: `Table.TransformationInfo.Structure.categorized`, `Table.TransformationInfo.Structure.pivot`

## Discussion

It’s reserved for categorized and pivot tables, which version 1.0 doesn’t support. `filter_set` and `sort` are separate settings, and apply to a plain table without it.

This value takes one of the following forms:

- `categorized`: A categorized table, which version 1.0 doesn’t support. `CategoryRules` is reserved to describe how its rows are grouped.
- `pivot`: A pivot table, which version 1.0 doesn’t support. `PivotRules` is reserved to describe its row, column, and value axes.

## Topics

### Dictionaries
- [object Table.TransformationInfo.Structure.categorized](./table.transformationinfo.structure/categorized.md)
  A categorized table, which version 1.0 doesn’t support.
- [object Table.TransformationInfo.Structure.pivot](./table.transformationinfo.structure/pivot.md)
  A pivot table, which version 1.0 doesn’t support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.transformationinfo.structure)*