# isActive

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The visibility state of the search interface.

**Availability**:
- iOS 3.0+ - Deprecated in 8.0
- iPadOS 3.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UISearchDisplayController`](../uisearchdisplaycontroller.md).

## Declaration

```swift
var isActive: Bool { get set }
```

```objc
@property (nonatomic, getter=isActive) BOOL active;
```

#### Discussion

The default value is [`false`](../../Swift/false.md).

If you set this value directly, any change is performed without animation. Use [`setActive(_:animated:)`](./setactive%28_,animated%29.md) if a change in state should be animated.

When the user focus in the search field of a managed search bar, the search display controller automatically displays the search interface. You can use this property to force the search interface to appear.

## See Also

### Displaying the search Interface
- [func setActive(Bool, animated: Bool)](./setactive%28_,animated%29.md)
  Displays or hides the search interface, optionally with animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/isactive)*