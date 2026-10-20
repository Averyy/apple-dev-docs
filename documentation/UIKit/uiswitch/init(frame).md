# init(frame:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a switch control.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(frame: CGRect)
```

```objc
- (instancetype) initWithFrame:(CGRect) frame;
```

#### Return Value

An initialized [`UISwitch`](../uiswitch.md) object.

#### Discussion

[`UISwitch`](../uiswitch.md) overrides [`init(frame:)`](../uiview/init%28frame%29.md) and enforces a size appropriate for the control.

## Parameters

- `frame`: A rectangle defining the frame of the [`UISwitch`](../uiswitch.md) object. The size components of this rectangle are ignored.

## See Also

### Creating a switch
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a switch control from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiswitch/init(frame:))*