# WKUserInterfaceDirectionPolicy

**Framework**: WebKit  
**Kind**: enum

The policy that determines the directionality of user interface elements in a web view.

**Availability**:
- macOS 10.12+

## Declaration

```swift
enum WKUserInterfaceDirectionPolicy
```

#### Overview

When `WKUserInterfaceDirectionPolicyContent` is specified, the directionality of user interface elements is affected by the `dir` attribute or the `direction` CSS property. When `WKUserInterfaceDirectionPolicySystem` is specified, the directionality of user interface elements is affected by the direction of the view.

## Topics

### Direction Policies
- [WKUserInterfaceDirectionPolicy.content](wkuserinterfacedirectionpolicy/content.md)
  The directionality follows the CSS/HTML/XHTML specifications.
- [WKUserInterfaceDirectionPolicy.system](wkuserinterfacedirectionpolicy/system.md)
  The directionality follows the view’s user interface layout direction.
### Initializers
- [init?(rawValue: Int)](wkuserinterfacedirectionpolicy/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var userInterfaceDirectionPolicy: WKUserInterfaceDirectionPolicy](wkwebviewconfiguration/userinterfacedirectionpolicy.md)
  The directionality of user interface elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkuserinterfacedirectionpolicy)*