# MPSNNPadding

**Framework**: Metal Performance Shaders  
**Kind**: intf

The protocol that provides a description of how kernels should pad images.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
protocol MPSNNPadding
```

## Topics

### Instance Methods
- [func destinationImageDescriptor(forSourceImages: [MPSImage], sourceStates: [MPSState]?, for: MPSKernel, suggestedDescriptor: MPSImageDescriptor) -> MPSImageDescriptor](mpsnnpadding/2867167-destinationimagedescriptor.md)
- [class MPSImage](mpsimage.md)
  A texture that may have more than four channels for use in convolutional neural networks.
- [class MPSState](mpsstate.md)
  An opaque data container for large storage in MPS CNN filters.
- [class MPSKernel](mpskernel.md)
  A standard interface for Metal Performance Shaders kernels.
- [class MPSImageDescriptor](mpsimagedescriptor.md)
  A description of the attributes used to create an [`MPSImage`](mpsimage.md).
- [func paddingMethod() -> MPSNNPaddingMethod](mpsnnpadding/2866950-paddingmethod.md)
- [func label() -> String](mpsnnpadding/2889870-label.md)
- [func inverse() -> Self?](mpsnnpadding/2942456-inverse.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
### Conforming Types
- [MPSNNDefaultPadding](mpsnndefaultpadding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnpadding)*