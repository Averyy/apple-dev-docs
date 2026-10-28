# immersiveEnvironmentDelegate

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- visionOS 27.0+

## Declaration

```swift
weak var immersiveEnvironmentDelegate: (any WKImmersiveEnvironmentDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<WKImmersiveEnvironmentDelegate> immersiveEnvironmentDelegate;
```

## Discussion

The delegate that manages immersive environment presentation.

## See Also

### Immersive environments
- [class WKImmersiveEnvironment](../wkimmersiveenvironment.md)
- [protocol WKImmersiveEnvironmentDelegate](../wkimmersiveenvironmentdelegate.md)
- [var allowsImmersiveEnvironments: Bool](../wkwebviewconfiguration/allowsimmersiveenvironments.md)
- [func dismissImmersiveEnvironment(completionHandler: () -> Void)](./dismissimmersiveenvironment%28completionhandler%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/immersiveenvironmentdelegate)*