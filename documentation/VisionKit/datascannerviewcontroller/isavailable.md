# isAvailable

**Framework**: VisionKit  
**Kind**: property

A Boolean value that indicates whether a person grants your app access to the camera and doesn’t have any restrictions to using the camera.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class var isAvailable: Bool { get }
```

## Mentions

- [Scanning data with the camera](scanning-data-with-the-camera.md)

#### Discussion

For example, this property may be `false` if a person has Screen Time restrictions.

## See Also

- [class var isSupported: Bool](datascannerviewcontroller/issupported.md)
  A Boolean value that indicates whether the device supports data scanning.
- [class var supportedTextRecognitionLanguages: [String]](datascannerviewcontroller/supportedtextrecognitionlanguages.md)
  The identifiers for the languages that the data scanner recognizes.
- [DataScannerViewController.ScanningUnavailable](datascannerviewcontroller/scanningunavailable.md)
  The possible reasons the data scanner is unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontroller/isavailable)*