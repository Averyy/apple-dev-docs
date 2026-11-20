# Table.Cell.UnformattedValue

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The unformatted value of a cell, which can be one of several data types.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
(Table.Cell.UnformattedValue.boolean | Table.Cell.UnformattedValue.date | Table.Cell.UnformattedValue.number | Table.Cell.UnformattedValue.rich_text | Table.Cell.UnformattedValue.text) Table.Cell.UnformattedValue
```



**Allowed Types**: `Table.Cell.UnformattedValue.boolean`, `Table.Cell.UnformattedValue.date`, `Table.Cell.UnformattedValue.number`, `Table.Cell.UnformattedValue.rich_text`, `Table.Cell.UnformattedValue.text`

## Discussion

This value takes one of the following forms:

- `boolean`: A Boolean value of true or false.
- `date`: A date value, a time value, or both.
- `number`: A numeric value that’s an integer or decimal. The cell’s `value` property carries the formatted string. A duration cell’s number is a count of seconds, so check `cell_format` before using it in arithmetic.
- `rich_text`: Rich text with styling, such as paragraph and character styles.
- `text`: A plain text value with no styling. For styled text, use `rich_text` instead.

## Topics

### Dictionaries
- [object Table.Cell.UnformattedValue.boolean](./table.cell.unformattedvalue/boolean.md)
  A Boolean value of true or false.
- [object Table.Cell.UnformattedValue.date](./table.cell.unformattedvalue/date.md)
  A date value, a time value, or both.
- [object Table.Cell.UnformattedValue.number](./table.cell.unformattedvalue/number.md)
  A numeric value that’s an integer or decimal.
- [object Table.Cell.UnformattedValue.rich_text](./table.cell.unformattedvalue/rich_text.md)
  Rich text with styling, such as paragraph and character styles.
- [object Table.Cell.UnformattedValue.text](./table.cell.unformattedvalue/text.md)
  A plain text value with no styling.

## See Also

### Enumerations
- [type Table.Cell.Formula](./table.cell.formula.md)
  The form in which a cell’s formula is carried.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.cell.unformattedvalue)*