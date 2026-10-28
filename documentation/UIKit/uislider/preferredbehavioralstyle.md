# preferredBehavioralStyle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The preferred behavioral style.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
var preferredBehavioralStyle: UIBehavioralStyle { get set }
```

```objc
@property (nonatomic) UIBehavioralStyle preferredBehavioralStyle;
```

## Mentions

- [Choosing a user interface idiom for your Mac app](../choosing-a-user-interface-idiom-for-your-mac-app.md)

## Discussion

Use this property to specify the behavioral style for the slider. If the value of the property is [`UIBehavioralStyle.automatic`](../uibehavioralstyle/automatic.md), use the [`behavioralStyle`](./behavioralstyle.md) property to determine the actual style.

The default value for [`preferredBehavioralStyle`](./preferredbehavioralstyle.md) is [`UIBehavioralStyle.automatic`](../uibehavioralstyle/automatic.md). To learn more about behavior styles, see [`UIBehavioralStyle`](../uibehavioralstyle.md).

## See Also

### Modifying the slider’s behavior
- [var isContinuous: Bool](./iscontinuous.md)
  A Boolean value indicating whether changes in the slider’s value generate continuous update events.
- [var behavioralStyle: UIBehavioralStyle](./behavioralstyle.md)
  The style that determines how the slider behaves.
- [enum UIBehavioralStyle](../uibehavioralstyle.md)
  Constants that indicate how a control behaves in apps built with Mac Catalyst.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uislider/preferredbehavioralstyle)*