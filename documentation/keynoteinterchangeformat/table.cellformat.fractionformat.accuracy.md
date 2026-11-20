# Table.CellFormat.FractionFormat.Accuracy

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The granularity of a fraction display.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
string Table.CellFormat.FractionFormat.Accuracy
```

## Discussion

It’s either a maximum digit count for the numerator and denominator, or a fixed denominator such as halves or quarters.

This value takes one of the following forms:

- `conflicting`: A value that marks a range of cells with mixed fraction accuracies. It’s not a value to set on a single cell.
- `eighths`: Fixed denominator of 8.
- `halves`: Fixed denominator of 2 (for example, 0/2, 1/2).
- `hundredths`: Fixed denominator of 100.
- `quarters`: Fixed denominator of 4 (for example, 1/4, 3/4).
- `sixteenths`: Fixed denominator of 16.
- `tenths`: Fixed denominator of 10.
- `up_to_one_digit`: At most one digit in the numerator and denominator (for example, 1/2, 3/4).
- `up_to_three_digits`: At most three digits in the numerator and denominator.
- `up_to_two_digits`: At most two digits in the numerator and denominator (for example, 5/16, 22/87).


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.cellformat.fractionformat.accuracy)*