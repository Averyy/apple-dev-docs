# boundingRegion

**Framework**: Vision  
**Kind**: property

The bounding region of the text.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var boundingRegion: NormalizedRegion { get }
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizedtextobservation/boundingregion)*