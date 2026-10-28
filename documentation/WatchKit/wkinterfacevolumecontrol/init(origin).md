# init(origin:)

**Framework**: WatchKit  
**Kind**: init  
**Role**: Initializer

Creates a volume control for use in SwiftUI.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
init(origin: WKInterfaceVolumeControl.Origin)
```

```objc
- (instancetype) initWithOrigin:(WKInterfaceVolumeControlOrigin) origin;
```

## Discussion

Use this initializer to create an instance that you can wrap in a [`WKInterfaceObjectRepresentable`](../../SwiftUI/wkinterfaceobjectrepresentable.md) view. If you aren’t using SwiftUI, create the control by dragging it from the Object library to your storyboard instead.

## Parameters

- `origin`: The source of the audio managed by the volume control. For a list of possible values, see [`WKInterfaceVolumeControl.Origin`](./origin.md).

## See Also

### SwiftUI
- [WKInterfaceVolumeControl.Origin](./origin.md)
  The source of the audio managed by the volume control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacevolumecontrol/init(origin:))*