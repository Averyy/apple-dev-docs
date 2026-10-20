# recognitionLanguages

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The languages in which the recognized text was written.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
let recognitionLanguages: [Locale.Language]
```

## See Also

### Inspecting an observation
- [var boundingRegion: NormalizedRegion](./boundingregion.md)
  The bounding region of the text.
- [let isTitle: Bool](./istitle.md)
  Whether this text is the title of the document.
- [let shouldWrapToNextLine: Bool?](./shouldwraptonextline.md)
  Whether the text continues on the next line.
- [let textDirection: RecognizedTextObservation.Direction?](./textdirection.md)
- [RecognizedTextObservation.Direction](./direction.md)
  An enum representing which direction the text is read.
- [var transcript: String](./transcript.md)
  The top text candidate as a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizedtextobservation/recognitionlanguages)*