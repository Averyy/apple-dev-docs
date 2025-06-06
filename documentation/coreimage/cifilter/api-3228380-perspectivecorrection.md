# perspectiveCorrection()

**Framework**: Core Image  
**Kind**: clm

Transforms an image’s perspective.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func perspectiveCorrection() -> any CIFilter & CIPerspectiveCorrection
```

#### Return_value

The adjusted image.

#### Discussion

This method applies the perspective correction filter to an image. The effect applies a perspective correction transforming nonrectangular area in the source image to a rectangular output image.

The perspective correction filter uses the following properties:

The following code creates a filter that corrects the perspective to appear straight:

```swift
func perspectiveCorrection(inputImage: CIImage) -> CIImage {
    let perspectiveCorrectionFilter = CIFilter.perspectiveCorrection()
    perspectiveCorrectionFilter.inputImage = inputImage
    perspectiveCorrectionFilter.topRight = CGPoint(x: 0, y: 3024)
    perspectiveCorrectionFilter.topLeft = CGPoint(x: 4032, y: 3024)
    perspectiveCorrectionFilter.bottomRight = CGPoint(x: 200, y: 0)
    perspectiveCorrectionFilter.bottomLeft = CGPoint(x: 4032, y: 0)
    return perspectiveCorrectionFilter.outputImage!
}
```

![Two photographs of a large building on the corner of an intersection. The building has small windows and is made of a brick structure. The photo on the left has no modifications to size or color. In the photo on the right, a perspective correction filter is applied, resulting in the perspective of the windows appearing as if the photo was taken in the front of the building.](https://docs-assets.developer.apple.com/published/9db5c00507/rendered2x-1587583578.png)

## See Also

- [class func bicubicScaleTransform() -> any CIFilter & CIBicubicScaleTransform](cifilter/3228271-bicubicscaletransform.md)
  Produces a high-quality scaled version of an image.
- [class func edgePreserveUpsample() -> any CIFilter & CIEdgePreserveUpsample](cifilter/3228319-edgepreserveupsample.md)
  Creates a high-quality upscaled image.
- [class func keystoneCorrectionCombined() -> any CIFilter & CIKeystoneCorrectionCombined](cifilter/3325509-keystonecorrectioncombined.md)
  Adjusts the image vertically and horizontally to remove distortion.
- [class func keystoneCorrectionHorizontal() -> any CIFilter & CIKeystoneCorrectionHorizontal](cifilter/3325510-keystonecorrectionhorizontal.md)
  Horizontally adjusts an image to remove distortion.
- [class func keystoneCorrectionVertical() -> any CIFilter & CIKeystoneCorrectionVertical](cifilter/3325511-keystonecorrectionvertical.md)
  Vertically adjusts an image to remove distortion.
- [class func lanczosScaleTransform() -> any CIFilter & CILanczosScaleTransform](cifilter/3228344-lanczosscaletransform.md)
  Creates a high-quality, scaled version of a source image.
- [class func perspectiveRotate() -> any CIFilter & CIPerspectiveRotate](cifilter/3325512-perspectiverotate.md)
  Rotates an image in a 3D space.
- [class func perspectiveTransform() -> any CIFilter & CIPerspectiveTransform](cifilter/3228382-perspectivetransform.md)
  Alters an image’s geometry to adjust the perspective.
- [class func perspectiveTransformWithExtent() -> any CIFilter & CIPerspectiveTransformWithExtent](cifilter/3228383-perspectivetransformwithextent.md)
  Alters an image’s geometry to adjust the perspective while applying constraints.
- [class func straighten() -> any CIFilter & CIStraighten](cifilter/3228416-straighten.md)
  Rotates and crops an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/3228380-perspectivecorrection)*