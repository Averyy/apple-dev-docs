# filterArray(fromSerializedXMP:inputImageExtent:error:)

**Framework**: Core Image  
**Kind**: clm

Returns an array of filter objects de-serialized from XMP data.

**Availability**:
- iOS 6.0+ - Deprecated in 17.0
- iPadOS 6.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0
- macOS 10.9+ - Deprecated in 14.0
- tvOS 9.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
class func filterArray(fromSerializedXMP xmpData: Data, inputImageExtent extent: CGRect, error outError: NSErrorPointer) -> [CIFilter]
```

## Parameters

- `xmpData`: The XMP data created previously by calling  .
- `extent`: The extent of the image from which the XMP data was extracted.
- `outError`: The address of an   object for receiving errors, otherwise  .

## See Also

- [init!(cvPixelBuffer: CVPixelBuffer!, properties: [AnyHashable : Any]!, options: [CIRAWFilterOption : Any]!)](cifilter/2138288-init.md)
  Creates a filter from a Core Video pixel buffer.
- [init!(imageData: Data!, options: [CIRAWFilterOption : Any]!)](cifilter/1437879-init.md)
  Creates a filter that allows the processing of RAW images.
- [init!(imageURL: URL!, options: [CIRAWFilterOption : Any]!)](cifilter/1438096-init.md)
  Creates a filter that allows the processing of RAW images.
- [struct CIRAWFilterOption](cirawfilteroption.md)
- [class func serializedXMP(from: [CIFilter], inputImageExtent: CGRect) -> Data?](cifilter/1438006-serializedxmp.md)
  Serializes filter parameters into XMP form that is suitable for embedding in an image.
- [class func supportedRawCameraModels() -> [String]!](cifilter/3242782-supportedrawcameramodels.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/1438237-filterarray)*