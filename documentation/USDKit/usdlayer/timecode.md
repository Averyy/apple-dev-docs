# USDLayer.TimeCode

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A time value in USD, typically used for animation keyframe times.

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

## Overview

Wraps a `Double` but is treated as a distinct schema-registered value type by USD, allowing attributes to be explicitly typed as time code rather than generic floating-point.

## Topics

### Initializers
- [init(Double)](./timecode/init%28_%29.md)
  Creates a time code at the given time.
### Instance Properties
- [var value: Double](./timecode/value.md)
  The underlying time value as a Double.
### Type Properties
- [static let `default`: USDLayer.TimeCode](./timecode/default.md)
  The default time code (0.0).

## Relationships

### Conforms To
- [Comparable](../../Swift/comparable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [ExpressibleByFloatLiteral](../../Swift/expressiblebyfloatliteral.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [USDPrim.Attribute.Value](../usdprim/attribute/value.md)
- [USDValueProtocol](../usdvalueprotocol.md)

## See Also

### Setting the time range
- [var startTimeCode: USDLayer.TimeCode?](./starttimecode.md)
  The first time code in the layer’s animation range. `nil` if not authored.
- [var endTimeCode: USDLayer.TimeCode?](./endtimecode.md)
  The last time code in the layer’s animation range. `nil` if not authored.
- [var timeCodesPerSecond: Double?](./timecodespersecond.md)
  The rate at which time codes advance per second. `nil` if not authored.
- [USDLayer.TimeOffset](./timeoffset.md)
  A time transformation applied when composing layers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/timecode)*