# isSupported

**Framework**: VisionKit  
**Kind**: property

A Boolean value that indicates whether the device supports image analysis.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
final class var isSupported: Bool { get }
```

## Mentions

- [Enabling Live Text interactions with images](enabling-live-text-interactions-with-images.md)

#### Discussion

Check this property at runtime to determine if the device supports finding text, machine-readable codes, and subjects in images. The system sets this property to `true` on devices that have an A12 Bionic chip or later.

For more information on the kinds of things the analyzer finds in images, see [`ImageAnalyzer.AnalysisTypes`](imageanalyzer/analysistypes.md).

> **Note**: If image analysis is a fundamental requirement for your app’s operation, you can prevent unsupported devices from installing your app. Add the [`UIRequiredDeviceCapabilities`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIRequiredDeviceCapabilities) key to your app’s `Info.plist` (or update the key if it’s already present) and include the array member `iphone-ipad-minimum-performance-a12`.

## See Also

- [class var supportedTextRecognitionLanguages: [String]](imageanalyzer/supportedtextrecognitionlanguages.md)
  The identifiers for the languages that the image analyzer recognizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalyzer/issupported)*