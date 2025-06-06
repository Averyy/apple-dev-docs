# suggestions

**Framework**: TVMLKit JS  
**Kind**: instp

Search parameters to offer as shortcuts.

**Availability**:
- tvOS 14.0+

## Declaration

```swift
attribute Array suggestions;
```

#### Discussion

Provide search suggestions to help the user complete their query quickly. Update the suggestions as the user types. This property is only available if the [`Keyboard`](keyboard.md) is associated with a [`searchField`](https://developer.apple.com/documentation/tvml/searchfield).

Each suggestion in this array should have the following properties:

## See Also

- [onSuggestionSelected](keyboard/3678707-onsuggestionselected.md)
  A function the system calls when the user selects a suggestion on a search field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/keyboard/3589336-suggestions)*