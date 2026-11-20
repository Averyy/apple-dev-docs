# ColumnMetrics

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The arrangement of a text area into columns, and the width of the gutters between them.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
(ColumnMetrics.equal | ColumnMetrics.unequal | string("single")) ColumnMetrics
```



**Allowed Types**: `ColumnMetrics.equal`, `ColumnMetrics.unequal`, `string("single")`

## Discussion

This value takes one of the following forms:

- `equal`: All the columns are the same width, and so are all the gutters.
- `single`: A single column.
- `unequal`: Each of the column and gutter widths is specified.

## Topics

### Objects
- [object ColumnMetrics.EqualColumnsDescription](./columnmetrics.equalcolumnsdescription.md)
  An arrangement of a text area into columns of equal width.
- [object ColumnMetrics.UnequalColumnsDescription](./columnmetrics.unequalcolumnsdescription.md)
  An arrangement of a text area into columns of specified widths.
### Dictionaries
- [object ColumnMetrics.equal](./columnmetrics/equal.md)
  All the columns are the same width, and so are all the gutters.
- [object ColumnMetrics.unequal](./columnmetrics/unequal.md)
  Each of the column and gutter widths is specified.

## See Also

### Tables
- [object Table](./table.md)
  A table of cells, nested two levels deep.
- [object Table.TransformationInfo](./table.transformationinfo.md)
  Information about how the reader derives a table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/columnmetrics)*