# UNError.Code

**Framework**: User Notifications  
**Kind**: enum

Constants that identify notification errors.

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
enum Code
```

## Topics

### Constants
- [UNError.Code.notificationsNotAllowed](unerror/code/notificationsnotallowed.md)
  Notifications aren’t allowed.
- [UNError.Code.attachmentInvalidURL](unerror/code/attachmentinvalidurl.md)
  The URL for an attachment was invalid.
- [UNError.Code.attachmentUnrecognizedType](unerror/code/attachmentunrecognizedtype.md)
  The file type of an attachment isn’t supported.
- [UNError.Code.attachmentInvalidFileSize](unerror/code/attachmentinvalidfilesize.md)
  An attachment is too large.
- [UNError.Code.attachmentNotInDataStore](unerror/code/attachmentnotindatastore.md)
  The specified attachment isn’t in the system data store.
- [UNError.Code.attachmentMoveIntoDataStoreFailed](unerror/code/attachmentmoveintodatastorefailed.md)
  An error occurred when trying to move an attachment to the system data store.
- [UNError.Code.attachmentCorrupt](unerror/code/attachmentcorrupt.md)
  The file for an attachment is corrupt.
- [UNError.Code.notificationInvalidNoDate](unerror/code/notificationinvalidnodate.md)
  The notification doesn’t have an associated date, but should.
- [UNError.Code.notificationInvalidNoContent](unerror/code/notificationinvalidnocontent.md)
  The notification has no user-facing content, but should.
- [UNError.Code.contentProvidingInvalid](unerror/code/contentprovidinginvalid.md)
- [UNError.Code.contentProvidingObjectNotAllowed](unerror/code/contentprovidingobjectnotallowed.md)
### Enumeration Cases
- [UNError.Code.badgeInputInvalid](unerror/code/badgeinputinvalid.md)
### Initializers
- [init?(rawValue: Int)](unerror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct UNError](unerror.md)
  An object that represents a notification error.
- [let UNErrorDomain: String](unerrordomain.md)
  The error domain for notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unerror/code)*