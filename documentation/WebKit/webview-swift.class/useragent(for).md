# userAgent(for:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns the appropriate user-agent string for a given URL.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

> **Deprecated**: No longer supported; please adopt WKWebView.

## Declaration

```swift
func userAgent(for URL: URL!) -> String!
```

```objc
- (NSString *) userAgentForURL:(NSURL *) URL;
```

#### Return Value

The user-agent string for a given URL. The user-agent string is used by websites to identify the client browser.

## Parameters

- `URL`: The URL that you need the user-agent string for.

## See Also

### Getting and Setting User-agent Strings
- [var applicationNameForUserAgent: String!](./applicationnameforuseragent.md)
  The receiver’s application name that is used in the user-agent string.
- [var customUserAgent: String!](./customuseragent.md)
  The receiver’s custom user-agent string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/useragent(for:))*