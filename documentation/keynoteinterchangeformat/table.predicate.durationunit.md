# Table.Predicate.DurationUnit

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The display unit for a duration predicate’s values.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
string Table.Predicate.DurationUnit
```

## Discussion

The duration value itself is stored as a number of seconds; this unit indicates how to interpret and render that value. For example, a value of 7200 with the unit `hour` means “2 hours.” It’s required for a predicate with duration values to be read back correctly.

This value takes one of the following forms:

- `day`: Days
- `hour`: Hours
- `millisecond`: Milliseconds
- `minute`: Minutes
- `second`: Seconds
- `week`: Weeks

## See Also

### Enumerations
- [type Table.Predicate.DateQualifier](./table.predicate.datequalifier.md)
  A time unit for relative date predicates, as in “in the last 5 years.”
- [type Table.Predicate.PredicateType](./table.predicate.predicatetype.md)
  The type of conditional test to perform.
- [type Table.Predicate.Qualifier](./table.predicate.qualifier.md)
  A qualifier for text-matching predicates.
- [type Table.Predicate.Value](./table.predicate.value.md)
  A typed comparison value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.predicate.durationunit)*