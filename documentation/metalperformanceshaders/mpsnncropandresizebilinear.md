# MPSNNCropAndResizeBilinear

**Framework**: Metal Performance Shaders  
**Kind**: cl

A cropping and bilinear resizing filter.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNNCropAndResizeBilinear : MPSCNNKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsnncropandresizebilinear/3013788-init.md)
- [init(device: any MTLDevice, resizeWidth: Int, resizeHeight: Int, numberOfRegions: Int, regions: UnsafePointer<MPSRegion>)](mpsnncropandresizebilinear/3013789-init.md)
### Instance Properties
- [var numberOfRegions: Int](mpsnncropandresizebilinear/3013790-numberofregions.md)
- [var regions: UnsafePointer<MPSRegion>](mpsnncropandresizebilinear/3013791-regions.md)
- [var resizeHeight: Int](mpsnncropandresizebilinear/3013792-resizeheight.md)
- [var resizeWidth: Int](mpsnncropandresizebilinear/3013793-resizewidth.md)

## Relationships

### Inherits From
- [MPSCNNKernel](mpscnnkernel.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnncropandresizebilinear)*