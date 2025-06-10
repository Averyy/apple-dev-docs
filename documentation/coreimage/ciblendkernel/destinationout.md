# destinationOut

**Framework**: Core Image  
**Kind**: property

A blend kernel that uses the background image to define what to take out of the foreground image.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
class var destinationOut: CIBlendKernel { get }
```

#### Discussion

![The result of using the destination out blend kernel (background image is top left, foreground image is bottom left)](https://docs-assets.developer.apple.com/published/11d7d7d3c21f289ec8e4cb1b7a6d49ed/media-2926862%402x.png)

## See Also

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
- [class var destinationOver: CIBlendKernel](ciblendkernel/destinationover.md)
  A blend kernel that places the background image over the input foreground image.
- [class var difference: CIBlendKernel](ciblendkernel/difference.md)
  A blend kernel that creates an image using the difference between the background and foreground images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciblendkernel/destinationout)*