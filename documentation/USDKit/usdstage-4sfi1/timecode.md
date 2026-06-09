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
- [init(Double)](usdstage-4sfi1/timecode/init(_:)-20ucy.md)
  A numeric time value.
- [init(USDLayer.TimeCode)](usdstage-4sfi1/timecode/init(_:)-336gn.md)
  A numeric time value.
- [init(preTime: USDLayer.TimeCode)](usdstage-4sfi1/timecode/init(pretime:)-2p3ii.md)
  The instant directly before the given time value.
- [init(preTime: Double)](usdstage-4sfi1/timecode/init(pretime:)-7gpbh.md)
  The instant directly before the given time value.
### Instance Properties
- [var isPreTime: Bool](usdstage-4sfi1/timecode/ispretime.md)
  Whether this time code is a pre-time (the limit approaching from the left of a discontinuous value).
- [var value: Double?](usdstage-4sfi1/timecode/value.md)
  The numeric value of this time code, or `nil` for the default time code.
### Type Properties
- [static var `default`: USDStage.TimeCode](usdstage-4sfi1/timecode/default.md)
  The default time code, used to represent un-time-varying authoring.
- [static var earliest: USDStage.TimeCode](usdstage-4sfi1/timecode/earliest.md)
  A sentinel time code that represents the earliest authored sample for a value.
### Default Implementations
- [CustomStringConvertible Implementations](usdstage-4sfi1/timecode/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Comparable](../Swift/Comparable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [ExpressibleByFloatLiteral](../Swift/ExpressibleByFloatLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var timeCodeRange: ClosedRange<USDStage.TimeCode>](usdstage-4sfi1/timecoderange.md)
  The animation range authored on this stage, in time codes.
- [var timeCodesPerSecond: Double](usdstage-4sfi1/timecodespersecond.md)
  The rate at which time codes advance per second on this stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage-4sfi1/timecode)*