# observation

**Framework**: VisionKit  
**Kind**: property

An object that contains details about the location and content of text and glyphs in an image.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var observation: VNRecognizedTextObservation { get }
```

#### Discussion

Use this property only if you need vision details that aren’t included in the recognized item properties.

## See Also

- [var bounds: RecognizedItem.Bounds](recognizeditem/text/bounds.md)
  The bounds of the recognized item in view coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/recognizeditem/text/observation)*