# searchSuggestions

**Framework**: UIKit  
**Kind**: property

A list of suggestions to offer as shortcuts below the search field.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var searchSuggestions: [any UISearchSuggestion]? { get set }
```

## Mentions

- [Building a desktop-class iPad app](building-a-desktop-class-ipad-app.md)

#### Discussion

Provide search suggestions to help people complete their query quickly. Update the suggestions as a person types by registering for the [`textDidChangeNotification`](uitextfield/textdidchangenotification.md) notification and implementing [`textFieldDidEndEditing(_:reason:)`](uitextfielddelegate/textfielddidendediting(_:reason:).md).

The suggestions appear in a menu under the search field. When you assign new suggestions to this property, the suggestions onscreen refresh automatically. When a person chooses a suggestion, the system sets this property to `nil` and dismisses the search suggestions menu. Implement [`searchTextField(_:didSelect:)`](uisearchtextfielddelegate/searchtextfield(_:didselect:).md) in your delegate to execute any necessary updates when a person chooses a suggestion.

If the search suggestions menu dismisses for other reasons, such as a person tapping outside the search bar, [`searchSuggestions`](uisearchtextfield/searchsuggestions.md) doesn’t reset to `nil` immediately. The system sets [`searchSuggestions`](uisearchtextfield/searchsuggestions.md) to `nil` only when a person interacts with search directly — for example, by typing in the search field, canceling search, or changing the search scope using the search bar’s scope bar. To dismiss the menu manually, set this property to `nil` or `[]`.

> ❗ **Important**:  UIKit allows setting this property directly on an instance of [`UISearchTextField`](uisearchtextfield.md) only when the search field isn’t associated with a [`UISearchController`](uisearchcontroller.md). If the search field is associated with a search controller, the system raises an [`invalidArgumentException`](https://developer.apple.com/documentation/foundation/nsexceptionname/1415426-invalidargumentexception) to use the [`searchSuggestions`](uisearchcontroller/searchsuggestions.md) property on [`UISearchController`](uisearchcontroller.md) instead.

 UIKit allows setting this property directly on an instance of [`UISearchTextField`](uisearchtextfield.md) only when the search field isn’t associated with a [`UISearchController`](uisearchcontroller.md). If the search field is associated with a search controller, the system raises an [`invalidArgumentException`](https://developer.apple.com/documentation/foundation/nsexceptionname/1415426-invalidargumentexception) to use the [`searchSuggestions`](uisearchcontroller/searchsuggestions.md) property on [`UISearchController`](uisearchcontroller.md) instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchtextfield/searchsuggestions)*