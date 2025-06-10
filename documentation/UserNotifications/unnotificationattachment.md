# UNNotificationAttachment

**Framework**: User Notifications  
**Kind**: class

A media file associated with a notification.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class UNNotificationAttachment
```

#### Overview

Create a [`UNNotificationAttachment`](unnotificationattachment.md) object when you want to include audio, image, or video content together in an alert-based notification. When creating the [`UNNotificationAttachment`](unnotificationattachment.md) object, the file you specify must be on disk, and the file format must be one of the supported types.

You’re responsible for supplying attachments before the system displays your notification’s alert. For local notifications, add attachments when creating the notification’s content. For remote notifications, use a notification service app extension to download the attached files and then add them to the notification’s content before delivery.

The system validates attachments before displaying the associated notification. If you attach a file to a local notification request that’s corrupted, invalid, or of an unsupported file type, the system doesn’t schedule your request. For remote notifications, the system validates attachments after your notification service app extension finishes. Once validated, the system moves the attached files into the attachment data store so that the appropriate processes can access the files. The system copies attachments located inside an app’s bundle.

##### Supported File Types

Table 1 lists the types of files you can include as an attachment and the supported file formats. The table also lists the maximum size allowed for attachments of each type. An image file may contain a static image or an animated image sequence.

Table 1. Supported attachment file types

| Attachment | Supported file types | Maximum size |
| --- | --- | --- |
| Audio | `kUTTypeAudioInterchangeFileFormat` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `kUTTypeWaveformAudio` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `kUTTypeMP3` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `kUTTypeMPEG4Audio` | 5 MB |
| Image | `kUTTypeJPEG` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `kUTTypeGIF` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `kUTTypePNG` | 10 MB |
| Movie | `kUTTypeMPEG` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `kUTTypeMPEG2Video` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `kUTTypeMPEG4` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `kUTTypeAVIMovie` | 50 MB |

When creating an attachment, you can specify optional details about how to present the thumbnail image for the image or movie. Use the [`UNNotificationAttachmentOptionsThumbnailClippingRectKey`](unnotificationattachmentoptionsthumbnailclippingrectkey.md) option to use only the specified portion of an image as a thumbnail. For animated images and movies, use the [`UNNotificationAttachmentOptionsThumbnailTimeKey`](unnotificationattachmentoptionsthumbnailtimekey.md) option to select which frame to use for the thumbnail image.

The system limits the amount of storage space allocated for attachments for each app. To delete attachments, use the methods of the [`UNUserNotificationCenter`](unusernotificationcenter.md) class to remove the notification requests that contain those attachments.

## Topics

### Creating an Attachment
- [convenience init(identifier: String, url: URL, options: [AnyHashable : Any]?) throws](unnotificationattachment/init(identifier:url:options:).md)
  Creates an attachment object from the specified file and options.
- [let UNNotificationAttachmentOptionsTypeHintKey: String](unnotificationattachmentoptionstypehintkey.md)
  A hint about an attachment’s file type.
- [let UNNotificationAttachmentOptionsThumbnailHiddenKey: String](unnotificationattachmentoptionsthumbnailhiddenkey.md)
  A Boolean value indicating whether the system hides the attachment’s thumbnail.
- [let UNNotificationAttachmentOptionsThumbnailClippingRectKey: String](unnotificationattachmentoptionsthumbnailclippingrectkey.md)
  The clipping rectangle for a thumbnail image.
- [let UNNotificationAttachmentOptionsThumbnailTimeKey: String](unnotificationattachmentoptionsthumbnailtimekey.md)
  The frame number of an animation to use as a thumbnail image.
### Getting the Attachment Contents
- [var identifier: String](unnotificationattachment/identifier.md)
  The unique identifier for the attachment.
- [var url: URL](unnotificationattachment/url.md)
  The URL of the file for this attachment.
- [var type: String](unnotificationattachment/type.md)
  The UTI type of the attachment.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Implementing communication notifications](implementing-communication-notifications.md)
  Configure and display your app’s communication notifications by using intents.
- [protocol UNNotificationContentProviding](unnotificationcontentproviding.md)
  A protocol the system uses to provide context relevant to user notifications.
- [class UNNotificationActionIcon](unnotificationactionicon.md)
  An icon associated with an action.
- [class UNMutableNotificationContent](unmutablenotificationcontent.md)
  The editable content for a notification.
- [class UNNotificationContent](unnotificationcontent.md)
  The uneditable content of a notification.
- [class UNNotificationSound](unnotificationsound.md)
  The sound played upon delivery of a notification.
- [struct UNNotificationSoundName](unnotificationsoundname.md)
  A string providing the name of a sound file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationattachment)*