# selectedAttributedText

**Framework**: Visionkit  
**Kind**: property

The current selected attributed text.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
final var selectedAttributedText: AttributedString { get }
```

## See Also

- [var text: String](imageanalysisoverlayview/text.md)
  The text contents of the current image analysis.
- [var selectedText: String](imageanalysisoverlayview/selectedtext.md)
  The current selected text.
- [var hasActiveTextSelection: Bool](imageanalysisoverlayview/hasactivetextselection.md)
  A Boolean value that indicates whether a person or the app has text selected within the image.
- [func analysisHasText(at: CGPoint) -> Bool](imageanalysisoverlayview/analysishastext(at:).md)
  Returns a Boolean value that indicates whether the analysis finds text at the specified point.
- [func hasText(at: CGPoint) -> Bool](imageanalysisoverlayview/hastext(at:).md)
  Returns a Boolean value that indicates whether active text exists at the specified point.
- [func hasDataDetector(at: CGPoint) -> Bool](imageanalysisoverlayview/hasdatadetector(at:).md)
  Returns a Boolean value that indicates whether the analysis detects data at the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/selectedattributedtext)*