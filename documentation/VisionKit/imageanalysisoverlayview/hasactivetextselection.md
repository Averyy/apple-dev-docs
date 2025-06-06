# hasActiveTextSelection

**Framework**: Visionkit  
**Kind**: property

A Boolean value that indicates whether a person or the app has text selected within the image.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
final var hasActiveTextSelection: Bool { get }
```

#### Discussion

If [`textSelection`](imageanalysisoverlayview/interactiontypes/textselection.md) is an active interaction type, a person can select text using a standard input method and the app can select text through the [`selectedRanges`](imageanalysisoverlayview/selectedranges.md) property. If neither a person nor the app select any text, then this property returns `false`.

## See Also

- [var text: String](imageanalysisoverlayview/text.md)
  The text contents of the current image analysis.
- [var selectedText: String](imageanalysisoverlayview/selectedtext.md)
  The current selected text.
- [var selectedAttributedText: AttributedString](imageanalysisoverlayview/selectedattributedtext.md)
  The current selected attributed text.
- [func analysisHasText(at: CGPoint) -> Bool](imageanalysisoverlayview/analysishastext(at:).md)
  Returns a Boolean value that indicates whether the analysis finds text at the specified point.
- [func hasText(at: CGPoint) -> Bool](imageanalysisoverlayview/hastext(at:).md)
  Returns a Boolean value that indicates whether active text exists at the specified point.
- [func hasDataDetector(at: CGPoint) -> Bool](imageanalysisoverlayview/hasdatadetector(at:).md)
  Returns a Boolean value that indicates whether the analysis detects data at the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/hasactivetextselection)*