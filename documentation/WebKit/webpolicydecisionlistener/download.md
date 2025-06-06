# download()

**Framework**: Webkit  
**Kind**: method  
**Required**: Yes

Tells the listener to download the resource instead of displaying it.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func download()
```

#### Discussion

This method converts a location change that may be in progress to a download operation without having to stop and restart the download. You might invoke this method based on the content’s MIME type.

## See Also

- [func ignore()](webpolicydecisionlistener/ignore.md)
  Tells the listener to ignore the resource.
- [func use()](webpolicydecisionlistener/use.md)
  Tells the listener to use the resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpolicydecisionlistener/download())*