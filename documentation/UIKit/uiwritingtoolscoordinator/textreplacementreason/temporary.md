# UIWritingToolsCoordinator.TextReplacementReason.temporary

**Framework**: UIKit  
**Kind**: case

An option to replace the text in your view when a grammar suggestion is temporarily shown to preview the proposed change in the text.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case temporary
```

#### Discussion

When the user interacts with a grammar issue and the UI is shown, in some cases the suggestion needs to be shown temporarily. Update your view’s text storage without animating the change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/textreplacementreason/temporary)*