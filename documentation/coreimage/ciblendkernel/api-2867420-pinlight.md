# pinLight

**Framework**: Core Image  
**Kind**: cldata

A blend kernel that conditionally replaces background image samples with source image samples depending on the brightness of the source image samples.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class var pinLight: CIBlendKernel { get }
```

#### Discussion

![The result of using the pin light blend kernel (background image is top left, foreground image is bottom left)](https://docs-assets.developer.apple.com/published/c24b83f7af/e9885a50-1d5e-422f-b8c8-3d4cdd3943e6.png)

## See Also

- [class var clear: CIBlendKernel](ciblendkernel/2867388-clear.md)
  A blend kernel that returns a clear color.
- [class var color: CIBlendKernel](ciblendkernel/2867350-color.md)
  A blend kernel that uses the luminance values of the background with the hue and saturation values of the foreground image.
- [class var colorBurn: CIBlendKernel](ciblendkernel/2867391-colorburn.md)
  A blend kernel that darkens the background image samples to reflect the foreground image samples.
- [class var colorDodge: CIBlendKernel](ciblendkernel/2867417-colordodge.md)
  A blend kernel that brightens the background image samples to reflect the foreground image samples.
- [class var componentAdd: CIBlendKernel](ciblendkernel/2867384-componentadd.md)
  A blend kernel that adds color components to achieve a brightening effect.
- [class var componentMax: CIBlendKernel](ciblendkernel/2867433-componentmax.md)
  A blend kernel that creates an image using the maximum values of two input images.
- [class var componentMin: CIBlendKernel](ciblendkernel/2867425-componentmin.md)
  A blend kernel that creates an image using the minimum values of two input images.
- [class var componentMultiply: CIBlendKernel](ciblendkernel/2867406-componentmultiply.md)
  A blend kernel that multiplies the color components of its input images.
- [class var darken: CIBlendKernel](ciblendkernel/2867348-darken.md)
  A blend kernel that creates an image using the darker values of two input images.
- [class var darkerColor: CIBlendKernel](ciblendkernel/2867351-darkercolor.md)
  A blend kernel that creates an image using the darker color of two input images.
- [class var destination: CIBlendKernel](ciblendkernel/2867422-destination.md)
  A blend kernel that returns the background input image.
- [class var destinationAtop: CIBlendKernel](ciblendkernel/2867385-destinationatop.md)
  A blend kernel that places the background over the foreground and crops based on the visibility of the foreground.
- [class var destinationIn: CIBlendKernel](ciblendkernel/2867352-destinationin.md)
  A blend kernel that places the background over the foreground and crops based on the visibility of both.
- [class var destinationOut: CIBlendKernel](ciblendkernel/2867368-destinationout.md)
  A blend kernel that uses the background image to define what to take out of the foreground image.
- [class var destinationOver: CIBlendKernel](ciblendkernel/2867432-destinationover.md)
  A blend kernel that places the background image over the input foreground image.
- [class var difference: CIBlendKernel](ciblendkernel/2867416-difference.md)
  A blend kernel that creates an image using the difference between the background and foreground images.
- [class var divide: CIBlendKernel](ciblendkernel/2867410-divide.md)
  A blend kernel that divides the background image sample color with the foreground image sample color.
- [class var exclusion: CIBlendKernel](ciblendkernel/2867343-exclusion.md)
  A blend kernel that produces an effect similar to difference blending but with lower contrast. 
- [class var exclusiveOr: CIBlendKernel](ciblendkernel/2867421-exclusiveor.md)
  A blend kernel that returns either the foreground or background image if the other contains a clear color.
- [class var hardLight: CIBlendKernel](ciblendkernel/2867418-hardlight.md)
  A blend kernel that either multiplies or screens colors, depending on the source image sample color.
- [class var hardMix: CIBlendKernel](ciblendkernel/2867347-hardmix.md)
  A blend kernel that adds two images together, setting each color channel value to either 0 or 1.
- [class var hue: CIBlendKernel](ciblendkernel/2867408-hue.md)
  A blend kernel that uses the luminance and saturation values of the background image with the hue of the foreground image.
- [class var lighten: CIBlendKernel](ciblendkernel/2867424-lighten.md)
  A blend kernel that creates an image using the lighter values of two input images.
- [class var lighterColor: CIBlendKernel](ciblendkernel/2867427-lightercolor.md)
  A blend kernel that creates an image using the lighter color of two input images.
- [class var linearBurn: CIBlendKernel](ciblendkernel/2867409-linearburn.md)
  A blend kernel that darkens the background image samples to reflect the foreground image samples while also increasing contrast.
- [class var linearDodge: CIBlendKernel](ciblendkernel/2867354-lineardodge.md)
  A blend kernel that lightens the background image samples to reflect the foreground image samples while also increasing contrast.
- [class var linearLight: CIBlendKernel](ciblendkernel/2867435-linearlight.md)
  A blend kernel that burns or dodges colors by changing brightness, depending on the blend color. 
- [class var luminosity: CIBlendKernel](ciblendkernel/2867423-luminosity.md)
  A blend kernel that uses the hue and saturation of the background image with the luminance of the foreground image.
- [class var multiply: CIBlendKernel](ciblendkernel/2867419-multiply.md)
  A blend kernel that multiplies the background image sample color with the foreground image sample color.
- [class var overlay: CIBlendKernel](ciblendkernel/2867411-overlay.md)
  A blend kernel that either multiplies or screens the foreground image samples with the background image samples, depending on the background color.
- [class var saturation: CIBlendKernel](ciblendkernel/2867431-saturation.md)
  A blend kernel that uses the luminance and hue values of the background image with the saturation of the foreground image.
- [class var screen: CIBlendKernel](ciblendkernel/2867356-screen.md)
  A blend kernel that multiplies the inverse of the foreground image samples with the inverse of the background image samples.
- [class var softLight: CIBlendKernel](ciblendkernel/2867434-softlight.md)
  A blend kernel that either darkens or lightens colors, depending on the foreground image sample color.
- [class var source: CIBlendKernel](ciblendkernel/2867407-source.md)
  A blend kernel that returns the foreground input image.
- [class var sourceAtop: CIBlendKernel](ciblendkernel/2867357-sourceatop.md)
  A blend kernel that places the foreground over the background and crops based on the visibility of the background.
- [class var sourceIn: CIBlendKernel](ciblendkernel/2867428-sourcein.md)
  A blend kernel that places the foreground over the background and crops based on the visibility of both.
- [class var sourceOut: CIBlendKernel](ciblendkernel/2867415-sourceout.md)
  A blend kernel that uses the foreground image to define what to take out of the background image.
- [class var sourceOver: CIBlendKernel](ciblendkernel/2867413-sourceover.md)
  A blend kernel that places the foreground image over the input background image.
- [class var subtract: CIBlendKernel](ciblendkernel/2867370-subtract.md)
  A blend kernel that subtracts the background image sample color from the foreground image sample color.
- [class var vividLight: CIBlendKernel](ciblendkernel/2867358-vividlight.md)
  A blend kernel that burns or dodges colors by changing contrast, depending on the blend color. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciblendkernel/2867420-pinlight)*