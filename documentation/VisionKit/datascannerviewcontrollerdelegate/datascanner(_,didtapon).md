# dataScanner(_:didTapOn:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Responds when a person taps an item that the data scanner recognizes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func dataScanner(_ dataScanner: DataScannerViewController, didTapOn item: RecognizedItem)
```

## Mentions

- [Scanning data with the camera](../scanning-data-with-the-camera.md)

#### Discussion

Implement this method to take some action, depending on the type of data that a person taps.

## Parameters

- `dataScanner`: The data scanner with the zoom factor that changes.
- `item`: The item that a person taps.

## Default Implementations

### DataScannerViewControllerDelegate Implementations
- [func dataScanner(DataScannerViewController, didTapOn: RecognizedItem)](./datascanner%28_,didtapon%29-4ugfh.md)
  A default, blank implementation for when a person taps an item that the data scanner recognizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontrollerdelegate/datascanner(_:didtapon:))*