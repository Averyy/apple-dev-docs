# isGuidanceEnabled

**Framework**: Visionkit  
**Kind**: property

A Boolean value that indicates whether the scanner provides help to a person when selecting items.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
final let isGuidanceEnabled: Bool
```

#### Discussion

The guidance text, such as “Slow Down,” appears over the live video. The default value for this property is `true`.

## See Also

- [var delegate: (any DataScannerViewControllerDelegate)?](datascannerviewcontroller/delegate.md)
  The delegate that handles user interaction with items recognized by the data scanner.
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
- [let isHighlightingEnabled: Bool](datascannerviewcontroller/ishighlightingenabled.md)
  A Boolean value that indicates whether the scanner displays highlights around recognized items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontroller/isguidanceenabled)*