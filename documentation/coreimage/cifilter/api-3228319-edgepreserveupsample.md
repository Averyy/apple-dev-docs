# edgePreserveUpsample()

**Framework**: Core Image  
**Kind**: clm

Creates a high-quality upscaled image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func edgePreserveUpsample() -> any CIFilter & CIEdgePreserveUpsample
```

#### Return_value

The adjusted image.

#### Discussion

This method applies the edge preserve upsample filter to an image. The effect upsamples a small input image to be the size of the scale image using the luminance of the input image to preserve detail.

The edge preserve upsample filter uses the following properties:

The following code creates a filter that upscales the smaller image to the size of the scale image:

```swift
func edgePerserveUp(inputImage: CIImage, smallImage: CIImage) -> CIImage {
    let edgePerserveUpFilter = CIFilter.edgePreserveUpsample()
    edgePerserveUpFilter.inputImage = inputImage
    edgePerserveUpFilter.smallImage = smallImage
    edgePerserveUpFilter.spatialSigma = 5
    edgePerserveUpFilter.lumaSigma = 0.15
    return edgePerserveUpFilter.outputImage!
}
```

![Two photographs of two large buildings with a clear sky in the background. The buildings have small windows with a lot of horizonal and vertical details. The photo on the left has no modifications to size or color. In the photo on the right, an edge preserve upsample filter is applied, resulting in a scaled-up, larger image.](https://docs-assets.developer.apple.com/published/2a09df33a9/rendered2x-1587583557.png)

## See Also

- [class func bicubicScaleTransform() -> any CIFilter & CIBicubicScaleTransform](cifilter/3228271-bicubicscaletransform.md)
  Produces a high-quality scaled version of an image.
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
- [class func perspectiveTransformWithExtent() -> any CIFilter & CIPerspectiveTransformWithExtent](cifilter/3228383-perspectivetransformwithextent.md)
  Alters an image’s geometry to adjust the perspective while applying constraints.
- [class func straighten() -> any CIFilter & CIStraighten](cifilter/3228416-straighten.md)
  Rotates and crops an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/3228319-edgepreserveupsample)*