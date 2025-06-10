# DataScannerViewController.QualityLevel

**Framework**: VisionKit  
**Kind**: enum

The possible quality levels that the scanner uses to find data.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum QualityLevel
```

#### Overview

The quality levels mostly impact the camera resolution.

## Topics

### Identifying quality levels
- [DataScannerViewController.QualityLevel.balanced](datascannerviewcontroller/qualitylevel-swift.enum/balanced.md)
  A quality level that’s between fast and accurate.
- [DataScannerViewController.QualityLevel.fast](datascannerviewcontroller/qualitylevel-swift.enum/fast.md)
  A quality level that prioritizes recognition speed over accuracy.
- [DataScannerViewController.QualityLevel.accurate](datascannerviewcontroller/qualitylevel-swift.enum/accurate.md)
  A quality level that prioritizes recognition accuracy over speed.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var delegate: (any DataScannerViewControllerDelegate)?](datascannerviewcontroller/delegate.md)
  The delegate that handles user interaction with items recognized by the data scanner.
- [let qualityLevel: DataScannerViewController.QualityLevel](datascannerviewcontroller/qualitylevel-swift.property.md)
  The resolution that the scanner uses to find data.
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

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontroller/qualitylevel-swift.enum)*