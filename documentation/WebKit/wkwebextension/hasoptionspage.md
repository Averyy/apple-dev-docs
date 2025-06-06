# hasOptionsPage

**Framework**: Webkit  
**Kind**: property

A Boolean value indicating whether the extension has an options page.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var hasOptionsPage: Bool { get }
```

#### Discussion

If this property is `YES`, the extension includes a dedicated options page where users can customize settings. The app should provide access to this page through a user interface element, which can be accessed via [`optionsPageURL`](wkwebextensioncontext/optionspageurl.md) on an extension context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/hasoptionspage)*