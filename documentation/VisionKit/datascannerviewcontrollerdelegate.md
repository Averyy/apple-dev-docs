# DataScannerViewControllerDelegate

**Framework**: VisionKit  
**Kind**: protocol  
**Role**: Protocol

A delegate object that responds when people interact with items that the data scanner recognizes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol DataScannerViewControllerDelegate : AnyObject
```

## Mentions

- [Scanning data with the camera](./scanning-data-with-the-camera.md)

## Overview

Implement this protocol to handle when people tap recognized items and, optionally, provide additional feedback when the data scanner updates the recognized items.

## Topics

### Customizing highlighting
- [func dataScanner(DataScannerViewController, didAdd: [RecognizedItem], allItems: [RecognizedItem])](./datascannerviewcontrollerdelegate/datascanner%28_,didadd,allitems%29.md)
  Responds when the data scanner starts recognizing an item.
- [func dataScanner(DataScannerViewController, didUpdate: [RecognizedItem], allItems: [RecognizedItem])](./datascannerviewcontrollerdelegate/datascanner%28_,didupdate,allitems%29.md)
  Responds when the data scanner updates the geometry of an item it recognizes.
- [func dataScanner(DataScannerViewController, didRemove: [RecognizedItem], allItems: [RecognizedItem])](./datascannerviewcontrollerdelegate/datascanner%28_,didremove,allitems%29.md)
  Responds when the data scanner stops recognizing an item.
### Zooming
- [func dataScannerDidZoom(DataScannerViewController)](./datascannerviewcontrollerdelegate/datascannerdidzoom%28_%29.md)
  Responds when a person or your code changes the zoom factor.
### Tapping items
- [func dataScanner(DataScannerViewController, didTapOn: RecognizedItem)](./datascannerviewcontrollerdelegate/datascanner%28_,didtapon%29.md)
  Responds when a person taps an item that the data scanner recognizes.
### Handling errors
- [func dataScanner(DataScannerViewController, becameUnavailableWithError: DataScannerViewController.ScanningUnavailable)](./datascannerviewcontrollerdelegate/datascanner%28_,becameunavailablewitherror%29.md)
  Responds when the data scanner becomes unavailable and stops scanning.

## See Also

### Barcode and text scanning through the camera
- [Scanning data with the camera](./scanning-data-with-the-camera.md)
  Enable Live Text data scanning of text and codes that appear in the camera’s viewfinder.
- [class DataScannerViewController](./datascannerviewcontroller.md)
  An object that scans the camera live video for text, data in text, and machine-readable codes.
- [enum RecognizedItem](./recognizeditem.md)
  An item that the data scanner recognizes in the camera’s live video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontrollerdelegate)*