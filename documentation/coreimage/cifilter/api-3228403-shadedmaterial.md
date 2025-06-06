# shadedMaterial()

**Framework**: Core Image  
**Kind**: clm

Creates a shaded image from a height-field image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func shadedMaterial() -> any CIFilter & CIShadedMaterial
```

#### Return_value

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

![Three pictures side by side. The first photo on the left is a black image with the text Core Image in the center with the shading detail inside the white text. The center photograph of a colorful sphere. In the photo on the right, a shaded material filter is applied, resulting in the color from the center image being overlaid onto the text, creating a shiny effect on the text and giving the image the effect of becoming three-dimensional.](https://docs-assets.developer.apple.com/published/924c18fa84/rendered2x-1590529241.png)

## See Also

- [class func blendWithAlphaMask() -> any CIFilter & CIBlendWithMask](cifilter/3228272-blendwithalphamask.md)
  Blends two images by using an alpha mask image.
- [class func blendWithBlueMask() -> any CIFilter & CIBlendWithMask](cifilter/3228273-blendwithbluemask.md)
  Blends two images by using a blue mask image.
- [class func blendWithMask() -> any CIFilter & CIBlendWithMask](cifilter/3228274-blendwithmask.md)
  Blends two images by using a mask image.
- [class func blendWithRedMask() -> any CIFilter & CIBlendWithMask](cifilter/3228275-blendwithredmask.md)
  Blends two images by using a red mask image.
- [class func bloom() -> any CIFilter & CIBloom](cifilter/3228276-bloom.md)
  Adjusts an image’s colors by applying a blur effect.
- [class func comicEffect() -> any CIFilter & CIComicEffect](cifilter/3228298-comiceffect.md)
  Creates an image with a comic book effect.
- [class func coreMLModel() -> any CIFilter & CICoreMLModel](cifilter/3228305-coremlmodel.md)
  Filters an image with a Core ML model.
- [class func crystallize() -> any CIFilter & CICrystallize](cifilter/3228306-crystallize.md)
  Creates an image made with a series of colorful polygons.
- [class func depthOfField() -> any CIFilter & CIDepthOfField](cifilter/3228308-depthoffield.md)
  Simulates a depth of field effect.
- [class func edges() -> any CIFilter & CIEdges](cifilter/3228321-edges.md)
  Hilghlights edges of objects found within an image.
- [class func edgeWork() -> any CIFilter & CIEdgeWork](cifilter/3228320-edgework.md)
  Produces a black-and-white image that looks similar to a woodblock print.
- [class func gaborGradients() -> any CIFilter & CIGaborGradients](cifilter/3325508-gaborgradients.md)
  Highlights textures in an image.
- [class func gloom() -> any CIFilter & CIGloom](cifilter/3228334-gloom.md)
  Adjusts an image’s color by applying a gloom filter.
- [class func heightFieldFromMask() -> any CIFilter & CIHeightFieldFromMask](cifilter/3228337-heightfieldfrommask.md)
  Creates a realistic shaded height-field image.
- [class func hexagonalPixellate() -> any CIFilter & CIHexagonalPixellate](cifilter/3228338-hexagonalpixellate.md)
  Creates an image made of a series of colorful hexagons.
- [class func highlightShadowAdjust() -> any CIFilter & CIHighlightShadowAdjust](cifilter/3228339-highlightshadowadjust.md)
  Adjusts the highlights of colors to reduce shadows.
- [class func lineOverlay() -> any CIFilter & CILineOverlay](cifilter/3228347-lineoverlay.md)
  Creates an image that resembles a sketch of the outlines of objects.
- [class func mix() -> any CIFilter & CIMix](cifilter/3228362-mix.md)
  Blends two images together.
- [class func personSegmentation() -> any CIFilter & CIPersonSegmentation](cifilter/4401873-personsegmentation.md)
  Creates a mask where red pixels indicate areas of the image that are likely to contain a person.
- [class func pixellate() -> any CIFilter & CIPixellate](cifilter/3228393-pixellate.md)
  Enlarges the colors of the pixels to create a blurred effect.
- [class func pointillize() -> any CIFilter & CIPointillize](cifilter/3228394-pointillize.md)
  Applies a pointillize effect to an image.
- [class func saliencyMap() -> any CIFilter & CISaliencyMap](cifilter/3228399-saliencymap.md)
  Creates a saliency map from an image.
- [class func sobelGradients() -> any CIFilter & CISobelGradients](cifilter/4401876-sobelgradients.md)
  Calculates the Sobel gradients for an image.
- [class func spotColor() -> any CIFilter & CISpotColor](cifilter/3228413-spotcolor.md)
  Replaces colors of an image with specifed colors.
- [class func spotLight() -> any CIFilter & CISpotLight](cifilter/3228414-spotlight.md)
  Highlights a definined area of the image.
- [class func cannyEdgeDetector() -> any CIFilter & CICannyEdgeDetector](cifilter/4401852-cannyedgedetector.md)
  Applies the Canny edge-detection algorithm to an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/3228403-shadedmaterial)*