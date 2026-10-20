# viewWillMove(toHostWindow:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Invoked when a web view’s host window is about to change.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
func viewWillMove(toHostWindow hostWindow: NSWindow!)
```

```objc
- (void) viewWillMoveToHostWindow:(NSWindow *) hostWindow;
```

## Parameters

- `hostWindow`: The new host window for the view.

## See Also

### Related Documentation
- [var hostWindow: NSWindow!](../webview-swift.class/hostwindow.md)
  The receiver’s host window.
### Attaching to a window
- [func viewDidMoveToHostWindow()](./viewdidmovetohostwindow%28%29.md)
  Invoked when a web view’s host window is set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdocumentview/viewwillmove(tohostwindow:))*