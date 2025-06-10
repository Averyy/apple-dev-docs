# downloadWindow(forAuthenticationSheet:)

**Framework**: WebKit  
**Kind**: method

Returns the window to be used by the authentication sheet.

**Availability**:
- macOS 10.4+

## Declaration

```swift
optional func downloadWindow(forAuthenticationSheet download: WebDownload!) -> NSWindow!
```

#### Return Value

An [`NSWindow`](https://developer.apple.com/documentation/AppKit/NSWindow) object into which the `WebDownload` object should draw its authentication sheet.

#### Discussion

The default implementation prompts the user for authentication using the standard WebKit authentication panel, as either a sheet or window.

## Parameters

- `download`: The download object that is requesting the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdownloaddelegate/downloadwindow(forauthenticationsheet:))*