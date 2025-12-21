# pointillize()

**Framework**: Core Image  
**Kind**: method

Applies a pointillize effect to an image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func pointillize() -> any CIFilter & CIPointillize
```

#### Return Value

A [`CIImage`](ciimage.md) containing the pointillized image.

#### Discussion

This filter applies a pointillize effect to an image. The effect generates an output image made of small, single-color, circular points distributed on a randomly perturbed grid.

The pointillize filter uses the following properties:

The following code applies the pointillize filter with a radius of 40 pixels.

```swift
func pointillize(inputImage: CIImage) -> CIImage {
    let pointillizeFilter = CIFilter.pointillize()
    pointillizeFilter.inputImage = inputImage
    pointillizeFilter.radius = 40
    pointillizeFilter.center = CGPoint(x: 0,y: 0)
    return pointillizeFilter.outputImage!
}
```

![Two images arranged horizontally. The left image contains a photo of a colorful bunch of flowers. The right image shows the result of applying the pointillize filter. The image is made of small circular points. The color of each point matches up with the color at the location of the dot in the original image.](https://docs-assets.developer.apple.com/published/70e93800225aff907168a23ef0f4d7e6/media-4333706%402x.png)

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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/pointillize())*