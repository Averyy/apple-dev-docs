# edgeWork()

**Framework**: Core Image  
**Kind**: method

Produces a black-and-white image that looks similar to a woodblock print.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func edgeWork() -> any CIFilter & CIEdgeWork
```

#### Return Value

The modified image.

#### Discussion

This method applies the edge work filter to an image. The effect creates a stylized black-and-white rendition of the image that looks similar to a woodblock print.

The edge work filter uses the following properties:

The following code creates a filter that results in a monochrome image with the edges of objects highlighted:

```swift
func edgeWork(inputImage: CIImage) -> CIImage {
    let edgeWorkFilter = CIFilter.edgeWork()
    edgeWorkFilter.inputImage = inputImage
    edgeWorkFilter.radius = 4
    return edgeWorkFilter.outputImage!
}
```

![Two pictures of a pink flower surrounded by foliage. The photo on the left shows a single flower photographed close up, in focus, with good light and no effects. In the photo on the right, an edge work filter is applied, resulting in the image becoming monochrome with the outlines of objects black and the flower white.](https://docs-assets.developer.apple.com/published/a9c62cc9c3538dce5b7502c1e039c879/media-3600010%402x.png)

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
- [class func gaborGradients() -> any CIFilter & CIGaborGradients](cifilter-swift.class/gaborgradients.md)
  Highlights textures in an image.
- [class func gloom() -> any CIFilter & CIGloom](cifilter-swift.class/gloom.md)
  Adjusts an image’s color by applying a gloom filter.
- [class func heightFieldFromMask() -> any CIFilter & CIHeightFieldFromMask](cifilter-swift.class/heightfieldfrommask.md)
  Creates a realistic shaded height-field image.
- [class func hexagonalPixellate() -> any CIFilter & CIHexagonalPixellate](cifilter-swift.class/hexagonalpixellate.md)
  Creates an image made of a series of colorful hexagons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/edgework())*