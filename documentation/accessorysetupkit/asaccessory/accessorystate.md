# ASAccessory.AccessoryState

**Framework**: AccessorySetupKit  
**Kind**: enum

An enumeration of possible authorization states of an accessory.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
enum AccessoryState
```

## Topics

### Creating a state instance
- [init?(rawValue: Int)](asaccessory/accessorystate/init(rawvalue:).md)
### Accessory states
- [ASAccessory.AccessoryState.unauthorized](asaccessory/accessorystate/unauthorized.md)
  The accessory is invalid or unauthorized.
- [ASAccessory.AccessoryState.awaitingAuthorization](asaccessory/accessorystate/awaitingauthorization.md)
  The accessory is selected, but full authorization is still pending.
- [ASAccessory.AccessoryState.authorized](asaccessory/accessorystate/authorized.md)
  The accessory is authorized and available.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class ASAccessory](asaccessory.md)
  An accessory discovered by the accessory session.
- [class ASDiscoveredAccessory](asdiscoveredaccessory.md)
  A discovered accessory, for use in creating a customized picker display item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessory/accessorystate)*