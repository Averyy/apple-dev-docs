# DataScannerViewController.ScanningUnavailable

**Framework**: VisionKit  
**Kind**: enum  
**Role**: Enumeration

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
- [DataScannerViewController.ScanningUnavailable.unsupported](./scanningunavailable/unsupported.md)
  The data scanner isn’t supported on this device.
- [DataScannerViewController.ScanningUnavailable.cameraRestricted](./scanningunavailable/camerarestricted.md)
  The data scanner isn’t available due to user restrictions on the use of the camera.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Error](../../Swift/error.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Related Documentation
- [func dataScanner(DataScannerViewController, becameUnavailableWithError: DataScannerViewController.ScanningUnavailable)](../datascannerviewcontrollerdelegate/datascanner%28_,becameunavailablewitherror%29.md)
  Responds when the data scanner becomes unavailable and stops scanning.
### Handling availability
- [class var isSupported: Bool](./issupported.md)
  A Boolean value that indicates whether the device supports data scanning.
- [class var isAvailable: Bool](./isavailable.md)
  A Boolean value that indicates whether a person grants your app access to the camera and doesn’t have any restrictions to using the camera.
- [class var supportedTextRecognitionLanguages: [String]](./supportedtextrecognitionlanguages.md)
  The identifiers for the languages that the data scanner recognizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontroller/scanningunavailable)*