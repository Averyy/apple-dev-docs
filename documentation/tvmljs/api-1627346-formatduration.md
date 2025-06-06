# formatDuration

**Framework**: TVMLKit JS  
**Kind**: func

Formats the given duration into the standard tvOS format.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
String formatDuration(
    in int duration
);
```

#### Return_value

A string containing the formatted duration.

#### Discussion

This function changes a number of seconds into the standard hour:minute:second format. For example, `formatDuration(90)` returns “1:30”.

## Parameters

- `duration`: An integer specifying the duration, in seconds.

## See Also

- [formatDate](1627445-formatdate.md)
  Formats the given date into the given format.
- [formatNumber](1627348-formatnumber.md)
  Formats the specified number into the given format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/1627346-formatduration)*