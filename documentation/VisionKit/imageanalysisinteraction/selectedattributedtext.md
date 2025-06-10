# selectedAttributedText

**Framework**: VisionKit  
**Kind**: property

The current selected attributed text.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
final var selectedAttributedText: AttributedString { get }
```

## See Also

- [var text: String](imageanalysisinteraction/text.md)
  The text contents of the current image analysis.
- [var selectedText: String](imageanalysisinteraction/selectedtext.md)
  The current selected text.
- [func hasText(at: CGPoint) -> Bool](imageanalysisinteraction/hastext(at:).md)
  Returns a Boolean value that indicates whether active text exists at the specified point.
- [var hasActiveTextSelection: Bool](imageanalysisinteraction/hasactivetextselection.md)
  A Boolean value that indicates whether a person or the app has text selected within the image.
- [func analysisHasText(at: CGPoint) -> Bool](imageanalysisinteraction/analysishastext(at:).md)
  Returns a Boolean value that indicates whether the analysis finds text at the specified point.
- [func hasDataDetector(at: CGPoint) -> Bool](imageanalysisinteraction/hasdatadetector(at:).md)
  Returns a Boolean value that indicates whether the analysis detects data at the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction/selectedattributedtext)*