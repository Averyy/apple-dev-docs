# WKTextInputMode

**Framework**: WatchKit  
**Kind**: enum

The input modes supported by the text input controller.

**Availability**:
- watchOS ?+

## Declaration

```swift
enum WKTextInputMode
```

## Topics

### Constants
- [WKTextInputMode.plain](wktextinputmode/plain.md)
  Text from dictation and suggestions only. Do not allow emoji of any kind.
- [WKTextInputMode.allowEmoji](wktextinputmode/allowemoji.md)
  Text from dictation and suggestions plus non animated emoji.
- [WKTextInputMode.allowAnimatedEmoji](wktextinputmode/allowanimatedemoji.md)
  Text from dictation and suggestions plus both animated and non animated emoji.
### Initializers
- [init?(rawValue: Int)](wktextinputmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func presentTextInputController(withSuggestions: [String]?, allowedInputMode: WKTextInputMode, completion: ([Any]?) -> Void)](wkinterfacecontroller/presenttextinputcontroller(withsuggestions:allowedinputmode:completion:).md)
  Displays a modal interface for gathering text input from the user.
- [func presentTextInputControllerWithSuggestions(forLanguage: ((String) -> [Any]?)?, allowedInputMode: WKTextInputMode, completion: ([Any]?) -> Void)](wkinterfacecontroller/presenttextinputcontrollerwithsuggestions(forlanguage:allowedinputmode:completion:).md)
  Displays a modal interface for gathering language-specific text input from the user.
- [func dismissTextInputController()](wkinterfacecontroller/dismisstextinputcontroller.md)
  Dismisses the text input controller without returning any text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wktextinputmode)*