# delegate

**Framework**: VisionKit  
**Kind**: property

The delegate that handles user interaction with items recognized by the data scanner.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any DataScannerViewControllerDelegate)?
```

## See Also

- [let qualityLevel: DataScannerViewController.QualityLevel](datascannerviewcontroller/qualitylevel-swift.property.md)
  The resolution that the scanner uses to find data.
- [DataScannerViewController.QualityLevel](datascannerviewcontroller/qualitylevel-swift.enum.md)
  The possible quality levels that the scanner uses to find data.
- [let recognizesMultipleItems: Bool](datascannerviewcontroller/recognizesmultipleitems.md)
  A Boolean value that indicates whether the scanner should identify all items in the live video.
- [let isHighFrameRateTrackingEnabled: Bool](datascannerviewcontroller/ishighframeratetrackingenabled.md)
  A Boolean value that determines the frequency at which the scanner updates the geometry of recognized items.
- [let isPinchToZoomEnabled: Bool](datascannerviewcontroller/ispinchtozoomenabled.md)
  A Boolean value that indicates whether people can use a two-finger pinch-to-zoom gesture.
- [let isGuidanceEnabled: Bool](datascannerviewcontroller/isguidanceenabled.md)
  A Boolean value that indicates whether the scanner provides help to a person when selecting items.
- [let isHighlightingEnabled: Bool](datascannerviewcontroller/ishighlightingenabled.md)
  A Boolean value that indicates whether the scanner displays highlights around recognized items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontroller/delegate)*