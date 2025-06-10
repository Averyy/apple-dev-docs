# UNNotificationAttachmentOptionsThumbnailTimeKey

**Framework**: User Notifications  
**Kind**: var

The frame number of an animation to use as a thumbnail image.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
let UNNotificationAttachmentOptionsThumbnailTimeKey: String
```

#### Discussion

For animated images, the value of this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) containing the frame number to use as the thumbnail. For movies, the value of this key is the time (in seconds) into the movie from which to grab the thumbnail image; you may also specify the value as a [`CMTime`](https://developer.apple.com/documentation/CoreMedia/CMTime) structure encoded using the [`CMTimeCopyAsDictionary(_:allocator:)`](https://developer.apple.com/documentation/CoreMedia/CMTimeCopyAsDictionary(_:allocator:)) function.

## See Also

- [convenience init(identifier: String, url: URL, options: [AnyHashable : Any]?) throws](unnotificationattachment/init(identifier:url:options:).md)
  Creates an attachment object from the specified file and options.
- [let UNNotificationAttachmentOptionsTypeHintKey: String](unnotificationattachmentoptionstypehintkey.md)
  A hint about an attachment’s file type.
- [let UNNotificationAttachmentOptionsThumbnailHiddenKey: String](unnotificationattachmentoptionsthumbnailhiddenkey.md)
  A Boolean value indicating whether the system hides the attachment’s thumbnail.
- [let UNNotificationAttachmentOptionsThumbnailClippingRectKey: String](unnotificationattachmentoptionsthumbnailclippingrectkey.md)
  The clipping rectangle for a thumbnail image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationattachmentoptionsthumbnailtimekey)*