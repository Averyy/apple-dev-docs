# stripTextColorFromPreviews

**Framework**: UIKit  
**Kind**: property

Strips the foreground and background colors for a system-provided text drag preview.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
static var stripTextColorFromPreviews: UITextDragOptions { get }
```

#### Discussion

When the system creates a preview for a text drag operation, the preview keeps the foreground and background text colors. Using the [`stripTextColorFromPreviews`](uitextdragoptions/striptextcolorfrompreviews.md) option strips away those colors, leaving the preview with black text on a clear background. This option changes only the preview, not the view used to create the preview. Also, this option doesn’t affect any images included in the preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdragoptions/striptextcolorfrompreviews)*