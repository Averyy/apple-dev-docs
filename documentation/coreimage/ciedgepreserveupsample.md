# CIEdgePreserveUpsample

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure an edge preserve upsample filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIEdgePreserveUpsample : CIFilterProtocol
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](ciedgepreserveupsample/inputimage.md)
  The image to use as an input image.
- [var lumaSigma: Float](ciedgepreserveupsample/lumasigma.md)
  A value that specifies the influence of the input image’s luma information on the upsampling operation.
- [var smallImage: CIImage?](ciedgepreserveupsample/smallimage.md)
  The image that the filter upsamples.
- [var spatialSigma: Float](ciedgepreserveupsample/spatialsigma.md)
  A value that specifies the influence of the input image’s spatial information on the upsampling operation.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func edgePreserveUpsample() -> any CIFilter & CIEdgePreserveUpsample](cifilter-swift.class/edgepreserveupsample.md)
  Creates a high-quality upscaled image.
- [protocol CIBicubicScaleTransform](cibicubicscaletransform.md)
  The properties you use to configure a bicubic scale transform filter.
- [protocol CIFourCoordinateGeometryFilter](cifourcoordinategeometryfilter.md)
  The properties you use to configure a geometry adjustment filters that requires four coordinates.
- [protocol CIKeystoneCorrectionCombined](cikeystonecorrectioncombined.md)
  The properties you use to configure a keystone correction combined filter.
- [protocol CIKeystoneCorrectionHorizontal](cikeystonecorrectionhorizontal.md)
  The properties you use to configure a keystone correction horizontal filter.
- [protocol CIKeystoneCorrectionVertical](cikeystonecorrectionvertical.md)
  The properties you use to configure a keystone correction vertical filter.
- [protocol CILanczosScaleTransform](cilanczosscaletransform.md)
  The properties you use to configure a Lanczos scale transform filter.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciedgepreserveupsample)*