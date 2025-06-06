# behavioralStyle

**Framework**: UIKit  
**Kind**: property

The style that determines how the slider behaves.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var behavioralStyle: UIBehavioralStyle { get }
```

#### Discussion

Use this property to determine the actual behavior style when the [`preferredBehavioralStyle`](uibutton/preferredbehavioralstyle.md) is [`UIBehavioralStyle.automatic`](uibehavioralstyle/automatic.md).

## See Also

- [var isContinuous: Bool](uislider/iscontinuous.md)
  A Boolean value indicating whether changes in the slider’s value generate continuous update events.
- [var preferredBehavioralStyle: UIBehavioralStyle](uislider/preferredbehavioralstyle.md)
  The preferred behavioral style.
- [enum UIBehavioralStyle](uibehavioralstyle.md)
  Constants that indicate how a control behaves in apps built with Mac Catalyst.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uislider/behavioralstyle)*