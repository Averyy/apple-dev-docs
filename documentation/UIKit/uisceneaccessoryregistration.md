# UISceneAccessoryRegistration

**Framework**: UIKit  
**Kind**: class

A type which represents the registration for a given scene accessory.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
class UISceneAccessoryRegistration
```

#### Overview

Instances of this type allow for observing availability of a given scene accessory, as well as controlling whether the contents should be displayed when the system determines the scene is available.

## Topics

### Instance Properties
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneaccessoryregistration)*