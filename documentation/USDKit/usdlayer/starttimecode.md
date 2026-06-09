# startTimeCode

**Framework**: USDKit  
**Kind**: property

The first time code in the layer’s animation range. `nil` if not authored.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var startTimeCode: USDLayer.TimeCode? { get nonmutating set }
```

## See Also

- [var endTimeCode: USDLayer.TimeCode?](usdlayer/endtimecode.md)
  The last time code in the layer’s animation range. `nil` if not authored.
- [var timeCodesPerSecond: Double?](usdlayer/timecodespersecond.md)
  The rate at which time codes advance per second. `nil` if not authored.
- [USDLayer.TimeCode](usdlayer/timecode.md)
  A time value in USD, typically used for animation keyframe times.
- [USDLayer.TimeOffset](usdlayer/timeoffset.md)
  A time transformation applied when composing layers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/starttimecode)*