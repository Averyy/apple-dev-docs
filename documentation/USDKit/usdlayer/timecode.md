# USDLayer.TimeCode

**Framework**: USDKit  
**Kind**: struct

A time value in USD, typically used for animation keyframe times.

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

#### Overview

Wraps a `Double` but is treated as a distinct schema-registered value type by USD, allowing attributes to be explicitly typed as time code rather than generic floating-point.

## Topics

### Initializers
- [init(Double)](usdlayer/timecode/init(_:).md)
  Creates a time code at the given time.
### Instance Properties
- [var value: Double](usdlayer/timecode/value.md)
  The underlying time value as a Double.
### Type Properties
- [static let `default`: USDLayer.TimeCode](usdlayer/timecode/default.md)
  The default time code (0.0).

## Relationships

### Conforms To
- [Comparable](../Swift/Comparable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [ExpressibleByFloatLiteral](../Swift/ExpressibleByFloatLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [USDPrim.Attribute.Value](usdprim/attribute/value.md)
- [USDValueProtocol](usdvalueprotocol.md)

## See Also

- [var startTimeCode: USDLayer.TimeCode?](usdlayer/starttimecode.md)
  The first time code in the layer’s animation range. `nil` if not authored.
- [var endTimeCode: USDLayer.TimeCode?](usdlayer/endtimecode.md)
  The last time code in the layer’s animation range. `nil` if not authored.
- [var timeCodesPerSecond: Double?](usdlayer/timecodespersecond.md)
  The rate at which time codes advance per second. `nil` if not authored.
- [USDLayer.TimeOffset](usdlayer/timeoffset.md)
  A time transformation applied when composing layers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/timecode)*