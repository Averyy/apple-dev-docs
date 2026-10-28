# didEstablishConnection(withHost:version:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method

Notifies your XPC service that a connection was established with the host.

**Availability**:
- FxPlug 4.1+

## Declaration

```swift
optional func didEstablishConnection(withHost hostBundleIdentifier: String!, version hostVersionString: String!)
```

```objc
- (void) didEstablishConnectionWithHost:(NSString *) hostBundleIdentifier version:(NSString *) hostVersionString;
```

## Discussion

Your delegate can implement this protocol to be informed of which host application is calling your plug-in.

## Parameters

- `hostBundleIdentifier`: The NSBundleIdentifier of the host application that launched this XPC service.
- `hostVersionString`: The NSShortVersionString of the host application that launched this XPC service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxprincipaldelegate/didestablishconnection(withhost:version:))*