# ignore()

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the listener to ignore the resource.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
func ignore()
```

```objc
- (void) ignore;
```

## Discussion

You might invoke this method to handle the resource request yourself. For example, you might want to open a new window, open a window behind the current window, open a URL in an external application, or show a file URL location in the Finder.

## See Also

### Making Resource-Usage Decisions
- [func download()](./download%28%29.md)
  Tells the listener to download the resource instead of displaying it.
- [func use()](./use%28%29.md)
  Tells the listener to use the resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpolicydecisionlistener/ignore())*