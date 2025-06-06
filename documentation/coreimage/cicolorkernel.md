# CIColorKernel

**Framework**: Core Image  
**Kind**: cl

A GPU-based image-processing routine that processes only the color information in images, used to create custom Core Image filters.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CIColorKernel : CIKernel
```

#### Overview

The kernel language routine for a color kernel has the following characteristics:

- Its return type is `vec4` (Core Image Kernel Language) or `float4` (Metal Shading Language); that is, it returns a pixel color for the output image.
- It may use zero or more input images. Each input image is represented by a parameter of type `__sample` (Core Image Kernel Language) or `sample_t` (Metal Shading Language), which can be treated as a single pixel color of type `vec4` (Core Image Kernel Language) or `float4` (Metal Shading Language);.

A color kernel routine receives as input single-pixel colors (one sampled from each input image) and computes a final pixel color (output using the `return` keyword). For example, the Metal Shading Language source below implements a filter that passes through its input image unchanged.

```other
#include <CoreImage/CoreImage.h>
 
extern "C" {
    namespace coreimage {
        float4 do_nothing(sample_t s) {
            return s;
        }
    }
}
```

The equivalent code in Core Image Kernel Language is:

```other
kernel vec4 do_nothing(__sample s) {
    return s.rgba;
}
```

The Core Image Kernel Language is a dialect of the OpenGL Shading Language. See [`Core Image Kernel Language Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CIKernelLangRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004397) and [`Core Image Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185) for more details.

## Topics

### Creating a Kernel
- [init?(source: String)](cicolorkernel/1438143-init.md)
  Creates a color kernel object from the specified kernel source code.
### Applying a Kernel to Filter an Image
- [func apply(extent: CGRect, arguments: [Any]) -> CIImage?](cicolorkernel/1438110-apply.md)
  Creates a new image using the kernel and specified arguments.

## Relationships

### Inherits From
- [CIKernel](cikernel.md)

## See Also

- [Writing Custom Kernels](writing_custom_kernels.md)
  Write your own custom kernels in either the Core Image Kernel Language or the Metal Shading Language.
- [class CIKernel](cikernel.md)
  A GPU-based image-processing routine used to create custom Core Image filters.
- [class CIWarpKernel](ciwarpkernel.md)
  A GPU-based image-processing routine that processes only the geometry information in an image, used to create custom Core Image filters.
- [class CIBlendKernel](ciblendkernel.md)
  A GPU-based image-processing routine that is optimized for blending two images.
- [class CISampler](cisampler.md)
  An object that retrieves pixel samples for processing by a filter kernel.
- [class CIFilterShape](cifiltershape.md)
  A description of the bounding shape of a filter and the domain of definition for a filter operation.
- [struct CIFormat](ciformat.md)
  Pixel data formats for image input, output, and processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolorkernel)*