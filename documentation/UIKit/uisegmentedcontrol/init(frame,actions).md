# init(frame:actions:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a segmented control with the given frame and adds segments for the actions you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(frame: CGRect, actions: [UIAction])
```

```objc
- (instancetype) initWithFrame:(CGRect) frame actions:(NSArray<UIAction *> *) actions;
```

#### Discussion

Segments prefer images over titles when the action contains both. Selecting a segment invokes the action’s [`UIActionHandler`](../uiactionhandler.md), as well as handlers for the [`valueChanged`](../uicontrol/event/valuechanged.md) and [`primaryActionTriggered`](../uicontrol/event/primaryactiontriggered.md) control events.

## Parameters

- `frame`: A rectangle that specifies the segmented control’s frame in a superview’s coordinate system.
- `actions`: An array of [`UIAction`](../uiaction.md) objects.

## See Also

### Creating a segmented control
- [init(items: [Any]?)](./init%28items%29.md)
  Creates a segmented control with segments having the given titles or images.
- [init(frame: CGRect)](./init%28frame%29.md)
  Creates an empty segmented control with the frame you specify.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a segmented control with data from an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisegmentedcontrol/init(frame:actions:))*