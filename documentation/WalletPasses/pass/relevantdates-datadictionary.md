# Pass.RelevantDates

**Framework**: Wallet Passes  
**Kind**: dictionary

An object that represents a date interval that the system uses to show a relevant pass.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- watchOS 11.0+

## Declaration

```swift
object Pass.RelevantDates
```

#### Discussion

> **Note**:  The values need to be a complete dates that include hours and minutes, and may optionally include seconds. For information about the ISO 8601 timestamp format, see [`Time and Date Formats`](https://developer.apple.comhttp://www.w3.org/TR/NOTE-datetime) on the W3C website.

## See Also

- [Showing a Pass on the Lock Screen](showing-a-pass-on-the-lock-screen.md)
  Add information to your pass so the system can display it on the Lock Screen at a relevant time and place.
- [object Pass.Locations](pass/locations-data.dictionary.md)
  An object that represents a location that the system uses to show a relevant pass.
- [object Pass.Beacons](pass/beacons-data.dictionary.md)
  An object that represents the identifier of a Bluetooth Low Energy beacon the system uses to show a relevant pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/pass/relevantdates-data.dictionary)*