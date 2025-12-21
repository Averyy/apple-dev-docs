# RecognizedTextObservation

**Framework**: Vision  
**Kind**: struct

An object that contains information about both the location and content of text and glyphs that the framework recognizes in an image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
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
### Inspecting an observation
- [var boundingRegion: NormalizedRegion](recognizedtextobservation/boundingregion.md)
  The bounding region of the text.
- [let isTitle: Bool](recognizedtextobservation/istitle.md)
  Whether this text is the title of the document.
- [let recognitionLanguages: [Locale.Language]](recognizedtextobservation/recognitionlanguages.md)
  The languages in which the recognized text was written.
- [let shouldWrapToNextLine: Bool?](recognizedtextobservation/shouldwraptonextline.md)
  Whether the text continues on the next line.
- [let textDirection: RecognizedTextObservation.Direction?](recognizedtextobservation/textdirection.md)
- [RecognizedTextObservation.Direction](recognizedtextobservation/direction.md)
  An enum representing which direction the text is read.
- [var transcript: String](recognizedtextobservation/transcript.md)
  The top text candidate as a string.
### Getting the recognized text
- [func topCandidates(Int) -> [RecognizedText]](recognizedtextobservation/topcandidates(_:).md)
  Requests the top candidates for a recognized text string.
- [struct RecognizedText](recognizedtext.md)
  Text recognized in an image through a text recognition request.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizedtextobservation)*