# ImageAnalyzer.Configuration

**Framework**: Visionkit  
**Kind**: struct

A configuration that specifies the types of items and locales that the image analyzer recognizes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
struct Configuration
```

## Mentions

- [Enabling Live Text interactions with images](enabling-live-text-interactions-with-images.md)

#### Overview

Create an `ImageAnalyzer.Configuration` structure to specify the criteria when analyzing an image. Then pass the configuration object to the `ImageAnalyzer` [`analyze(_:configuration:)`](imageanalyzer/analyze(_:configuration:).md) or similar method to find the items you want.

## Topics

### Creating configurations
- [init(ImageAnalyzer.AnalysisTypes)](imageanalyzer/configuration/init(_:).md)
  Creates a configuration that an image analyzer uses to find items.
- [let analysisTypes: ImageAnalyzer.AnalysisTypes](imageanalyzer/configuration/analysistypes.md)
  The types of items that the image analyzer looks for in the image.
- [ImageAnalyzer.AnalysisTypes](imageanalyzer/analysistypes.md)
  The types of items that an image analyzer looks for in an image.
### Recognizing languages
- [var locales: [String]](imageanalyzer/configuration/locales.md)
  The languages to use in text items that the image analyzer recognizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalyzer/configuration)*