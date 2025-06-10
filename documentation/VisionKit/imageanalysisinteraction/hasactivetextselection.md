# hasActiveTextSelection

**Framework**: VisionKit  
**Kind**: property

A Boolean value that indicates whether a person or the app has text selected within the image.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
final var hasActiveTextSelection: Bool { get }
```

#### Discussion

If [`textSelection`](imageanalysisinteraction/interactiontypes/textselection.md) is an active interaction type, a person can select text using a standard input method and the app can select text through the [`selectedRanges`](imageanalysisinteraction/selectedranges.md) property. If neither a person nor the app select any text, then this property returns `false`.

## See Also

- [var text: String](imageanalysisinteraction/text.md)
  The text contents of the current image analysis.
- [var selectedText: String](imageanalysisinteraction/selectedtext.md)
  The current selected text.
- [var selectedAttributedText: AttributedString](imageanalysisinteraction/selectedattributedtext.md)
  The current selected attributed text.
- [func hasText(at: CGPoint) -> Bool](imageanalysisinteraction/hastext(at:).md)
  Returns a Boolean value that indicates whether active text exists at the specified point.
- [func analysisHasText(at: CGPoint) -> Bool](imageanalysisinteraction/analysishastext(at:).md)
  Returns a Boolean value that indicates whether the analysis finds text at the specified point.
- [func hasDataDetector(at: CGPoint) -> Bool](imageanalysisinteraction/hasdatadetector(at:).md)
  Returns a Boolean value that indicates whether the analysis detects data at the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction/hasactivetextselection)*