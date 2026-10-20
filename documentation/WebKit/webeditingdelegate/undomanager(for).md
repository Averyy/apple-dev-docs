# undoManager(for:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns the undo manager to be used by a web view.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
optional func undoManager(for webView: WebView!) -> UndoManager!
```

```objc
- (NSUndoManager *) undoManagerForWebView:(WebView *) webView;
```

#### Return Value

The undo manager.

## Parameters

- `webView`: The web view that the user is editing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webeditingdelegate/undomanager(for:))*