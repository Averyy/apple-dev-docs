# Table.Row.VisibilityState

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

Whether a row is visible, and if not, whether it was hidden explicitly or excluded by the active filter.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
string Table.Row.VisibilityState
```

## Discussion

This value takes one of the following forms:

- `filtered`: The row didn’t pass the active filter rules in `transformation.filter_set`. Disabling the filter or removing the failing rule makes the row visible again.
- `user_hidden`: The user hid the row with the Hide Row command.
- `visible`: The row is shown.

## See Also

### Enumerations
- [object Table.Row.Kind](./table.row.kind.md)
  The structural role of a row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.row.visibilitystate)*