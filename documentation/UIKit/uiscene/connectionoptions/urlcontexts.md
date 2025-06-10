# urlContexts

**Framework**: UIKit  
**Kind**: property

The URLs to open, along with metadata specifying how to open them.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var urlContexts: Set<UIOpenURLContext> { get }
```

#### Discussion

An empty set indicates that there are no URLs to open.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/connectionoptions/urlcontexts)*