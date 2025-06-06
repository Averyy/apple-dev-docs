# applicationNameForUserAgent

**Framework**: Webkit  
**Kind**: property

The receiver’s application name that is used in the user-agent string.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
var applicationNameForUserAgent: String! { get set }
```

#### Discussion

The user-agent is used by websites to identify the client browser.

## See Also

- [func userAgent(for: URL!) -> String!](webview/useragent(for:).md)
  Returns the appropriate user-agent string for a given URL.
- [var customUserAgent: String!](webview/customuseragent.md)
  The receiver’s custom user-agent string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/applicationnameforuseragent)*