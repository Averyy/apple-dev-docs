# hasInjectedContent

**Framework**: Webkit  
**Kind**: property

A Boolean value indicating whether the extension has script or stylesheet content that can be injected into webpages.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var hasInjectedContent: Bool { get }
```

#### Discussion

If this property is `YES`, the extension has content that can be injected by matching against the extension’s requested match patterns.

## See Also

- [func hasInjectedContent(for: URL) -> Bool](wkwebextensioncontext/hasinjectedcontent(for:).md)
  Checks if the extension has script or stylesheet content that can be injected into the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/hasinjectedcontent)*