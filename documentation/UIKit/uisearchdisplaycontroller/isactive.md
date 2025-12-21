# isActive

**Framework**: UIKit  
**Kind**: property

The visibility state of the search interface.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var isActive: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

If you set this value directly, any change is performed without animation. Use [`setActive(_:animated:)`](uisearchdisplaycontroller/setactive(_:animated:).md) if a change in state should be animated.

When the user focus in the search field of a managed search bar, the search display controller automatically displays the search interface. You can use this property to force the search interface to appear.

## See Also

- [func setActive(Bool, animated: Bool)](uisearchdisplaycontroller/setactive(_:animated:).md)
  Displays or hides the search interface, optionally with animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/isactive)*