# Table.Predicate.PredicateType

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The type of conditional test to perform.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
string Table.Predicate.PredicateType
```

## Discussion

This value takes one of the following forms:

- `date_after_relative`: Cell date is after a relative offset of `value1` time units (the unit is given by `date_qualifier1`).
- `date_before_relative`: Cell date is before a relative offset of `value1` time units (the unit is given by `date_qualifier1`).
- `date_between_relative`: Cell date is between two relative offsets of `value1` and `value2` time units.
- `date_in_this`: Cell date is in the day, week, month, or year (the unit is given by `date_qualifier1`).
- `date_is_after`: Cell date is after `value1`.
- `date_is_before`: Cell date is before `value1`.
- `date_is_between`: Cell date is between `value1` and `value2`.
- `date_is_exactly`: Cell date is exactly `value1`.
- `date_is_in_the_last`: Cell date is within the last `value1` units (the unit is given by `date_qualifier1`).
- `date_is_in_the_next`: Cell date is within the next `value1` units (the unit is given by `date_qualifier1`).
- `date_is_the_date`: Cell date is on the same calendar day as `value1`. It’s distinct from `date_is_exactly`.
- `date_is_today`: Cell date is today.
- `date_is_tomorrow`: Cell date is tomorrow.
- `date_is_yesterday`: Cell date is yesterday.
- `distincts`: Cell is one of the distinct values in the column.
- `duplicates`: Cell value is duplicated elsewhere in the column.
- `duration_above_average`: Cell duration is above the average.
- `duration_below_average`: Cell duration is below the average.
- `duration_bottom`: Cell duration is in the bottom N values (or bottom N percent) of its column. The threshold N is given by `value1`.
- `duration_is_between`: Cell duration is between `value1` and `value2`.
- `duration_is_equal`: Cell duration equals `value1`.
- `duration_is_greater_than`: Cell duration is greater than `value1`.
- `duration_is_greater_than_or_equal`: Cell duration is greater than or equal to `value1`.
- `duration_is_less_than`: Cell duration is less than `value1`.
- `duration_is_less_than_or_equal`: Cell duration is less than or equal to `value1`.
- `duration_is_not_between`: Cell duration isn’t between `value1` and `value2`.
- `duration_is_not_equal`: Cell duration doesn’t equal `value1`.
- `duration_top`: Cell duration is in the top N values (or top N percent) of its column. The threshold N is given by `value1`.
- `formula`: Cell matches an arbitrary formula-based predicate. The formula text is given by `value1`, in the consuming application’s formula syntax.
- `in_list`: Cell value matches any value in `value_list`.
- `is_blank`: Cell is blank.
- `is_checked`: Cell checkbox is checked.
- `is_false`: Cell value is FALSE.
- `is_negative`: Cell numeric value is negative (< 0).
- `is_not_blank`: Cell isn’t blank.
- `is_not_checked`: Cell checkbox isn’t checked.
- `is_positive`: Cell numeric value is zero or positive (>= 0).
- `is_true`: Cell value is TRUE.
- `not_in_list`: Cell value matches none of the values in `value_list`.
- `pivot_source_filtered_for_column`: The column is filtered by a pivot table’s source predicates. It’s reserved for pivot tables, which version 1.0 doesn’t support.
- `pivot_source_filtered_for_row`: The row is filtered by a pivot table’s source predicates. It’s reserved for pivot tables, which version 1.0 doesn’t support.
- `text_begins_with`: Cell text begins with `value1`.
- `text_contains`: Cell text contains `value1`.
- `text_does_not_contain`: Cell text doesn’t contain `value1`.
- `text_ends_with`: Cell text ends with `value1`.
- `text_is`: Cell text is exactly `value1`.
- `text_is_not`: Cell text isn’t `value1`.
- `text_not_ends_with`: Cell text doesn’t end with `value1`.
- `text_not_starts_with`: Cell text doesn’t begin with `value1`.
- `uniques`: Cell value is unique in the column.
- `value_above_average`: Cell value is above the column or row average.
- `value_below_average`: Cell value is below the column or row average.
- `value_between`: Cell value is between `value1` and `value2` (inclusive).
- `value_bottom`: Cell value is in the bottom N values (or bottom N percent) of its column. The threshold N is given by `value1`.
- `value_equal`: Cell value equals `value1`.
- `value_greater_than`: Cell value is greater than `value1`.
- `value_greater_than_or_equal`: Cell value is greater than or equal to `value1`.
- `value_less_than`: Cell value is less than `value1`.
- `value_less_than_or_equal`: Cell value is less than or equal to `value1`.
- `value_not_between`: Cell value isn’t between `value1` and `value2`.
- `value_not_equal`: Cell value doesn’t equal `value1`.
- `value_top`: Cell value is in the top N values (or top N percent) of its column. The threshold N is given by `value1`.

## See Also

### Enumerations
- [type Table.Predicate.DateQualifier](./table.predicate.datequalifier.md)
  A time unit for relative date predicates, as in “in the last 5 years.”
- [type Table.Predicate.DurationUnit](./table.predicate.durationunit.md)
  The display unit for a duration predicate’s values.
- [type Table.Predicate.Qualifier](./table.predicate.qualifier.md)
  A qualifier for text-matching predicates.
- [type Table.Predicate.Value](./table.predicate.value.md)
  A typed comparison value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.predicate.predicatetype)*