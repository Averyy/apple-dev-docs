# makeKey()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Makes the window the key window.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func makeKey()
```

```objc
- (void) makeKeyWindow;
```

#### Discussion

Use this method to make the window key without changing its visibility. The key window receives keyboard and other non-touch related events. This method causes the previous key window to resign the key status.

## See Also

### Making windows key
- [var isKeyWindow: Bool](./iskeywindow.md)
  A Boolean value that indicates whether the window is the key window.
- [var canBecomeKey: Bool](./canbecomekey.md)
  A Boolean value that indicates whether the window can become the key window.
- [func makeKeyAndVisible()](./makekeyandvisible%28%29.md)
  Shows the window and makes it the key window.
- [func becomeKey()](./becomekey%28%29.md)
  Tells the window that it’s the key window.
- [func resignKey()](./resignkey%28%29.md)
  Tells the window that it’s no longer the key window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindow/makekey())*