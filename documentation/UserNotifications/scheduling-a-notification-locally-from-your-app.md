# Scheduling a notification locally from your app

**Framework**: User Notifications

Create and schedule notifications from your app when you want to get the user’s attention.

#### Overview

Use local notifications to get the user’s attention. You can display an alert, play a sound, or badge your app’s icon. For example, a background app could ask the system to display an alert when your app finishes a particular task. Always use local notifications to convey important information that the user wants.

The system handles delivery of notifications based on a time or location that you specify. If the delivery of the notification occurs when your app isn’t running or in the background, the system interacts with the user for you. If your app is in the foreground, the system delivers the notification to your app for handling.

##### Create the Notifications Content

Fill in the properties of a [`UNMutableNotificationContent`](unmutablenotificationcontent.md) object with the details of your notification. The fields you fill in define how the system delivers your notification. For example, to play a sound, assign a value to the [`sound`](unnotificationcontent/sound.md) property of the object. Listing 1 shows a content object that displays an alert containing a title string and body text. You can specify multiple types of interaction in the same request.

Listing 1. Configuring the notification content

```swift
let content = UNMutableNotificationContent()
content.title = "Weekly Staff Meeting"
content.body = "Every Tuesday at 2pm"
```

##### Specify the Conditions for Delivery

Specify the conditions for delivering your notification using a [`UNCalendarNotificationTrigger`](uncalendarnotificationtrigger.md), [`UNTimeIntervalNotificationTrigger`](untimeintervalnotificationtrigger.md), or [`UNLocationNotificationTrigger`](unlocationnotificationtrigger.md) object. Each trigger object requires different parameters. For example, a calendar-based trigger requires you to specify the date and time of delivery.

Listing 2 shows you how to configure a notification for the system to deliver every Tuesday at 2pm. The [`DateComponents`](https://developer.apple.com/documentation/Foundation/DateComponents) structure specifies the timing for the event. Configuring the trigger with the `repeats` parameter set to [`true`](https://developer.apple.com/documentation/Swift/true) causes the system to reschedule the event after its delivery.

Listing 2. Configuring a recurring date-based trigger

```swift
// Configure the recurring date.
var dateComponents = DateComponents()
dateComponents.calendar = Calendar.current

dateComponents.weekday = 3  // Tuesday
dateComponents.hour = 14    // 14:00 hours
   
// Create the trigger as a repeating event.    
let trigger = UNCalendarNotificationTrigger(
         dateMatching: dateComponents, repeats: true)
```

##### Create and Register a Notification Request

Create a [`UNNotificationRequest`](unnotificationrequest.md) object that includes your content and trigger conditions, and call the  ([`add(_:withCompletionHandler:)`](unusernotificationcenter/add(_:withcompletionhandler:).md) method to schedule your request with the system. Listing 1 shows an example that uses the content from Listing 1 and Listing 2 to fill in the request object.

Listing 1. Registering the notification request

```swift
let uuidString = UUID().uuidString
let request = UNNotificationRequest(identifier: uuidString, content: content, trigger: trigger)

// Schedule the request with the system.
let notificationCenter = UNUserNotificationCenter.current()
do {
    try await notificationCenter.add(request)
} catch {
    // Handle errors that may occur during add.
}
```

##### Cancel a Scheduled Notification Request

Once scheduled, a notification request remains active until its trigger condition is met, or you explicitly cancel it. Typically, you cancel a request when conditions change and you no longer need to notify the user. For example, if the user completes a reminder, you’d cancel any active requests associated with that reminder. To cancel an active notification request, call the [`removePendingNotificationRequests(withIdentifiers:)`](unusernotificationcenter/removependingnotificationrequests(withidentifiers:).md) method of [`UNUserNotificationCenter`](unusernotificationcenter.md).

## Topics

### Related Topics
- [Handling notifications and notification-related actions](handling-notifications-and-notification-related-actions.md)
  Respond to user interactions with the system’s notification interfaces, including handling your app’s custom actions.

## See Also

- [class UNNotificationRequest](unnotificationrequest.md)
  A request to schedule a local notification, which includes the content of the notification and the trigger conditions for delivery.
- [class UNNotification](unnotification.md)
  The data for a local or remote notification the system delivers to your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/scheduling-a-notification-locally-from-your-app)*