# VNVideoProcessor.TimeIntervalCadence

**Framework**: Vision  
**Kind**: class  
**Role**: Class

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

```objc
@interface VNVideoProcessorTimeIntervalCadence : VNVideoProcessorCadence
```

## Topics

### Creating a Cadence
- [init(CFTimeInterval)](./timeintervalcadence/init%28_%29.md)
  Creates a new time-based cadence with a time interval.
- [init(timeInterval: CFTimeInterval)](./timeintervalcadence/init%28timeinterval%29.md)
### Inspecting the Time Interval
- [var timeInterval: CFTimeInterval](./timeintervalcadence/timeinterval.md)
  The time interval of the cadence.

## Relationships

### Inherits From
- [VNVideoProcessor.Cadence](./cadence.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Configuring Options
- [var cadence: VNVideoProcessor.Cadence?](./requestprocessingoptions/cadence.md)
  The cadence the video processor maintains to process the request.
- [VNVideoProcessor.Cadence](./cadence.md)
  An object that defines the cadence at which to process video.
- [VNVideoProcessor.FrameRateCadence](./frameratecadence.md)
  An object that defines a frame-based cadence for processing a video stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnvideoprocessor/timeintervalcadence)*