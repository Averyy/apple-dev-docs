# Table.CellFormat.DurationFormat.Style

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The length of the unit labels in a displayed duration.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
string Table.CellFormat.DurationFormat.Style
```

## Discussion

This value takes one of the following forms:

- `compact`: Single-letter labels with no space (for example, “1h 30m”). Shown in Keynote as None, since the option suppresses unit labels entirely.
- `long`: Full-word labels (for example, “1 hour 30 minutes”).
- `short`: Abbreviated labels (for example, “1 hr 30 min”).

## See Also

### Enumerations
- [type Table.CellFormat.DurationFormat.Unit](./table.cellformat.durationformat.unit.md)
  A duration unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.cellformat.durationformat.style)*