# handle(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Responds to Handoff–related activity from Siri.

**Availability**:
- watchOS 3.2+ - Deprecated in 9.2

## Declaration

```swift
optional func handle(_ userActivity: NSUserActivity)
```

```objc
- (void) handleActivity:(NSUserActivity *) userActivity;
```

## Mentions

- [Handling User Activity](../handling-user-activity.md)

#### Discussion

The WatchKit app extension calls this method when it receives data associated with a user activity. Use this method to update your app on Apple Watch so that the user can continue the activity from where they left off.

##### Handling Activities from SiriKit

This method is called whenever your app is launched to handle a SiriKit intent. Update your app’s user interface based on the `userActivity` parameter. Your app should seamlessly continue the interaction that began in Siri.

By default, the intent provides an [`NSUserActivity`](../../Foundation/nsuseractivity.md) object whose [`interaction`](../../Foundation/nsuseractivity/interaction.md) property contains both the originating intent and your response. You can add additional, app-specific information by creating a new [`NSUserActivity`](../../Foundation/nsuseractivity.md) object in your intent’s `confirm` or `handle` method, and adding your data to the activity’s [`userInfo`](../../Foundation/nsuseractivity/userinfo.md) dictionary.

When continuing activities from SiriKit:

- Look for the intent specified in the [`interaction`](../../Foundation/nsuseractivity/interaction.md) property. Resume handling this intent in your app.
- Avoid accidentally repeating actions (such as making double payments). For example, check the `INInteraction` object’s `intentResponse` property to see if the action has already been completed.

Intents may launch your app under the following circumstances:

- Some intents always launch the app after the intent is successfully handled (for example, intents with a `continueInApp` response code).
- Your intent’s `handle` and `confirm` methods launch the app when you resolve the intent with a `failureRequiringAppLaunch` (or similar) response code.
- The user can always decide to launch the app at any point in a Siri transaction.

## Parameters

- `userActivity`: The activity object containing the data associated with the task the user was performing. Use the data to continue the user’s activity in your app on Apple Watch.

## See Also

### Coordinating handoff activity
- [func handleUserActivity([AnyHashable : Any]?)](./handleuseractivity%28_%29.md)
  Responds to Handoff–related activity from complications and notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handle(_:)-5pyj1)*