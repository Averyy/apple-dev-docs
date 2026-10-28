# recognizesMultipleItems

**Framework**: VisionKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the scanner should identify all items in the live video.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
final let recognizesMultipleItems: Bool
```

## Discussion

If `true`, the scanner finds all items in the live video. If `false`, the scanner finds only the item closest to a person’s point of interest. The point of interest is the middle of the view by default or where a person taps in the live video. The default value is `false`.

## See Also

### Configuring data scanners
- [var delegate: (any DataScannerViewControllerDelegate)?](./delegate.md)
  The delegate that handles user interaction with items recognized by the data scanner.
- [let qualityLevel: DataScannerViewController.QualityLevel](./qualitylevel-swift.property.md)
  The resolution that the scanner uses to find data.
- [DataScannerViewController.QualityLevel](./qualitylevel-swift.enum.md)
  The possible quality levels that the scanner uses to find data.
- [let isHighFrameRateTrackingEnabled: Bool](./ishighframeratetrackingenabled.md)
  A Boolean value that determines the frequency at which the scanner updates the geometry of recognized items.
- [let isPinchToZoomEnabled: Bool](./ispinchtozoomenabled.md)
  A Boolean value that indicates whether people can use a two-finger pinch-to-zoom gesture.
- [let isGuidanceEnabled: Bool](./isguidanceenabled.md)
  A Boolean value that indicates whether the scanner provides help to a person when selecting items.
- [let isHighlightingEnabled: Bool](./ishighlightingenabled.md)
  A Boolean value that indicates whether the scanner displays highlights around recognized items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontroller/recognizesmultipleitems)*