# filterArray(fromSerializedXMP:inputImageExtent:error:)

**Framework**: Core Image  
**Kind**: method

Returns an array of filter objects de-serialized from XMP data.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class func filterArray(fromSerializedXMP xmpData: Data, inputImageExtent extent: CGRect, error outError: NSErrorPointer) -> [CIFilter]
```

## Parameters

- `xmpData`: The XMP data created previously by calling  .
- `extent`: The extent of the image from which the XMP data was extracted.
- `outError`: The address of an   object for receiving errors, otherwise  .

## See Also

- [init!(CVPixelBuffer: CVPixelBuffer!, properties: [AnyHashable : Any]!, options: [CIRAWFilterOption : Any]!)](cifilter-swift.class/init(cvpixelbuffer:properties:options:).md)
  Creates a filter from a Core Video pixel buffer.
- [init!(imageData: Data!, options: [CIRAWFilterOption : Any]!)](cifilter-swift.class/init(imagedata:options:).md)
  Creates a filter that allows the processing of RAW images.
- [init!(imageURL: URL!, options: [CIRAWFilterOption : Any]!)](cifilter-swift.class/init(imageurl:options:).md)
  Creates a filter that allows the processing of RAW images.
- [struct CIRAWFilterOption](cirawfilteroption.md)
- [class func serializedXMP(from: [CIFilter], inputImageExtent: CGRect) -> Data?](cifilter-swift.class/serializedxmp(from:inputimageextent:).md)
  Serializes filter parameters into XMP form that is suitable for embedding in an image.
- [class func supportedRawCameraModels() -> [String]!](cifilter-swift.class/supportedrawcameramodels.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/filterarray(fromserializedxmp:inputimageextent:error:))*