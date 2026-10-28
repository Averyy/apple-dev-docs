# stopSpeaking(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

An action method that stops speaking that is in progress.

**Availability**:
- macOS

## Declaration

```swift
func stopSpeaking(_ sender: Any?)
```

```objc
- (void) stopSpeaking:(id) sender;
```

## Discussion

This action method stops speech that was previously started with [`startSpeaking(_:)`](./startspeaking%28_%29.md). This method behaves similar to the [`stopSpeaking(_:)`](../../AppKit/nstextview/stopspeaking%28_%29.md) method in [`NSTextView`](../../AppKit/nstextview.md).

## Parameters

- `sender`: The object that sent this message.

## See Also

### Controlling Speakable Text
- [func startSpeaking(Any?)](./startspeaking%28_%29.md)
  An action method that starts speaking the selected text or all text if there’s no selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/stopspeaking(_:))*