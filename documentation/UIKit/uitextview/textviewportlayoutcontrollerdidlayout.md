# textViewportLayoutControllerDidLayout(_:)

**Framework**: UIKit  
**Kind**: method

`NSTextViewportLayoutControllerDelegate` method that the framework calls when the text viewport layout controller finishes its layout process. Requires a call to super.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func textViewportLayoutControllerDidLayout(_ textViewportLayoutController: NSTextViewportLayoutController)
```

## Mentions

- [Managing viewport layout and attachment reuse in text views](managing-viewport-layout-and-attachment-reuse-in-a-text-view-subclass.md)

## See Also

- [func viewportBounds(for: NSTextViewportLayoutController) -> CGRect](uitextview/viewportbounds(for:).md)
  `NSTextViewportLayoutControllerDelegate` method that the framework calls to request the current viewport, which is the view visible bounds plus the overdraw area. Requires a call to super.
- [func textViewportLayoutControllerWillLayout(NSTextViewportLayoutController)](uitextview/textviewportlayoutcontrollerwilllayout(_:).md)
  `NSTextViewportLayoutControllerDelegate` method that the framework calls when the text viewport layout controller starts its layout process. Requires a call to super.
- [func textViewportLayoutControllerReceivedSetNeedsLayout(NSTextViewportLayoutController)](uitextview/textviewportlayoutcontrollerreceivedsetneedslayout(_:).md)
  `NSTextViewportLayoutControllerDelegate` method that the framework calls when the text viewport layout controller receives a `setNeedsLayout` call. Requires a call to super.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/textviewportlayoutcontrollerdidlayout(_:))*