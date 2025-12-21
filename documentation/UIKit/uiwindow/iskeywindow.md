# isKeyWindow

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the window is the key window.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isKeyWindow: Bool { get }
```

#### Discussion

In iOS 15 and later, the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) when the window is the key window of its scene. In iOS 14 and earlier, the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) when the window is the key window in the app.

The key window receives keyboard and other non-touch-related events. Only one window at a time may be the key window.

## See Also

- [var canBecomeKey: Bool](uiwindow/canbecomekey.md)
  A Boolean value that indicates whether the window can become the key window.
- [func makeKeyAndVisible()](uiwindow/makekeyandvisible.md)
  Shows the window and makes it the key window.
- [func makeKey()](uiwindow/makekey.md)
  Makes the window the key window.
- [func becomeKey()](uiwindow/becomekey.md)
  Tells the window that it’s the key window.
- [func resignKey()](uiwindow/resignkey.md)
  Tells the window that it’s no longer the key window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindow/iskeywindow)*