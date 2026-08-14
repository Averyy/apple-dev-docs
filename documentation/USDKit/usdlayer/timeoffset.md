# USDLayer.TimeOffset

**Framework**: USDKit  
**Kind**: struct

A time transformation applied when composing layers.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct TimeOffset
```

#### Overview

Consists of an offset (time shift) and a scale factor. Used in references and payloads to remap animation timing from a referenced layer into the referencing layer’s timeline.

## Topics

### Initializers
- [init(offset: Double, scale: Double)](usdlayer/timeoffset/init(offset:scale:).md)
  Creates a time offset with the given shift and scale.
### Instance Properties
- [var isIdentity: Bool](usdlayer/timeoffset/isidentity.md)
  Whether this offset has no effect (`offset == 0`, `scale == 1`).
- [var isValid: Bool](usdlayer/timeoffset/isvalid.md)
  Whether both `offset` and `scale` are finite (not NaN or infinite).
- [var offset: Double](usdlayer/timeoffset/offset.md)
  The time shift applied during composition.
- [var scale: Double](usdlayer/timeoffset/scale.md)
  The scale factor applied during composition.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [USDValueProtocol](usdvalueprotocol.md)

## See Also

- [var startTimeCode: USDLayer.TimeCode?](usdlayer/starttimecode.md)
  The first time code in the layer’s animation range. `nil` if not authored.
- [var endTimeCode: USDLayer.TimeCode?](usdlayer/endtimecode.md)
  The last time code in the layer’s animation range. `nil` if not authored.
- [var timeCodesPerSecond: Double?](usdlayer/timecodespersecond.md)
  The rate at which time codes advance per second. `nil` if not authored.
- [USDLayer.TimeCode](usdlayer/timecode.md)
  A time value in USD, typically used for animation keyframe times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/timeoffset)*