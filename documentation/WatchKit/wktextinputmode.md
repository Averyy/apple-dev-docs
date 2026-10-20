# WKTextInputMode

**Framework**: WatchKit  
**Kind**: enum  
**Role**: Enumeration

The input modes supported by the text input controller.

**Availability**:
- watchOS

## Declaration

```swift
enum WKTextInputMode
```

```c
enum WKTextInputMode : NSInteger;
```

## Topics

### Constants
- [WKTextInputMode.plain](./wktextinputmode/plain.md)
  Text from dictation and suggestions only. Do not allow emoji of any kind.
- [WKTextInputMode.allowEmoji](./wktextinputmode/allowemoji.md)
  Text from dictation and suggestions plus non animated emoji.
- [WKTextInputMode.allowAnimatedEmoji](./wktextinputmode/allowanimatedemoji.md)
  Text from dictation and suggestions plus both animated and non animated emoji.
### Initializers
- [init?(rawValue: Int)](./wktextinputmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Handling text input
- [func presentTextInputController(withSuggestions: [String]?, allowedInputMode: WKTextInputMode, completion: ([Any]?) -> Void)](./wkinterfacecontroller/presenttextinputcontroller%28withsuggestions,allowedinputmode,completion%29.md)
  Displays a modal interface for gathering text input from the user.
- [func presentTextInputControllerWithSuggestions(forLanguage: ((String) -> [Any]?)?, allowedInputMode: WKTextInputMode, completion: ([Any]?) -> Void)](./wkinterfacecontroller/presenttextinputcontrollerwithsuggestions%28forlanguage,allowedinputmode,completion%29.md)
  Displays a modal interface for gathering language-specific text input from the user.
- [func dismissTextInputController()](./wkinterfacecontroller/dismisstextinputcontroller%28%29.md)
  Dismisses the text input controller without returning any text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wktextinputmode)*