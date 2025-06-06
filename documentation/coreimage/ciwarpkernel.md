# CIWarpKernel

**Framework**: Core Image  
**Kind**: cl

A GPU-based image-processing routine that processes only the geometry information in an image, used to create custom Core Image filters.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CIWarpKernel : CIKernel
```

#### Overview

The kernel language routine for a warp kernel has the following characteristics:

- It uses exactly one input image.
- Its return type is `vec2 `(Core Image Kernel Language) or `float2` (Metal Shading Language), specifying a position in source image coordinates. 

A warp kernel routine requires no input parameters (but can use additional custom parameters you declare). Typically, a warp kernel uses the destination coordinate function to look up the coordinates of the destination pixel currently being rendered, then computes a corresponding position in source image coordinates (output using the `return` keyword). Core Image then samples from the source image at the returned coordinates to produce a pixel color for the output image. For example, the Metal Shading Language source below implements a filter that passes through its input image unchanged.

```other
#include <CoreImage/CoreImage.h>
 
extern "C" {
    namespace coreimage {
        float2 do_nothing(destination dest) {
            return dest.coord();
        }
    }
}
```

The equivalent code in Core Image Kernel Language is:

```other
kernel vec2 do_nothing() {
    return destCoord();
}
```

The Core Image Kernel Language is a dialect of the OpenGL Shading Language. See [`Core Image Kernel Language Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CIKernelLangRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004397) and [`Core Image Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185) for more details.

## Topics

### Creating a Kernel
- [init?(source: String)](ciwarpkernel/1438278-init.md)
  Creates a warp kernel object from the specified kernel source code.
### Applying a Kernel to Filter an Image
- [func apply(extent: CGRect, roiCallback: CIKernelROICallback, image: CIImage, arguments: [Any]) -> CIImage?](ciwarpkernel/1437798-apply.md)
  Creates a new image using the kernel and the specified input image and arguments.

## Relationships

### Inherits From
- [CIKernel](cikernel.md)

## See Also

- [Writing Custom Kernels](writing_custom_kernels.md)
  Write your own custom kernels in either the Core Image Kernel Language or the Metal Shading Language.
- [class CIKernel](cikernel.md)
  A GPU-based image-processing routine used to create custom Core Image filters.
- [class CIColorKernel](cicolorkernel.md)
  A GPU-based image-processing routine that processes only the color information in images, used to create custom Core Image filters.
- [class CIBlendKernel](ciblendkernel.md)
  A GPU-based image-processing routine that is optimized for blending two images.
- [class CISampler](cisampler.md)
  An object that retrieves pixel samples for processing by a filter kernel.
- [class CIFilterShape](cifiltershape.md)
  A description of the bounding shape of a filter and the domain of definition for a filter operation.
- [struct CIFormat](ciformat.md)
  Pixel data formats for image input, output, and processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciwarpkernel)*