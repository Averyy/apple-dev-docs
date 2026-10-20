# becomeKey()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the window that it’s the key window.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func becomeKey()
```

```objc
- (void) becomeKeyWindow;
```

#### Discussion

Never call this method directly. The system calls this method and posts [`didBecomeKeyNotification`](./didbecomekeynotification.md) to let the window know that it’s the key window. The default implementation of this method does nothing, but subclasses can override it and use it to perform tasks related to becoming the key window.

In iOS 15 and later, the system calls this method when the window becomes the key window in its scene. In iOS 14 and earlier, the system calls this method when the window becomes the key window in the app.

## See Also

### Making windows key
- [var isKeyWindow: Bool](./iskeywindow.md)
  A Boolean value that indicates whether the window is the key window.
- [var canBecomeKey: Bool](./canbecomekey.md)
  A Boolean value that indicates whether the window can become the key window.
- [func makeKeyAndVisible()](./makekeyandvisible%28%29.md)
  Shows the window and makes it the key window.
- [func makeKey()](./makekey%28%29.md)
  Makes the window the key window.
- [func resignKey()](./resignkey%28%29.md)
  Tells the window that it’s no longer the key window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindow/becomekey())*