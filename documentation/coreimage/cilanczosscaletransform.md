# CILanczosScaleTransform

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a Lanczos scale transform filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CILanczosScaleTransform : CIFilterProtocol
```

## Topics

### Instance Properties
- [var aspectRatio: Float](cilanczosscaletransform/aspectratio.md)
  The additional horizontal scaling factor to use on the image.
- [var inputImage: CIImage?](cilanczosscaletransform/inputimage.md)
  The image to use as an input image.
- [var scale: Float](cilanczosscaletransform/scale.md)
  The scaling factor to use on the image.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func lanczosScaleTransform() -> any CIFilter & CILanczosScaleTransform](cifilter-swift.class/lanczosscaletransform.md)
  Creates a high-quality, scaled version of a source image.
- [protocol CIBicubicScaleTransform](cibicubicscaletransform.md)
  The properties you use to configure a bicubic scale transform filter.
- [protocol CIEdgePreserveUpsample](ciedgepreserveupsample.md)
  The properties you use to configure an edge preserve upsample filter.
- [protocol CIFourCoordinateGeometryFilter](cifourcoordinategeometryfilter.md)
  The properties you use to configure a geometry adjustment filters that requires four coordinates.
- [protocol CIKeystoneCorrectionCombined](cikeystonecorrectioncombined.md)
  The properties you use to configure a keystone correction combined filter.
- [protocol CIKeystoneCorrectionHorizontal](cikeystonecorrectionhorizontal.md)
  The properties you use to configure a keystone correction horizontal filter.
- [protocol CIKeystoneCorrectionVertical](cikeystonecorrectionvertical.md)
  The properties you use to configure a keystone correction vertical filter.
- [protocol CIPerspectiveCorrection](ciperspectivecorrection.md)
  The properties you use to configure a perspective correction filter.
- [protocol CIPerspectiveRotate](ciperspectiverotate.md)
  The properties you use to configure a perspective rotate filter.
- [protocol CIPerspectiveTransform](ciperspectivetransform.md)
  The properties you use to configure a perspective transform filter.
- [protocol CIPerspectiveTransformWithExtent](ciperspectivetransformwithextent.md)
  The properties you use to configure a perspective transform with extent filter.
- [protocol CIStraighten](cistraighten.md)
  The properties you use to configure a straighten filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cilanczosscaletransform)*