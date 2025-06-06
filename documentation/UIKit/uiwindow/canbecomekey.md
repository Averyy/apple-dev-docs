# canBecomeKey

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the window can become the key window.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var canBecomeKey: Bool { get }
```

#### Discussion

The default value is [`true`](https://developer.apple.com/documentation/swift/true). To indicate that the window can’t become the key window, override [`canBecomeKey`](uiwindow/canbecomekey.md) and return [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var isKeyWindow: Bool](uiwindow/iskeywindow.md)
  A Boolean value that indicates whether the window is the key window.
- [func makeKeyAndVisible()](uiwindow/makekeyandvisible.md)
  Shows the window and makes it the key window.
- [func makeKey()](uiwindow/makekey.md)
  Makes the window the key window.
- [func becomeKey()](uiwindow/becomekey.md)
  Tells the window that it’s the key window.
- [func resignKey()](uiwindow/resignkey.md)
  Tells the window that it’s no longer the key window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindow/canbecomekey)*