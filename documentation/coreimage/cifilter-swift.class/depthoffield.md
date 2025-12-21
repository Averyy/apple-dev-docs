# depthOfField()

**Framework**: Core Image  
**Kind**: method

Simulates a depth of field effect.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func depthOfField() -> any CIFilter & CIDepthOfField
```

#### Return Value

The modified image.

#### Discussion

This method applies the depth of field filter to an image. The effect simulates changing the focus of the camera before taking a photograph.

The depth of field filter uses the following properties:

The following code creates a filter that results in the center cilantro being in focus while gradually blurring to the top and bottom of the image:

```swift
func depthOfField(inputImage: CIImage) -> CIImage {
    let depthOfFieldFilter = CIFilter.depthOfField()
    depthOfFieldFilter.inputImage = inputImage
    depthOfFieldFilter.radius = 5
    depthOfFieldFilter.point0 = CGPoint(x: 2349, y: 846)
    depthOfFieldFilter.point1 = CGPoint(x: 571, y: 3121)
    depthOfFieldFilter.unsharpMaskRadius = 7
    depthOfFieldFilter.unsharpMaskIntensity = 10
    return depthOfFieldFilter.outputImage!
}
```

![Two photographs of a pile of cilantro. The photo on the left is clear and crisp with good lighting. In the photo on the right, a depth of field filter is applied, resulting in the cilantro in the image’s periphery becoming blurred while the center remains in focus.](https://docs-assets.developer.apple.com/published/84d361393ec043526e977893a93da4b3/media-3599997%402x.png)

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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/depthoffield())*