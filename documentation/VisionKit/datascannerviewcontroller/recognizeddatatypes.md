# recognizedDataTypes

**Framework**: VisionKit  
**Kind**: property

The types of data that the data scanner identifies in the live video.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
final let recognizedDataTypes: Set<DataScannerViewController.RecognizedDataType>
```

## See Also

- [init(recognizedDataTypes: Set<DataScannerViewController.RecognizedDataType>, qualityLevel: DataScannerViewController.QualityLevel, recognizesMultipleItems: Bool, isHighFrameRateTrackingEnabled: Bool, isPinchToZoomEnabled: Bool, isGuidanceEnabled: Bool, isHighlightingEnabled: Bool)](datascannerviewcontroller/init(recognizeddatatypes:qualitylevel:recognizesmultipleitems:ishighframeratetrackingenabled:ispinchtozoomenabled:isguidanceenabled:ishighlightingenabled:).md)
  Creates a scanner for finding data, such as text and machine-readable codes, in the camera’s live video.
- [DataScannerViewController.RecognizedDataType](datascannerviewcontroller/recognizeddatatype.md)
  A type of data that the scanner recognizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontroller/recognizeddatatypes)*