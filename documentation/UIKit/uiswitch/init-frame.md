# init(frame:)

**Framework**: UIKit  
**Kind**: init

Creates a switch control.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(frame: CGRect)
```

#### Return Value

An initialized [`UISwitch`](uiswitch.md) object.

#### Discussion

[`UISwitch`](uiswitch.md) overrides [`init(frame:)`](uiview/init(frame:).md) and enforces a size appropriate for the control.

## Parameters

- `frame`: A rectangle defining the frame of the   object. The size components of this rectangle are ignored.

## See Also

- [init?(coder: NSCoder)](uiswitch/init(coder:).md)
  Creates a switch control from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiswitch/init(frame:))*