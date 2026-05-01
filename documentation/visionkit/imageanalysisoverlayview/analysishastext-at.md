# analysisHasText(at:)

**Framework**: VisionKit  
**Kind**: method

Returns a Boolean value that indicates whether the analysis finds text at the specified point.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
final func analysisHasText(at point: CGPoint) -> Bool
```

#### Return Value

`true` if text exists at point; otherwise, `false`.

## Parameters

- `point`: A point in the image, in view coordinates.

## See Also

- [var text: String](imageanalysisoverlayview/text.md)
  The text contents of the current image analysis.
- [var selectedText: String](imageanalysisoverlayview/selectedtext.md)
  The current selected text.
- [var selectedAttributedText: AttributedString](imageanalysisoverlayview/selectedattributedtext.md)
  The current selected attributed text.
- [var hasActiveTextSelection: Bool](imageanalysisoverlayview/hasactivetextselection.md)
  A Boolean value that indicates whether a person or the app has text selected within the image.
- [func hasText(at: CGPoint) -> Bool](imageanalysisoverlayview/hastext(at:).md)
  Returns a Boolean value that indicates whether active text exists at the specified point.
- [func hasDataDetector(at: CGPoint) -> Bool](imageanalysisoverlayview/hasdatadetector(at:).md)
  Returns a Boolean value that indicates whether the analysis detects data at the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/analysishastext(at:))*