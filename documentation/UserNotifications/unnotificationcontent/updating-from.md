# updating(from:)

**Framework**: User Notifications  
**Kind**: method

Returns a copy of the notification that includes content from the specified provider.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func updating(from provider: any UNNotificationContentProviding) throws -> UNNotificationContent
```

## Mentions

- [Implementing communication notifications](implementing-communication-notifications.md)

#### Return Value

The notification content object for the content handler.

#### Discussion

The system contextualizes your [`UNNotificationContent`](unnotificationcontent.md) object with other Apple SDK objects conforming to [`UNNotificationContentProviding`](unnotificationcontentproviding.md). The system specializes the notification and decorates its look and behavior accordingly.

For example, the system treats the notification as a message with an avatar and promotes it to the top of notification center if the object passed in is a valid [`INSendMessageIntent`](https://developer.apple.com/documentation/Intents/INSendMessageIntent) that conforms to `UNNotificationContentProviding`. The system throws an error with a [`UNError.Code`](unerror/code.md), if the `UNNotificationContentProviding` object is invalid. Pass the valid `UNNotificationContent` result directly to [`UNUserNotificationCenter`](unusernotificationcenter.md) without mutating.

Add this call to the [`UNNotificationServiceExtension`](unnotificationserviceextension.md) in [`didReceive(_:withContentHandler:)`](unnotificationserviceextension/didreceive(_:withcontenthandler:).md). Your app passes the returned `UNNotificationContent` to the `contentHandler` for incoming push notifications.

## Parameters

- `provider`: The notification content providing object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationcontent/updating(from:))*