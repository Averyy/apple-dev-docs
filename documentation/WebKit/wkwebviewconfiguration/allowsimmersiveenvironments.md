# allowsImmersiveEnvironments

**Framework**: WebKit  
**Kind**: property

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 27.0+ (Beta)

## Declaration

```swift
var allowsImmersiveEnvironments: Bool { get set }
```

#### Discussion

A Boolean value that determines whether the web view allows immersive environments.

Set this property to YES to enable support for website-provided immersive environments. If NO, requests to present immersive environments are ignored. If YES, requests are routed to your `WKImmersiveEnvironmentDelegate`. The default value is NO.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/allowsimmersiveenvironments)*