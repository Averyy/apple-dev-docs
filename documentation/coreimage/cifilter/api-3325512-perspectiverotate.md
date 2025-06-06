# perspectiveRotate()

**Framework**: Core Image  
**Kind**: clm

Rotates an image in a 3D space.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func perspectiveRotate() -> any CIFilter & CIPerspectiveRotate
```

#### Return_value

The adjusted image.

#### Discussion

This method applies the perspective rotate filter to an image. The effect rotates the image in 3D space to simulate the observer changing viewing position.

The perspective rotate filter uses the following properties:

The following code creates a filter that rotates the image:

```swift
func perspectiveRotate(inputImage: CIImage) -> CIImage {
    let perspectiveRotateFilter = CIFilter.perspectiveRotate()
    perspectiveRotateFilter.inputImage = inputImage
    perspectiveRotateFilter.pitch = 0
    perspectiveRotateFilter.yaw = 0.1
    perspectiveRotateFilter.roll = 0.3
    perspectiveRotateFilter.focalLength = 18
    return perspectiveRotateFilter.outputImage!
}
```

![Two photographs of a large building on the corner of an intersection. The building has small windows and is made of a brick structure. The photo on the left has no modifications to size or color. In the photo on the right, a perspective rotate filter is applied, resulting in the the image becoming smaller and rotated.](https://docs-assets.developer.apple.com/published/583ed74873/rendered2x-1587583563.png)

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
- [class func perspectiveCorrection() -> any CIFilter & CIPerspectiveCorrection](cifilter/3228380-perspectivecorrection.md)
  Transforms an image’s perspective.
- [class func perspectiveTransform() -> any CIFilter & CIPerspectiveTransform](cifilter/3228382-perspectivetransform.md)
  Alters an image’s geometry to adjust the perspective.
- [class func perspectiveTransformWithExtent() -> any CIFilter & CIPerspectiveTransformWithExtent](cifilter/3228383-perspectivetransformwithextent.md)
  Alters an image’s geometry to adjust the perspective while applying constraints.
- [class func straighten() -> any CIFilter & CIStraighten](cifilter/3228416-straighten.md)
  Rotates and crops an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/3325512-perspectiverotate)*