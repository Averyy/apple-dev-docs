# startSpeaking(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

An action method that starts speaking the selected text or all text if there’s no selection.

**Availability**:
- macOS

## Declaration

```swift
func startSpeaking(_ sender: Any?)
```

```objc
- (void) startSpeaking:(id) sender;
```

#### Discussion

Speech continues asynchronously until the end of the text or until terminated by invoking the [`stopSpeaking(_:)`](./stopspeaking%28_%29.md) method. This method behaves similar to the [`startSpeaking(_:)`](../../AppKit/nstextview/startspeaking%28_%29.md) method in [`NSTextView`](../../AppKit/nstextview.md).

## Parameters

- `sender`: The object that sent this message.

## See Also

### Controlling Speakable Text
- [func stopSpeaking(Any?)](./stopspeaking%28_%29.md)
  An action method that stops speaking that is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/startspeaking(_:))*