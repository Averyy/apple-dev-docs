# cannyEdgeDetector()

**Framework**: Core Image  
**Kind**: method

Applies the Canny edge-detection algorithm to an image.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class func cannyEdgeDetector() -> any CIFilter & CICannyEdgeDetector
```

#### Return Value

A [`CIImage`](ciimage.md) with the detected edges.

#### Discussion

This filter performs a Canny edge-detection on the input image, producing a black-and-white image with the detected edges. White pixels indicate an edge, and black pixels indicate no edge.

The Canny edge-detection filter uses the following properties:

The following code applies Canny edge-detection to an image:

```swift
func cannyEdgeDetector(inputImage: CIImage) -> CIImage {
    let filter = CIFilter.cannyEdgeDetector()
    filter.inputImage = inputImage
    filter.gaussianSigma = 5
    filter.perceptual = false
    filter.thresholdLow = 0.02
    filter.thresholdHigh = 0.05
    filter.hysteresisPasses = 1
    return filter.outputImage!
}
```

![Two images arranged horizontally. The left image contains a palm tree against a clear sky. The right image contains the result of running the Canny edge-detection filter. The result image contains the outline of the palm tree.](https://docs-assets.developer.apple.com/published/167f41db69e548d6940d775342c2072c/media-4407284%402x.png)

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
- [class func hexagonalPixellate() -> any CIFilter & CIHexagonalPixellate](cifilter-swift.class/hexagonalpixellate.md)
  Creates an image made of a series of colorful hexagons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/cannyedgedetector())*