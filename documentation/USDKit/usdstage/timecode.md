# USDStage.TimeCode

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A unitless point in time, used with time-varying values authored in 3D scenes.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct TimeCode
```

## Topics

### Initializers
- [init(Double)](./timecode/init%28_%29-20ucy.md)
  A numeric time value.
- [init(USDLayer.TimeCode)](./timecode/init%28_%29-336gn.md)
  A numeric time value.
- [init(preTime: USDLayer.TimeCode)](./timecode/init%28pretime%29-2p3ii.md)
  The instant directly before the given time value.
- [init(preTime: Double)](./timecode/init%28pretime%29-7gpbh.md)
  The instant directly before the given time value.
### Instance Properties
- [var isPreTime: Bool](./timecode/ispretime.md)
  A Boolean value that indicates whether this time code represents the limit of a value approaching from the left of a discontinuity.
- [var value: Double?](./timecode/value.md)
  The numeric value of this time code, or `nil` if it is the default time code.
### Type Properties
- [static var `default`: USDStage.TimeCode](./timecode/default.md)
  The time code used to author and read values that do not vary over time.
- [static var earliest: USDStage.TimeCode](./timecode/earliest.md)
  A sentinel time code that resolves to the earliest authored sample of a value.
### Type Methods
- [static func safeStep(maxValue: Double, maxCompression: Double) -> Double](./timecode/safestep%28maxvalue,maxcompression%29.md)
  Returns a time delta small enough to represent a jump discontinuity, but large enough to survive scaling and shifting without collapsing to zero.
### Default Implementations
- [CustomStringConvertible Implementations](./timecode/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Comparable](../../Swift/comparable.md)
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [ExpressibleByFloatLiteral](../../Swift/expressiblebyfloatliteral.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Working with time codes
- [var timeCodeRange: ClosedRange<USDStage.TimeCode>](./timecoderange.md)
  The range of time codes over which this stage has authored animation.
- [var timeCodesPerSecond: Double](./timecodespersecond.md)
  The number of time codes per second of playback for this stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/timecode)*