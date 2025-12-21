# shadedMaterial()

**Framework**: Core Image  
**Kind**: method

Creates a shaded image from a height-field image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func shadedMaterial() -> any CIFilter & CIShadedMaterial
```

#### Return Value

The modified image.

#### Discussion

This method applies the shaded material filter to an image. The effect produces a shaded image from a height-field image. Areas of the height field image that have a darker shaded area produce a stronger effect. You can combine the filter with [`CIHeightFieldFromMask`](ciheightfieldfrommask.md) to produce quick shadings of masks, such as text.

The shaded material filter uses the following properties:

The following code creates a filter that results in an image containing glossy text by applying the shading image.

```swift
func shadowMaterial(inputImage: CIImage, shadeImage: CIImage) -> CIImage {
    let shadowMaterialFilter = CIFilter.shadedMaterial()
    shadowMaterialFilter.inputImage = inputImage
    shadowMaterialFilter.shadingImage = shadeImage
    shadowMaterialFilter.scale = 10
    return shadowMaterialFilter.outputImage!
}
```

![Three pictures side by side. The first photo on the left is a black image with the text Core Image in the center with the shading detail inside the white text. The center photograph of a colorful sphere. In the photo on the right, a shaded material filter is applied, resulting in the color from the center image being overlaid onto the text, creating a shiny effect on the text and giving the image the effect of becoming three-dimensional.](https://docs-assets.developer.apple.com/published/b4fcb61f14dbbf9386865921e50ee6ef/media-3600005%402x.png)

## See Also

- [class func blendWithAlphaMask() -> any CIFilter & CIBlendWithMask](cifilter-swift.class/blendwithalphamask.md)
  Blends two images by using an alpha mask image.
- [class func blendWithBlueMask() -> any CIFilter & CIBlendWithMask](cifilter-swift.class/blendwithbluemask.md)
  Blends two images by using a blue mask image.
- [class func blendWithMask() -> any CIFilter & CIBlendWithMask](cifilter-swift.class/blendwithmask.md)
  Blends two images by using a mask image.
- [class func blendWithRedMask() -> any CIFilter & CIBlendWithMask](cifilter-swift.class/blendwithredmask.md)
  Blends two images by using a red mask image.
- [class func bloom() -> any CIFilter & CIBloom](cifilter-swift.class/bloom.md)
  Adjusts an image’s colors by applying a blur effect.
- [class func cannyEdgeDetector() -> any CIFilter & CICannyEdgeDetector](cifilter-swift.class/cannyedgedetector.md)
  Applies the Canny edge-detection algorithm to an image.
- [class func comicEffect() -> any CIFilter & CIComicEffect](cifilter-swift.class/comiceffect.md)
  Creates an image with a comic book effect.
- [class func coreMLModel() -> any CIFilter & CICoreMLModel](cifilter-swift.class/coremlmodel.md)
  Filters an image with a Core ML model.
- [class func crystallize() -> any CIFilter & CICrystallize](cifilter-swift.class/crystallize.md)
  Creates an image made with a series of colorful polygons.
- [class func depthOfField() -> any CIFilter & CIDepthOfField](cifilter-swift.class/depthoffield.md)
  Simulates a depth of field effect.
- [class func edges() -> any CIFilter & CIEdges](cifilter-swift.class/edges.md)
  Hilghlights edges of objects found within an image.
- [class func edgeWork() -> any CIFilter & CIEdgeWork](cifilter-swift.class/edgework.md)
  Produces a black-and-white image that looks similar to a woodblock print.
- [class func gaborGradients() -> any CIFilter & CIGaborGradients](cifilter-swift.class/gaborgradients.md)
  Highlights textures in an image.
- [class func gloom() -> any CIFilter & CIGloom](cifilter-swift.class/gloom.md)
  Adjusts an image’s color by applying a gloom filter.
- [class func heightFieldFromMask() -> any CIFilter & CIHeightFieldFromMask](cifilter-swift.class/heightfieldfrommask.md)
  Creates a realistic shaded height-field image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/shadedmaterial())*