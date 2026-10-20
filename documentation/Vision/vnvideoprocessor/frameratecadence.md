# VNVideoProcessor.FrameRateCadence

**Framework**: Vision  
**Kind**: class  
**Role**: Class

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

```objc
@interface VNVideoProcessorFrameRateCadence : VNVideoProcessorCadence
```

## Topics

### Creating a Cadence
- [init(Int)](./frameratecadence/init%28_%29.md)
  Creates a new frame-based cadence with a frame rate.
- [init(frameRate: Int)](./frameratecadence/init%28framerate%29.md)
### Inspecting the Frame Rate
- [var frameRate: Int](./frameratecadence/framerate.md)
  The frame rate at which to process video.

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
- [VNVideoProcessor.TimeIntervalCadence](./timeintervalcadence.md)
  An object that defines a time-based cadence for processing a video stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnvideoprocessor/frameratecadence)*