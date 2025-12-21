# VTTemporalNoiseFilterParameters

**Framework**: Video Toolbox  
**Kind**: class

Encapsulates the frame-level parameters necessary for processing a source frame using temporal noise-filter processor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
class VTTemporalNoiseFilterParameters
```

#### Overview

This object is intended for sending input parameters into the `processWithParameters` method of the `VTFrameProcessor` class. Temporal noise-filter processor utilizes past and future reference frames, provided in presentation time order, to reduce noise from the source frame. The `previousFrameCount` and `nextFrameCount` properties in [`VTTemporalNoiseFilterConfiguration`](vttemporalnoisefilterconfiguration.md) represent the maximum number of past and future reference frames that the processor can use to achieve optimum noise reduction quality. The number of reference frames provided shall depend on their availability, but at a minimum, you must provide one reference frame, either past or future. The parameter `destinationFrame` stores the output frame that the processor returns to the caller upon the successful completion of the `processWithParameters` operation.

## Topics

### Initializers
- [init?(sourceFrame: VTFrameProcessorFrame, nextFrames: [VTFrameProcessorFrame], previousFrames: [VTFrameProcessorFrame], destinationFrame: VTFrameProcessorFrame, filterStrength: Float, hasDiscontinuity: Bool)](vttemporalnoisefilterparameters/init(sourceframe:nextframes:previousframes:destinationframe:filterstrength:hasdiscontinuity:).md)
  Creates a new `VTTemporalNoiseFilterParameters` object.
### Instance Properties
- [var filterStrength: Float](vttemporalnoisefilterparameters/filterstrength.md)
  A parameter to control the strength of noise-filtering. The value can range from the minimum strength of 0.0 to the maximum strength of 1.0. Change in filter strength causes the processor to flush all frames in the queue prior to processing the source frame.
- [var hasDiscontinuity: Bool](vttemporalnoisefilterparameters/hasdiscontinuity.md)
  A Boolean that indicates sequence discontinuity, forcing the processor to reset prior to processing the source frame.
- [var nextFrames: [VTFrameProcessorFrame]](vttemporalnoisefilterparameters/nextframes.md)
  Future reference frames in presentation time order that you use to process the source frame.
- [var previousFrames: [VTFrameProcessorFrame]](vttemporalnoisefilterparameters/previousframes.md)
  Past reference frames in presentation time order that you use to process the source frame.
- [var sourceFrame: VTFrameProcessorFrame](vttemporalnoisefilterparameters/sourceframe.md)
  Current source frame; must be non `nil`.

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