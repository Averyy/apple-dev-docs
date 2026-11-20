# Table.Predicate.Value

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

A typed comparison value.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
(Table.Predicate.Value.date | Table.Predicate.Value.duration | Table.Predicate.Value.number | Table.Predicate.Value.reference | Table.Predicate.Value.text) Table.Predicate.Value
```



**Allowed Types**: `Table.Predicate.Value.date`, `Table.Predicate.Value.duration`, `Table.Predicate.Value.number`, `Table.Predicate.Value.reference`, `Table.Predicate.Value.text`

## Discussion

This value is carried in `Table.Predicate.value1` or `Table.Predicate.value2`.

Its case must match the data type the predicate operates on.

This value takes one of the following forms:

- `date`: Absolute date value, used by absolute date predicates. Examples of these values are `date_is_before`, `date_is_after`, `date_is_between`, `date_is_exactly`, and `date_is_the_date`.
- `duration`: Duration value in seconds, used by duration predicates. The accompanying `Table.Predicate.duration_unit1` (or `duration_unit2`) determines how to interpret the value.
- `number`: Numeric value, used by value-comparison predicates, for example, `value_equal`, `value_greater_than`, and `value_between`, and by relative date predicates that take a unit count, for example, `date_is_in_the_last`.
- `reference`: The comparison operand is another cell rather than a literal value (for example, “date is before [B2]”). A reader compares the referenced cell’s value at evaluation time. A version 1.0 reader doesn’t support a cell operand: a rule that compares against a `reference` in `value1` or `value2` is dropped and a warning is reported, and a `reference` entry in `value_list` is skipped.
- `text`: Text value, used by text-matching predicates (such as `text_contains`, `text_begins_with`, `text_ends_with`, and `text_is`).

## Topics

### Dictionaries
- [object Table.Predicate.Value.date](./table.predicate.value/date.md)
  Absolute date value, used by absolute date predicates.
- [object Table.Predicate.Value.duration](./table.predicate.value/duration.md)
  Duration value in seconds, used by duration predicates. The accompanying `Table.Predicate.duration_unit1` (or `duration_unit2`) determines how to interpret the value.
- [object Table.Predicate.Value.number](./table.predicate.value/number.md)
  Numeric value, used by value-comparison predicates, for example, `value_equal`, `value_greater_than`, and `value_between`, and by relative date predicates that take a unit count, for example, `date_is_in_the_last`.
- [object Table.Predicate.Value.reference](./table.predicate.value/reference.md)
  The comparison operand is another cell rather than a literal value (for example, “date is before [B2]”). A reader compares the referenced cell’s value at evaluation time. A version 1.0 reader doesn’t support a cell operand: a rule that compares against a `reference` in `value1` or `value2` is dropped and a warning is reported, and a `reference` entry in `value_list` is skipped.
- [object Table.Predicate.Value.text](./table.predicate.value/text.md)
  Text value, used by text-matching predicates (such as `text_contains`, `text_begins_with`, `text_ends_with`, and `text_is`).

## See Also

### Enumerations
- [type Table.Predicate.DateQualifier](./table.predicate.datequalifier.md)
  A time unit for relative date predicates, as in “in the last 5 years.”
- [type Table.Predicate.DurationUnit](./table.predicate.durationunit.md)
  The display unit for a duration predicate’s values.
- [type Table.Predicate.PredicateType](./table.predicate.predicatetype.md)
  The type of conditional test to perform.
- [type Table.Predicate.Qualifier](./table.predicate.qualifier.md)
  A qualifier for text-matching predicates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.predicate.value)*