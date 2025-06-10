# init(identifier:url:options:)

**Framework**: User Notifications  
**Kind**: init

Creates an attachment object from the specified file and options.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
convenience init(identifier: String, url URL: URL, options: [AnyHashable : Any]? = nil) throws
```

#### Return Value

An attachment object containing information about the specified file or `nil` if the attachment could not be created.

#### Discussion

This method verifies that the specified file is readable and that the file format is one of the supported types. When errors occur, the method provides an appropriate `error` object.

When you schedule a notification request containing the attachment, the system moves the attachment’s file to a new location to facilitate access by the appropriate processes. After the move, the only way to access the file is using the methods of the [`UNUserNotificationCenter`](unusernotificationcenter.md) object.

## Parameters

- `identifier`: The unique identifier of the attachment. Use this string to identify the attachment later. If you specify an empty string, this method creates a unique identifier string for you.
- `URL`: The URL of the file you want to attach to the notification. The URL must be a file URL and the file must be readable by the current process. This parameter must not be  . For a list of supported file types, see  .
- `options`: A dictionary of options related to the attached file. Use the options to specify meta information about the attachment, such as the clipping rectangle to use for the resulting thumbnail.

## See Also

- [let UNNotificationAttachmentOptionsTypeHintKey: String](unnotificationattachmentoptionstypehintkey.md)
  A hint about an attachment’s file type.
- [let UNNotificationAttachmentOptionsThumbnailHiddenKey: String](unnotificationattachmentoptionsthumbnailhiddenkey.md)
  A Boolean value indicating whether the system hides the attachment’s thumbnail.
- [let UNNotificationAttachmentOptionsThumbnailClippingRectKey: String](unnotificationattachmentoptionsthumbnailclippingrectkey.md)
  The clipping rectangle for a thumbnail image.
- [let UNNotificationAttachmentOptionsThumbnailTimeKey: String](unnotificationattachmentoptionsthumbnailtimekey.md)
  The frame number of an animation to use as a thumbnail image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationattachment/init(identifier:url:options:))*