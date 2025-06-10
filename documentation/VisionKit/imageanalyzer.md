# ImageAnalyzer

**Framework**: VisionKit  
**Kind**: class

An object that finds items in images that people can interact with, such as subjects, text, and QR codes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
final class ImageAnalyzer
```

## Mentions

- [Enabling Live Text interactions with images](enabling-live-text-interactions-with-images.md)

#### Overview

To use an `ImageAnalyzer` object, first create an [`ImageAnalyzer.Configuration`](imageanalyzer/configuration.md) object, and specify the types of items you want to find in an image. Then pass the image you want to analyze and the configuration object to an `ImageAnalyzer` object using the [`analyze(_:configuration:)`](imageanalyzer/analyze(_:configuration:).md) or similar method. This method returns an [`ImageAnalysis`](imageanalysis.md) object that contains all the data VisionKit needs to implement the Live Text interface.

Next, show the Live Text interface. For iOS apps, set the interaction object of the view that contains the image to an instance of [`ImageAnalysisInteraction`](imageanalysisinteraction.md) and set its [`analysis`](imageanalysisinteraction/analysis.md) property to the `ImageAnalysis` object. To enable interactions with the image, set the interaction object’s [`preferredInteractionTypes`](imageanalysisinteraction/preferredinteractiontypes.md) property. To customize the Live Text interface, set the `ImageAnalysisInteraction `object’s [`delegate`](imageanalysisinteraction/delegate.md) property and implement the [`ImageAnalysisInteractionDelegate`](imageanalysisinteractiondelegate.md) protocol methods.

For macOS apps, add an `ImageAnalysisOverlayView` object above the view that contains the image, and set its `analysis` property. To enable interactions with the image, set the overlay view’s `preferredInteractionTypes` property. Set the `ImageAnalysisOverlayView `object’s `delegate` property and implement the `ImageAnalysisOverlayViewDelegate` protocol methods.

By default, the Live Text interface starts immediately when you show the view.

## Topics

### Handling availability
- [class var isSupported: Bool](imageanalyzer/issupported.md)
  A Boolean value that indicates whether the device supports image analysis.
- [class var supportedTextRecognitionLanguages: [String]](imageanalyzer/supportedtextrecognitionlanguages.md)
  The identifiers for the languages that the image analyzer recognizes.
### Creating image analyzers
- [init()](imageanalyzer/init.md)
  Creates an image analyzer that identifies subjects, text, and machine-readable codes in images.
### Configuring image analyzers
- [ImageAnalyzer.Configuration](imageanalyzer/configuration.md)
  A configuration that specifies the types of items and locales that the image analyzer recognizes.
### Finding items in images
- [func analyze(UIImage, configuration: ImageAnalyzer.Configuration) async throws -> ImageAnalysis](imageanalyzer/analyze(_:configuration:).md)
  Returns the data for providing a Live Text interaction with an image.
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
### Structures
- [ImageAnalyzer.AnalysisTypes](imageanalyzer/analysistypes.md)
  The types of items that an image analyzer looks for in an image.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Enabling Live Text interactions with images](enabling-live-text-interactions-with-images.md)
  Add a Live Text interface that enables users to perform actions with text and QR codes that appear in images.
- [class ImageAnalysis](imageanalysis.md)
  An object that represents the results of analyzing an image, and provides the input for the Live Text interface object.
- [class ImageAnalysisInteraction](imageanalysisinteraction.md)
  An interface that enables people to interact with recognized text, barcodes, and other objects in an image.
- [protocol ImageAnalysisInteractionDelegate](imageanalysisinteractiondelegate.md)
  A delegate that handles image-analysis and user-interaction callbacks for an interaction object.
- [class ImageAnalysisOverlayView](imageanalysisoverlayview.md)
  A view that enables people to interact with recognized text, barcodes, and other objects in an image.
- [protocol ImageAnalysisOverlayViewDelegate](imageanalysisoverlayviewdelegate.md)
  A delegate that handles image-analysis and user-interaction callbacks for an overlay view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalyzer)*