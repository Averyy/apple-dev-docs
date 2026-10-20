# UNError.Code

**Framework**: User Notifications  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum UNErrorCode : NSInteger;
```

## Topics

### Constants
- [UNError.Code.notificationsNotAllowed](./code/notificationsnotallowed.md)
  Notifications aren’t allowed.
- [UNError.Code.attachmentInvalidURL](./code/attachmentinvalidurl.md)
  The URL for an attachment was invalid.
- [UNError.Code.attachmentUnrecognizedType](./code/attachmentunrecognizedtype.md)
  The file type of an attachment isn’t supported.
- [UNError.Code.attachmentInvalidFileSize](./code/attachmentinvalidfilesize.md)
  An attachment is too large.
- [UNError.Code.attachmentNotInDataStore](./code/attachmentnotindatastore.md)
  The specified attachment isn’t in the system data store.
- [UNError.Code.attachmentMoveIntoDataStoreFailed](./code/attachmentmoveintodatastorefailed.md)
  An error occurred when trying to move an attachment to the system data store.
- [UNError.Code.attachmentCorrupt](./code/attachmentcorrupt.md)
  The file for an attachment is corrupt.
- [UNError.Code.notificationInvalidNoDate](./code/notificationinvalidnodate.md)
  The notification doesn’t have an associated date, but should.
- [UNError.Code.notificationInvalidNoContent](./code/notificationinvalidnocontent.md)
  The notification has no user-facing content, but should.
- [UNError.Code.contentProvidingInvalid](./code/contentprovidinginvalid.md)
- [UNError.Code.contentProvidingObjectNotAllowed](./code/contentprovidingobjectnotallowed.md)
### Enumeration Cases
- [UNError.Code.badgeInputInvalid](./code/badgeinputinvalid.md)
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Handling errors
- [struct UNError](../unerror.md)
  An object that represents a notification error.
- [let UNErrorDomain: String](../unerrordomain.md)
  The error domain for notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unerror/code)*