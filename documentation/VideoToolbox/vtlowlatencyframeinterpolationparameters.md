# VTLowLatencyFrameInterpolationParameters

**Framework**: Video Toolbox  
**Kind**: class

An object that contains both input and output parameters that the low-latency frame interpolation processor needs.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class VTLowLatencyFrameInterpolationParameters
```

#### Overview

Use this object in the `processWithParameters` call of `VTFrameProcessor` class.

`VTLowLatencyFrameInterpolationParameters` are frame-level parameters.

## Topics

### Initializers
- [convenience init?(sourceFrame: VTFrameProcessorFrame, previousFrame: VTFrameProcessorFrame, interpolationPhase: [Float], destinationFrames: [VTFrameProcessorFrame])](vtlowlatencyframeinterpolationparameters/init(sourceframe:previousframe:interpolationphase:destinationframes:).md)
### Instance Properties
- [var interpolationPhase: [Float]](vtlowlatencyframeinterpolationparameters/interpolationphase-886vi.md)
- [var previousFrame: VTFrameProcessorFrame](vtlowlatencyframeinterpolationparameters/previousframe.md)
  Previous frame that you provided when creating the low-latency frame interpolation parameters object.
- [var sourceFrame: VTFrameProcessorFrame](vtlowlatencyframeinterpolationparameters/sourceframe.md)
  Source frame that you provided when creating the low-latency frame interpolation parameters object.

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

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtlowlatencyframeinterpolationparameters)*