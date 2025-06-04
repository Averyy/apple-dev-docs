# dismissTextInputController()

**Framework**: Watchkit  
**Kind**: method

Dismisses the text input controller without returning any text.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor func dismissTextInputController()
```

## Overview

Use this method to cancel a text input operation without accepting any input from the user. Dismissing the interface controller animates it off the screen and does not call the associated completion block.

## See Also

- [func presentTextInputController(withSuggestions: [String]?, allowedInputMode: WKTextInputMode, completion: ([Any]?) -> Void)](presenttextinputcontroller(withsuggestions:allowedinputmode:completion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presenttextinputcontroller(withsuggestions:allowedinputmode:completion:)))
- [func presentTextInputControllerWithSuggestions(forLanguage: ((String) -> [Any]?)?, allowedInputMode: WKTextInputMode, completion: ([Any]?) -> Void)](presenttextinputcontrollerwithsuggestions(forlanguage:allowedinputmode:completion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presenttextinputcontrollerwithsuggestions(forlanguage:allowedinputmode:completion:)))
- [enum WKTextInputMode](wktextinputmode.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wktextinputmode))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismisstextinputcontroller())*