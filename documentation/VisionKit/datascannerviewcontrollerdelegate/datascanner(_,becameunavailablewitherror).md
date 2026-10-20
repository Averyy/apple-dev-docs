# dataScanner(_:becameUnavailableWithError:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Responds when the data scanner becomes unavailable and stops scanning.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func dataScanner(_ dataScanner: DataScannerViewController, becameUnavailableWithError error: DataScannerViewController.ScanningUnavailable)
```

## Mentions

- [Scanning data with the camera](../scanning-data-with-the-camera.md)

## Parameters

- `dataScanner`: The data scanner that’s not available.
- `error`: Describes an error if it occurs.

## Default Implementations

### DataScannerViewControllerDelegate Implementations
- [func dataScanner(DataScannerViewController, becameUnavailableWithError: DataScannerViewController.ScanningUnavailable)](./datascanner%28_,becameunavailablewitherror%29-89v47.md)
  A default, blank implementation for when the data scanner becomes unavailable and stops scanning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontrollerdelegate/datascanner(_:becameunavailablewitherror:))*