# actions

**Framework**: UIKit  
**Kind**: property

The swipe actions.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var actions: [UIContextualAction] { get }
```

#### Discussion

The first object in this array corresponds to the default action, which is the action that’s performed in response to a full swipe.

## See Also

- [var performsFirstActionWithFullSwipe: Bool](uiswipeactionsconfiguration/performsfirstactionwithfullswipe.md)
  A Boolean value indicating whether a full swipe automatically performs the first action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiswipeactionsconfiguration/actions)*