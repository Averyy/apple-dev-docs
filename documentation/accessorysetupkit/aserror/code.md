# ASError.Code

**Framework**: AccessorySetupKit  
**Kind**: enum

Codes that describe errors encountered during accessory discovery.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
enum Code
```

## Topics

### Activation errors
- [ASError.Code.activationFailed](aserror/code/activationfailed.md)
  Session activation failed.
### Timeout and life cycle errors
- [ASError.Code.discoveryTimeout](aserror/code/discoverytimeout.md)
  Accessory discovery timed out.
- [ASError.Code.invalidated](aserror/code/invalidated.md)
  The session invalidated prior to completing the operation.
### Configuration errors
- [ASError.Code.extensionNotFound](aserror/code/extensionnotfound.md)
  The framework couldn’t find the app extension.
- [ASError.Code.userRestricted](aserror/code/userrestricted.md)
  The person using the app restricted access.
- [ASError.Code.invalidRequest](aserror/code/invalidrequest.md)
  The session received an invalid request.
### Picker errors
- [ASError.Code.pickerRestricted](aserror/code/pickerrestricted.md)
  The picker can’t be used because the app is in the background.
- [ASError.Code.pickerAlreadyActive](aserror/code/pickeralreadyactive.md)
  The picker received a show request when it was already active.
### Cancellation errors
- [ASError.Code.userCancelled](aserror/code/usercancelled.md)
  The person using the app canceled the operation.
### Communication errors
- [ASError.Code.connectionFailed](aserror/code/connectionfailed.md)
  The session was unable to establish a connection.
### Success cases
- [ASError.Code.success](aserror/code/success.md)
  A code that represents a successful action.
### Unclassified errors
- [ASError.Code.unknown](aserror/code/unknown.md)
  An underlying failure with an unknown cause.
### Accessing the error domain
- [static var errorDomain: String](aserror/errordomain.md)
  The domain of the error.
- [let ASErrorDomain: String](aserrordomain.md)
  NSError domain for AccessorySetupKit errors.
### Working with raw values
- [init?(rawValue: Int)](aserror/code/init(rawvalue:).md)
### Default Implementations
- [Equatable Implementations](aserror/code/equatable-implementations.md)
- [RawRepresentable Implementations](aserror/code/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct ASError](aserror.md)
  An error encountered during accessory discovery.
- [let ASErrorDomain: String](aserrordomain.md)
  NSError domain for AccessorySetupKit errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/aserror/code)*