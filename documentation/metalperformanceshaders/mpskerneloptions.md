# MPSKernelOptions

**Framework**: Metal Performance Shaders  
**Kind**: struct

The options used when creating a kernel.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct MPSKernelOptions
```

#### Overview

The Metal Performance Shaders framework uses the same API validation layer that Metal uses to alert you to API mistakes during development. While this option is turned on in your Xcode scheme, common programming errors will either trigger an assert or send a warning to the debug log. Except in the case of serious errors, little or no output should arrive in the console under standard usage. You can set a kernel’s [`options`](mpskernel/options.md) parameter to the [`skipAPIValidation`](mpskerneloptions/skipapivalidation.md) value to skip most of this checking. This flag may also lead to small reductions in CPU cost.

## Topics

### Constants
- [static var none: MPSKernelOptions](mpskerneloptions/none.md)
  The default option for the kernel. Kernels created with this option will not skip any API validation and will not use reduced precision.
- [static var skipAPIValidation: MPSKernelOptions](mpskerneloptions/skipapivalidation.md)
  A property that directs the kernel to perform or skip argument validation.
- [static var allowReducedPrecision: MPSKernelOptions](mpskerneloptions/allowreducedprecision.md)
  When possible, kernels use a higher-precision data representation internally than the destination storage format to avoid excessive accumulation of computational rounding error in the result. This option advises the kernel that the destination storage format already has too much precision for what is ultimately required downstream, and the kernel may use reduced precision internally when it determines that a less precise result would yield better performance. When enabled, the performance win is often small and the precision of the result may vary by hardware and OS.
- [static var disableInternalTiling: MPSKernelOptions](mpskerneloptions/disableinternaltiling.md)
  Some kernels may automatically split up their work internally into multiple tiles. This improves performance on larger textures and reduces the amount of memory needed by the framework for temporary storage. However, if you are using your own tiling scheme to achieve similar results, your tile sizes and the framework’s choice of tile sizes may interfere with one another, causing the framework to subdivide your tiles for its own use inefficiently. Use this option to force the framework to process your data tile as a single chunk.
- [static var insertDebugGroups: MPSKernelOptions](mpskerneloptions/insertdebuggroups.md)
  Enables calling kernel encode methods.
### Initializers
- [init(rawValue: UInt)](mpskerneloptions/init(rawvalue:).md)
### Type Properties
- [static var verbose: MPSKernelOptions](mpskerneloptions/verbose.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var options: MPSKernelOptions](mpskernel/options.md)
  The set of options used to run the kernel.
- [var device: any MTLDevice](mpskernel/device.md)
  The device on which the kernel will be used.
- [var label: String?](mpskernel/label.md)
  The string that identifies the kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpskerneloptions)*