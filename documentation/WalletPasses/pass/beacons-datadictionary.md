# Pass.Beacons

**Framework**: Wallet Passes  
**Kind**: dictionary

An object that represents the identifier of a Bluetooth Low Energy beacon the system uses to show a relevant pass.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- watchOS 1.0+

## Declaration

```swift
object Pass.Beacons
```

## Properties

- `major` (16-bit unsigned integer): The major identifier of a Bluetooth Low Energy location beacon.
- `minor` (16-bit unsigned integer): The minor identifier of a Bluetooth Low Energy location beacon.
- `proximityUUID` (string) *(required)*: The unique identifier of a Bluetooth Low Energy location beacon.
- `relevantText` (string): The text to display on the lock screen when the pass is relevant. For example, a description of a nearby location, such as `“Store nearby on 1st and Main”`.

## See Also

- [Showing a Pass on the Lock Screen](showing-a-pass-on-the-lock-screen.md)
  Add information to your pass so the system can display it on the Lock Screen at a relevant time and place.
- [object Pass.Locations](pass/locations-data.dictionary.md)
  An object that represents a location that the system uses to show a relevant pass.
- [object Pass.RelevantDates](pass/relevantdates-data.dictionary.md)
  An object that represents a date interval that the system uses to show a relevant pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/pass/beacons-data.dictionary)*