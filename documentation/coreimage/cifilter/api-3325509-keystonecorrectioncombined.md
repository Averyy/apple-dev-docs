# keystoneCorrectionCombined()

**Framework**: Core Image  
**Kind**: clm

Adjusts the image vertically and horizontally to remove distortion.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func keystoneCorrectionCombined() -> any CIFilter & CIKeystoneCorrectionCombined
```

#### Return_value

The adjusted image.

#### Discussion

This method applies the keystone correction combined filter to an image. The effect applies a combined set of horizontal and vertical guides to adjust the shape of the input image. This effect is commonly used when cropping an image to correct distortion. In the figure below, both vertical and horizontal adjustments are made, resulting in a trapezoid-shaped image.

The keystone correction filter uses the following properties:

The following code creates a filter that distorts the image:

```swift
func keystoneCorrectionCombined(inputImage: CIImage) -> CIImage {
    let keystoneCorrect = CIFilter.keystoneCorrectionCombined()
    keystoneCorrect.inputImage = inputImage
    keystoneCorrect.topLeft = CGPoint(x: 0, y: 2448)
    keystoneCorrect.topRight = CGPoint(x: 3164, y: 2248)
    keystoneCorrect.bottomLeft = CGPoint(x: 0, y: 0)
    keystoneCorrect.bottomRight = CGPoint(x: 3164, y: 150)
    keystoneCorrect.focalLength = 35
    return keystoneCorrect.outputImage!
}
```

![Two photographs of a large building on the corner of an intersection. The building has small windows and is made of a brick structure. The photo on the left has no modifications to size or color. In the photo on the right, a keystone correction combined filter is applied, distorting the rectangular image to become a trapezoid.](https://docs-assets.developer.apple.com/published/6f2fff4986/rendered2x-1587583562.png)

## See Also

- [class func bicubicScaleTransform() -> any CIFilter & CIBicubicScaleTransform](cifilter/3228271-bicubicscaletransform.md)
  Produces a high-quality scaled version of an image.
- [class func edgePreserveUpsample() -> any CIFilter & CIEdgePreserveUpsample](cifilter/3228319-edgepreserveupsample.md)
  Creates a high-quality upscaled image.
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
- [class func perspectiveTransformWithExtent() -> any CIFilter & CIPerspectiveTransformWithExtent](cifilter/3228383-perspectivetransformwithextent.md)
  Alters an image’s geometry to adjust the perspective while applying constraints.
- [class func straighten() -> any CIFilter & CIStraighten](cifilter/3228416-straighten.md)
  Rotates and crops an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/3325509-keystonecorrectioncombined)*