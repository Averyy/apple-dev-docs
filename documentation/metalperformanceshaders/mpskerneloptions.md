# MPSKernelOptions

**Framework**: Metal Performance Shaders  
**Kind**: struct

The options used when creating a kernel.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct MPSKernelOptions
```

#### Overview

The Metal Performance Shaders framework uses the same API validation layer that Metal uses to alert you to API mistakes during development. While this option is turned on in your Xcode scheme, common programming errors will either trigger an assert or send a warning to the debug log. Except in the case of serious errors, little or no output should arrive in the console under standard usage. You can set a kernel’s [`options`](mpskernel/1618889-options.md) parameter to the [`skipAPIValidation`](mpskerneloptions/1618826-skipapivalidation.md) value to skip most of this checking. This flag may also lead to small reductions in CPU cost.

## Topics

### Constants
- [static var none: MPSKernelOptions](mpskerneloptions/1618816-none.md)
  The default option for the kernel. Kernels created with this option will not skip any API validation and will not use reduced precision.
- [static var skipAPIValidation: MPSKernelOptions](mpskerneloptions/1618826-skipapivalidation.md)
  A property that directs the kernel to perform or skip argument validation.
- [static var allowReducedPrecision: MPSKernelOptions](mpskerneloptions/1618748-allowreducedprecision.md)
  When possible, kernels use a higher-precision data representation internally than the destination storage format to avoid excessive accumulation of computational rounding error in the result. This option advises the kernel that the destination storage format already has too much precision for what is ultimately required downstream, and the kernel may use reduced precision internally when it determines that a less precise result would yield better performance. When enabled, the performance win is often small and the precision of the result may vary by hardware and OS.
- [static var disableInternalTiling: MPSKernelOptions](mpskerneloptions/1648950-disableinternaltiling.md)
  Some kernels may automatically split up their work internally into multiple tiles. This improves performance on larger textures and reduces the amount of memory needed by the framework for temporary storage. However, if you are using your own tiling scheme to achieve similar results, your tile sizes and the framework’s choice of tile sizes may interfere with one another, causing the framework to subdivide your tiles for its own use inefficiently. Use this option to force the framework to process your data tile as a single chunk.
- [static var insertDebugGroups: MPSKernelOptions](mpskerneloptions/1648897-insertdebuggroups.md)
  Enabling this option will cause various kernel `encode` methods to call the [`pushDebugGroup(_:)`](https://developer.apple.com/documentation/metal/mtlcommandencoder/pushdebuggroup(_:)) and [`popDebugGroup()`](https://developer.apple.com/documentation/metal/mtlcommandencoder/popdebuggroup()) methods. The debug string will be drawn from the kernel’s [`label`](mpskernel/1618803-label.md) property, if available, or the name of the class otherwise.
### Initializers
- [init(rawValue: UInt)](mpskerneloptions/1618747-init.md)
### Type Properties
- [static var verbose: MPSKernelOptions](mpskerneloptions/2889867-verbose.md)

## Relationships

### Conforms To
- [OptionSet](../swift/optionset.md)
- [Sendable](../swift/sendable.md)

## See Also

- [var options: MPSKernelOptions](mpskernel/1618889-options.md)
  The set of options used to run the kernel.
- [var device: any MTLDevice](mpskernel/1618824-device.md)
  The device on which the kernel will be used.
- [var label: String?](mpskernel/1618803-label.md)
  The string that identifies the kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpskerneloptions)*