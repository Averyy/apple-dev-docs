# search(for:direction:caseSensitive:wrap:)

**Framework**: Webkit  
**Kind**: method  
**Required**: Yes

Searches for a string in a given direction from the current position.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func search(for string: String!, direction forward: Bool, caseSensitive caseFlag: Bool, wrap wrapFlag: Bool) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver contains `string` in the specified direction; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The receiver should select the string if it is found.

## Parameters

- `string`: The string to search for.
- `forward`: If  , the search is in the forward direction from the current location; otherwise, the search is in the backward direction.
- `caseFlag`: If   then the search is case sensitive; otherwise, it is not.
- `wrapFlag`: If  , the search continues from the end of the document to the current location; otherwise, it stops at the end of the document.

## See Also

- [WebKit Objective-C Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/DisplayWebContent.html#//apple_ref/doc/uid/10000164i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdocumentsearching/search(for:direction:casesensitive:wrap:))*