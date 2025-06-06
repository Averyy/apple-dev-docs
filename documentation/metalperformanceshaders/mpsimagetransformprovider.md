# MPSImageTransformProvider

**Framework**: Metal Performance Shaders  
**Kind**: intf

A general interface for objects that provide image resampling. 

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
protocol MPSImageTransformProvider
```

## Topics

### Instance Methods
- [func transform(forSourceImage: MPSImage, handle: (any MPSHandle)?) -> MPSScaleTransform](mpsimagetransformprovider/2915282-transform.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class MPSNNBilinearScaleNode](mpsnnbilinearscalenode.md)
  A representation of a bilinear resampling filter.
- [class MPSNNLanczosScaleNode](mpsnnlanczosscalenode.md)
  A representation of a Lanczos resampling filter.
- [class MPSNNScaleNode](mpsnnscalenode.md)
  Abstract node representing an image resampling filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagetransformprovider)*