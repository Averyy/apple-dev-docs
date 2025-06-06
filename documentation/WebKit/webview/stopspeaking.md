# stopSpeaking(_:)

**Framework**: Webkit  
**Kind**: method

An action method that stops speaking that is in progress.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func stopSpeaking(_ sender: Any?)
```

#### Discussion

This action method stops speech that was previously started with [`startSpeaking(_:)`](webview/startspeaking(_:).md). This method behaves similar to the [`stopSpeaking(_:)`](https://developer.apple.com/documentation/AppKit/NSTextView/stopSpeaking(_:)) method in [`NSTextView`](https://developer.apple.com/documentation/AppKit/NSTextView).

## Parameters

- `sender`: The object that sent this message.

## See Also

- [func startSpeaking(Any?)](webview/startspeaking(_:).md)
  An action method that starts speaking the selected text or all text if there’s no selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/stopspeaking(_:))*