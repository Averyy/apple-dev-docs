# viewWillMove(toHostWindow:)

**Framework**: Webkit  
**Kind**: method  
**Required**: Yes

Invoked when a web view’s host window is about to change.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func viewWillMove(toHostWindow hostWindow: NSWindow!)
```

## Parameters

- `hostWindow`: The new host window for the view.

## See Also

- [var hostWindow: NSWindow!](webview/hostwindow.md)
  The receiver’s host window.
- [func viewDidMoveToHostWindow()](webdocumentview/viewdidmovetohostwindow.md)
  Invoked when a web view’s host window is set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdocumentview/viewwillmove(tohostwindow:))*