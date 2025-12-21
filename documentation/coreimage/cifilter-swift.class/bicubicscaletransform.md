# bicubicScaleTransform()

**Framework**: Core Image  
**Kind**: method

Produces a high-quality scaled version of an image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func bicubicScaleTransform() -> any CIFilter & CIBicubicScaleTransform
```

#### Return Value

The adjusted image.

#### Discussion

This method applies the bicubic scale transform filter to an image. The effect produces a high-quality, scaled version of the input image. The parameters of `B` and `C` determine the sharpness and softness of the resampling.

The bicubic scale transform filter uses the following properties:

The following code creates a filter that results in the image becoming square:

```swift
func bicubicScale(inputImage: CIImage) -> CIImage {
    let bicubicScaleFilter = CIFilter.bicubicScaleTransform()
    bicubicScaleFilter.inputImage = inputImage
    bicubicScaleFilter.aspectRatio = 0.7
    bicubicScaleFilter.parameterB = 1
    bicubicScaleFilter.parameterC = 0.75
    return bicubicScaleFilter.outputImage!
}
```

![Two photographs of a large building on the corner of an intersection. The building has small windows and is made of a brick structure. The photo on the left has no modifications to size or color. In the photo on the right, a bicubic scale transform filter is applied, resulting in a square image.](https://docs-assets.developer.apple.com/published/f16ce1fe17c3c42f0fd7ed3209dc27e0/media-3582224%402x.png)

## See Also

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
- [class func perspectiveTransform() -> any CIFilter & CIPerspectiveTransform](cifilter-swift.class/perspectivetransform.md)
  Alters an image’s geometry to adjust the perspective.
- [class func perspectiveTransformWithExtent() -> any CIFilter & CIPerspectiveTransformWithExtent](cifilter-swift.class/perspectivetransformwithextent.md)
  Alters an image’s geometry to adjust the perspective while applying constraints.
- [class func straighten() -> any CIFilter & CIStraighten](cifilter-swift.class/straighten.md)
  Rotates and crops an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/bicubicscaletransform())*