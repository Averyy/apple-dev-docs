# matchFound

**Framework**: WebKit  
**Kind**: property

A Boolean value that indicates whether the web view found a match during the search.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var matchFound: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if the web view found a match, or [`false`](https://developer.apple.com/documentation/Swift/false) if it didn’t.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkfindresult/matchfound)*