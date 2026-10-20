# USDLayer.TimeOffset

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A time transformation applied when composing layers.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct TimeOffset
```

#### Overview

Consists of an offset (time shift) and a scale factor. Used in references and payloads to remap animation timing from a referenced layer into the referencing layer’s timeline.

## Topics

### Initializers
- [init(offset: Double, scale: Double)](./timeoffset/init%28offset,scale%29.md)
  Creates a time offset with the given shift and scale.
### Instance Properties
- [var isIdentity: Bool](./timeoffset/isidentity.md)
  Whether this offset has no effect (`offset == 0`, `scale == 1`).
- [var isValid: Bool](./timeoffset/isvalid.md)
  Whether both `offset` and `scale` are finite (not NaN or infinite).
- [var offset: Double](./timeoffset/offset.md)
  The time shift applied during composition.
- [var scale: Double](./timeoffset/scale.md)
  The scale factor applied during composition.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [USDValueProtocol](../usdvalueprotocol.md)

## See Also

### Setting the time range
- [var startTimeCode: USDLayer.TimeCode?](./starttimecode.md)
  The first time code in the layer’s animation range. `nil` if not authored.
- [var endTimeCode: USDLayer.TimeCode?](./endtimecode.md)
  The last time code in the layer’s animation range. `nil` if not authored.
- [var timeCodesPerSecond: Double?](./timecodespersecond.md)
  The rate at which time codes advance per second. `nil` if not authored.
- [USDLayer.TimeCode](./timecode.md)
  A time value in USD, typically used for animation keyframe times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/timeoffset)*