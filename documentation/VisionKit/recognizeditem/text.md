# RecognizedItem.Text

**Framework**: Visionkit  
**Kind**: struct

An object that represents a text item that the scanner recognizes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct Text
```

## Topics

### Getting text strings
- [var transcript: String](recognizeditem/text/transcript.md)
  The string that the text item represents.
### Locating text
- [var bounds: RecognizedItem.Bounds](recognizeditem/text/bounds.md)
  The bounds of the recognized item in view coordinates.
- [var observation: VNRecognizedTextObservation](recognizeditem/text/observation.md)
  An object that contains details about the location and content of text and glyphs in an image.
### Identifying text
- [var id: UUID](recognizeditem/text/id.md)
  A unique identifier for the recognized item.

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [case text(RecognizedItem.Text)](recognizeditem/text(_:).md)
  Text or data the analyzer detects in text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/recognizeditem/text)*