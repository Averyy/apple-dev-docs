# DataScannerViewController.RecognizedDataType

**Framework**: Visionkit  
**Kind**: struct

A type of data that the scanner recognizes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct RecognizedDataType
```

## Mentions

- [Scanning data with the camera](scanning-data-with-the-camera.md)

## Topics

### Recognizing text
- [static func text(languages: [String], textContentType: DataScannerViewController.TextContentType?) -> DataScannerViewController.RecognizedDataType](datascannerviewcontroller/recognizeddatatype/text(languages:textcontenttype:).md)
  Creates a data type for text and information the scanner finds in text.
- [DataScannerViewController.TextContentType](datascannerviewcontroller/textcontenttype.md)
  Types of text that a data scanner recognizes.
### Recognizing machine-readable codes
- [static func barcode(symbologies: [VNBarcodeSymbology]) -> DataScannerViewController.RecognizedDataType](datascannerviewcontroller/recognizeddatatype/barcode(symbologies:).md)
  Creates a data type for barcodes the use the specified symbologies.
### Hashing and comparing
- [func hash(into: inout Hasher)](datascannerviewcontroller/recognizeddatatype/hash(into:).md)
  Hashes the components of this value using the specified hasher.
- [static func == (DataScannerViewController.RecognizedDataType, DataScannerViewController.RecognizedDataType) -> Bool](datascannerviewcontroller/recognizeddatatype/==(_:_:).md)
  Returns a Boolean value indicating whether two sets have equal elements.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [init(recognizedDataTypes: Set<DataScannerViewController.RecognizedDataType>, qualityLevel: DataScannerViewController.QualityLevel, recognizesMultipleItems: Bool, isHighFrameRateTrackingEnabled: Bool, isPinchToZoomEnabled: Bool, isGuidanceEnabled: Bool, isHighlightingEnabled: Bool)](datascannerviewcontroller/init(recognizeddatatypes:qualitylevel:recognizesmultipleitems:ishighframeratetrackingenabled:ispinchtozoomenabled:isguidanceenabled:ishighlightingenabled:).md)
  Creates a scanner for finding data, such as text and machine-readable codes, in the camera’s live video.
- [let recognizedDataTypes: Set<DataScannerViewController.RecognizedDataType>](datascannerviewcontroller/recognizeddatatypes.md)
  The types of data that the data scanner identifies in the live video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontroller/recognizeddatatype)*