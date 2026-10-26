# embeddedPrincipal()

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Type Method

Start your XPC service listening for connections from the host application.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
class func embeddedPrincipal() -> Any!
```

```objc
+ (id) embeddedPrincipal;
```

#### Return Value

An object used for XPC communication with the in-process embedded principal.

#### Discussion

If this method returns `nil`, the host app is unable to communicate with your plug-in’s XPC service.

## See Also

### Type Methods
- [class func startServicePrincipal()](./startserviceprincipal%28%29.md)
  Start your XPC service listening for connections from the host application.
- [class func startServicePrincipal(with: (any FxPrincipalDelegate)!)](./startserviceprincipal%28with%29.md)
  Start your XPC service listening for connections from the host application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxprincipal/embeddedprincipal())*