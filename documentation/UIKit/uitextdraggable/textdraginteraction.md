# textDragInteraction

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The drag interaction object added by UIKit to the text view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var textDragInteraction: UIDragInteraction? { get }
```

```objc
@property (nonatomic, readonly, nullable) UIDragInteraction * textDragInteraction;
```

#### Discussion

You can set the text drag interaction’s [`isEnabled`](../uidraginteraction/isenabled.md) property to [`false`](../../Swift/false.md) if you need to explicitly turn off drag interactions for a UIKit-provided text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdraggable/textdraginteraction)*