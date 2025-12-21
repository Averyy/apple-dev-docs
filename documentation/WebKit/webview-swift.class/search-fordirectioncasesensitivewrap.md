# search(for:direction:caseSensitive:wrap:)

**Framework**: WebKit  
**Kind**: method

Searches a document view for a string and highlights it if it is found.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func search(for string: String!, direction forward: Bool, caseSensitive caseFlag: Bool, wrap wrapFlag: Bool) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the search is successful; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

The search for `string` begins from the current selection and continues in the direction specified by `forward`. The search continues across all frames.

## Parameters

- `string`: The search string.
- `forward`: If   the direction of the search is forward; if  , the direction is backward.
- `caseFlag`: If   if the search is case sensitive; otherwise, it is not.
- `wrapFlag`: If   if the search wraps; otherwise, it does not.

## See Also

- [var applicationNameForUserAgent: String!](webview-swift.class/applicationnameforuseragent.md)
  The receiver’s application name that is used in the user-agent string.
- [var customUserAgent: String!](webview-swift.class/customuseragent.md)
  The receiver’s custom user-agent string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/search(for:direction:casesensitive:wrap:))*