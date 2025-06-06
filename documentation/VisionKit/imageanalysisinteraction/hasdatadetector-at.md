# hasDataDetector(at:)

**Framework**: Visionkit  
**Kind**: method

Returns a Boolean value that indicates whether the analysis detects data at the specified point.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
final func hasDataDetector(at point: CGPoint) -> Bool
```

#### Return Value

`true` if the analyzer detects data at `point`; otherwise, `false`.

## Parameters

- `point`: A point in the image, in view coordinates.

## See Also

- [var text: String](imageanalysisinteraction/text.md)
  The text contents of the current image analysis.
- [var selectedText: String](imageanalysisinteraction/selectedtext.md)
  The current selected text.
- [var selectedAttributedText: AttributedString](imageanalysisinteraction/selectedattributedtext.md)
  The current selected attributed text.
- [func hasText(at: CGPoint) -> Bool](imageanalysisinteraction/hastext(at:).md)
  Returns a Boolean value that indicates whether active text exists at the specified point.
- [var hasActiveTextSelection: Bool](imageanalysisinteraction/hasactivetextselection.md)
  A Boolean value that indicates whether a person or the app has text selected within the image.
- [func analysisHasText(at: CGPoint) -> Bool](imageanalysisinteraction/analysishastext(at:).md)
  Returns a Boolean value that indicates whether the analysis finds text at the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction/hasdatadetector(at:))*