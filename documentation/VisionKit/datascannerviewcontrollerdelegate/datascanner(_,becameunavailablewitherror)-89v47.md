# dataScanner(_:becameUnavailableWithError:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method

A default, blank implementation for when the data scanner becomes unavailable and stops scanning.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func dataScanner(_ dataScanner: DataScannerViewController, becameUnavailableWithError error: DataScannerViewController.ScanningUnavailable)
```

## Parameters

- `dataScanner`: The data scanner that’s not available.
- `error`: Describes an error if it occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontrollerdelegate/datascanner(_:becameunavailablewitherror:)-89v47)*