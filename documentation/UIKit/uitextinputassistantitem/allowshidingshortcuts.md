# allowsHidingShortcuts

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the user can hide the shortcuts bar.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var allowsHidingShortcuts: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the user may hide the shortcuts bar when the keyboard is visible. When the value is [`false`](https://developer.apple.com/documentation/Swift/false), the shortcuts bar remains visible while the keyboard is visible. The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var leadingBarButtonGroups: [UIBarButtonItemGroup]](uitextinputassistantitem/leadingbarbuttongroups.md)
  The array of button item groups to display before the typing suggestions.
- [var trailingBarButtonGroups: [UIBarButtonItemGroup]](uitextinputassistantitem/trailingbarbuttongroups.md)
  The array of button item groups to display after the typing suggestions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputassistantitem/allowshidingshortcuts)*