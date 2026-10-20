# textViewportLayoutController(_:configureRenderingSurfaceFor:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

`NSTextViewportLayoutControllerDelegate` method that the framework calls when the layout controller lays out a text layout fragment in the UI. Requires a call to super.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func textViewportLayoutController(_ textViewportLayoutController: NSTextViewportLayoutController, configureRenderingSurfaceFor textLayoutFragment: NSTextLayoutFragment)
```

```objc
- (void) textViewportLayoutController:(NSTextViewportLayoutController *) textViewportLayoutController configureRenderingSurfaceForTextLayoutFragment:(NSTextLayoutFragment *) textLayoutFragment;
```

## Mentions

- [Managing viewport layout and attachment reuse in text views](../managing-viewport-layout-and-attachment-reuse-in-a-text-view-subclass.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextview/textviewportlayoutcontroller(_:configurerenderingsurfacefor:))*