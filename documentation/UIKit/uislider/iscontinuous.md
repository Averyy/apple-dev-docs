# isContinuous

**Framework**: UIKit  
**Kind**: property

A Boolean value indicating whether changes in the slider’s value generate continuous update events.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isContinuous: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/Swift/true), the slider triggers the associated target’s action method repeatedly, as the user moves the thumb. If [`false`](https://developer.apple.com/documentation/Swift/false), the slider triggers the associated action method just once, when the user releases the slider’s thumb control to set the final value.

The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var behavioralStyle: UIBehavioralStyle](uislider/behavioralstyle.md)
  The style that determines how the slider behaves.
- [var preferredBehavioralStyle: UIBehavioralStyle](uislider/preferredbehavioralstyle.md)
  The preferred behavioral style.
- [enum UIBehavioralStyle](uibehavioralstyle.md)
  Constants that indicate how a control behaves in apps built with Mac Catalyst.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uislider/iscontinuous)*