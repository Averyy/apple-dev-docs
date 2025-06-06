# Testing custom notification interfaces

**Framework**: Watchos Apps

Test your notification interfaces on watchOS using a notification scheme and payload file.

#### Overview

When you’re ready to test your dynamic interface in the simulator, create a custom build scheme for running your notification interface. To configure the scheme, specify the JSON data file containing the test data you want delivered to your interface.

When you create a new WatchKit App project or add a WatchKit App template to an existing project, Xcode adds notification scenes by default. This includes setting up the scheme and providing `PushNotificationPayload.apns`, a file with test JSON data. This file contains most of the keys you need to simulate a remote notification; however, you can add more keys.

If Xcode added the notification scenes for you, just modify the `PushNotificationPayload.apns` file so that it contains test data appropriate for your app. If you added the notification scenes yourself, you need to set up the scheme and payload file as well.

##### Add a Scheme

As you add notifications to your app, you also need to add a scheme to test the notifications. To test multiple notification categories, add a scheme for each category.

To add a scheme, click the current scheme in Xcode’s toolbar, and select New Scheme.

![A screenshot showing the New Scheme menu item.](https://docs-assets.developer.apple.com/published/23bc5c43b706661cdd36dfb4c8477f0e/testing-custom-notification-interfaces-1%402x.png)

In the New Scheme sheet, set the Target to your WatchKit app, and give the scheme a meaningful name.

![A screenshot showing the New Scheme sheet, with the WatchKit App target set.](https://docs-assets.developer.apple.com/published/f91a57797c7f5116ef9f1d34a9f5d609/testing-custom-notification-interfaces-2%402x.png)

Click OK. Xcode adds and selects the scheme. To configure the new scheme, click the current scheme again, and select Edit Scheme.

In the Edit Scheme sheet, set the Watch Interface to Dynamic Notification. Also set the Notification Payload to the desired payload file. Then click Close.

![A screenshot showing the Edit Scheme sheet, with the notification interface and test data selected.](https://docs-assets.developer.apple.com/published/1c10ba9ef126e1f438301a9f2143e1ca/testing-custom-notification-interfaces-3%402x.png)

##### Create a Payload File

To test notification interfaces, you can specify a payload file that contains the test data for your notification. Payload files are text files with an `.apns` extension. They contain the JSON payload data for your notification. For example, a simple payload file includes the following.

```javascript
{
    "aps": {
        "alert": {
            "body": "Test message",
            "title": "Optional title",
            "subtitle": "Optional subtitle"
        },
        "category": "myCategory",
        "thread-id": "5280"
    },
    
    "Simulator Target Bundle": "<iOS or watchOS App Bundle ID>",
    
    "customKey": "Use this file to define a testing payload for your notifications. The aps dictionary specifies the category, alert text and title. The WatchKit Simulator Actions array can provide info for one or more action buttons in addition to the standard Dismiss button. Any other top level keys are custom payload. If you have multiple such JSON files in your project, you'll be able to select them when choosing to debug the notification interface of your Watch App."
}
```

Running a notification scheme sends the corresponding payload to the watch. You can also trigger a notification by dragging and dropping a payload file onto either the iPhone or Apple Watch simulator. In this case, you must set the “Simulator Target Bundle” to the correct target’s bundle ID. Also, your app must have already requested permission to receive notifications on that device. Finally, the system doesn’t necessarily deliver the notification immediately. You may have a delay of up to a minute before the notification appears.

To add a new payload file:

1. Select File > New > File.
2. In the file template sheet, make sure the iOS tab is selected, then scroll down to the Apple Watch group. Select the Notification Simulation File template and click Next.
3. Name the payload file and click Create.

![A screenshot showing the Notification Simulation File in the file template sheet.](https://docs-assets.developer.apple.com/published/d0c5f4d2efce22e41711486d4ca69683/testing-custom-notification-interfaces-4%402x.png)

The template creates a new file with the default JSON payload data. To use this file, select it in the Scheme editor when configuring the build scheme for a notification interface. You can include multiple payload files in your project and either change the build scheme or create multiple build schemes to simplify your testing.

##### Edit the Json Payload

The system packages most of the JSON data into a dictionary and delivers it to your app at runtime. You can modify the contents of the payload file to match the actual content of typical notifications sent to your app. At a minimum, change the value of the `category` key to match the name of your notification category. For more information on creating a notification payload, see [`Generating a remote notification`](https://developer.apple.com/documentation/UserNotifications/generating-a-remote-notification).

Note that the payload file includes a WatchKit Simulator Actions key. This key isn’t part of a normal notification’s payload. The Apple Watch simulator doesn’t have access to your iOS app’s registered actions, so you must define the actions in the payload file. The WatchKit Simulator Actions key contains an array of dictionaries, each of which represents an action button.

Each dictionary can contain the following keys:

##### Send Test Notifications to the Watch

Because the system automatically determines whether to deliver notifications to Apple Watch, when testing on the device, you may need to set the devices’ states to make sure the system routes the notification to Apple Watch as expected. To test your notification interfaces while the device isn’t on your wrist:

- Disable Wrist Detection on Apple Watch. You can set this in the Watch app on the companion iPhone or in the Settings app on the watch. The option is under Passcode > Wrist Detection.
- Make sure your Apple Watch isn’t on a charger.
- Make sure to lock your iPhone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-apps/testing-custom-notification-interfaces)*