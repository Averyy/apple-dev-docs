# hasDataDetector(at:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the analysis detects data at the specified point.

**Availability**:
- macOS 13.0+

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

### Accessing text information
- [var text: String](./text.md)
  The text contents of the current image analysis.
- [var selectedText: String](./selectedtext.md)
  The current selected text.
- [var selectedAttributedText: AttributedString](./selectedattributedtext.md)
  The current selected attributed text.
- [var hasActiveTextSelection: Bool](./hasactivetextselection.md)
  A Boolean value that indicates whether a person or the app has text selected within the image.
- [func analysisHasText(at: CGPoint) -> Bool](./analysishastext%28at%29.md)
  Returns a Boolean value that indicates whether the analysis finds text at the specified point.
- [func hasText(at: CGPoint) -> Bool](./hastext%28at%29.md)
  Returns a Boolean value that indicates whether active text exists at the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/hasdatadetector(at:))*