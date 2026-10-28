# Keyboard

**Framework**: TVMLKit JS  
**Kind**: cl  
**Role**: Class

An object used to retrieve user input from search fields and text fields.

**Availability**:
- tvOS 9.0+

## Declaration

```
interface Keyboard
```

## Overview

Use the `getFeature` function with the feature name `Keyboard` to retrieve an instance of this class from the `searchField` and `textField` elements, as in, for example, `getFeature('Keyboard')`.

## Topics

### Setting and Retrieving Text
- [text](./keyboard/api-1627359-text.md)
  The text inside a search or text field.
- [onTextChange](./keyboard/api-1627355-ontextchange.md)
  A function the system calls when the text in a search or text field changes.
### Providing and Handling Search Suggestions
- [suggestions](./keyboard/api-3589336-suggestions.md)
  Search parameters to offer as shortcuts.
- [onSuggestionSelected](./keyboard/api-3678707-onsuggestionselected.md)
  A function the system calls when the user selects a suggestion on a search field.

## See Also

### Element Access
- [MenuBarDocument](./menubardocument.md)
  An object used for setting and retrieving documents associated with a menu item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/keyboard)*