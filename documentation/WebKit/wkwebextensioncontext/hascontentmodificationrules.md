# hasContentModificationRules

**Framework**: WebKit  
**Kind**: property

A boolean value indicating whether the extension includes rules used for content modification or blocking.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var hasContentModificationRules: Bool { get }
```

#### Discussion

This includes both static rules available in the extension’s manifest and dynamic rules applied during a browsing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/hascontentmodificationrules)*