# UISceneAccessoryRegistration

**Framework**: UIKit  
**Kind**: class

A type which represents the registration for a given scene accessory.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
class UISceneAccessoryRegistration
```

## Mentions

- [Presenting content on a connected display](presenting-content-on-a-connected-display.md)

#### Overview

Instances of this type allow for observing availability of a given scene accessory, as well as controlling whether the contents should be displayed when the system determines the scene is available.

## Topics

### Observing availability and controlling display
- [var isAvailable: Bool](uisceneaccessoryregistration/isavailable.md)
  Whether the associated scene accessory is available for display by the system or not.
- [var isEnabled: Bool](uisceneaccessoryregistration/isenabled.md)
  Whether the content defined by this scene accessory should be displayed or not.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UISceneAccessory](uisceneaccessory.md)
  A type which can be used to register for a specific type of scene accessory presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneaccessoryregistration)*