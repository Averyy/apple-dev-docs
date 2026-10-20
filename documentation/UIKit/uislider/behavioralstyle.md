# behavioralStyle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The style that determines how the slider behaves.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
var behavioralStyle: UIBehavioralStyle { get }
```

```objc
@property (nonatomic, readonly) UIBehavioralStyle behavioralStyle;
```

#### Discussion

Use this property to determine the actual behavior style when the [`preferredBehavioralStyle`](../uibutton/preferredbehavioralstyle.md) is [`UIBehavioralStyle.automatic`](../uibehavioralstyle/automatic.md).

## See Also

### Modifying the slider’s behavior
- [var isContinuous: Bool](./iscontinuous.md)
  A Boolean value indicating whether changes in the slider’s value generate continuous update events.
- [var preferredBehavioralStyle: UIBehavioralStyle](./preferredbehavioralstyle.md)
  The preferred behavioral style.
- [enum UIBehavioralStyle](../uibehavioralstyle.md)
  Constants that indicate how a control behaves in apps built with Mac Catalyst.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uislider/behavioralstyle)*