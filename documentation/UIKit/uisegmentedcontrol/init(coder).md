# init(coder:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a segmented control with data from an unarchiver.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
init?(coder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) coder;
```

## Parameters

- `coder`: The unarchiver to read data from.

## See Also

### Creating a segmented control
- [init(items: [Any]?)](./init%28items%29.md)
  Creates a segmented control with segments having the given titles or images.
- [convenience init(frame: CGRect, actions: [UIAction])](./init%28frame,actions%29.md)
  Creates a segmented control with the given frame and adds segments for the actions you specify.
- [init(frame: CGRect)](./init%28frame%29.md)
  Creates an empty segmented control with the frame you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/init(coder:))*