# Declaring your actionable notification types

**Framework**: Usernotifications

Differentiate your notifications and add action buttons to the notification interface.

#### Overview

Actionable notifications let the user respond to a delivered notification without launching the corresponding app. Other notifications display information in a notification interface, but the user’s only course of action is to launch the app. For an actionable notification, the system displays one or more buttons in addition to the notification interface. Tapping a button sends the selected action to the app, which then processes the action in the background.

![A notification for a meeting app contains an invitation along with buttons for accepting or declining the invitation.](https://docs-assets.developer.apple.com/published/b7551599d1d79bbde862870b8b2c59f2/media-2953609%402x.png)

> **Note**:  When someone performs a Double Tap gesture while viewing a notification on Apple Watch Series 9 or Apple Watch Ultra 2, the system invokes the first nondestructive action. A nondestructive action doesn’t include the [`destructive`](unnotificationactionoptions/destructive.md) option, and won’t delete user data or change the app irrevocably.

 When someone performs a Double Tap gesture while viewing a notification on Apple Watch Series 9 or Apple Watch Ultra 2, the system invokes the first nondestructive action. A nondestructive action doesn’t include the [`destructive`](unnotificationactionoptions/destructive.md) option, and won’t delete user data or change the app irrevocably.

To support actionable notifications, you must:

- Declare one or more notification categories at launch time from your iOS app.
- Assign appropriate actions to your notification categories.
- Handle all actions that you register.
- Assign category identifiers to notification payloads when generating notifications.

> **Note**:  The system also uses categories to determine whether it should launch your notification service app extension or notification content app extension. For information about how to create a notification service app extension, see [`Modifying content in newly delivered notifications`](modifying-content-in-newly-delivered-notifications.md). For information about how to create a notification content app extension, see [`Customizing the Appearance of Notifications`](https://developer.apple.com/documentation/UserNotificationsUI/customizing-the-appearance-of-notifications).

 The system also uses categories to determine whether it should launch your notification service app extension or notification content app extension. For information about how to create a notification service app extension, see [`Modifying content in newly delivered notifications`](modifying-content-in-newly-delivered-notifications.md). For information about how to create a notification content app extension, see [`Customizing the Appearance of Notifications`](https://developer.apple.com/documentation/UserNotificationsUI/customizing-the-appearance-of-notifications).

##### Declare Your Custom Actions and Notification Types

Because your app must handle all actions, you must declare the actions that your app supports at launch time. You declare actions using a combination of category and action objects. [`UNNotificationCategory`](unnotificationcategory.md) objects define the types of notifications that your app supports, and [`UNNotificationAction`](unnotificationaction.md) objects define the buttons to display for each type. For example, a notification for a meeting invitation might include buttons to accept or reject the invitation.

Each [`UNNotificationCategory`](unnotificationcategory.md) object has a unique identifier and options for how you want to handle notifications of that type. The string in the [`identifier`](unnotificationcategory/identifier.md) property is the most important part of the category object. When generating notifications, you must include the same string in your notification’s payload. The system uses that string to locate the corresponding category object and any actions.

To associate actions with a notification category, assign one or more [`UNNotificationAction`](unnotificationaction.md) objects to it. Each action object contains the localized string to display to the user and options indicating how you want that action handled. For example, when you tag an action as destructive, the system displays it with a different highlight to indicate its behavior.

Listing 1 shows how to register a custom category with two actions. In addition to a title and options, each action has a unique identifier. When the user selects the action, the system passes that identifier to your app.

Listing 1. Registering actions and notification types

```swift
// Define the custom actions.
let acceptAction = UNNotificationAction(identifier: "ACCEPT_ACTION",
      title: "Accept", 
      options: [])
let declineAction = UNNotificationAction(identifier: "DECLINE_ACTION",
      title: "Decline", 
      options: [])
// Define the notification type
let meetingInviteCategory = 
      UNNotificationCategory(identifier: "MEETING_INVITATION",
      actions: [acceptAction, declineAction], 
      intentIdentifiers: [], 
      hiddenPreviewsBodyPlaceholder: "",
      options: .customDismissAction)
// Register the notification type.
let notificationCenter = UNUserNotificationCenter.current()
notificationCenter.setNotificationCategories([meetingInviteCategory])
```

> ❗ **Important**:  All of your action objects must have unique identifiers. When handling actions, the identifier is the only way to distinguish one action from another, even when those actions belong to different categories.

 All of your action objects must have unique identifiers. When handling actions, the identifier is the only way to distinguish one action from another, even when those actions belong to different categories.

Most actions result in a user selection, but text input actions also let the user type custom text-based responses. Your app can then incorporate the user’s typed response into your handling of the action. For example, a messaging app could send the typed text as the response to an incoming message. To create a text input action, create a [`UNTextInputNotificationAction`](untextinputnotificationaction.md) object instead of a [`UNNotificationAction`](unnotificationaction.md) object. When the user taps the button for a text input action, the system displays an editable text field. When reporting the action to your app, the system includes the text that the user typed as part of the response.

##### Include a Notification Category in the Payload

The system displays actions only for notifications whose payload contains a valid category identifier string. The system uses the category identifier to look up your app’s registered categories and their associated actions. It then uses that information to add the action buttons to the notification interface.

To assign a category to a local notification, assign the appropriate string to the [`categoryIdentifier`](unmutablenotificationcontent/categoryidentifier.md) property of your [`UNMutableNotificationContent`](unmutablenotificationcontent.md) object. Listing 2 shows the creation of the content for a local notification. In addition to the basic information, this code also adds custom data to the notification’s [`userInfo`](unmutablenotificationcontent/userinfo.md) dictionary, which it uses later to process the invitation.

Listing 2. Assigning a category to a local notification

```swift
let content = UNMutableNotificationContent()
content.title = "Weekly Staff Meeting"
content.body = "Every Tuesday at 2pm"
content.userInfo = ["MEETING_ID" : meetingID, 
                    "USER_ID" : userID ]
content.categoryIdentifier = "MEETING_INVITATION"
```

To add a category identifier to a remote notification, include the `category` key in the `aps` dictionary of your JSON payload, as shown in Listing 3. Set the value of this key to the appropriate category string. In the example, the category is set to the same meeting invitation category that was previously defined. As in the local notification example, the payload includes custom keys with the meeting ID and user ID, which are put into the payload’s [`userInfo`](unnotificationcontent/userinfo.md) dictionary. The app can use that information to accept or decline the invitation.

Listing 3. Assigning a category to a remote notification

```other
{
   "aps" : {
      "category" : "MEETING_INVITATION"
      "alert" : {
         "title" : "Weekly Staff Meeting"
         "body" : "Every Tuesday at 2pm"
      },
   },
   "MEETING_ID" : "123456789",
   "USER_ID" : "ABCD1234"

} 
```

##### Handle the Selected Action

Your app must handle all of the actions that it defines. When the user selects an action, the system launches your app in the background and notifies the shared [`UNUserNotificationCenter`](unusernotificationcenter.md) object, which notifies its delegate. Use your delegate object’s [`userNotificationCenter(_:didReceive:withCompletionHandler:)`](unusernotificationcenterdelegate/usernotificationcenter(_:didreceive:withcompletionhandler:).md) method to identify the selected action and provide an appropriate response.

Listing 4 shows an implementation of the delegate method for an app that manages meeting invitations. The method uses the [`actionIdentifier`](unnotificationresponse/actionidentifier.md) property of the response to determine whether to accept or decline a given invitation. It also relies on custom data from the notification payload to process the notification successfully. Always call the completion handler after you finish handling the action.

Listing 4. Performing a selected action

```swift
func userNotificationCenter(_ center: UNUserNotificationCenter,
       didReceive response: UNNotificationResponse,
       withCompletionHandler completionHandler: 
         @escaping () -> Void) {
       
   // Get the meeting ID from the original notification.
   let userInfo = response.notification.request.content.userInfo
   let meetingID = userInfo["MEETING_ID"] as! String
   let userID = userInfo["USER_ID"] as! String
        
   // Perform the task associated with the action.
   switch response.actionIdentifier {
   case "ACCEPT_ACTION":
      sharedMeetingManager.acceptMeeting(user: userID, 
                                    meetingID: meetingID)
      break
        
   case "DECLINE_ACTION":
      sharedMeetingManager.declineMeeting(user: userID, 
                                     meetingID: meetingID)
      break
        
   // Handle other actions...
   default:
      break
   }
    
   // Always call the completion handler when done.    
   completionHandler()
}
```

> ❗ **Important**:  If your response to an action involves accessing files on disk, consider a different approach. Users can respond to actions while the device is locked, which would make files encrypted with the [`complete`](https://developer.apple.com/documentation/foundation/fileprotectiontype/1616200-complete) option unavailable to your app. If that happens, you may need to save changes temporarily and integrate them into your app’s data structures later.

 If your response to an action involves accessing files on disk, consider a different approach. Users can respond to actions while the device is locked, which would make files encrypted with the [`complete`](https://developer.apple.com/documentation/foundation/fileprotectiontype/1616200-complete) option unavailable to your app. If that happens, you may need to save changes temporarily and integrate them into your app’s data structures later.

## See Also

- [class UNNotificationCategory](unnotificationcategory.md)
  A type of notification your app supports and the custom actions that the system displays.
- [class UNNotificationAction](unnotificationaction.md)
  A task your app performs in response to a notification that the system delivers.
- [class UNTextInputNotificationAction](untextinputnotificationaction.md)
  An action that accepts user-typed text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/declaring-your-actionable-notification-types)*