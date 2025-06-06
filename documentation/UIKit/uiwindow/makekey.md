# makeKey()

**Framework**: UIKit  
**Kind**: method

Makes the window the key window.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func makeKey()
```

#### Discussion

Use this method to make the window key without changing its visibility. The key window receives keyboard and other non-touch related events. This method causes the previous key window to resign the key status.

## See Also

- [var isKeyWindow: Bool](uiwindow/iskeywindow.md)
  A Boolean value that indicates whether the window is the key window.
- [var canBecomeKey: Bool](uiwindow/canbecomekey.md)
  A Boolean value that indicates whether the window can become the key window.
- [func makeKeyAndVisible()](uiwindow/makekeyandvisible.md)
  Shows the window and makes it the key window.
- [func becomeKey()](uiwindow/becomekey.md)
  Tells the window that it’s the key window.
- [func resignKey()](uiwindow/resignkey.md)
  Tells the window that it’s no longer the key window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindow/makekey())*