# UIWindowScenePlacement

**Framework**: UIKit  
**Kind**: protocol

The placement of a window scene in the workspace.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
protocol UIWindowScenePlacement : Hashable
```

## Topics

### Positioning windows
- [static func prominent() -> Self](uiwindowsceneplacement-swift.protocol/prominent.md)
  Creates a placement that indicates the system should present the window more prominently than others in the space.
- [static func standard() -> Self](uiwindowsceneplacement-swift.protocol/standard.md)
  Creates a placement that indicates the system should present the window using the default style of the system in the space.
### Type Methods
- [static func push(onto: UISceneSession) -> Self](uiwindowsceneplacement-swift.protocol/push(onto:).md)
- [static func replacing(UISceneSession) -> Self](uiwindowsceneplacement-swift.protocol/replacing(_:).md)

## Relationships

### Inherits From
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
### Conforming Types
- [UIWindowSceneProminentPlacement](uiwindowsceneprominentplacement-swift.struct.md)
- [UIWindowScenePushPlacement](uiwindowscenepushplacement-swift.struct.md)
- [UIWindowSceneReplacePlacement](uiwindowscenereplaceplacement-swift.struct.md)
- [UIWindowSceneStandardPlacement](uiwindowscenestandardplacement-swift.struct.md)

## See Also

- [var placement: (any UIWindowScenePlacement)?](uiwindowscene/activationrequestoptions/placement.md)
  The placement you prefer when the system activates the window scene.
- [struct UIWindowSceneProminentPlacement](uiwindowsceneprominentplacement-swift.struct.md)
  A placement that indicates the system should present the window more prominently than others in the space.
- [struct UIWindowSceneStandardPlacement](uiwindowscenestandardplacement-swift.struct.md)
  A placement that indicates the system should present the window using the default style of the system in the space.
- [struct UIWindowScenePushPlacement](uiwindowscenepushplacement-swift.struct.md)
  A placement that indicates the system needs to present the window by pushing it onto another window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowsceneplacement-swift.protocol)*