# UIScrollView.KeyboardDismissMode

**Framework**: UIKit  
**Kind**: enum

Constants that determine how the system dismisses the keyboard when a drag begins in the scroll view.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
enum KeyboardDismissMode
```

#### Overview

You use these constants to set the value of the [`keyboardDismissMode`](uiscrollview/keyboarddismissmode-swift.property.md) property.

## Topics

### Constants
- [UIScrollView.KeyboardDismissMode.none](uiscrollview/keyboarddismissmode-swift.enum/none.md)
  A mode in which a drag doesn’t dismiss the keyboard.
- [UIScrollView.KeyboardDismissMode.onDrag](uiscrollview/keyboarddismissmode-swift.enum/ondrag.md)
  A mode in which the keyboard dismisses when a drag begins.
- [UIScrollView.KeyboardDismissMode.interactive](uiscrollview/keyboarddismissmode-swift.enum/interactive.md)
  A mode in which the keyboard follows the dragging touch offscreen, and can be pulled upward again to cancel the dismiss.
- [UIScrollView.KeyboardDismissMode.onDragWithAccessory](uiscrollview/keyboarddismissmode-swift.enum/ondragwithaccessory.md)
  A mode in which the keyboard and accessory view dismiss together when a drag begins.
- [UIScrollView.KeyboardDismissMode.interactiveWithAccessory](uiscrollview/keyboarddismissmode-swift.enum/interactivewithaccessory.md)
  A mode in which the keyboard and accessory view both follow the dragging touch offscreen, and can be pulled upward again to cancel the dismiss.
### Initializers
- [init?(rawValue: Int)](uiscrollview/keyboarddismissmode-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var keyboardDismissMode: UIScrollView.KeyboardDismissMode](uiscrollview/keyboarddismissmode-swift.property.md)
  The manner in which the system dismisses the keyboard when a drag begins in the scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/keyboarddismissmode-swift.enum)*