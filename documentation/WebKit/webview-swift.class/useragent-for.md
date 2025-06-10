# userAgent(for:)

**Framework**: WebKit  
**Kind**: method

Returns the appropriate user-agent string for a given URL.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func userAgent(for URL: URL!) -> String!
```

#### Return Value

The user-agent string for a given URL. The user-agent string is used by websites to identify the client browser.

## Parameters

- `URL`: The URL that you need the user-agent string for.

## See Also

- [var applicationNameForUserAgent: String!](webview-swift.class/applicationnameforuseragent.md)
  The receiver’s application name that is used in the user-agent string.
- [var customUserAgent: String!](webview-swift.class/customuseragent.md)
  The receiver’s custom user-agent string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/useragent(for:))*