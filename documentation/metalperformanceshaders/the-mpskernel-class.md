# The MPSKernel Class

**Framework**: Metal Performance Shaders

#### Overview

The [`MPSKernel`](mpskernel.md) is the base class for all Metal Performance Shaders kernels. It defines the baseline behavior for all kernels, declaring the device to run the kernel on, some debugging options, and a user-friendly label, should one be required. Derived from this class are the [`MPSUnaryImageKernel`](mpsunaryimagekernel.md) and [`MPSBinaryImageKernel`](mpsbinaryimagekernel.md) subclasses, which define shared behavior for most image processing kernels (filters) such as edging modes, clipping, and tiling support for image operations that consume one or two source textures. Neither these nor the [`MPSKernel`](mpskernel.md) class are meant to be used directly. They just provide API abstraction and in some cases may allow some level of polymorphic manipulation of image kernel objects.

Subclasses of the [`MPSUnaryImageKernel`](mpsunaryimagekernel.md) and [`MPSBinaryImageKernel`](mpsbinaryimagekernel.md) classes provide specialized initialization and encoding methods to encode various image processing primitives into a command buffer, and may also provide additional configurable properties on their own. Many such image filters are available, such as:

- Convolution filters (Sobel, Gaussian)
- Morphological operators (dilate, erode)
- Histogram operators (equalization, specification)

All of these run on the GPU directly on texture and buffer objects.

As the [`MPSKernel`](mpskernel.md), [`MPSUnaryImageKernel`](mpsunaryimagekernel.md), and [`MPSBinaryImageKernel`](mpsbinaryimagekernel.md) classes serve to unify a diversity of image operations into a simple consistent interface and calling sequence to apply image filters, subclasses implement details that diverge from the norm. For example, some filters may take a small set of parameters (for example, a convolution kernel) to govern how they function. However, the overall sequence for using kernel subclasses remains the same:

1. Determine whether the Metal Performance Shaders framework supports your device by querying the [`MPSSupportsMTLDevice(_:)`](1618849-mpssupportsmtldevice.md) function.
2. Allocate the usual Metal objects to drive a Metal compute pipeline: [`MTLDevice`](https://developer.apple.com/documentation/metal/mtldevice), [`MTLCommandQueue`](https://developer.apple.com/documentation/metal/mtlcommandqueue), and [`MTLCommandBuffer`](https://developer.apple.com/documentation/metal/mtlcommandbuffer). If your app has already written to any command buffers, Metal Performance Shaders can encode onto them inline with your own workload.
3. Create an appropriate kernel—for example, a [`MPSImageGaussianBlur`](mpsimagegaussianblur.md) object if you want to do a Gaussian blur. Kernels are generally lightweight but can be reused to save some setup time. They cannot be used by multiple threads concurrently, so if your app uses Metal from many threads concurrently, make extra kernels. [`MPSKernel`](mpskernel.md) objects conform to the [`NSCopying`](https://developer.apple.com/documentation/foundation/nscopying) protocol.
4. Call the kernel’s encoding method. Parameters for the encoding call vary by kernel type, but operate similarly. They create a command encoder, write commands to run the kernel into the command buffer, and then end the command encoder. This means you must call the [`endEncoding()`](https://developer.apple.com/documentation/metal/mtlcommandencoder/endencoding()) method on your current command encoder before calling a kernel’s encode method. At this point, you can either release the kernel or keep it for later use to save some setup cost.
5. If you wish to encode further commands of your own on the command buffer, you must create a new command encoder to do so.
6. When you are done with the command buffer, submit it to the device using the [`commit()`](https://developer.apple.com/documentation/metal/mtlcommandbuffer/commit()) method. The kernel will then begin running on the GPU. You can either use the [`waitUntilCompleted()`](https://developer.apple.com/documentation/metal/mtlcommandbuffer/waituntilcompleted()) or [`addCompletedHandler(_:)`](https://developer.apple.com/documentation/metal/mtlcommandbuffer/addcompletedhandler(_:)) methods to be notified when the work is done.

Each kernel is allocated against a particular device; a single kernel may not be used with multiple devices. This is necessary because the [`init(device:)`](mpskernel/1618763-init.md) methods sometimes allocate buffers and textures to hold data passed in as parameters to the initialization method, and a device is required to allocate them. Kernels provide a [`copy(with:device:)`](mpskernel/1618912-copy.md) method that allows them to be copied for a new device.

> **Note**: Kernel objects are not entirely thread safe. While they may be used in a multithreaded context, you should not attempt to have multiple kernel objects writing to the same command buffer at the same time. They share restrictions with the command encoder in this regard. In limited circumstances, the same kernel can be used to write to multiple command buffers concurrently. However, that only works if the kernel is treated as an immutable object. That is, if subclass properties of a shared kernel are changed, then the change can be reflected on the other thread while the other thread is encoding its work, leading to undefined behavior. It is generally safest to just make copies of kernel objects, one for each thread.

## See Also

- [Tuning Hints](tuning_hints.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/the_mpskernel_class)*