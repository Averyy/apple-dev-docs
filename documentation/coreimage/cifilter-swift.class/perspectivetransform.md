# perspectiveTransform()

**Framework**: Core Image  
**Kind**: method

Alters an image’s geometry to adjust the perspective.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func perspectiveTransform() -> any CIFilter & CIPerspectiveTransform
```

#### Return Value

The adjusted image.

#### Discussion

This method applies the perspective transform filter to an image. The effect alters the geometry of an image to simulate the observer changing viewing position. You can use the perspective filter to skew an image.

The perspective transform filter uses the following properties:

The following code creates a filter that changes the perspective of the input image:

```swift
func perspectiveTransform(inputImage: CIImage) -> CIImage {
    let perspectiveTransformFilter = CIFilter.perspectiveTransform()
    perspectiveTransformFilter.inputImage = inputImage
    perspectiveTransformFilter.topLeft = CGPoint(x: 100, y: 3984)
    perspectiveTransformFilter.topRight = CGPoint(x: 3732, y: 3025)
    perspectiveTransformFilter.bottomLeft = CGPoint(x: 0, y: 500)
    perspectiveTransformFilter.bottomRight = CGPoint(x: 4032, y: 120)
    return perspectiveTransformFilter.outputImage!
}
```

![Two photographs of a large building on the corner of an intersection. The building has small windows and is made of a brick structure. The photo on the left has no modifications to size or color. In the photo on the right, a perspective transform is applied, resulting in it appearing as though the photograph was taken from a different angle.](https://docs-assets.developer.apple.com/published/5dd78a188cc1a50357c4eba0a6e6d012/media-3582227%402x.png)

## See Also

- [class func bicubicScaleTransform() -> any CIFilter & CIBicubicScaleTransform](cifilter-swift.class/bicubicscaletransform.md)
  Produces a high-quality scaled version of an image.
- [class func edgePreserveUpsample() -> any CIFilter & CIEdgePreserveUpsample](cifilter-swift.class/edgepreserveupsample.md)
  Creates a high-quality upscaled image.
- [class func keystoneCorrectionCombined() -> any CIFilter & CIKeystoneCorrectionCombined](cifilter-swift.class/keystonecorrectioncombined.md)
  Adjusts the image vertically and horizontally to remove distortion.
- [class func keystoneCorrectionHorizontal() -> any CIFilter & CIKeystoneCorrectionHorizontal](cifilter-swift.class/keystonecorrectionhorizontal.md)
  Horizontally adjusts an image to remove distortion.
- [class func keystoneCorrectionVertical() -> any CIFilter & CIKeystoneCorrectionVertical](cifilter-swift.class/keystonecorrectionvertical.md)
  Vertically adjusts an image to remove distortion.
- [class func lanczosScaleTransform() -> any CIFilter & CILanczosScaleTransform](cifilter-swift.class/lanczosscaletransform.md)
  Creates a high-quality, scaled version of a source image.
- [class func perspectiveCorrection() -> any CIFilter & CIPerspectiveCorrection](cifilter-swift.class/perspectivecorrection.md)
  Transforms an image’s perspective.
- [class func perspectiveRotate() -> any CIFilter & CIPerspectiveRotate](cifilter-swift.class/perspectiverotate.md)
  Rotates an image in a 3D space.
- [class func perspectiveTransformWithExtent() -> any CIFilter & CIPerspectiveTransformWithExtent](cifilter-swift.class/perspectivetransformwithextent.md)
  Alters an image’s geometry to adjust the perspective while applying constraints.
- [class func straighten() -> any CIFilter & CIStraighten](cifilter-swift.class/straighten.md)
  Rotates and crops an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/perspectivetransform())*