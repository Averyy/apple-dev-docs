# CIBlendKernel

**Framework**: Core Image  
**Kind**: class

A GPU-based image-processing routine that is optimized for blending two images.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class CIBlendKernel
```

#### Overview

The blend kernel function has the following characteristics:

- It has two arguments of type `__sample` (Core Image Kernel Language) or `sample_t` (Metal Shading Language), representing the foreground and background images.
- Its return type is `vec4` (Core Image Kernel Language) or `float4` (Metal Shading Language); that is, it returns a pixel color for the output image.

A blend kernel routine receives as input single-pixel colors (one sampled from each input image) and computes a final pixel color (output using the return keyword). For example, the Metal Shading Language source below implements a filter that returns the average of its two input images.

```c
#include <CoreImage/CoreImage.h>
 
float4 averageBlend(sample_t foreground, sample_t background) {
    return (foreground + background) / 2.0;
}
```

Generally, the extent of the output image is the union of the extents of the foreground and background images.

## Topics

### Creating a Kernel
- [convenience init?(source: String)](ciblendkernel/init(source:).md)
  Creates a custom blend kernel from a program string.
### Applying a Kernel to Filter an Image
- [func apply(foreground: CIImage, background: CIImage) -> CIImage?](ciblendkernel/apply(foreground:background:).md)
  Creates a new image using the blend kernel and specified foreground and background images.
### Builtin Blend Kernels
- [class var clear: CIBlendKernel](ciblendkernel/clear.md)
  A blend kernel that returns a clear color.
- [class var color: CIBlendKernel](ciblendkernel/color.md)
  A blend kernel that uses the luminance values of the background with the hue and saturation values of the foreground image.
- [class var colorBurn: CIBlendKernel](ciblendkernel/colorburn.md)
  A blend kernel that darkens the background image samples to reflect the foreground image samples.
- [class var colorDodge: CIBlendKernel](ciblendkernel/colordodge.md)
  A blend kernel that brightens the background image samples to reflect the foreground image samples.
- [class var componentAdd: CIBlendKernel](ciblendkernel/componentadd.md)
  A blend kernel that adds color components to achieve a brightening effect.
- [class var componentMax: CIBlendKernel](ciblendkernel/componentmax.md)
  A blend kernel that creates an image using the maximum values of two input images.
- [class var componentMin: CIBlendKernel](ciblendkernel/componentmin.md)
  A blend kernel that creates an image using the minimum values of two input images.
- [class var componentMultiply: CIBlendKernel](ciblendkernel/componentmultiply.md)
  A blend kernel that multiplies the color components of its input images.
- [class var darken: CIBlendKernel](ciblendkernel/darken.md)
  A blend kernel that creates an image using the darker values of two input images.
- [class var darkerColor: CIBlendKernel](ciblendkernel/darkercolor.md)
  A blend kernel that creates an image using the darker color of two input images.
- [class var destination: CIBlendKernel](ciblendkernel/destination.md)
  A blend kernel that returns the background input image.
- [class var destinationAtop: CIBlendKernel](ciblendkernel/destinationatop.md)
  A blend kernel that places the background over the foreground and crops based on the visibility of the foreground.
- [class var destinationIn: CIBlendKernel](ciblendkernel/destinationin.md)
  A blend kernel that places the background over the foreground and crops based on the visibility of both.
- [class var destinationOut: CIBlendKernel](ciblendkernel/destinationout.md)
  A blend kernel that uses the background image to define what to take out of the foreground image.
- [class var destinationOver: CIBlendKernel](ciblendkernel/destinationover.md)
  A blend kernel that places the background image over the input foreground image.
- [class var difference: CIBlendKernel](ciblendkernel/difference.md)
  A blend kernel that creates an image using the difference between the background and foreground images.
- [class var divide: CIBlendKernel](ciblendkernel/divide.md)
  A blend kernel that divides the background image sample color with the foreground image sample color.
- [class var exclusion: CIBlendKernel](ciblendkernel/exclusion.md)
  A blend kernel that produces an effect similar to difference blending but with lower contrast.
- [class var exclusiveOr: CIBlendKernel](ciblendkernel/exclusiveor.md)
  A blend kernel that returns either the foreground or background image if the other contains a clear color.
- [class var hardLight: CIBlendKernel](ciblendkernel/hardlight.md)
  A blend kernel that either multiplies or screens colors, depending on the source image sample color.
- [class var hardMix: CIBlendKernel](ciblendkernel/hardmix.md)
  A blend kernel that adds two images together, setting each color channel value to either 0 or 1.
- [class var hue: CIBlendKernel](ciblendkernel/hue.md)
  A blend kernel that uses the luminance and saturation values of the background image with the hue of the foreground image.
- [class var lighten: CIBlendKernel](ciblendkernel/lighten.md)
  A blend kernel that creates an image using the lighter values of two input images.
- [class var lighterColor: CIBlendKernel](ciblendkernel/lightercolor.md)
  A blend kernel that creates an image using the lighter color of two input images.
- [class var linearBurn: CIBlendKernel](ciblendkernel/linearburn.md)
  A blend kernel that darkens the background image samples to reflect the foreground image samples while also increasing contrast.
- [class var linearDodge: CIBlendKernel](ciblendkernel/lineardodge.md)
  A blend kernel that lightens the background image samples to reflect the foreground image samples while also increasing contrast.
- [class var linearLight: CIBlendKernel](ciblendkernel/linearlight.md)
  A blend kernel that burns or dodges colors by changing brightness, depending on the blend color.
- [class var luminosity: CIBlendKernel](ciblendkernel/luminosity.md)
  A blend kernel that uses the hue and saturation of the background image with the luminance of the foreground image.
- [class var multiply: CIBlendKernel](ciblendkernel/multiply.md)
  A blend kernel that multiplies the background image sample color with the foreground image sample color.
- [class var overlay: CIBlendKernel](ciblendkernel/overlay.md)
  A blend kernel that either multiplies or screens the foreground image samples with the background image samples, depending on the background color.
- [class var pinLight: CIBlendKernel](ciblendkernel/pinlight.md)
  A blend kernel that conditionally replaces background image samples with source image samples depending on the brightness of the source image samples.
- [class var saturation: CIBlendKernel](ciblendkernel/saturation.md)
  A blend kernel that uses the luminance and hue values of the background image with the saturation of the foreground image.
- [class var screen: CIBlendKernel](ciblendkernel/screen.md)
  A blend kernel that multiplies the inverse of the foreground image samples with the inverse of the background image samples.
- [class var softLight: CIBlendKernel](ciblendkernel/softlight.md)
  A blend kernel that either darkens or lightens colors, depending on the foreground image sample color.
- [class var source: CIBlendKernel](ciblendkernel/source.md)
  A blend kernel that returns the foreground input image.
- [class var sourceAtop: CIBlendKernel](ciblendkernel/sourceatop.md)
  A blend kernel that places the foreground over the background and crops based on the visibility of the background.
- [class var sourceIn: CIBlendKernel](ciblendkernel/sourcein.md)
  A blend kernel that places the foreground over the background and crops based on the visibility of both.
- [class var sourceOut: CIBlendKernel](ciblendkernel/sourceout.md)
  A blend kernel that uses the foreground image to define what to take out of the background image.
- [class var sourceOver: CIBlendKernel](ciblendkernel/sourceover.md)
  A blend kernel that places the foreground image over the input background image.
- [class var subtract: CIBlendKernel](ciblendkernel/subtract.md)
  A blend kernel that subtracts the background image sample color from the foreground image sample color.
- [class var vividLight: CIBlendKernel](ciblendkernel/vividlight.md)
  A blend kernel that burns or dodges colors by changing contrast, depending on the blend color.
### Instance Methods
- [func apply(foreground: CIImage, background: CIImage, colorSpace: CGColorSpace) -> CIImage?](ciblendkernel/apply(foreground:background:colorspace:).md)

## Relationships

### Inherits From
- [CIColorKernel](cicolorkernel.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Writing Custom Kernels](writing-custom-kernels.md)
  Write your own custom kernels in either the Core Image Kernel Language or the Metal Shading Language.
- [class CIKernel](cikernel.md)
  A GPU-based image-processing routine used to create custom Core Image filters.
- [class CIColorKernel](cicolorkernel.md)
  A GPU-based image-processing routine that processes only the color information in images, used to create custom Core Image filters.
- [class CIWarpKernel](ciwarpkernel.md)
  A GPU-based image-processing routine that processes only the geometry information in an image, used to create custom Core Image filters.
- [class CISampler](cisampler.md)
  An object that retrieves pixel samples for processing by a filter kernel.
- [class CIFilterShape](cifiltershape.md)
  A description of the bounding shape of a filter and the domain of definition for a filter operation.
- [struct CIFormat](ciformat.md)
  Pixel data formats for image input, output, and processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciblendkernel)*