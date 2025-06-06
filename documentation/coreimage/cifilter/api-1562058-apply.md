# apply:

**Framework**: Core Image  
**Kind**: instm

Produces a [`CIImage`](ciimage.md) object by applying a kernel function.

**Availability**:
- macOS 10.4+

## Declaration

```swift
- (CIImage *)apply:(CIKernel *)k, ...;
```

#### Discussion

If you are implementing a custom filter, this method needs to be called from within the [`outputImage`](cifilter/1438169-outputimage.md) method in order to apply your kernel function to the [`CIImage`](ciimage.md) object. For example, if the kernel function has this signature:

```occ
kernel vec4 brightenEffect (sampler src, float k)
```

You would supply two arguments after the `k` argument  to the `apply:k, ..` method. In this case, the first argument must be a sampler and the second a floating-point value. For more information on kernels, see [`Core Image Kernel Language Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CIKernelLangRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004397).

## Parameters

- `k`: A   object that contains a kernel function.
- `...`: A list of arguments to supply to the kernel function. The supplied arguments must be type-compatible with the function signature of the kernel function. The list of arguments must be terminated by the   object. 

## See Also

- [- apply:arguments:options:](cifilter/1438077-apply.md)
  Produces a [`CIImage`](ciimage.md) object by applying arguments to a kernel function and using options to control how the kernel function is evaluated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/1562058-apply)*