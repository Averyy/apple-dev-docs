# allowsImmersiveEnvironments

**Framework**: WebKit  
**Kind**: property

Indicates whether website immersive environments are allowed.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
var allowsImmersiveEnvironments: Bool { get set }
```

#### Discussion

Set this property to `true` to enable support for website immersive environments. If `false`, requests to present immersive environments are ignored. If `true`, requests are routed through the `onWebViewImmersiveEnvironmentRequest` view modifier callbacks.

The default value is `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/configuration/allowsimmersiveenvironments)*