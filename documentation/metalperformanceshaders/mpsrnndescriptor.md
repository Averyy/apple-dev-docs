# MPSRNNDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: class

A description of a recursive neural network block or layer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSRNNDescriptor
```

## Topics

### Instance Properties
- [var inputFeatureChannels: Int](mpsrnndescriptor/inputfeaturechannels.md)
- [var layerSequenceDirection: MPSRNNSequenceDirection](mpsrnndescriptor/layersequencedirection.md)
- [var outputFeatureChannels: Int](mpsrnndescriptor/outputfeaturechannels.md)
- [var useFloat32Weights: Bool](mpsrnndescriptor/usefloat32weights.md)
- [var useLayerInputUnitTransformMode: Bool](mpsrnndescriptor/uselayerinputunittransformmode.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [MPSGRUDescriptor](mpsgrudescriptor.md)
- [MPSLSTMDescriptor](mpslstmdescriptor.md)
- [MPSRNNSingleGateDescriptor](mpsrnnsinglegatedescriptor.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [init?(coder: NSCoder, device: any MTLDevice)](mpsrnnimageinferencelayer/init(coder:device:).md)
- [init(device: any MTLDevice, rnnDescriptor: MPSRNNDescriptor)](mpsrnnimageinferencelayer/init(device:rnndescriptor:).md)
- [init(device: any MTLDevice, rnnDescriptors: [MPSRNNDescriptor])](mpsrnnimageinferencelayer/init(device:rnndescriptors:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrnndescriptor)*