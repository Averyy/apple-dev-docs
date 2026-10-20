# init(frame:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates an empty segmented control with the frame you specify.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
init(frame: CGRect)
```

```objc
- (instancetype) initWithFrame:(CGRect) frame;
```

## Parameters

- `frame`: A rectangle that specifies the segmented control’s frame in a superview’s coordinate system.

## See Also

### Creating a segmented control
- [init(items: [Any]?)](./init%28items%29.md)
  Creates a segmented control with segments having the given titles or images.
- [convenience init(frame: CGRect, actions: [UIAction])](./init%28frame,actions%29.md)
  Creates a segmented control with the given frame and adds segments for the actions you specify.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a segmented control with data from an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/init(frame:))*