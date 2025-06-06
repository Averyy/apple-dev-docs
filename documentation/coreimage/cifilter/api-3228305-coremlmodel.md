# coreMLModel()

**Framework**: Core Image  
**Kind**: clm

Filters an image with a Core ML model.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func coreMLModel() -> any CIFilter & CICoreMLModel
```

#### Return_value

The modified image.

#### Discussion

This method applies the Core ML model filter to an image. The effect filters the image using a trained Core ML model to produce the result. Specifying the head index allows you to produce a result from various components of a multiheaded coreML model.

The Core ML model filter uses the following properties:

The following code creates a filter that results in the flowers appearing to be glass panes:

```swift
func coreML(inputImage: CIImage) -> CIImage {
    let coreMLFilter = CIFilter.coreMLModel()
    let model = GlassModel().model
    coreMLFilter.inputImage = inputImage
    coreMLFilter.headIndex = 0
    coreMLFilter.softmaxNormalization = false
    return coreMLFilter.outputImage!
}
```

![Two photographs of colorful flowers. The photo on the left is clear and crisp with good lighting. In the photo on the right, a Core ML model filter is applied, and the image flowers appear to be made of colorful glass panes.](https://docs-assets.developer.apple.com/published/3234697665/rendered2x-1590529264.png)

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
- [class func shadedMaterial() -> any CIFilter & CIShadedMaterial](cifilter/3228403-shadedmaterial.md)
  Creates a shaded image from a height-field image.
- [class func sobelGradients() -> any CIFilter & CISobelGradients](cifilter/4401876-sobelgradients.md)
  Calculates the Sobel gradients for an image.
- [class func spotColor() -> any CIFilter & CISpotColor](cifilter/3228413-spotcolor.md)
  Replaces colors of an image with specifed colors.
- [class func spotLight() -> any CIFilter & CISpotLight](cifilter/3228414-spotlight.md)
  Highlights a definined area of the image.
- [class func cannyEdgeDetector() -> any CIFilter & CICannyEdgeDetector](cifilter/4401852-cannyedgedetector.md)
  Applies the Canny edge-detection algorithm to an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/3228305-coremlmodel)*