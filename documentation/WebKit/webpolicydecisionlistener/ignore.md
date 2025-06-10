# ignore()

**Framework**: WebKit  
**Kind**: method  
**Required**: Yes

Tells the listener to ignore the resource.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func ignore()
```

#### Discussion

You might invoke this method to handle the resource request yourself. For example, you might want to open a new window, open a window behind the current window, open a URL in an external application, or show a file URL location in the Finder.

## See Also

- [func download()](webpolicydecisionlistener/download.md)
  Tells the listener to download the resource instead of displaying it.
- [func use()](webpolicydecisionlistener/use.md)
  Tells the listener to use the resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpolicydecisionlistener/ignore())*