# isSupported

**Framework**: VisionKit  
**Kind**: property  
**Role**: Type Property

A Boolean value that indicates whether the device supports data scanning.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class var isSupported: Bool { get }
```

## Mentions

- [Scanning data with the camera](../scanning-data-with-the-camera.md)

#### Discussion

For this property to be `true`, the device must have the A12 Bionic chip or later. This property is `false` for apps running in visionOS.

> ❗ **Important**: If your app requires data scanning for its core functionality, you can make your app available only on devices that support data scanning. Add the [`UIRequiredDeviceCapabilities`](../../BundleResources/information-property-list/uirequireddevicecapabilities.md) key to your app’s information property list and include the `iphone-ipad-minimum-performance-a12` subkey in the array of device capabilities.

## See Also

### Handling availability
- [class var isAvailable: Bool](./isavailable.md)
  A Boolean value that indicates whether a person grants your app access to the camera and doesn’t have any restrictions to using the camera.
- [class var supportedTextRecognitionLanguages: [String]](./supportedtextrecognitionlanguages.md)
  The identifiers for the languages that the data scanner recognizes.
- [DataScannerViewController.ScanningUnavailable](./scanningunavailable.md)
  The possible reasons the data scanner is unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontroller/issupported)*