# Table.Predicate

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A condition that’s evaluated against a single cell’s value.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.Predicate
```

## Overview

Some predicates evaluate the cell relative to its column instead. Predicates are used by conditional highlighting rules and, in future versions, by table filter rules.

## Topics

### Objects
- [object Table.Predicate.Reference](./table.predicate.reference.md)
  A reference to a single cell, used as a predicate’s comparison operand.
### Enumerations
- [type Table.Predicate.DateQualifier](./table.predicate.datequalifier.md)
  A time unit for relative date predicates, as in “in the last 5 years.”
- [type Table.Predicate.DurationUnit](./table.predicate.durationunit.md)
  The display unit for a duration predicate’s values.
- [type Table.Predicate.PredicateType](./table.predicate.predicatetype.md)
  The type of conditional test to perform.
- [type Table.Predicate.Qualifier](./table.predicate.qualifier.md)
  A qualifier for text-matching predicates.
- [type Table.Predicate.Value](./table.predicate.value.md)
  A typed comparison value.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.predicate`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `predicate_type` (Table.Predicate.PredicateType) *(required)*: The kind of comparison or test to perform. It determines which of `value1`, `value2`, `value_list`, `qualifier`, `date_qualifier1`, `date_qualifier2`, `duration_unit1`, and `duration_unit2` are required.
- `value1` (Table.Predicate.Value): The value the predicate compares the cell against. Predicates that take no operand, such as `is_blank` or `date_is_today`, ignore it, and the top and bottom predicates use it as the threshold count N. Its `Value` case must match the data type `predicate_type` operates on. For example, `text_contains` expects text.
- `value2` (Table.Predicate.Value): The second comparison value. It’s required only for range predicates (`value_between`, `value_not_between`, `date_is_between`, `duration_is_between`, `date_between_relative`, `duration_is_not_between`). It must use the same `Value` case as `value1`.
- `qualifier` (Table.Predicate.Qualifier): The case sensitivity of a text predicate (`text_contains`, `text_begins_with`, `text_ends_with`, `text_is`, `text_is_not`, `text_does_not_contain`, `text_not_starts_with`, `text_not_ends_with`). If it’s omitted, it defaults to `case_insensitive`.
- `date_qualifier1` (Table.Predicate.DateQualifier): The time unit for the first value of relative date predicates (`date_is_in_the_last`, `date_is_in_the_next`, `date_before_relative`, `date_after_relative`, `date_between_relative`, `date_in_this`). For example, a `value1` of 5 with a `date_qualifier1` of `years` means “5 years.” It’s required for these predicates.
- `date_qualifier2` (Table.Predicate.DateQualifier): The time unit for the second value of relative-date range predicates (`date_between_relative`). It’s required only when both ends of the range need separate units.
- `duration_unit1` (Table.Predicate.DurationUnit): The display unit for the first value of duration predicates. The duration value itself is stored as a number of seconds, and this unit determines how to interpret it; for example, 3600 seconds with a `duration_unit1` of `hour` means “1 hour.” It’s required for duration predicates.
- `duration_unit2` (Table.Predicate.DurationUnit): The display unit for the second value of duration range predicates (`duration_is_between`, `duration_is_not_between`). It’s required when those predicates are used.
- `value_list` ([Table.Predicate.Value]): The ordered list of typed values that the `in_list` and `not_in_list` predicates compare the cell against. All entries must use the same `Value` case. If it’s present, `value1` and `value2` are ignored.

## See Also

### Objects
- [object Table.CategoryRules](./table.categoryrules.md)
  An empty object for a categorized table’s rules, which version 1.0 doesn’t support.
- [object Table.Cell](./table.cell.md)
  A cell in a table.
- [object Table.CellFormat](./table.cellformat.md)
  The display format of a cell’s value.
- [object Table.CellProperties](./table.cellproperties.md)
  The styling of a table cell, other than its strokes.
- [object Table.ColumnHeader](./table.columnheader.md)
  The metadata for a column in a table.
- [object Table.ConditionalStyleSet](./table.conditionalstyleset.md)
  A shared set of conditional highlighting rules that multiple cells can reference.
- [object Table.CustomFormat](./table.customformat.md)
  A user-defined format for a cell.
- [object Table.Date](./table.date.md)
  An absolute point in time.
- [object Table.FilterSet](./table.filterset.md)
  The complete filter configuration for a table.
- [object Table.PivotRules](./table.pivotrules.md)
  A placeholder for a pivot table’s rules, which version 1.0 doesn’t support.
- [object Table.Row](./table.row.md)
  A row in a table.
- [object Table.Sort](./table.sort.md)
  The sort rules that the reader applies to the rows of a table’s content.
- [object Table.VisualProperties](./table.visualproperties.md)
  The default styling of a table, broken down by region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.predicate)*