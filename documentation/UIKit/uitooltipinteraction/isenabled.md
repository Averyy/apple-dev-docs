# isEnabled

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the tooltip interaction is in the enabled state.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
var isEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isEnabled) BOOL enabled;
```

## Discussion

A view or control can only display a tooltip from an enabled interaction. Set the value of the [`isEnabled`](./isenabled.md) property to [`true`](../../Swift/true.md) to enable the interaction or [`false`](../../Swift/false.md) to disable it. The default value is [`true`](../../Swift/true.md).

## See Also

### Managing the interaction
- [var defaultToolTip: String?](./defaulttooltip.md)
  The text that appears in a tooltip by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitooltipinteraction/isenabled)*