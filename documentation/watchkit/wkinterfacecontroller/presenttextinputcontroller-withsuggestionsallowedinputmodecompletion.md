# presentTextInputController(withSuggestions:allowedInputMode:completion:)

**Framework**: Watchkit  
**Kind**: method

Displays a modal interface for gathering text input from the user.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
func presentTextInputController(withSuggestions suggestions: [String]?, allowedInputMode inputMode: WKTextInputMode) async -> [Any]?
```

## Mentions

- [Navigating Between Scenes](navigating-between-scenes.md)

#### Discussion

This method executes asynchronously, returning shortly after you call it. During a subsequent run loop cycle, the system displays a text input controller to the user. The input controller displays the list of input phrases you specify and provides options to enter new text phrases through dictation or to select from a list of emoji.

When the user accepts a value or cancels input, the text input controller dismisses itself and then executes the block in the `completion` parameter on the WatchKit extension’s main thread. Use the block to retrieve the accepted value and apply it to your content. The presenting interface controller is activated before the block is executed.

Always call this method from your WatchKit extension’s main thread.

## Parameters

- `suggestions`: An array of   objects, each of which contains a suggested phrase for input. The user can either select one of the phrases you suggest or input a new text phrase.
- `inputMode`: The type of input to allow. For a list of possible values, see  .
- `completion`: The block to execute after the user dismisses the modal interface. This block has no return value and takes the following parameter:

## See Also

- [func presentTextInputControllerWithSuggestions(forLanguage: ((String) -> [Any]?)?, allowedInputMode: WKTextInputMode, completion: ([Any]?) -> Void)](wkinterfacecontroller/presenttextinputcontrollerwithsuggestions(forlanguage:allowedinputmode:completion:).md)
  Displays a modal interface for gathering language-specific text input from the user.
- [func dismissTextInputController()](wkinterfacecontroller/dismisstextinputcontroller.md)
  Dismisses the text input controller without returning any text.
- [enum WKTextInputMode](wktextinputmode.md)
  The input modes supported by the text input controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presenttextinputcontroller(withsuggestions:allowedinputmode:completion:))*