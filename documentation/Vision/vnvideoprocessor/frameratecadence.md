# VNVideoProcessor.FrameRateCadence

**Framework**: Vision  
**Kind**: class

An object that defines a frame-based cadence for processing a video stream.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class FrameRateCadence
```

## Topics

### Creating a Cadence
- [init(Int)](vnvideoprocessor/frameratecadence/init(_:).md)
  Creates a new frame-based cadence with a frame rate.
### Inspecting the Frame Rate
- [var frameRate: Int](vnvideoprocessor/frameratecadence/framerate.md)
  The frame rate at which to process video.

## Relationships

### Inherits From
- [VNVideoProcessor.Cadence](vnvideoprocessor/cadence.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var cadence: VNVideoProcessor.Cadence?](vnvideoprocessor/requestprocessingoptions/cadence.md)
  The cadence the video processor maintains to process the request.
- [VNVideoProcessor.Cadence](vnvideoprocessor/cadence.md)
  An object that defines the cadence at which to process video.
- [VNVideoProcessor.TimeIntervalCadence](vnvideoprocessor/timeintervalcadence.md)
  An object that defines a time-based cadence for processing a video stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnvideoprocessor/frameratecadence)*