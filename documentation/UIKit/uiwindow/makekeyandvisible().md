# makeKeyAndVisible()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Shows the window and makes it the key window.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func makeKeyAndVisible()
```

```objc
- (void) makeKeyAndVisible;
```

#### Discussion

This is a convenience method to show the current window and position it in front of all other windows at the same level or lower. If you only want to show the window, change its [`isHidden`](../uiview/ishidden.md) property to [`false`](../../Swift/false.md).

## See Also

### Making windows key
- [var isKeyWindow: Bool](./iskeywindow.md)
  A Boolean value that indicates whether the window is the key window.
- [var canBecomeKey: Bool](./canbecomekey.md)
  A Boolean value that indicates whether the window can become the key window.
- [func makeKey()](./makekey%28%29.md)
  Makes the window the key window.
- [func becomeKey()](./becomekey%28%29.md)
  Tells the window that it’s the key window.
- [func resignKey()](./resignkey%28%29.md)
  Tells the window that it’s no longer the key window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindow/makekeyandvisible())*