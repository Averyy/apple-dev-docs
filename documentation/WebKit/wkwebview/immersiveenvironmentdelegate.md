# immersiveEnvironmentDelegate

**Framework**: WebKit  
**Kind**: property

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 27.0+ (Beta)

## Declaration

```swift
weak var immersiveEnvironmentDelegate: (any WKImmersiveEnvironmentDelegate)? { get set }
```

#### Discussion

The delegate that manages immersive environment presentation.

## See Also

- [class WKImmersiveEnvironment](wkimmersiveenvironment.md)
- [protocol WKImmersiveEnvironmentDelegate](wkimmersiveenvironmentdelegate.md)
- [var allowsImmersiveEnvironments: Bool](wkwebviewconfiguration/allowsimmersiveenvironments.md)
- [func dismissImmersiveEnvironment(completionHandler: () -> Void)](wkwebview/dismissimmersiveenvironment(completionhandler:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/immersiveenvironmentdelegate)*