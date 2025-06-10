# analyze(_:configuration:)

**Framework**: VisionKit  
**Kind**: method

Returns the data for providing a Live Text interaction with an image.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
final func analyze(_ image: UIImage, configuration: ImageAnalyzer.Configuration) async throws -> ImageAnalysis
```

## Mentions

- [Enabling Live Text interactions with images](enabling-live-text-interactions-with-images.md)

#### Return Value

The data items that the analyzer finds in the image.

#### Discussion

This function configures orientation automatically based on the given image’s orientation property.

## Parameters

- `image`: An image that the analyzer processes.
- `configuration`: A configuration that specifies the data types, and   locales for text items, to recognize.

## See Also

- [func analyze(NSImage, orientation: CGImagePropertyOrientation, configuration: ImageAnalyzer.Configuration) async throws -> ImageAnalysis](imageanalyzer/analyze(_:orientation:configuration:)-5bs2w.md)
  Returns the data for providing a Live Text interaction with an image in the specified orientation.
- [func analyze(CGImage, orientation: CGImagePropertyOrientation, configuration: ImageAnalyzer.Configuration) async throws -> ImageAnalysis](imageanalyzer/analyze(_:orientation:configuration:)-ufrs.md)
  Returns the data for providing a Live Text interaction with a Core Graphics image in the specified orientation.
- [func analyze(CVPixelBuffer, orientation: CGImagePropertyOrientation, configuration: ImageAnalyzer.Configuration) async throws -> ImageAnalysis](imageanalyzer/analyze(_:orientation:configuration:)-2ezqw.md)
  Returns the data for providing a Live Text interaction with a pixel buffer image in the specified orientation.
- [func analyze(CIImage, orientation: CGImagePropertyOrientation, configuration: ImageAnalyzer.Configuration) async throws -> ImageAnalysis](imageanalyzer/analyze(_:orientation:configuration:)-4h43g.md)
  Returns the data for providing a Live Text interaction with a bitmap image in the specified orientation.
- [func analyze(UIImage, orientation: UIImage.Orientation, configuration: ImageAnalyzer.Configuration) async throws -> ImageAnalysis](imageanalyzer/analyze(_:orientation:configuration:)-fcjz.md)
  Returns the data for providing a Live Text interaction with an image in the specified orientation.
- [func analyze(imageAt: URL, orientation: CGImagePropertyOrientation, configuration: ImageAnalyzer.Configuration) async throws -> ImageAnalysis](imageanalyzer/analyze(imageat:orientation:configuration:).md)
  Returns the data for providing a Live Text interaction with an image at a URL and in the specified orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalyzer/analyze(_:configuration:))*