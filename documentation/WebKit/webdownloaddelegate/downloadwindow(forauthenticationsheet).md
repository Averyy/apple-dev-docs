# downloadWindow(forAuthenticationSheet:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns the window to be used by the authentication sheet.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

## Declaration

```swift
optional func downloadWindow(forAuthenticationSheet download: WebDownload!) -> NSWindow!
```

```objc
- (NSWindow *) downloadWindowForAuthenticationSheet:(WebDownload *) download;
```

## Return Value

An [`NSWindow`](../../AppKit/nswindow.md) object into which the `WebDownload` object should draw its authentication sheet.

## Discussion

The default implementation prompts the user for authentication using the standard WebKit authentication panel, as either a sheet or window.

## Parameters

- `download`: The download object that is requesting the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdownloaddelegate/downloadwindow(forauthenticationsheet:))*