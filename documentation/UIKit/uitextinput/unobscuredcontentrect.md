# unobscuredContentRect

**Framework**: UIKit  
**Kind**: property

The visible content region, excluding parts covered by view-specific UI.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- tvOS 26.4+
- visionOS 26.4+

## Declaration

```swift
optional var unobscuredContentRect: CGRect { get }
```

#### Return Value

The visible content rectangle, or CGRectNull if there is no specific constraint.

#### Discussion

Account for scroll position, insets, and any custom UI elements (toolbars, accessories, etc.) that obscure content. The system automatically accounts for keyboard obscuring when editing.

The rectangle is in the `textInputView` coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/unobscuredcontentrect)*