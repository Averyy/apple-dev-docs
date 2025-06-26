# none

**Framework**: Metal Performance Shaders  
**Kind**: property

The default option for the kernel. Kernels created with this option will not skip any API validation and will not use reduced precision.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static var none: MPSKernelOptions { get }
```

## See Also

- [static var skipAPIValidation: MPSKernelOptions](mpskerneloptions/skipapivalidation.md)
  A property that directs the kernel to perform or skip argument validation.
- [static var allowReducedPrecision: MPSKernelOptions](mpskerneloptions/allowreducedprecision.md)
  When possible, kernels use a higher-precision data representation internally than the destination storage format to avoid excessive accumulation of computational rounding error in the result. This option advises the kernel that the destination storage format already has too much precision for what is ultimately required downstream, and the kernel may use reduced precision internally when it determines that a less precise result would yield better performance. When enabled, the performance win is often small and the precision of the result may vary by hardware and OS.
- [static var disableInternalTiling: MPSKernelOptions](mpskerneloptions/disableinternaltiling.md)
  Some kernels may automatically split up their work internally into multiple tiles. This improves performance on larger textures and reduces the amount of memory needed by the framework for temporary storage. However, if you are using your own tiling scheme to achieve similar results, your tile sizes and the framework’s choice of tile sizes may interfere with one another, causing the framework to subdivide your tiles for its own use inefficiently. Use this option to force the framework to process your data tile as a single chunk.
- [static var insertDebugGroups: MPSKernelOptions](mpskerneloptions/insertdebuggroups.md)
  Enables calling kernel encode methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpskerneloptions/none)*