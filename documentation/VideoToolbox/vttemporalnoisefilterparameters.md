# VTTemporalNoiseFilterParameters

**Framework**: Video Toolbox  
**Kind**: class

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
class VTTemporalNoiseFilterParameters
```

#### Overview

This object is intended for sending input parameters into the processWithParameters method of the VTFrameProcessor class. Temporal Noise Filter processor utilizes past and future reference frames, provided in presentation time order, to reduce noise from the source frame. The previousFrameCount and nextFrameCount properties in VTTemporalNoiseFilterConfiguration represent the maximum number of past and future reference frames that can be used by the processor to achieve optimum noise reduction quality. The number of reference frames provided shall depend on their availability, but at a minimum, one reference frame, either past or future, must be provided. The parameter destinationFrame stores the output frame that is returned to the caller upon the successful completion of the processWithParameters operation.

## Topics

### Initializers
- [init(sourceFrame: VTFrameProcessorFrame, nextFrames: [VTFrameProcessorFrame]?, previousFrames: [VTFrameProcessorFrame]?, destinationFrame: VTFrameProcessorFrame, filterStrength: Float, discontinuity: Bool)](vttemporalnoisefilterparameters/init(sourceframe:nextframes:previousframes:destinationframe:filterstrength:discontinuity:).md)
### Instance Properties
- [var discontinuity: Bool](vttemporalnoisefilterparameters/discontinuity.md)
- [var filterStrength: Float](vttemporalnoisefilterparameters/filterstrength.md)
- [var nextFrames: [VTFrameProcessorFrame]?](vttemporalnoisefilterparameters/nextframes.md)
- [var previousFrames: [VTFrameProcessorFrame]?](vttemporalnoisefilterparameters/previousframes.md)
- [var sourceFrame: VTFrameProcessorFrame](vttemporalnoisefilterparameters/sourceframe.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [VTFrameProcessorParameters](vtframeprocessorparameters.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vttemporalnoisefilterparameters)*