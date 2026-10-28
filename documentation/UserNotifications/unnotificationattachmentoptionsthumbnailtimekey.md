# UNNotificationAttachmentOptionsThumbnailTimeKey

**Framework**: User Notifications  
**Kind**: var  
**Role**: Global Variable

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

```c
extern NSString * const UNNotificationAttachmentOptionsThumbnailTimeKey;
```

## Discussion

For animated images, the value of this key is an [`NSNumber`](../Foundation/nsnumber.md) containing the frame number to use as the thumbnail. For movies, the value of this key is the time (in seconds) into the movie from which to grab the thumbnail image; you may also specify the value as a [`CMTime`](../CoreMedia/cmtime.md) structure encoded using the [`CMTimeCopyAsDictionary(_:allocator:)`](../CoreMedia/cmtimecopyasdictionary%28_,allocator%29.md) function.

## See Also

### Creating an Attachment
- [convenience init(identifier: String, url: URL, options: [AnyHashable : Any]?) throws](./unnotificationattachment/init%28identifier,url,options%29-83grx.md)
  Creates an attachment object from the specified file and options.
- [let UNNotificationAttachmentOptionsTypeHintKey: String](./unnotificationattachmentoptionstypehintkey.md)
  A hint about an attachment’s file type.
- [let UNNotificationAttachmentOptionsThumbnailHiddenKey: String](./unnotificationattachmentoptionsthumbnailhiddenkey.md)
  A Boolean value indicating whether the system hides the attachment’s thumbnail.
- [let UNNotificationAttachmentOptionsThumbnailClippingRectKey: String](./unnotificationattachmentoptionsthumbnailclippingrectkey.md)
  The clipping rectangle for a thumbnail image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationattachmentoptionsthumbnailtimekey)*