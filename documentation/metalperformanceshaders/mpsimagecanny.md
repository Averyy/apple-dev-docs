# MPSImageCanny

**Framework**: Metal Performance Shaders  
**Kind**: cl

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageCanny : MPSUnaryImageKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsimagecanny/3547971-init.md)
- [init(device: any MTLDevice)](mpsimagecanny/3547972-init.md)
- [init(device: any MTLDevice, linearToGrayScaleTransform: UnsafePointer<Float>, sigma: Float)](mpsimagecanny/3547973-init.md)
### Instance Properties
- [var colorTransform: UnsafePointer<Float>](mpsimagecanny/3547969-colortransform.md)
- [var highThreshold: Float](mpsimagecanny/3547970-highthreshold.md)
- [var lowThreshold: Float](mpsimagecanny/3547974-lowthreshold.md)
- [var sigma: Float](mpsimagecanny/3547975-sigma.md)
- [var useFastMode: Bool](mpsimagecanny/3547976-usefastmode.md)

## Relationships

### Inherits From
- [MPSUnaryImageKernel](mpsunaryimagekernel.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagecanny)*