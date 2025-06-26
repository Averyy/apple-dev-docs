# destinationImageDescriptor(forSourceImages:sourceStates:for:suggestedDescriptor:)

**Framework**: Metal Performance Shaders  
**Kind**: method

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional func destinationImageDescriptor(forSourceImages sourceImages: [MPSImage], sourceStates: [MPSState]?, for kernel: MPSKernel, suggestedDescriptor inDescriptor: MPSImageDescriptor) -> MPSImageDescriptor
```

## See Also

- [class MPSImage](mpsimage.md)
  A texture that may have more than four channels for use in convolutional neural networks.
- [class MPSState](mpsstate.md)
  An opaque data container for large storage in MPS CNN filters.
- [class MPSKernel](mpskernel.md)
  A standard interface for Metal Performance Shaders kernels.
- [class MPSImageDescriptor](mpsimagedescriptor.md)
  A description of the attributes used to create an [`MPSImage`](mpsimage.md).
- [func paddingMethod() -> MPSNNPaddingMethod](mpsnnpadding/paddingmethod.md)
- [func label() -> String](mpsnnpadding/label.md)
- [func inverse() -> Self?](mpsnnpadding/inverse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnpadding/destinationimagedescriptor(forsourceimages:sourcestates:for:suggesteddescriptor:))*