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

> **Note**: Once the extension is loaded, use the [`hasInjectedContent`](wkwebextension/hasinjectedcontent.md) property on an extension context, as the injectable content can change after the extension is loaded.

Once the extension is loaded, use the [`hasInjectedContent`](wkwebextension/hasinjectedcontent.md) property on an extension context, as the injectable content can change after the extension is loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/hasinjectedcontent)*