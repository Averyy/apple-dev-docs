# textViewportLayoutControllerReceivedSetNeedsLayout(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

`NSTextViewportLayoutControllerDelegate` method that the framework calls when the text viewport layout controller receives a `setNeedsLayout` call. Requires a call to super.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func textViewportLayoutControllerReceivedSetNeedsLayout(_ textViewportLayoutController: NSTextViewportLayoutController)
```

```objc
- (void) textViewportLayoutControllerReceivedSetNeedsLayout:(NSTextViewportLayoutController *) textViewportLayoutController;
```

## Mentions

- [Managing viewport layout and attachment reuse in text views](../managing-viewport-layout-and-attachment-reuse-in-a-text-view-subclass.md)

## See Also

### Customizing viewport layout
- [func viewportBounds(for: NSTextViewportLayoutController) -> CGRect](./viewportbounds%28for%29.md)
  `NSTextViewportLayoutControllerDelegate` method that the framework calls to request the current viewport, which is the view visible bounds plus the overdraw area. Requires a call to super.
- [func textViewportLayoutControllerWillLayout(NSTextViewportLayoutController)](./textviewportlayoutcontrollerwilllayout%28_%29.md)
  `NSTextViewportLayoutControllerDelegate` method that the framework calls when the text viewport layout controller starts its layout process. Requires a call to super.
- [func textViewportLayoutControllerDidLayout(NSTextViewportLayoutController)](./textviewportlayoutcontrollerdidlayout%28_%29.md)
  `NSTextViewportLayoutControllerDelegate` method that the framework calls when the text viewport layout controller finishes its layout process. Requires a call to super.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/textviewportlayoutcontrollerreceivedsetneedslayout(_:))*