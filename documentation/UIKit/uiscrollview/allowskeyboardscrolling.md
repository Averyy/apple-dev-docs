# allowsKeyboardScrolling

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the scroll view allows scrolling its content with hardware keyboard input.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
var allowsKeyboardScrolling: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL allowsKeyboardScrolling;
```

## Discussion

When this value is [`true`](../../Swift/true.md), the scroll view animates its content offset in response to input from hardware keyboard keys like Page Up, Page Down, Home, End, and the arrow keys. The scroll view needs to have focus or be first responder to receive these key events.

The default value is [`true`](../../Swift/true.md) for apps that link against iOS 17 and later. Set this value to [`false`](../../Swift/false.md) to disable the ability to scroll content with hardware keyboard keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/allowskeyboardscrolling)*