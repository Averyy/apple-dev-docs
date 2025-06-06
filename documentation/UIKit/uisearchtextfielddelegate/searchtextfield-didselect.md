# searchTextField(_:didSelect:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate when a person selects a search suggestion in the search text field.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func searchTextField(_ searchTextField: UISearchTextField, didSelect suggestion: any UISearchSuggestion)
```

#### Discussion

Implement this method to execute any necessary updates when a person chooses a search suggestion.

## Parameters

- `searchTextField`: The search text field displaying search suggestions.
- `suggestion`: The suggestion a person selects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchtextfielddelegate/searchtextfield(_:didselect:))*