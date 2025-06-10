# ImageAnalyzer.AnalysisTypes

**Framework**: VisionKit  
**Kind**: struct

The types of items that an image analyzer looks for in an image.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
struct AnalysisTypes
```

## Topics

### Specifying types to find
- [static let machineReadableCode: ImageAnalyzer.AnalysisTypes](imageanalyzer/analysistypes/machinereadablecode.md)
  An option that analyzes an image for machine-readable codes, such as QR codes.
- [static let text: ImageAnalyzer.AnalysisTypes](imageanalyzer/analysistypes/text.md)
  An option that analyzes an image for text.
- [static let visualLookUp: ImageAnalyzer.AnalysisTypes](imageanalyzer/analysistypes/visuallookup.md)
  An option that analyzes an image for subjects that the framework can look up for more information.
### Managing sets
- [Set properties and methods](analysistypes-set-properties-and-methods.md)
  The properties and methods that conform to the option set protocol.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [init(ImageAnalyzer.AnalysisTypes)](imageanalyzer/configuration/init(_:).md)
  Creates a configuration that an image analyzer uses to find items.
- [let analysisTypes: ImageAnalyzer.AnalysisTypes](imageanalyzer/configuration/analysistypes.md)
  The types of items that the image analyzer looks for in the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalyzer/analysistypes)*