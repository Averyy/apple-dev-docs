# VTLowLatencySuperResolutionScalerParameters

**Framework**: Video Toolbox  
**Kind**: class

An object that contains both input and output parameters that the low-latency super-resolution scaler frame processor needs.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class VTLowLatencySuperResolutionScalerParameters
```

#### Overview

Use this object in the `processWithParameters` call of `VTFrameProcessor` class.

`VTLowLatencySuperResolutionScalerParameters` are frame-level parameters.

## Topics

### Creating a parameters object
- [init(sourceFrame: VTFrameProcessorFrame, destinationFrame: VTFrameProcessorFrame)](vtlowlatencysuperresolutionscalerparameters/init(sourceframe:destinationframe:).md)
  Creates a new low-latency, super-resolution scaler parameters object.
### Inspecting the parameters
- [var sourceFrame: VTFrameProcessorFrame](vtlowlatencysuperresolutionscalerparameters/sourceframe.md)
  Current source frame, which must be non `nil`.

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

## See Also

- [class VTLowLatencySuperResolutionScalerConfiguration](vtlowlatencysuperresolutionscalerconfiguration.md)
  An object you use to configure frame processor for low-latency super-resolution scaler processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtlowlatencysuperresolutionscalerparameters)*