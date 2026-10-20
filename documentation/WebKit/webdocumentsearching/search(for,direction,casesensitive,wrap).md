# search(for:direction:caseSensitive:wrap:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Searches for a string in a given direction from the current position.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
func search(for string: String!, direction forward: Bool, caseSensitive caseFlag: Bool, wrap wrapFlag: Bool) -> Bool
```

```objc
- (BOOL) searchFor:(NSString *) string direction:(BOOL) forward caseSensitive:(BOOL) caseFlag wrap:(BOOL) wrapFlag;
```

#### Return Value

[`true`](../../Swift/true.md) if the receiver contains `string` in the specified direction; otherwise, [`false`](../../Swift/false.md).

#### Discussion

The receiver should select the string if it is found.

## Parameters

- `string`: The string to search for.
- `forward`: If [`true`](../../Swift/true.md), the search is in the forward direction from the current location; otherwise, the search is in the backward direction.
- `caseFlag`: If [`true`](../../Swift/true.md) then the search is case sensitive; otherwise, it is not.
- `wrapFlag`: If [`true`](../../Swift/true.md), the search continues from the end of the document to the current location; otherwise, it stops at the end of the document.

## See Also

### Related Documentation
- [WebKit Objective-C Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/DisplayWebContent.html#//apple_ref/doc/uid/10000164i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdocumentsearching/search(for:direction:casesensitive:wrap:))*