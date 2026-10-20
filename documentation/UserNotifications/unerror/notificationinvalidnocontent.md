# notificationInvalidNoContent

**Framework**: User Notifications  
**Kind**: property  
**Role**: Type Property

The notification has no user-facing content, but should.

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
static var notificationInvalidNoContent: UNError.Code { get }
```

## See Also

### Type Properties
- [static var notificationsNotAllowed: UNError.Code](./notificationsnotallowed.md)
  Notifications are not allowed.
- [static var attachmentInvalidURL: UNError.Code](./attachmentinvalidurl.md)
  The URL for an attachment was invalid.
- [static var attachmentUnrecognizedType: UNError.Code](./attachmentunrecognizedtype.md)
  The file type of an attachment is not supported.
- [static var attachmentInvalidFileSize: UNError.Code](./attachmentinvalidfilesize.md)
  An attachment is too large.
- [static var attachmentNotInDataStore: UNError.Code](./attachmentnotindatastore.md)
  The specified attachment is not in the system data store.
- [static var attachmentMoveIntoDataStoreFailed: UNError.Code](./attachmentmoveintodatastorefailed.md)
  An error occurred when trying to move an attachment to the system data store.
- [static var attachmentCorrupt: UNError.Code](./attachmentcorrupt.md)
  The file for an attachment is corrupt.
- [static var notificationInvalidNoDate: UNError.Code](./notificationinvalidnodate.md)
  The notification does not have an associated date, but should.
- [static var contentProvidingInvalid: UNError.Code](./contentprovidinginvalid.md)
- [static var contentProvidingObjectNotAllowed: UNError.Code](./contentprovidingobjectnotallowed.md)
- [static var badgeInputInvalid: UNError.Code](./badgeinputinvalid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unerror/notificationinvalidnocontent)*