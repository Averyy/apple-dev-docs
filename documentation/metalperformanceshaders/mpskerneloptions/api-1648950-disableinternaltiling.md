# disableInternalTiling

**Framework**: Metal Performance Shaders  
**Kind**: structdata

Some kernels may automatically split up their work internally into multiple tiles. This improves performance on larger textures and reduces the amount of memory needed by the framework for temporary storage. However, if you are using your own tiling scheme to achieve similar results, your tile sizes and the framework’s choice of tile sizes may interfere with one another, causing the framework to subdivide your tiles for its own use inefficiently. Use this option to force the framework to process your data tile as a single chunk.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
static var disableInternalTiling: MPSKernelOptions { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpskerneloptions/1648950-disableinternaltiling)*