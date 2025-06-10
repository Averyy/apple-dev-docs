# wraps

**Framework**: WebKit  
**Kind**: property

A Boolean value that indicates whether the search wraps around to the other side of the page.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var wraps: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the search wraps and continues at the other end of the page. For example, when a forward search reaches the bottom of the page, the search wraps back to the top of the page and continues. When a backward search reaches the top of the page, the search wraps back to the bottom of the page. The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var backwards: Bool](wkfindconfiguration/backwards.md)
  A Boolean value that indicates the search direction, relative to the current selection.
- [var caseSensitive: Bool](wkfindconfiguration/casesensitive.md)
  A Boolean value that indicates whether to consider case when matching the search string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkfindconfiguration/wraps)*