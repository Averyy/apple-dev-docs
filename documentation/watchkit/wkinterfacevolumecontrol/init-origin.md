# init(origin:)

**Framework**: Watchkit  
**Kind**: init

Creates a volume control for use in SwiftUI.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
init(origin: WKInterfaceVolumeControl.Origin)
```

#### Discussion

Use this initializer to create an instance that you can wrap in a [`WKInterfaceObjectRepresentable`](https://developer.apple.com/documentation/SwiftUI/WKInterfaceObjectRepresentable) view. If you aren’t using SwiftUI, create the control by dragging it from the Object library to your storyboard instead.

## Parameters

- `origin`: The source of the audio managed by the volume control. For a list of possible values, see  .

## See Also

- [WKInterfaceVolumeControl.Origin](wkinterfacevolumecontrol/origin.md)
  The source of the audio managed by the volume control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacevolumecontrol/init(origin:))*