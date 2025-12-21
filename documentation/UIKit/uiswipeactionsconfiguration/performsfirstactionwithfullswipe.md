# performsFirstActionWithFullSwipe

**Framework**: UIKit  
**Kind**: property

A Boolean value indicating whether a full swipe automatically performs the first action.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var performsFirstActionWithFullSwipe: Bool { get set }
```

#### Discussion

When this property is set to [`true`](https://developer.apple.com/documentation/Swift/true), a full swipe in the row performs the first action listed in the [`actions`](uiswipeactionsconfiguration/actions.md) property. The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var actions: [UIContextualAction]](uiswipeactionsconfiguration/actions.md)
  The swipe actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiswipeactionsconfiguration/performsfirstactionwithfullswipe)*