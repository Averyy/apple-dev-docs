# VNVideoProcessor.TimeIntervalCadence

**Framework**: Vision  
**Kind**: class

An object that defines a time-based cadence for processing a video stream.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class TimeIntervalCadence
```

## Topics

### Creating a Cadence
- [init(CFTimeInterval)](vnvideoprocessor/timeintervalcadence/init(_:).md)
  Creates a new time-based cadence with a time interval.
- [init(timeInterval: CFTimeInterval)](vnvideoprocessor/timeintervalcadence/init(timeinterval:).md)
### Inspecting the Time Interval
- [var timeInterval: CFTimeInterval](vnvideoprocessor/timeintervalcadence/timeinterval.md)
  The time interval of the cadence.

## Relationships

### Inherits From
- [VNVideoProcessor.Cadence](vnvideoprocessor/cadence.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [var cadence: VNVideoProcessor.Cadence?](vnvideoprocessor/requestprocessingoptions/cadence.md)
  The cadence the video processor maintains to process the request.
- [VNVideoProcessor.Cadence](vnvideoprocessor/cadence.md)
  An object that defines the cadence at which to process video.
- [VNVideoProcessor.FrameRateCadence](vnvideoprocessor/frameratecadence.md)
  An object that defines a frame-based cadence for processing a video stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnvideoprocessor/timeintervalcadence)*