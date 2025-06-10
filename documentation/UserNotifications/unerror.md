# UNError

**Framework**: User Notifications  
**Kind**: struct

An object that represents a notification error.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct UNError
```

## Topics

### Type Properties
- [static var notificationsNotAllowed: UNError.Code](unerror/notificationsnotallowed.md)
  Notifications are not allowed.
- [static var attachmentInvalidURL: UNError.Code](unerror/attachmentinvalidurl.md)
  The URL for an attachment was invalid.
- [static var attachmentUnrecognizedType: UNError.Code](unerror/attachmentunrecognizedtype.md)
  The file type of an attachment is not supported.
- [static var attachmentInvalidFileSize: UNError.Code](unerror/attachmentinvalidfilesize.md)
  An attachment is too large.
- [static var attachmentNotInDataStore: UNError.Code](unerror/attachmentnotindatastore.md)
  The specified attachment is not in the system data store.
- [static var attachmentMoveIntoDataStoreFailed: UNError.Code](unerror/attachmentmoveintodatastorefailed.md)
  An error occurred when trying to move an attachment to the system data store.
- [static var attachmentCorrupt: UNError.Code](unerror/attachmentcorrupt.md)
  The file for an attachment is corrupt.
- [static var notificationInvalidNoDate: UNError.Code](unerror/notificationinvalidnodate.md)
  The notification does not have an associated date, but should.
- [static var notificationInvalidNoContent: UNError.Code](unerror/notificationinvalidnocontent.md)
  The notification has no user-facing content, but should.
- [static var contentProvidingInvalid: UNError.Code](unerror/contentprovidinginvalid.md)
- [static var contentProvidingObjectNotAllowed: UNError.Code](unerror/contentprovidingobjectnotallowed.md)
- [static var badgeInputInvalid: UNError.Code](unerror/badgeinputinvalid.md)
### Error Information
- [static var errorDomain: String](unerror/errordomain.md)
- [let UNErrorDomain: String](unerrordomain.md)
  The error domain for notifications.
- [UNError.Code](unerror/code.md)
  Constants that identify notification errors.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [UNError.Code](unerror/code.md)
  Constants that identify notification errors.
- [let UNErrorDomain: String](unerrordomain.md)
  The error domain for notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unerror)*