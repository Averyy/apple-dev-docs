# pasteDelegate

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The text paste delegate that handles pasting and dropping of text, using item providers.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var pasteDelegate: (any UITextPasteDelegate)? { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextpasteconfigurationsupporting/pastedelegate)*