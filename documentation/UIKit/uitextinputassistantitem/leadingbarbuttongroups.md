# leadingBarButtonGroups

**Framework**: UIKit  
**Kind**: property

The array of button item groups to display before the typing suggestions.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var leadingBarButtonGroups: [UIBarButtonItemGroup] { get set }
```

#### Discussion

Assigning a value to this property installs the corresponding bar button items so that they lead the typing suggestions. (In a left-to-right environment, leading items are placed to the left of the typing suggestions.) If there is not enough room to display all of the items, UIKit may display a group’s representative item instead, if one was provided.

## See Also

- [var trailingBarButtonGroups: [UIBarButtonItemGroup]](uitextinputassistantitem/trailingbarbuttongroups.md)
  The array of button item groups to display after the typing suggestions.
- [var allowsHidingShortcuts: Bool](uitextinputassistantitem/allowshidingshortcuts.md)
  A Boolean value that indicates whether the user can hide the shortcuts bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputassistantitem/leadingbarbuttongroups)*