# startSpeaking(_:)

**Framework**: WebKit  
**Kind**: method

An action method that starts speaking the selected text or all text if there’s no selection.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func startSpeaking(_ sender: Any?)
```

#### Discussion

Speech continues asynchronously until the end of the text or until terminated by invoking the [`stopSpeaking(_:)`](webview-swift.class/stopspeaking(_:).md) method. This method behaves similar to the [`startSpeaking(_:)`](https://developer.apple.com/documentation/AppKit/NSTextView/startSpeaking(_:)) method in [`NSTextView`](https://developer.apple.com/documentation/AppKit/NSTextView).

## Parameters

- `sender`: The object that sent this message.

## See Also

- [func stopSpeaking(Any?)](webview-swift.class/stopspeaking(_:).md)
  An action method that stops speaking that is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/startspeaking(_:))*