# selectedText

**Framework**: VisionKit  
**Kind**: property  
**Role**: Instance Property

The current selected text.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
final var selectedText: String { get }
```

## See Also

### Accessing text information
- [var text: String](./text.md)
  The text contents of the current image analysis.
- [var selectedAttributedText: AttributedString](./selectedattributedtext.md)
  The current selected attributed text.
- [var hasActiveTextSelection: Bool](./hasactivetextselection.md)
  A Boolean value that indicates whether a person or the app has text selected within the image.
- [func analysisHasText(at: CGPoint) -> Bool](./analysishastext%28at%29.md)
  Returns a Boolean value that indicates whether the analysis finds text at the specified point.
- [func hasText(at: CGPoint) -> Bool](./hastext%28at%29.md)
  Returns a Boolean value that indicates whether active text exists at the specified point.
- [func hasDataDetector(at: CGPoint) -> Bool](./hasdatadetector%28at%29.md)
  Returns a Boolean value that indicates whether the analysis detects data at the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/selectedtext)*