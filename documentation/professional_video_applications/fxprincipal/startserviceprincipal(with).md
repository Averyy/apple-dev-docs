# startServicePrincipal(with:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Type Method

Start your XPC service listening for connections from the host application.

**Availability**:
- FxPlug 4.1+

## Declaration

```swift
class func startServicePrincipal(with delegate: (any FxPrincipalDelegate)!)
```

```objc
+ (void) startServicePrincipalWithDelegate:(id<FxPrincipalDelegate>) delegate;
```

## Discussion

Once a connection is established, your delegate will be informed of the host application’s ID and version.

## Parameters

- `delegate`: An object that implements the [`FxPrincipalDelegate`](../fxprincipaldelegate.md) or `nil`.

## See Also

### Type Methods
- [class func embeddedPrincipal() -> Any!](./embeddedprincipal%28%29.md)
  Start your XPC service listening for connections from the host application.
- [class func startServicePrincipal()](./startserviceprincipal%28%29.md)
  Start your XPC service listening for connections from the host application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxprincipal/startserviceprincipal(with:))*