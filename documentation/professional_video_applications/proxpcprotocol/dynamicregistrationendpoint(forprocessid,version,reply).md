# dynamicRegistrationEndpoint(forProcessID:version:reply:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- macOS 10.8+

## Declaration

```swift
func dynamicRegistrationEndpoint(forProcessID processID: pid_t, version: Int, reply: ((NSXPCListenerEndpoint?, (any Error)?) -> Void)!)
```

```swift
func dynamicRegistrationEndpoint(forProcessID processID: pid_t, version: Int) async throws -> NSXPCListenerEndpoint?
```

```objc
- (void) dynamicRegistrationEndpointForProcessID:(pid_t) processID version:(NSInteger) version reply:(void (^)(NSXPCListenerEndpoint * , NSError * )) reply;
```

## Discussion

Obtains the NSXPCListenerEndpoint for dynamic registration.

The host application automatically calls this so plug-ins should not call it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/proxpcprotocol/dynamicregistrationendpoint(forprocessid:version:reply:))*