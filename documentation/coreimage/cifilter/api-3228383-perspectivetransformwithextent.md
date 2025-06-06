# perspectiveTransformWithExtent()

**Framework**: Core Image  
**Kind**: clm

Alters an image’s geometry to adjust the perspective while applying constraints.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func perspectiveTransformWithExtent() -> any CIFilter & CIPerspectiveTransformWithExtent
```

#### Return_value

The adjusted image.

#### Discussion

This method applies the perspective transform with extent filter to an image. The effect alters the geometry of an image to simulate the observer changing viewing position. The extent filter crops the image within the bounds specified. You can use the perspective filter to skew an image.

The perspective transform with extent filter uses the following properties:

The following code creates a filter that changes the perspective of the input image:

```swift
func perspectiveTransformWithExtent(inputImage: CIImage) -> CIImage {
    let perspectiveTransformFilter = CIFilter.perspectiveTransformWithExtent()
    perspectiveTransformFilter.inputImage = inputImage
    perspectiveTransformFilter.topLeft = CGPoint(x: 100, y: 3984)
    perspectiveTransformFilter.topRight = CGPoint(x: 3732, y: 3025)
    perspectiveTransformFilter.bottomLeft = CGPoint(x: 0, y: 500)
    perspectiveTransformFilter.bottomRight = CGPoint(x: 4032, y: 120)
    perspectiveTransformFilter.extent = CGRect(x: 0, y: 0, width: 3800, height: 3200)
    return perspectiveTransformFilter.outputImage!
}
```

![Two photographs of a large building on the corner of an intersection. The building has small windows and is made of a brick structure. The photo on the left has no modifications to size or color. In the photo on the right, a perspective transform is applied, resulting in it appearing as though the photograph was taken from a different angle.](https://docs-assets.developer.apple.com/published/b734ae69bb/rendered2x-1587583573.png)

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
- [class func perspectiveRotate() -> any CIFilter & CIPerspectiveRotate](cifilter/3325512-perspectiverotate.md)
  Rotates an image in a 3D space.
- [class func perspectiveTransform() -> any CIFilter & CIPerspectiveTransform](cifilter/3228382-perspectivetransform.md)
  Alters an image’s geometry to adjust the perspective.
- [class func straighten() -> any CIFilter & CIStraighten](cifilter/3228416-straighten.md)
  Rotates and crops an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/3228383-perspectivetransformwithextent)*