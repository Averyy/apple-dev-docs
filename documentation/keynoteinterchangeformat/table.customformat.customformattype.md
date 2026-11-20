# Table.CustomFormat.CustomFormatType

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The kind of value the custom format applies to.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
string Table.CustomFormat.CustomFormatType
```

## Discussion

This value takes one of the following forms:

- `date_time`: Custom format for date and time values; only `format_string` applies.
- `number`: Custom format for numeric values; `number_format_data` and `conditions` may be set.
- `text`: Custom format for text values; only `format_string` applies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.customformat.customformattype)*