# download()

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the listener to download the resource instead of displaying it.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
func download()
```

```objc
- (void) download;
```

## Discussion

This method converts a location change that may be in progress to a download operation without having to stop and restart the download. You might invoke this method based on the content’s MIME type.

## See Also

### Making Resource-Usage Decisions
- [func ignore()](./ignore%28%29.md)
  Tells the listener to ignore the resource.
- [func use()](./use%28%29.md)
  Tells the listener to use the resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpolicydecisionlistener/download())*