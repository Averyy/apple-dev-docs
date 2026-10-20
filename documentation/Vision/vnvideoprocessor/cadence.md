# VNVideoProcessor.Cadence

**Framework**: Vision  
**Kind**: class  
**Role**: Class

An object that defines the cadence at which to process video.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class Cadence
```

```objc
@interface VNVideoProcessorCadence : NSObject
```

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [VNVideoProcessor.FrameRateCadence](./frameratecadence.md)
- [VNVideoProcessor.TimeIntervalCadence](./timeintervalcadence.md)
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
- [VNVideoProcessor.FrameRateCadence](./frameratecadence.md)
  An object that defines a frame-based cadence for processing a video stream.
- [VNVideoProcessor.TimeIntervalCadence](./timeintervalcadence.md)
  An object that defines a time-based cadence for processing a video stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnvideoprocessor/cadence)*