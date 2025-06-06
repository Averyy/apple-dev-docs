# setActive(_:animated:)

**Framework**: UIKit  
**Kind**: method

Displays or hides the search interface, optionally with animation.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func setActive(_ visible: Bool, animated: Bool)
```

#### Discussion

When the user focus in the search field of a managed search bar, the search display controller automatically displays the search interface. You can use this method to force the search interface to appear.

## Parameters

- `visible`:   to display the search interface if it is not already displayed;   to hide the search interface if it is currently displayed.
- `animated`:   to use animation for a change in visible state, otherwise  .

## See Also

- [var isActive: Bool](uisearchdisplaycontroller/isactive.md)
  The visibility state of the search interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/setactive(_:animated:))*