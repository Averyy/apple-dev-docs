# ignoresViewportScaleLimits

**Framework**: WebKit  
**Kind**: property

A Boolean value that determines whether a web view allows scaling of the webpage.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var ignoresViewportScaleLimits: Bool { get set }
```

#### Discussion

When set to [`true`](https://developer.apple.com/documentation/swift/true), this property overrides the `user-scalable` HTML property in a webpage, and lets the web view scale its webpage content regardless of the author’s intent. The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var suppressesIncrementalRendering: Bool](wkwebviewconfiguration/suppressesincrementalrendering.md)
  A Boolean value that indicates whether the web view suppresses content rendering until the content is fully loaded into memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/ignoresviewportscalelimits)*