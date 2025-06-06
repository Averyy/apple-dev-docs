# DataScannerViewController.ScanningUnavailable

**Framework**: Visionkit  
**Kind**: enum

The possible reasons the data scanner is unavailable.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum ScanningUnavailable
```

## Topics

### Unavailable errors
- [DataScannerViewController.ScanningUnavailable.unsupported](datascannerviewcontroller/scanningunavailable/unsupported.md)
  The data scanner isn’t supported on this device.
- [DataScannerViewController.ScanningUnavailable.cameraRestricted](datascannerviewcontroller/scanningunavailable/camerarestricted.md)
  The data scanner isn’t available due to user restrictions on the use of the camera.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func dataScanner(DataScannerViewController, becameUnavailableWithError: DataScannerViewController.ScanningUnavailable)](datascannerviewcontrollerdelegate/datascanner(_:becameunavailablewitherror:).md)
  Responds when the data scanner becomes unavailable and stops scanning.
- [class var isSupported: Bool](datascannerviewcontroller/issupported.md)
  A Boolean value that indicates whether the device supports data scanning.
- [class var isAvailable: Bool](datascannerviewcontroller/isavailable.md)
  A Boolean value that indicates whether a person grants your app access to the camera and doesn’t have any restrictions to using the camera.
- [class var supportedTextRecognitionLanguages: [String]](datascannerviewcontroller/supportedtextrecognitionlanguages.md)
  The identifiers for the languages that the data scanner recognizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontroller/scanningunavailable)*