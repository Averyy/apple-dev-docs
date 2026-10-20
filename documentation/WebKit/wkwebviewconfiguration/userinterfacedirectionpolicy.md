# userInterfaceDirectionPolicy

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The directionality of user interface elements.

**Availability**:
- macOS 10.12+

## Declaration

```swift
var userInterfaceDirectionPolicy: WKUserInterfaceDirectionPolicy { get set }
```

```objc
@property (nonatomic) WKUserInterfaceDirectionPolicy userInterfaceDirectionPolicy;
```

#### Discussion

The default value is [`WKUserInterfaceDirectionPolicy.content`](../wkuserinterfacedirectionpolicy/content.md). For other possible values, see [`WKUserInterfaceDirectionPolicy`](../wkuserinterfacedirectionpolicy.md).

## See Also

### Selecting user interface directionality
- [enum WKUserInterfaceDirectionPolicy](../wkuserinterfacedirectionpolicy.md)
  The policy that determines the directionality of user interface elements in a web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/userinterfacedirectionpolicy)*