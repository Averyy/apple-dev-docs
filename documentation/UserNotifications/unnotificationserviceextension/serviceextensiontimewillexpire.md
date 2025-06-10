# serviceExtensionTimeWillExpire()

**Framework**: User Notifications  
**Kind**: method

Tells you that the system is terminating your extension.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func serviceExtensionTimeWillExpire()
```

## Mentions

- [Modifying content in newly delivered notifications](modifying-content-in-newly-delivered-notifications.md)

#### Discussion

If your [`didReceive(_:withContentHandler:)`](unnotificationserviceextension/didreceive(_:withcontenthandler:).md) method takes too long to execute its completion block, the system calls this method on a separate thread to give you one last chance to execute the block. Use this method to execute the block as quickly as possible. Doing so might mean providing some fallback content. For example, if your extension is still downloading an image file with the intent of attaching it to the notification’s content, update the notification’s alert text to indicate that an image download is in progress. If you fail to execute the completion block from the [`didReceive(_:withContentHandler:)`](unnotificationserviceextension/didreceive(_:withcontenthandler:).md) method in time, the system displays the notification’s original content.

## See Also

- [func didReceive(UNNotificationRequest, withContentHandler: (UNNotificationContent) -> Void)](unnotificationserviceextension/didreceive(_:withcontenthandler:).md)
  Asks you to make any needed changes to the notification and notify the system when you’re done.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationserviceextension/serviceextensiontimewillexpire())*