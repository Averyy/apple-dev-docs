# cadence

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The cadence the video processor maintains to process the request.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var cadence: VNVideoProcessor.Cadence? { get set }
```

```objc
@property (copy, readwrite, nullable) VNVideoProcessorCadence * cadence;
```

#### Discussion

By default, the system processes every frame of video if you don’t provide a value for this property.

## See Also

### Configuring Options
- [VNVideoProcessor.Cadence](../cadence.md)
  An object that defines the cadence at which to process video.
- [VNVideoProcessor.FrameRateCadence](../frameratecadence.md)
  An object that defines a frame-based cadence for processing a video stream.
- [VNVideoProcessor.TimeIntervalCadence](../timeintervalcadence.md)
  An object that defines a time-based cadence for processing a video stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnvideoprocessor/requestprocessingoptions/cadence)*