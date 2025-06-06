# CIEdgePreserveUpsample

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure an edge preserve upsample filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIEdgePreserveUpsample
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](ciedgepreserveupsample/3228237-inputimage.md)
  The image to use as an input image.
- [var lumaSigma: Float](ciedgepreserveupsample/3228238-lumasigma.md)
  A value that specifies the influence of the input image’s luma information on the upsampling operation.
- [var smallImage: CIImage?](ciedgepreserveupsample/3228239-smallimage.md)
  The image that the filter upsamples.
- [var spatialSigma: Float](ciedgepreserveupsample/3228240-spatialsigma.md)
  A value that specifies the influence of the input image’s spatial information on the upsampling operation.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func edgePreserveUpsample() -> any CIFilter & CIEdgePreserveUpsample](cifilter/3228319-edgepreserveupsample.md)
  Creates a high-quality upscaled image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciedgepreserveupsample)*