# onSuggestionSelected

**Framework**: TVMLKit JS  
**Kind**: instp

A function the system calls when the user selects a suggestion on a search field.

**Availability**:
- tvOS 14.0+

## Declaration

```swift
attribute function onSuggestionSelected;
```

#### Discussion

Provide a callback function for the [`onSuggestionSelected`](keyboard/3678707-onsuggestionselected.md) attribute to respond to the user selecting one of a `searchField`’s [`suggestions`](keyboard/3589336-suggestions.md). This value of this attribute must be a function; for example, k`eyboard.onSuggestionSelected = function (searchTerm) {}`.

## See Also

- [suggestions](keyboard/3589336-suggestions.md)
  Search parameters to offer as shortcuts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/keyboard/3678707-onsuggestionselected)*