# formatNumber

**Framework**: TVMLKit JS  
**Kind**: func

Formats the specified number into the given format.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
String formatNumber(
    in int number, 
    in String styleValue, 
    in String positiveNumberFormat, 
    in String negativeNumberFormat
);
```

#### Return_value

A string containing the formatted number.

#### Discussion

This function changes an integer into a string, based on the formatting styles specified. For example, `formatNumber(-60, “”, “+”, “-”)` returns “-60”.

## Parameters

- `number`: An integer that is the number to be formatted.
- `styleValue`: A string that designates the style the number is formatted in to. Valid values are  ,  ,  ,  ,  ,  . If no value is given for this parameter, it defaults to  .
- `positiveNumberFormat`: The formatting used for a positive number value input.
- `negativeNumberFormat`: The formatting used for a negative number value input.

## See Also

- [formatDate](1627445-formatdate.md)
  Formats the given date into the given format.
- [formatDuration](1627346-formatduration.md)
  Formats the given duration into the standard tvOS format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/1627348-formatnumber)*