# UNNotificationAttachmentOptionsTypeHintKey

**Framework**: User Notifications  
**Kind**: var  
**Role**: Global Variable

A hint about an attachment’s file type.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
let UNNotificationAttachmentOptionsTypeHintKey: String
```

```c
extern NSString * const UNNotificationAttachmentOptionsTypeHintKey;
```

#### Discussion

The value of this key is an [`NSString`](../Foundation/nsstring.md) containing a Uniform Type Identifier (UTI) that describes the file’s type. If you don’t include this key, the system uses the attachment’s filename extension to determine its type.

## See Also

### Creating an Attachment
- [convenience init(identifier: String, url: URL, options: [AnyHashable : Any]?) throws](./unnotificationattachment/init%28identifier,url,options%29-83grx.md)
  Creates an attachment object from the specified file and options.
- [let UNNotificationAttachmentOptionsThumbnailHiddenKey: String](./unnotificationattachmentoptionsthumbnailhiddenkey.md)
  A Boolean value indicating whether the system hides the attachment’s thumbnail.
- [let UNNotificationAttachmentOptionsThumbnailClippingRectKey: String](./unnotificationattachmentoptionsthumbnailclippingrectkey.md)
  The clipping rectangle for a thumbnail image.
- [let UNNotificationAttachmentOptionsThumbnailTimeKey: String](./unnotificationattachmentoptionsthumbnailtimekey.md)
  The frame number of an animation to use as a thumbnail image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationattachmentoptionstypehintkey)*