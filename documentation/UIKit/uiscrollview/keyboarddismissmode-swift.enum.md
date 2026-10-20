# UIScrollView.KeyboardDismissMode

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that determine how the system dismisses the keyboard when a drag begins in the scroll view.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS

## Declaration

```swift
enum KeyboardDismissMode
```

```c
enum UIScrollViewKeyboardDismissMode : NSInteger;
```

#### Overview

You use these constants to set the value of the [`keyboardDismissMode`](./keyboarddismissmode-swift.property.md) property.

## Topics

### Constants
- [UIScrollView.KeyboardDismissMode.none](./keyboarddismissmode-swift.enum/none.md)
  A mode in which a drag doesn’t dismiss the keyboard.
- [UIScrollView.KeyboardDismissMode.onDrag](./keyboarddismissmode-swift.enum/ondrag.md)
  A mode in which the keyboard dismisses when a drag begins.
- [UIScrollView.KeyboardDismissMode.interactive](./keyboarddismissmode-swift.enum/interactive.md)
  A mode in which the keyboard follows the dragging touch offscreen, and can be pulled upward again to cancel the dismiss.
- [UIScrollView.KeyboardDismissMode.onDragWithAccessory](./keyboarddismissmode-swift.enum/ondragwithaccessory.md)
  A mode in which the keyboard and accessory view dismiss together when a drag begins.
- [UIScrollView.KeyboardDismissMode.interactiveWithAccessory](./keyboarddismissmode-swift.enum/interactivewithaccessory.md)
  A mode in which the keyboard and accessory view both follow the dragging touch offscreen, and can be pulled upward again to cancel the dismiss.
### Initializers
- [init?(rawValue: Int)](./keyboarddismissmode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Dismissing the keyboard
- [var keyboardDismissMode: UIScrollView.KeyboardDismissMode](./keyboarddismissmode-swift.property.md)
  The manner in which the system dismisses the keyboard when a drag begins in the scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/keyboarddismissmode-swift.enum)*