# select(_:)

**Framework**: UIKit  
**Kind**: method

Selects the content in your responder.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func select(_ sender: Any?)
```

#### Discussion

UIKit calls this method when the user selects the Select command from an editing menu. The command is used for the targeted selection of content in a view. For example, a text view uses this to select one or more words in the view and to display the selection interface.

## Parameters

- `sender`: The object calling this method.

## See Also

- [func selectAll(Any?)](uiresponderstandardeditactions/selectall(_:).md)
  Selects all of the content in the current responder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/select(_:))*