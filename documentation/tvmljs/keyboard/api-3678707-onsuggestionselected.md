# onSuggestionSelected

**Framework**: TVMLKit JS  
**Kind**: instp  
**Role**: Instance Property

A function the system calls when the user selects a suggestion on a search field.

**Availability**:
- tvOS 14.0+

## Declaration

```
attribute function onSuggestionSelected;
```

#### Discussion

Provide a callback function for the [`onSuggestionSelected`](./api-3678707-onsuggestionselected.md) attribute to respond to the user selecting one of a `searchField`’s [`suggestions`](./api-3589336-suggestions.md). This value of this attribute must be a function; for example, k`eyboard.onSuggestionSelected = function (searchTerm) {}`.

## See Also

### Providing and Handling Search Suggestions
- [suggestions](./api-3589336-suggestions.md)
  Search parameters to offer as shortcuts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/keyboard/3678707-onsuggestionselected)*