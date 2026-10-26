# viewServiceListenerEndPoint(_:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- macOS 10.8+

## Declaration

```swift
func viewServiceListenerEndPoint(_ reply: ((NSXPCListenerEndpoint?) -> Void)!)
```

```swift
func viewServiceListenerEndPoint() async -> NSXPCListenerEndpoint?
```

```objc
- (void) viewServiceListenerEndPoint:(void (^)(NSXPCListenerEndpoint * )) reply;
```

#### Discussion

Obtains the NSXPCListenerEndpoint for ViewBridge to communicate with custom views.

The host application automatically calls this so plug-ins should not call it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxxpcprotocol/viewservicelistenerendpoint(_:))*