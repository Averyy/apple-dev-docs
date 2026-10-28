# machineReadableCode

**Framework**: VisionKit  
**Kind**: property  
**Role**: Type Property

An option that analyzes an image for machine-readable codes, such as QR codes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
static let machineReadableCode: ImageAnalyzer.AnalysisTypes
```

## Mentions

- [Enabling Live Text interactions with images](../../enabling-live-text-interactions-with-images.md)

## Discussion

The framework recognizes the following code types:

Aztec, Codebar, Code 39 Checksum, Code 39, Code 39 Full ASCII, Code 39 Full ASCII Checksum, Code 93, Code 93, Code 128, Matrix EAN-8, Data, EAN-13, GS1 DataBar Expanded, GS1 DataBar Limited, ITF, ITF-14, MicroPDF417, MicroQR, PDF417 QR, UPC-E

> ❗ **Important**: The framework ignores this option on macOS.

## See Also

### Specifying types to find
- [static let text: ImageAnalyzer.AnalysisTypes](./text.md)
  An option that analyzes an image for text.
- [static let visualLookUp: ImageAnalyzer.AnalysisTypes](./visuallookup.md)
  An option that analyzes an image for subjects that the framework can look up for more information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalyzer/analysistypes/machinereadablecode)*