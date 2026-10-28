# startServicePrincipal()

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Type Method

Start your XPC service listening for connections from the host application.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
class func startServicePrincipal()
```

```objc
+ (void) startServicePrincipal;
```

## Discussion

The purpose of this method is so that plug-ins don’t have to link against `PlugInKit.framework`. You can simply link against `FxPlug.framework` and call `[FxPrincipal startServicePrincipal]` from the service principal’s `main()` function.

## See Also

### Type Methods
- [class func embeddedPrincipal() -> Any!](./embeddedprincipal%28%29.md)
  Start your XPC service listening for connections from the host application.
- [class func startServicePrincipal(with: (any FxPrincipalDelegate)!)](./startserviceprincipal%28with%29.md)
  Start your XPC service listening for connections from the host application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxprincipal/startserviceprincipal())*