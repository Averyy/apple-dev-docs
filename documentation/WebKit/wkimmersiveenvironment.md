# WKImmersiveEnvironment

**Framework**: WebKit  
**Kind**: class  
**Role**: Class

**Availability**:
- visionOS 27.0+

## Declaration

```swift
@MainActor
class WKImmersiveEnvironment
```

```objc
@interface WKImmersiveEnvironment : NSObject
```

#### Overview

An object representing a website-provided immersive environment that is ready for presentation.

## Topics

### Instance Properties
- [var sourceFrame: WKFrameInfo](./wkimmersiveenvironment/sourceframe.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Immersive environments
- [protocol WKImmersiveEnvironmentDelegate](./wkimmersiveenvironmentdelegate.md)
- [var allowsImmersiveEnvironments: Bool](./wkwebviewconfiguration/allowsimmersiveenvironments.md)
- [var immersiveEnvironmentDelegate: (any WKImmersiveEnvironmentDelegate)?](./wkwebview/immersiveenvironmentdelegate.md)
- [func dismissImmersiveEnvironment(completionHandler: () -> Void)](./wkwebview/dismissimmersiveenvironment%28completionhandler%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkimmersiveenvironment)*