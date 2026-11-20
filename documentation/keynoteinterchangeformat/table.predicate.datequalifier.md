# Table.Predicate.DateQualifier

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

A time unit for relative date predicates, as in “in the last 5 years.”

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
string Table.Predicate.DateQualifier
```

## Discussion

It’s used by predicates that take a unit count as their value, such as `date_is_in_the_last`, `date_is_in_the_next`, `date_before_relative`, `date_after_relative`, `date_between_relative`, and `date_in_this`.

This value takes one of the following forms:

- `ago`: The unit count is in the past, for use with the `date_before_relative` and `date_after_relative` predicates.
- `days`: Days
- `from_now`: The unit count is in the future, for use with the `date_before_relative` and `date_after_relative` predicates.
- `months`: Months
- `quarters`: Quarters
- `weeks`: Weeks
- `years`: Years

## See Also

### Enumerations
- [type Table.Predicate.DurationUnit](./table.predicate.durationunit.md)
  The display unit for a duration predicate’s values.
- [type Table.Predicate.PredicateType](./table.predicate.predicatetype.md)
  The type of conditional test to perform.
- [type Table.Predicate.Qualifier](./table.predicate.qualifier.md)
  A qualifier for text-matching predicates.
- [type Table.Predicate.Value](./table.predicate.value.md)
  A typed comparison value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.predicate.datequalifier)*