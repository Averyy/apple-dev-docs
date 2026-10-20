# UNNotificationAttachmentOptionsThumbnailHiddenKey

**Framework**: User Notifications  
**Kind**: var  
**Role**: Global Variable

A Boolean value indicating whether the system hides the attachment’s thumbnail.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
let UNNotificationAttachmentOptionsThumbnailHiddenKey: String
```

```c
extern NSString * const UNNotificationAttachmentOptionsThumbnailHiddenKey;
```

#### Discussion

The value of this key is an [`NSNumber`](../Foundation/nsnumber.md) containing a Boolean value. When set to [`true`](../Swift/true.md), the attachment’s thumbnail isn’t displayed. If you don’t include this key, the system shows the thumbnail.

## See Also

### Creating an Attachment
- [convenience init(identifier: String, url: URL, options: [AnyHashable : Any]?) throws](./unnotificationattachment/init%28identifier,url,options%29-83grx.md)
  Creates an attachment object from the specified file and options.
- [let UNNotificationAttachmentOptionsTypeHintKey: String](./unnotificationattachmentoptionstypehintkey.md)
  A hint about an attachment’s file type.
- [let UNNotificationAttachmentOptionsThumbnailClippingRectKey: String](./unnotificationattachmentoptionsthumbnailclippingrectkey.md)
  The clipping rectangle for a thumbnail image.
- [let UNNotificationAttachmentOptionsThumbnailTimeKey: String](./unnotificationattachmentoptionsthumbnailtimekey.md)
  The frame number of an animation to use as a thumbnail image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationattachmentoptionsthumbnailhiddenkey)*