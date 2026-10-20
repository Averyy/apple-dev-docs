# RecognizedTextObservation.Direction

**Framework**: Vision  
**Kind**: enum  
**Role**: Enumeration

An enum representing which direction the text is read.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum Direction
```

## Topics

### Directions
- [RecognizedTextObservation.Direction.leftToRight](./direction/lefttoright.md)
- [RecognizedTextObservation.Direction.rightToLeft](./direction/righttoleft.md)
- [RecognizedTextObservation.Direction.topToBottom](./direction/toptobottom.md)

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting an observation
- [var boundingRegion: NormalizedRegion](./boundingregion.md)
  The bounding region of the text.
- [let isTitle: Bool](./istitle.md)
  Whether this text is the title of the document.
- [let recognitionLanguages: [Locale.Language]](./recognitionlanguages.md)
  The languages in which the recognized text was written.
- [let shouldWrapToNextLine: Bool?](./shouldwraptonextline.md)
  Whether the text continues on the next line.
- [let textDirection: RecognizedTextObservation.Direction?](./textdirection.md)
- [var transcript: String](./transcript.md)
  The top text candidate as a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizedtextobservation/direction)*