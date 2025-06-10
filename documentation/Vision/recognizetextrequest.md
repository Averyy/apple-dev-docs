# RecognizeTextRequest

**Framework**: Vision  
**Kind**: struct

An image-analysis request that recognizes text in an image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct RecognizeTextRequest
```

#### Overview

This request generates a collection of [`RecognizedTextObservation`](recognizedtextobservation.md) objects that describe the text the request detects. By default, a text-recognition request first locates all possible glyphs or characters in the input image, and then analyzes each string. To specify or limit the languages to find in the request, set [`recognitionLanguages`](recognizetextrequest/recognitionlanguages.md) to an array that contains the names of the languages of text you want to recognize.

## Topics

### Creating a request
- [init(RecognizeTextRequest.Revision?)](recognizetextrequest/init(_:).md)
  Creates a text-recognition request.
### Getting the revision
- [let revision: RecognizeTextRequest.Revision](recognizetextrequest/revision-swift.property.md)
  The algorithm or implementation the request uses.
- [static let supportedRevisions: [RecognizeTextRequest.Revision]](recognizetextrequest/supportedrevisions.md)
  The collection of revisions the request supports.
- [RecognizeTextRequest.Revision](recognizetextrequest/revision-swift.enum.md)
  A type that describes the algorithm or implementation that the request performs.
### Inspecting a request
- [var automaticallyDetectsLanguage: Bool](recognizetextrequest/automaticallydetectslanguage.md)
  A Boolean value that indicates whether to attempt detecting the language to use the appropriate model for recognition and language correction.
- [var usesLanguageCorrection: Bool](recognizetextrequest/useslanguagecorrection.md)
  A Boolean value that indicates whether the request applies language correction during the recognition process.
- [var supportedRecognitionLanguages: [Locale.Language]](recognizetextrequest/supportedrecognitionlanguages.md)
  The identifiers of the languages that the request supports.
- [var customWords: [String]](recognizetextrequest/customwords.md)
  An array of strings to supplement the recognized languages at the word-recognition stage.
- [var minimumTextHeightFraction: Float](recognizetextrequest/minimumtextheightfraction.md)
  The minimum height, relative to the image height, of the text to recognize.
- [var recognitionLanguages: [Locale.Language]](recognizetextrequest/recognitionlanguages.md)
  An array of languages to detect, in priority order.
- [var recognitionLevel: RecognizeTextRequest.RecognitionLevel](recognizetextrequest/recognitionlevel-swift.property.md)
  A value that determines whether the request prioritizes accuracy or speed in text recognition.
- [RecognizeTextRequest.RecognitionLevel](recognizetextrequest/recognitionlevel-swift.enum.md)
  Constants that identify the performance and accuracy of the text recognition.
### Performing a request
- [func perform(on: URL, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-80bya.md)
  Performs the request on an image URL and produces observations.
- [func perform(on: Data, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-3f3f1.md)
  Performs the request on image data and produces observations.
- [func perform(on: CGImage, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-qxxx.md)
  Performs the request on a Core Graphics image and produces observations.
- [func perform(on: CVPixelBuffer, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-xspx.md)
  Performs the request on a pixel buffer and produces observations.
- [func perform(on: CMSampleBuffer, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-3hddl.md)
  Performs the request on a Core Media buffer and produces observations.
- [func perform(on: CIImage, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-85ex1.md)
  Performs the request on a Core Image image and produces observations.
- [struct RecognizedTextObservation](recognizedtextobservation.md)
  An object that contains information about both the location and content of text and glyphs that the framework recognizes in an image.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [ImageProcessingRequest](imageprocessingrequest.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [VisionRequest](visionrequest.md)

## See Also

- [Recognizing tables within a document](recognize-tables-within-a-document.md)
  Scan a document containing a contact table and extract the content within the table in a formatted way.
- [Locating and displaying recognized text](locating-and-displaying-recognized-text.md)
  Perform text recognition on a photo using the Vision framework’s text-recognition request.
- [struct RecognizeDocumentsRequest](recognizedocumentsrequest.md)
  An image-analysis request to scan an image of a document and provide information about its structure.
- [struct DocumentObservation](documentobservation.md)
  Information about the sections of content that an image-analysis request detects in a document.
- [struct DetectTextRectanglesRequest](detecttextrectanglesrequest.md)
  An image-analysis request that finds regions of visible text in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizetextrequest)*