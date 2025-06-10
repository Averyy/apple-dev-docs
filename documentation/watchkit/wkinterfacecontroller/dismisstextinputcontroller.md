# dismissTextInputController()

**Framework**: WatchKit  
**Kind**: method

Dismisses the text input controller without returning any text.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
func dismissTextInputController()
```

#### Discussion

Use this method to cancel a text input operation without accepting any input from the user. Dismissing the interface controller animates it off the screen and does not call the associated completion block.

## See Also

- [func presentTextInputController(withSuggestions: [String]?, allowedInputMode: WKTextInputMode, completion: ([Any]?) -> Void)](wkinterfacecontroller/presenttextinputcontroller(withsuggestions:allowedinputmode:completion:).md)
  Displays a modal interface for gathering text input from the user.
- [func presentTextInputControllerWithSuggestions(forLanguage: ((String) -> [Any]?)?, allowedInputMode: WKTextInputMode, completion: ([Any]?) -> Void)](wkinterfacecontroller/presenttextinputcontrollerwithsuggestions(forlanguage:allowedinputmode:completion:).md)
  Displays a modal interface for gathering language-specific text input from the user.
- [enum WKTextInputMode](wktextinputmode.md)
  The input modes supported by the text input controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismisstextinputcontroller())*