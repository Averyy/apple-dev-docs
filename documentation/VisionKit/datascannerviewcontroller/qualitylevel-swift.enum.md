# DataScannerViewController.QualityLevel

**Framework**: VisionKit  
**Kind**: enum  
**Role**: Enumeration

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
- [DataScannerViewController.QualityLevel.balanced](./qualitylevel-swift.enum/balanced.md)
  A quality level that’s between fast and accurate.
- [DataScannerViewController.QualityLevel.fast](./qualitylevel-swift.enum/fast.md)
  A quality level that prioritizes recognition speed over accuracy.
- [DataScannerViewController.QualityLevel.accurate](./qualitylevel-swift.enum/accurate.md)
  A quality level that prioritizes recognition accuracy over speed.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring data scanners
- [var delegate: (any DataScannerViewControllerDelegate)?](./delegate.md)
  The delegate that handles user interaction with items recognized by the data scanner.
- [let qualityLevel: DataScannerViewController.QualityLevel](./qualitylevel-swift.property.md)
  The resolution that the scanner uses to find data.
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

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontroller/qualitylevel-swift.enum)*