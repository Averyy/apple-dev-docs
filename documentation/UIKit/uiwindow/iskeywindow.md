# isKeyWindow

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the window is the key window.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isKeyWindow: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isKeyWindow) BOOL keyWindow;
```

## Discussion

In iOS 15 and later, the value of this property is [`true`](../../Swift/true.md) when the window is the key window of its scene. In iOS 14 and earlier, the value of this property is [`true`](../../Swift/true.md) when the window is the key window in the app.

The key window receives keyboard and other non-touch-related events. Only one window at a time may be the key window.

## See Also

### Making windows key
- [var canBecomeKey: Bool](./canbecomekey.md)
  A Boolean value that indicates whether the window can become the key window.
- [func makeKeyAndVisible()](./makekeyandvisible%28%29.md)
  Shows the window and makes it the key window.
- [func makeKey()](./makekey%28%29.md)
  Makes the window the key window.
- [func becomeKey()](./becomekey%28%29.md)
  Tells the window that it’s the key window.
- [func resignKey()](./resignkey%28%29.md)
  Tells the window that it’s no longer the key window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindow/iskeywindow)*