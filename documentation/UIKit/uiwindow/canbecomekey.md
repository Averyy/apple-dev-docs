# canBecomeKey

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the window can become the key window.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var canBecomeKey: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL canBecomeKeyWindow;
```

#### Discussion

The default value is [`true`](../../Swift/true.md). To indicate that the window can’t become the key window, override [`canBecomeKey`](./canbecomekey.md) and return [`false`](../../Swift/false.md).

## See Also

### Making windows key
- [var isKeyWindow: Bool](./iskeywindow.md)
  A Boolean value that indicates whether the window is the key window.
- [func makeKeyAndVisible()](./makekeyandvisible%28%29.md)
  Shows the window and makes it the key window.
- [func makeKey()](./makekey%28%29.md)
  Makes the window the key window.
- [func becomeKey()](./becomekey%28%29.md)
  Tells the window that it’s the key window.
- [func resignKey()](./resignkey%28%29.md)
  Tells the window that it’s no longer the key window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindow/canbecomekey)*