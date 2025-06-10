# Writing Custom Kernels

**Framework**: Core Image

Write your own custom kernels in either the Core Image Kernel Language or the Metal Shading Language.

#### Overview

The Core Image Kernel Language is a shading language optimized for writing custom kernels for use in apps leveraging Core Image.  You can add custom image processing routines to a Core Image pipeline.

You can also write your own kernels in the Metal Shading Language.  The following flowchart shows how you decide which language to use for writing custom kernels:

![Flowchart showing how to choose a kernel language for writing custom CIKernel filters.](https://docs-assets.developer.apple.com/published/475fd86172676d9a39b147cbc2eeac5f/media-3011610%402x.png)

Source code written in Core Image Kernel Language should contain one or more image processing routines and may optionally contain other functions that are called by these routines. The source code is parsed and validated when the code is passed to Core Image’s [`CIKernel`](cikernel.md) creation APIs. When rendering, Core Image can concatenate kernel functions used within an image graph and construct optimized shader programs. See [`Core Image Kernel Language Reference`](https://developer.apple.comhttps://developer.apple.com/go/?id=core-image-kernel-language-reference) for a list of supported data types, functions, and language features.

Alternatively, you can write custom kernels in the Metal Shading Language. If you intend to use Metal-only language features and support exclusively Metal-supported devices, then writing custom kernels in Metal Shading Language can reduce compile-time cost while providing code consistency across your Metal app. See [`Metal Shading Language for Core Image Kernels`](https://developer.apple.comhttps://developer.apple.com/go/?id=metal-shading-language-for-core-image-kernels) for a list of supported data types, functions, and language features.

## See Also

- [class CIKernel](cikernel.md)
  A GPU-based image-processing routine used to create custom Core Image filters.
- [class CIColorKernel](cicolorkernel.md)
  A GPU-based image-processing routine that processes only the color information in images, used to create custom Core Image filters.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/writing-custom-kernels)*