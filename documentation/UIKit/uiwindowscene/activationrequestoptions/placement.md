# placement

**Framework**: UIKit  
**Kind**: property

The placement you prefer when the system activates the window scene.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var placement: (any UIWindowScenePlacement)? { get set }
```

#### Discussion

Provide a scene placement to influence how the system positions the scene on activation. Set the value to `nil` to indicate that the system should determine the most appropriate placement.

## See Also

- [protocol UIWindowScenePlacement](uiwindowsceneplacement-swift.protocol.md)
  The placement of a window scene in the workspace.
- [struct UIWindowSceneProminentPlacement](uiwindowsceneprominentplacement-swift.struct.md)
  A placement that indicates the system should present the window more prominently than others in the space.
- [struct UIWindowSceneStandardPlacement](uiwindowscenestandardplacement-swift.struct.md)
  A placement that indicates the system should present the window using the default style of the system in the space.
- [struct UIWindowScenePushPlacement](uiwindowscenepushplacement-swift.struct.md)
  A placement that indicates the system needs to present the window by pushing it onto another window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/activationrequestoptions/placement)*