# allowsImmersiveEnvironments

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- visionOS 27.0+

## Declaration

```swift
var allowsImmersiveEnvironments: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsImmersiveEnvironments;
```

#### Discussion

A Boolean value that determines whether the web view allows immersive environments.

Set this property to YES to enable support for website-provided immersive environments. If NO, requests to present immersive environments are ignored. If YES, requests are routed to your `WKImmersiveEnvironmentDelegate`. The default value is NO.

## See Also

### Immersive environments
- [class WKImmersiveEnvironment](../wkimmersiveenvironment.md)
- [protocol WKImmersiveEnvironmentDelegate](../wkimmersiveenvironmentdelegate.md)
- [var immersiveEnvironmentDelegate: (any WKImmersiveEnvironmentDelegate)?](../wkwebview/immersiveenvironmentdelegate.md)
- [func dismissImmersiveEnvironment(completionHandler: () -> Void)](../wkwebview/dismissimmersiveenvironment%28completionhandler%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/allowsimmersiveenvironments)*