# qualityLevel

**Framework**: VisionKit  
**Kind**: property  
**Role**: Instance Property

The resolution that the scanner uses to find data.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
final let qualityLevel: DataScannerViewController.QualityLevel
```

#### Discussion

The default value is [`DataScannerViewController.QualityLevel.balanced`](./qualitylevel-swift.enum/balanced.md). To increase recognition speed for larger items, you can set this property to [`DataScannerViewController.QualityLevel.fast`](./qualitylevel-swift.enum/fast.md). For smaller items, you can set this property to [`DataScannerViewController.QualityLevel.accurate`](./qualitylevel-swift.enum/accurate.md) but it may impact the recognition speed.

## See Also

### Configuring data scanners
- [var delegate: (any DataScannerViewControllerDelegate)?](./delegate.md)
  The delegate that handles user interaction with items recognized by the data scanner.
- [DataScannerViewController.QualityLevel](./qualitylevel-swift.enum.md)
  The possible quality levels that the scanner uses to find data.
- [let recognizesMultipleItems: Bool](./recognizesmultipleitems.md)
  A Boolean value that indicates whether the scanner should identify all items in the live video.
- [let isHighFrameRateTrackingEnabled: Bool](./ishighframeratetrackingenabled.md)
  A Boolean value that determines the frequency at which the scanner updates the geometry of recognized items.
- [let isPinchToZoomEnabled: Bool](./ispinchtozoomenabled.md)
  A Boolean value that indicates whether people can use a two-finger pinch-to-zoom gesture.
- [let isGuidanceEnabled: Bool](./isguidanceenabled.md)
  A Boolean value that indicates whether the scanner provides help to a person when selecting items.
- [let isHighlightingEnabled: Bool](./ishighlightingenabled.md)
  A Boolean value that indicates whether the scanner displays highlights around recognized items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontroller/qualitylevel-swift.property)*