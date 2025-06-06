# UISearchToken

**Framework**: UIKit  
**Kind**: class

Search criteria in a search text field, represented by text and an optional icon.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UISearchToken
```

#### Overview

Use search tokens to help users understand and edit complex search queries in a [`UISearchTextField`](uisearchtextfield.md). A token acts like a single character in standard text interactions such as deleting, selecting, or dragging. A search token should always have text and may also have an icon.

![Screenshot of a search window with a red circle and the words “Red Flowers Carnation”. The red dot and “Red Flowers” are in a gray box labeled as a UISearchToken and “Carnation” is labeled as text. ](https://docs-assets.developer.apple.com/published/b20153ea69c598fc17ea2dd6e004c6c5/media-3539104%402x.png)

Assign a [`representedObject`](uisearchtoken/representedobject.md) to each search token that’s meaningful to your app. By attaching this extra data to the token you can reconstruct the full search query using information available in the search field when, for example, your app starts from state restoration or the user starts a search.

See [`Using suggested searches with a search controller`](using-suggested-searches-with-a-search-controller.md) to learn how to use search tokens.

## Topics

### Creating a search token
- [init(icon: UIImage?, text: String)](uisearchtoken/init(icon:text:).md)
  Creates a search token with the specified text and icon (if any).
- [var representedObject: Any?](uisearchtoken/representedobject.md)
  The object represented by the search token.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UISearchTextField](uisearchtextfield.md)
  A view for displaying and editing text and search tokens.
- [protocol UISearchTextFieldDelegate](uisearchtextfielddelegate.md)
  The interface for the delegate of a search field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchtoken)*