# caseSensitive

**Framework**: WebKit  
**Kind**: property

A Boolean value that indicates whether to consider case when matching the search string.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var caseSensitive: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the web view takes case into account when matching the search string. The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var backwards: Bool](wkfindconfiguration/backwards.md)
  A Boolean value that indicates the search direction, relative to the current selection.
- [var wraps: Bool](wkfindconfiguration/wraps.md)
  A Boolean value that indicates whether the search wraps around to the other side of the page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkfindconfiguration/casesensitive)*