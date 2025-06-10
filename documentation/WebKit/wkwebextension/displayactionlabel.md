# displayActionLabel

**Framework**: WebKit  
**Kind**: property

The default localized extension action label.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var displayActionLabel: String? { get }
```

#### Discussion

Returns `nil` if there was no default action label specified.

This label serves as a default and should be used to represent the extension in contexts like action sheets or toolbars prior to the extension being loaded into an extension context. Once the extension is loaded, use the [`action(for:)`](wkwebextensioncontext/action(for:).md) API to get the tab-specific label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/displayactionlabel)*