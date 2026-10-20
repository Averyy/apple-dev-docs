# fallbackUpAxis

**Framework**: USDKit  
**Kind**: property  
**Role**: Type Property

The up axis used when a stage has no authored opinion.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static var fallbackUpAxis: USDToken { get }
```

## See Also

### Reading stage metrics
- [var metersPerUnit: Double](./metersperunit.md)
  The number of meters represented by one unit in this stage’s coordinate system.
- [var hasAuthoredMetersPerUnit: Bool](./hasauthoredmetersperunit.md)
  A Boolean value that indicates whether this stage has an authored [`metersPerUnit`](./metersperunit.md) opinion.
- [var upAxis: USDToken](./upaxis.md)
  The axis that points upward in this stage’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/fallbackupaxis)*