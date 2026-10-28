# servicePrincipal()

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Retrieves a pointer to the proxy object used for sandboxed out-of-process tasks.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
func servicePrincipal() -> Any!
```

```objc
- (id) servicePrincipal;
```

## Return Value

An object used for XPC communication with the out-of-process service principal.

## Discussion

If this method returns `nil`, the host app is unable to communicate with your plug-in’s XPC service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxprincipalapi/serviceprincipal())*