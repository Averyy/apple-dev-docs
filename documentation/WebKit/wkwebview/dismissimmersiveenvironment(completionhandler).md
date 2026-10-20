# dismissImmersiveEnvironment(completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- visionOS 27.0+

## Declaration

```swift
func dismissImmersiveEnvironment(completionHandler: @escaping @MainActor @Sendable () -> Void)
```

```swift
func dismissImmersiveEnvironment() async
```

```objc
- (void) dismissImmersiveEnvironmentWithCompletionHandler:(void (^)(void)) completionHandler;
```

#### Discussion

Dismisses the currently presented immersive environment.

## See Also

### Immersive environments
- [class WKImmersiveEnvironment](../wkimmersiveenvironment.md)
- [protocol WKImmersiveEnvironmentDelegate](../wkimmersiveenvironmentdelegate.md)
- [var allowsImmersiveEnvironments: Bool](../wkwebviewconfiguration/allowsimmersiveenvironments.md)
- [var immersiveEnvironmentDelegate: (any WKImmersiveEnvironmentDelegate)?](./immersiveenvironmentdelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/dismissimmersiveenvironment(completionhandler:))*