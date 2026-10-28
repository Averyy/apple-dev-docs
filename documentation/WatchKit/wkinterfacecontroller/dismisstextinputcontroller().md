# dismissTextInputController()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Dismisses the text input controller without returning any text.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func dismissTextInputController()
```

```objc
- (void) dismissTextInputController;
```

## Discussion

Use this method to cancel a text input operation without accepting any input from the user. Dismissing the interface controller animates it off the screen and does not call the associated completion block.

## See Also

### Handling text input
- [func presentTextInputController(withSuggestions: [String]?, allowedInputMode: WKTextInputMode, completion: ([Any]?) -> Void)](./presenttextinputcontroller%28withsuggestions,allowedinputmode,completion%29.md)
  Displays a modal interface for gathering text input from the user.
- [func presentTextInputControllerWithSuggestions(forLanguage: ((String) -> [Any]?)?, allowedInputMode: WKTextInputMode, completion: ([Any]?) -> Void)](./presenttextinputcontrollerwithsuggestions%28forlanguage,allowedinputmode,completion%29.md)
  Displays a modal interface for gathering language-specific text input from the user.
- [enum WKTextInputMode](../wktextinputmode.md)
  The input modes supported by the text input controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismisstextinputcontroller())*