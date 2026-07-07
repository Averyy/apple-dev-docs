# RecognizedTextObservation.Direction

**Framework**: Vision  
**Kind**: enum

An enum representing which direction the text is read.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum Direction
```

## Topics

### Directions
- [RecognizedTextObservation.Direction.leftToRight](recognizedtextobservation/direction/lefttoright.md)
- [RecognizedTextObservation.Direction.rightToLeft](recognizedtextobservation/direction/righttoleft.md)
- [RecognizedTextObservation.Direction.topToBottom](recognizedtextobservation/direction/toptobottom.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizedtextobservation/direction)*