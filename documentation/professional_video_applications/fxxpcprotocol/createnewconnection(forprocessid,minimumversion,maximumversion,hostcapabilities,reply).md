# createNewConnection(forProcessID:minimumVersion:maximumVersion:hostCapabilities:reply:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- macOS 10.8+

## Declaration

```swift
func createNewConnection(forProcessID processID: pid_t, minimumVersion minVers: Int, maximumVersion maxVers: Int, hostCapabilities remoteCapabilities: [AnyHashable : Any]!, reply: ((NSXPCListenerEndpoint?, (any Error)?) -> Void)!)
```

```swift
func createNewConnection(forProcessID processID: pid_t, minimumVersion minVers: Int, maximumVersion maxVers: Int, hostCapabilities remoteCapabilities: [AnyHashable : Any]!) async throws -> NSXPCListenerEndpoint?
```

```objc
- (void) createNewConnectionForProcessID:(pid_t) processID minimumVersion:(NSUInteger) minVers maximumVersion:(NSUInteger) maxVers hostCapabilities:(NSDictionary *) remoteCapabilities reply:(void (^)(NSXPCListenerEndpoint * , NSError * )) reply;
```

## Discussion

Accepts a connection from the host application.

The host application automatically calls this so plug-ins should not call it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxxpcprotocol/createnewconnection(forprocessid:minimumversion:maximumversion:hostcapabilities:reply:))*