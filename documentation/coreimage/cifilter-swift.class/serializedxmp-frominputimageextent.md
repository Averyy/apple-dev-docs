# serializedXMP(from:inputImageExtent:)

**Framework**: Core Image  
**Kind**: method

Serializes filter parameters into XMP form that is suitable for embedding in an image.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class func serializedXMP(from filters: [CIFilter], inputImageExtent extent: CGRect) -> Data?
```

#### Discussion

At this time the only filters classes that can be serialized using this method are, CIAffineTransform, CICrop, and the filters returned by the [`CIImage`](ciimage.md) methods [`autoAdjustmentFilters()`](ciimage/autoadjustmentfilters().md) and [`autoAdjustmentFilters(options:)`](ciimage/autoadjustmentfilters(options:).md). The parameters of other filter classes will not be serialized.

## Parameters

- `filters`: The array of filters to serialize. See Discussion for the filters that can be serialized.
- `extent`: The extent of the input image to the filter.

## See Also

- [init!(CVPixelBuffer: CVPixelBuffer!, properties: [AnyHashable : Any]!, options: [CIRAWFilterOption : Any]!)](cifilter-swift.class/init(cvpixelbuffer:properties:options:).md)
  Creates a filter from a Core Video pixel buffer.
- [init!(imageData: Data!, options: [CIRAWFilterOption : Any]!)](cifilter-swift.class/init(imagedata:options:).md)
  Creates a filter that allows the processing of RAW images.
- [init!(imageURL: URL!, options: [CIRAWFilterOption : Any]!)](cifilter-swift.class/init(imageurl:options:).md)
  Creates a filter that allows the processing of RAW images.
- [struct CIRAWFilterOption](cirawfilteroption.md)
- [class func filterArray(fromSerializedXMP: Data, inputImageExtent: CGRect, error: NSErrorPointer) -> [CIFilter]](cifilter-swift.class/filterarray(fromserializedxmp:inputimageextent:error:).md)
  Returns an array of filter objects de-serialized from XMP data.
- [class func supportedRawCameraModels() -> [String]!](cifilter-swift.class/supportedrawcameramodels.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/serializedxmp(from:inputimageextent:))*