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
- [WKTextInputMode.plain](plain.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wktextinputmode/plain))
  Text from dictation and suggestions only. Do not allow emoji of any kind.
- [WKTextInputMode.allowEmoji](allowemoji.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wktextinputmode/allowemoji))
  Text from dictation and suggestions plus non animated emoji.
- [WKTextInputMode.allowAnimatedEmoji](allowanimatedemoji.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wktextinputmode/allowanimatedemoji))
  Text from dictation and suggestions plus both animated and non animated emoji.
### Initializers
- [init?(rawValue: Int)](init(rawvalue:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wktextinputmode/init(rawvalue:)))

## Relationships

### Conforms To
- BitwiseCopyable ([Apple Docs](https://developer.apple.com/documentation/Swift/BitwiseCopyable))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- RawRepresentable ([Apple Docs](https://developer.apple.com/documentation/Swift/RawRepresentable))
- Sendable ([Apple Docs](https://developer.apple.com/documentation/Swift/Sendable))

## See Also

- [func presentTextInputController(withSuggestions: [String]?, allowedInputMode: WKTextInputMode, completion: ([Any]?) -> Void)](presenttextinputcontroller(withsuggestions:allowedinputmode:completion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presenttextinputcontroller(withsuggestions:allowedinputmode:completion:)))
  Displays a modal interface for gathering text input from the user.
- [func presentTextInputControllerWithSuggestions(forLanguage: ((String) -> [Any]?)?, allowedInputMode: WKTextInputMode, completion: ([Any]?) -> Void)](presenttextinputcontrollerwithsuggestions(forlanguage:allowedinputmode:completion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presenttextinputcontrollerwithsuggestions(forlanguage:allowedinputmode:completion:)))
  Displays a modal interface for gathering language-specific text input from the user.
- [func dismissTextInputController()](dismisstextinputcontroller().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismisstextinputcontroller()))
  Dismisses the text input controller without returning any text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wktextinputmode)*