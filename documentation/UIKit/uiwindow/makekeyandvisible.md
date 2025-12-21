# makeKeyAndVisible()

**Framework**: UIKit  
**Kind**: method

Shows the window and makes it the key window.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func makeKeyAndVisible()
```

#### Discussion

This is a convenience method to show the current window and position it in front of all other windows at the same level or lower. If you only want to show the window, change its [`isHidden`](uiview/ishidden.md) property to [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var isKeyWindow: Bool](uiwindow/iskeywindow.md)
  A Boolean value that indicates whether the window is the key window.
- [var canBecomeKey: Bool](uiwindow/canbecomekey.md)
  A Boolean value that indicates whether the window can become the key window.
- [func makeKey()](uiwindow/makekey.md)
  Makes the window the key window.
- [func becomeKey()](uiwindow/becomekey.md)
  Tells the window that it’s the key window.
- [func resignKey()](uiwindow/resignkey.md)
  Tells the window that it’s no longer the key window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindow/makekeyandvisible())*