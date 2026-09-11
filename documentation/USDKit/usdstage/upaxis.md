# upAxis

**Framework**: USDKit  
**Kind**: property

The axis that points upward in this stage’s coordinate system.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var upAxis: USDToken { get nonmutating set }
```

## See Also

- [var metersPerUnit: Double](usdstage/metersperunit.md)
  The number of meters represented by one unit in this stage’s coordinate system.
- [var hasAuthoredMetersPerUnit: Bool](usdstage/hasauthoredmetersperunit.md)
  A Boolean value that indicates whether this stage has an authored [`metersPerUnit`](usdstage/metersperunit.md) opinion.
- [static var fallbackUpAxis: USDToken](usdstage/fallbackupaxis.md)
  The up axis used when a stage has no authored opinion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/upaxis)*