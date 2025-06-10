# RecognizedTextObservation

**Framework**: Vision  
**Kind**: struct

An object that contains information about both the location and content of text and glyphs that the framework recognizes in an image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct RecognizedTextObservation
```

## Topics

### Creating an observation
- [init(VNRecognizedTextObservation)](recognizedtextobservation/init(_:).md)
  Creates a recognized text observation.
### Getting the recognized text
- [func topCandidates(Int) -> [RecognizedText]](recognizedtextobservation/topcandidates(_:).md)
  Requests the top candidates for a recognized text string.
- [struct RecognizedText](recognizedtext.md)
  Text recognized in an image through a text recognition request.
### Instance Properties
- [var boundingRegion: NormalizedRegion](recognizedtextobservation/boundingregion.md)
  The bounding region of the text.
- [let isTitle: Bool](recognizedtextobservation/istitle.md)
  Whether this text is the title of the document.
- [let recognitionLanguages: [Locale.Language]](recognizedtextobservation/recognitionlanguages.md)
  The languages in which the recognized text was written.
- [let shouldWrapToNextLine: Bool?](recognizedtextobservation/shouldwraptonextline.md)
  Whether the text continues on the next line.
- [let textDirection: RecognizedTextObservation.Direction?](recognizedtextobservation/textdirection.md)
- [var transcript: String](recognizedtextobservation/transcript.md)
  The top text candidate as a string.
### Enumerations
- [RecognizedTextObservation.Direction](recognizedtextobservation/direction.md)
  An enum representing which direction the text is read.

## Relationships

### Conforms To
- [BoundingBoxProviding](boundingboxproviding.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [QuadrilateralProviding](quadrilateralproviding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [VisionObservation](visionobservation.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizedtextobservation)*