# checkSpelling(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

An action method that searches for a misspelled word in the receiver.

**Availability**:
- macOS

## Declaration

```swift
func checkSpelling(_ sender: Any?)
```

```objc
- (void) checkSpelling:(id) sender;
```

#### Discussion

This action method starts a search at the end of the selection and continues until it reaches a word suspected of being misspelled or the end of the content. If a word isn’t recognized by the spelling server, a [`showGuessPanel(_:)`](./showguesspanel%28_%29.md) message is sent to the receiver which opens the Guess panel and allows the user to make a correction or add the word to the local dictionary.

## Parameters

- `sender`: The object that sent this message.

## See Also

### Spell-checking Action Methods
- [func showGuessPanel(Any?)](./showguesspanel%28_%29.md)
  An action method that shows a spelling correction panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/checkspelling(_:))*