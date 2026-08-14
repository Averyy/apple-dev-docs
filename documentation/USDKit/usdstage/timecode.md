# USDStage.TimeCode

**Framework**: USDKit  
**Kind**: struct

A unitless point in time, used with time-varying values authored in 3D scenes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct TimeCode
```

## Topics

### Initializers
- [init(Double)](usdstage/timecode/init(_:)-20ucy.md)
  A numeric time value.
- [init(USDLayer.TimeCode)](usdstage/timecode/init(_:)-336gn.md)
  A numeric time value.
- [init(preTime: USDLayer.TimeCode)](usdstage/timecode/init(pretime:)-2p3ii.md)
  The instant directly before the given time value.
- [init(preTime: Double)](usdstage/timecode/init(pretime:)-7gpbh.md)
  The instant directly before the given time value.
### Instance Properties
- [var isPreTime: Bool](usdstage/timecode/ispretime.md)
  A Boolean value that indicates whether this time code represents the limit of a value approaching from the left of a discontinuity.
- [var value: Double?](usdstage/timecode/value.md)
  The numeric value of this time code, or `nil` if it is the default time code.
### Type Properties
- [static var `default`: USDStage.TimeCode](usdstage/timecode/default.md)
  The time code used to author and read values that do not vary over time.
- [static var earliest: USDStage.TimeCode](usdstage/timecode/earliest.md)
  A sentinel time code that resolves to the earliest authored sample of a value.
### Type Methods
- [static func safeStep(maxValue: Double, maxCompression: Double) -> Double](usdstage/timecode/safestep(maxvalue:maxcompression:).md)
  Returns a time delta small enough to represent a jump discontinuity, but large enough to survive scaling and shifting without collapsing to zero.
### Default Implementations
- [CustomStringConvertible Implementations](usdstage/timecode/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Comparable](../swift/comparable.md)
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [ExpressibleByFloatLiteral](../swift/expressiblebyfloatliteral.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var timeCodeRange: ClosedRange<USDStage.TimeCode>](usdstage/timecoderange.md)
  The range of time codes over which this stage has authored animation.
- [var timeCodesPerSecond: Double](usdstage/timecodespersecond.md)
  The number of time codes per second of playback for this stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/timecode)*