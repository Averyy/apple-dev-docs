# handle(_:)

**Framework**: Watchkit  
**Kind**: method

Responds to Handoff–related activity from Siri.

**Availability**:
- watchOS 3.2+

## Declaration

```swift
@MainActor
optional func handle(_ userActivity: NSUserActivity)
```

## Mentions

- [Handling User Activity](handling-user-activity.md)

#### Discussion

The WatchKit app extension calls this method when it receives data associated with a user activity. Use this method to update your app on Apple Watch so that the user can continue the activity from where they left off.

##### Handling Activities From Sirikit

This method is called whenever your app is launched to handle a SiriKit intent. Update your app’s user interface based on the `userActivity` parameter. Your app should seamlessly continue the interaction that began in Siri.

By default, the intent provides an [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object whose [`interaction`](https://developer.apple.com/documentation/foundation/nsuseractivity/1690346-interaction) property contains both the originating intent and your response. You can add additional, app-specific information by creating a new [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object in your intent’s `confirm` or `handle` method, and adding your data to the activity’s [`userInfo`](https://developer.apple.com/documentation/foundation/nsuseractivity/1411706-userinfo) dictionary.

When continuing activities from SiriKit:

- Look for the intent specified in the [`interaction`](https://developer.apple.com/documentation/foundation/nsuseractivity/1690346-interaction) property. Resume handling this intent in your app.
- Avoid accidentally repeating actions (such as making double payments). For example, check the `INInteraction` object’s `intentResponse` property to see if the action has already been completed.

Intents may launch your app under the following circumstances:

- Some intents always launch the app after the intent is successfully handled (for example, intents with a `continueInApp` response code).
- Your intent’s `handle` and `confirm` methods launch the app when you resolve the intent with a `failureRequiringAppLaunch` (or similar) response code.
- The user can always decide to launch the app at any point in a Siri transaction.

## Parameters

- `userActivity`: The activity object containing the data associated with the task the user was performing. Use the data to continue the user’s activity in your app on Apple Watch.

## See Also

- [func handleUserActivity([AnyHashable : Any]?)](wkextensiondelegate/handleuseractivity(_:).md)
  Responds to Handoff–related activity from complications and notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handle(_:)-5pyj1)*