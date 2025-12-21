# textDragInteraction

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The drag interaction object added by UIKit to the text view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var textDragInteraction: UIDragInteraction? { get }
```

#### Discussion

You can set the text drag interaction’s [`isEnabled`](uidraginteraction/isenabled.md) property to [`false`](https://developer.apple.com/documentation/Swift/false) if you need to explicitly turn off drag interactions for a UIKit-provided text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdraggable/textdraginteraction)*