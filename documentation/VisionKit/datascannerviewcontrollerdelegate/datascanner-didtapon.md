# dataScanner(_:didTapOn:)

**Framework**: Visionkit  
**Kind**: method  
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

- [Scanning data with the camera](scanning-data-with-the-camera.md)

#### Discussion

Implement this method to take some action, depending on the type of data that a person taps.

## Parameters

- `dataScanner`: The data scanner with the zoom factor that changes.
- `item`: The item that a person taps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontrollerdelegate/datascanner(_:didtapon:))*