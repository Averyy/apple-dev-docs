# pixellate()

**Framework**: Core Image  
**Kind**: clm

Enlarges the colors of the pixels to create a blurred effect.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func pixellate() -> any CIFilter & CIPixellate
```

#### Return_value

The modified image.

#### Discussion

This method applies the pixelate filter to an image. The effect produces a result by mapping the image to colored squares with colors defined by the pixels of the input image.

The pixelate filter uses the following properties:

The following code creates a filter that results in a distorted image made of squares:

```swift
func pixelate(inputImage: CIImage) -> CIImage {
    let pixelate = CIFilter.pixellate()
    pixelate.inputImage = inputImage
    pixelate.center = CGPoint(x: 150, y: 150)
    pixelate.scale = 30
    return pixelate.outputImage!
}
```

![Two pictures of a pink flower surrounded by foliage. The photo on the left shows a single flower photographed close up, in focus, with good light and no effects. In the photo on the right, the pixelate filter is applied, resulting in a distorted image made of small squares with less detail.](https://docs-assets.developer.apple.com/published/3a173c3426/rendered2x-1590529251.png)

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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/3228393-pixellate)*