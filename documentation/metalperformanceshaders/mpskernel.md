# MPSKernel

**Framework**: Metal Performance Shaders  
**Kind**: cl

A standard interface for Metal Performance Shaders kernels.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MPSKernel : NSObject
```

#### Overview

You should not use the [`MPSKernel`](mpskernel.md) class directly. Instead, a number of subclasses are available that define specific high-performance data-parallel operations.

The basic sequence for applying a kernel to an image is as follows:

1. Initialize a kernel corresponding to the operation you wish to perform: ```swift
let sobel = MPSImageSobel(device: mtlDevice)
```
2. Encode the kernel into a command buffer. ```swift
sobel.offset = ...
sobel.clipRect = ...
sobel.options = ...
sobel.encode(commandBuffer: commandBuffer,
             sourceTexture: inputImage,
             destinationTexture: resultImage)
``` Encoding the kernel merely encodes the operation into a command buffer. It does not modify any pixels, yet. All kernel state has been copied to the command buffer. Kernels may be reused. If the texture was previously operated on by another command encoder (e.g. a render command encoder), you should call the [`endEncoding()`](https://developer.apple.com/documentation/metal/mtlcommandencoder/endencoding()) method on the other encoder before encoding the filter. Some kernels work in place, even in situations where Metal might not normally allow in-place operation on textures. If in-place operation is desired, you may attempt to call the [`encode(commandBuffer:inPlaceTexture:fallbackCopyAllocator:)`](mpsunaryimagekernel/1618873-encode.md) method. If the operation cannot be completed in place, then [`false`](https://developer.apple.com/documentation/swift/false) will be returned and you will have to create a new result texture and try again. To make an in-place image filter reliable, pass a fallback [`MPSCopyAllocator`](mpscopyallocator.md) block to the method to create a new texture to write to in the event that a filter cannot operate in place. You may repeat step 2 to encode more kernels, as desired.
3. After encoding any additional work to the command buffer using other encoders, submit the command buffer to your command queue, using: ```swift
commandBuffer.commit()
```

> **Note**: It should be self evident that step 2 may not be thread safe. That is, you can not have multiple threads manipulating the same properties on the same kernel object at the same time and achieve coherent output. In common usage, the kernel properties don’t often need to be changed from their default values, but if you need to apply the same filter to multiple images on multiple threads with cropping/tiling, make additional kernel objects per thread (they are cheap). You can use multiple kernel objects on multiple threads, as long as only one thread is operating on any particular kernel object at a time.

It should be self evident that step 2 may not be thread safe. That is, you can not have multiple threads manipulating the same properties on the same kernel object at the same time and achieve coherent output. In common usage, the kernel properties don’t often need to be changed from their default values, but if you need to apply the same filter to multiple images on multiple threads with cropping/tiling, make additional kernel objects per thread (they are cheap). You can use multiple kernel objects on multiple threads, as long as only one thread is operating on any particular kernel object at a time.

## Topics

### Initializers
- [init?(coder: NSCoder)](mpskernel/2875161-init.md)
- [init?(coder: NSCoder, device: any MTLDevice)](mpskernel/2867190-init.md)
### Methods
- [init(device: any MTLDevice)](mpskernel/1618763-init.md)
  Initializes a new kernel object.
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpskernel/1618912-copy.md)
  Makes a copy of this kernel object for a new device.
### Properties
- [var options: MPSKernelOptions](mpskernel/1618889-options.md)
  The set of options used to run the kernel.
- [struct MPSKernelOptions](mpskerneloptions.md)
  The options used when creating a kernel.
- [var device: any MTLDevice](mpskernel/1618824-device.md)
  The device on which the kernel will be used.
- [var label: String?](mpskernel/1618803-label.md)
  The string that identifies the kernel.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../foundation/nscopying.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpskernel)*