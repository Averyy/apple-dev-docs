# timeCodeRange

**Framework**: USDKit  
**Kind**: property

The range of time codes over which this stage has authored animation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var timeCodeRange: ClosedRange<USDStage.TimeCode> { get nonmutating set }
```

## See Also

- [var timeCodesPerSecond: Double](usdstage/timecodespersecond.md)
  The number of time codes per second of playback for this stage.
- [USDStage.TimeCode](usdstage/timecode.md)
  A unitless point in time, used with time-varying values authored in 3D scenes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/timecoderange)*