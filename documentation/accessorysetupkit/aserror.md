# ASError

**Framework**: AccessorySetupKit  
**Kind**: struct

An error encountered during accessory discovery.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
struct ASError
```

## Topics

### Activation errors
- [static var activationFailed: ASError.Code](aserror/activationfailed.md)
### Life cycle errors
- [static var invalidated: ASError.Code](aserror/invalidated.md)
### Configuration errors
- [static var extensionNotFound: ASError.Code](aserror/extensionnotfound.md)
- [static var invalidRequest: ASError.Code](aserror/invalidrequest.md)
### Picker errors
- [static var pickerRestricted: ASError.Code](aserror/pickerrestricted.md)
- [static var pickerAlreadyActive: ASError.Code](aserror/pickeralreadyactive.md)
### Cancellation and permission errors
- [static var userCancelled: ASError.Code](aserror/usercancelled.md)
- [static var userRestricted: ASError.Code](aserror/userrestricted.md)
### Communication errors
- [static var connectionFailed: ASError.Code](aserror/connectionfailed.md)
- [static var discoveryTimeout: ASError.Code](aserror/discoverytimeout.md)
### Success cases
- [static var success: ASError.Code](aserror/success.md)
### Unclassified errors
- [static var unknown: ASError.Code](aserror/unknown.md)
### Accessing the error domain
- [static var errorDomain: String](aserror/errordomain.md)
  The domain of the error.
- [let ASErrorDomain: String](aserrordomain.md)
  NSError domain for AccessorySetupKit errors.
### Default Implementations
- [CustomNSError Implementations](aserror/customnserror-implementations.md)
- [Equatable Implementations](aserror/equatable-implementations.md)
- [Error Implementations](aserror/error-implementations.md)
- [Hashable Implementations](aserror/hashable-implementations.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let ASErrorDomain: String](aserrordomain.md)
  NSError domain for AccessorySetupKit errors.
- [ASError.Code](aserror/code.md)
  Codes that describe errors encountered during accessory discovery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/aserror)*