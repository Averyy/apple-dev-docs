# transcript

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The top text candidate as a string.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var transcript: String { get }
```

## Discussion

Please call `topCandidates` to see alternate text candidates.

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
- [RecognizedTextObservation.Direction](./direction.md)
  An enum representing which direction the text is read.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizedtextobservation/transcript)*