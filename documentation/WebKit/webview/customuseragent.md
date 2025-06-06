# customUserAgent

**Framework**: Webkit  
**Kind**: property

The receiver’s custom user-agent string.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
var customUserAgent: String! { get set }
```

#### Discussion

The custom user-agent string is used for all URLs. If `nil`, then the receiver constructs a user-agent string that produces the best rendering results for each URL.

## See Also

- [func userAgent(for: URL!) -> String!](webview/useragent(for:).md)
  Returns the appropriate user-agent string for a given URL.
- [var applicationNameForUserAgent: String!](webview/applicationnameforuseragent.md)
  The receiver’s application name that is used in the user-agent string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/customuseragent)*