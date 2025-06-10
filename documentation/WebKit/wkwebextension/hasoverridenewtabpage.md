# hasOverrideNewTabPage

**Framework**: WebKit  
**Kind**: property

A Boolean value indicating whether the extension provides an alternative to the default new tab page.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var hasOverrideNewTabPage: Bool { get }
```

#### Discussion

If this property is `YES`, the extension can specify a custom page that can be displayed when a new tab is opened in the app, instead of the default new tab page. The app should prompt the user for permission to use the extension’s new tab page as the default, which can be accessed via [`overrideNewTabPageURL`](wkwebextensioncontext/overridenewtabpageurl.md) on an extension context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/hasoverridenewtabpage)*