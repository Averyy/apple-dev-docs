# serializedXMP(from:inputImageExtent:)

**Framework**: Core Image  
**Kind**: clm

Serializes filter parameters into XMP form that is suitable for embedding in an image.

**Availability**:
- iOS 6.0+ - Deprecated in 17.0
- iPadOS 6.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0
- macOS 10.9+ - Deprecated in 14.0
- tvOS 9.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
class func serializedXMP(from filters: [CIFilter], inputImageExtent extent: CGRect) -> Data?
```

#### Discussion

At this time the only filters classes that can be serialized using this method are, CIAffineTransform, CICrop, and the filters returned by the [`CIImage`](ciimage.md) methods [`autoAdjustmentFilters()`](ciimage/1645889-autoadjustmentfilters.md) and [`autoAdjustmentFilters(options:)`](ciimage/1437792-autoadjustmentfilters.md). The parameters of other filter classes will not be serialized.

## Parameters

- `filters`: The array of filters to serialize. See Discussion for the filters that can be serialized.
- `extent`: The extent of the input image to the filter.

## See Also

- [init!(cvPixelBuffer: CVPixelBuffer!, properties: [AnyHashable : Any]!, options: [CIRAWFilterOption : Any]!)](cifilter/2138288-init.md)
  Creates a filter from a Core Video pixel buffer.
- [init!(imageData: Data!, options: [CIRAWFilterOption : Any]!)](cifilter/1437879-init.md)
  Creates a filter that allows the processing of RAW images.
- [init!(imageURL: URL!, options: [CIRAWFilterOption : Any]!)](cifilter/1438096-init.md)
  Creates a filter that allows the processing of RAW images.
- [struct CIRAWFilterOption](cirawfilteroption.md)
- [class func filterArray(fromSerializedXMP: Data, inputImageExtent: CGRect, error: NSErrorPointer) -> [CIFilter]](cifilter/1438237-filterarray.md)
  Returns an array of filter objects de-serialized from XMP data.
- [class func supportedRawCameraModels() -> [String]!](cifilter/3242782-supportedrawcameramodels.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/1438006-serializedxmp)*