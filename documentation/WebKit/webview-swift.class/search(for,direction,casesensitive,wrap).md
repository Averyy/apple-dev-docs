# search(for:direction:caseSensitive:wrap:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Searches a document view for a string and highlights it if it is found.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

> **Deprecated**: No longer supported; please adopt WKWebView.

## Declaration

```swift
func search(for string: String!, direction forward: Bool, caseSensitive caseFlag: Bool, wrap wrapFlag: Bool) -> Bool
```

```objc
- (BOOL) searchFor:(NSString *) string direction:(BOOL) forward caseSensitive:(BOOL) caseFlag wrap:(BOOL) wrapFlag;
```

#### Return Value

[`true`](../../Swift/true.md) if the search is successful; otherwise, [`false`](../../Swift/false.md).

#### Discussion

The search for `string` begins from the current selection and continues in the direction specified by `forward`. The search continues across all frames.

## Parameters

- `string`: The search string.
- `forward`: If [`true`](../../Swift/true.md) the direction of the search is forward; if [`false`](../../Swift/false.md), the direction is backward.
- `caseFlag`: If [`true`](../../Swift/true.md) if the search is case sensitive; otherwise, it is not.
- `wrapFlag`: If [`true`](../../Swift/true.md) if the search wraps; otherwise, it does not.

## See Also

### Related Documentation
- [var applicationNameForUserAgent: String!](./applicationnameforuseragent.md)
  The receiver’s application name that is used in the user-agent string.
- [var customUserAgent: String!](./customuseragent.md)
  The receiver’s custom user-agent string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/search(for:direction:casesensitive:wrap:))*