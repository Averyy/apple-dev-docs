# hasActiveTextSelection

**Framework**: VisionKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether a person or the app has text selected within the image.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
final var hasActiveTextSelection: Bool { get }
```

#### Discussion

If [`textSelection`](./interactiontypes/textselection.md) is an active interaction type, a person can select text using a standard input method and the app can select text through the [`selectedRanges`](./selectedranges.md) property. If neither a person nor the app select any text, then this property returns `false`.

## See Also

### Accessing text information
- [var text: String](./text.md)
  The text contents of the current image analysis.
- [var selectedText: String](./selectedtext.md)
  The current selected text.
- [var selectedAttributedText: AttributedString](./selectedattributedtext.md)
  The current selected attributed text.
- [func analysisHasText(at: CGPoint) -> Bool](./analysishastext%28at%29.md)
  Returns a Boolean value that indicates whether the analysis finds text at the specified point.
- [func hasText(at: CGPoint) -> Bool](./hastext%28at%29.md)
  Returns a Boolean value that indicates whether active text exists at the specified point.
- [func hasDataDetector(at: CGPoint) -> Bool](./hasdatadetector%28at%29.md)
  Returns a Boolean value that indicates whether the analysis detects data at the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/hasactivetextselection)*