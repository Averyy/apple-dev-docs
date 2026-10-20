# setActive(_:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Displays or hides the search interface, optionally with animation.

**Availability**:
- iOS 3.0+ - Deprecated in 8.0
- iPadOS 3.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: UISearchDisplayController has been replaced with UISearchController

## Declaration

```swift
func setActive(_ visible: Bool, animated: Bool)
```

```objc
- (void) setActive:(BOOL) visible animated:(BOOL) animated;
```

#### Discussion

When the user focus in the search field of a managed search bar, the search display controller automatically displays the search interface. You can use this method to force the search interface to appear.

## Parameters

- `visible`: [`true`](../../Swift/true.md) to display the search interface if it is not already displayed; [`false`](../../Swift/false.md) to hide the search interface if it is currently displayed.
- `animated`: [`true`](../../Swift/true.md) to use animation for a change in visible state, otherwise [`false`](../../Swift/false.md).

## See Also

### Displaying the search Interface
- [var isActive: Bool](./isactive.md)
  The visibility state of the search interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/setactive(_:animated:))*