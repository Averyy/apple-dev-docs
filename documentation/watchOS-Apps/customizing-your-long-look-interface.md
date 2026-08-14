# Customizing your long-look interface

**Framework**: watchOS apps

Create custom interfaces for your watchOS app’s notifications.

#### Overview

To customize the appearance of your app’s notifications, you can provide a [`Scene`](https://developer.apple.com/documentation/swiftui/scene) to your [`App`](https://developer.apple.com/documentation/swiftui/app) for each notification category. The scene defines either a *dynamic* or a *dynamic interactive* interface.

- **Dynamic interface**: Displays content that you can configure at runtime based on the notification’s payload. When designing a dynamic notification interface, use labels, images, groups, and separators to build the bulk of your interface. Include tables and maps only as needed. You can also use SpriteKit scenes, SceneKit scenes, or inline videos to produce visually rich notifications. Don’t include buttons, switches, or other interactive controls.
- **Dynamic interactive interface**: Contains controls like buttons or switches. Like the dynamic interface, you can configure this interface at runtime. It also lets the user interact directly with the notification.

Use the interactive controls to update or even reload the notification’s interface. In general, keep your action methods simple. Complex, multi-step tasks aren’t a good fit for interactive notifications.

##### Create a Notification Scene

The following code creates a notification scene using the [`WKNotificationScene`](https://developer.apple.com/documentation/swiftui/wknotificationscene) struct, specifying both the notification controller’s class and the notification’s category.

```swift
var body: some Scene {
    WindowGroup {
        NavigationView {
            ContentView()
        }
    }

    WKNotificationScene(controller: NotificationController.self, category: "myNotificationCategory")

}
```

When the system receives a notification with a matching category, it displays a dynamic view specified by the notification controller. By default, the view isn’t interactive; however, you can make the view interactive by returning [`true`](https://developer.apple.com/documentation/swift/true) from the notification controller’s [`isInteractive`](https://developer.apple.com/documentation/swiftui/wkusernotificationhostingcontroller/isinteractive) property.

```swift
// Create a dynamic, interactive notification interface.
override class var isInteractive: Bool {
    return true
}
```

##### Customize the Interface

To display a custom interface, override the notification controller’s [`didReceive(_:)`](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/didreceive(_:)) method to extract information from the incoming notification.

```swift
override func didReceive(_ notification: UNNotification) {
    content = notification.request.content
    date = notification.date
}
```

Then, override the [`body`](https://developer.apple.com/documentation/swiftui/wkusernotificationhostingcontroller/body) property to create the notification view using the notification’s content.

```swift
override var body: NotificationView {
    return NotificationView(content: content, date: date)
}
```

The navigation view is a standard SwiftUI view. In the view’s [`body`](https://developer.apple.com/documentation/swiftui/view/body-8kl5o), you lay out the content from your notification.

```swift
@State private var showMore = false

var body: some View {
    VStack {
        Text(title)
            .font(.headline)
        Text(subtitle)

        if showMore {
            Divider()
            Text(messageBody)
            Divider()
        }

        Text(time)
        Spacer()
        Toggle("Show more", isOn: $showMore)
    }
}
```

## See Also

- [Taking advantage of notification forwarding](taking-advantage-of-notification-forwarding.md)
  Deliver notifications to the user’s iPhone or Apple Watch.
- [Adding actions to notifications on watchOS](adding-actions-to-notifications-on-watchos.md)
  Provide a set of responses to a notification.
- [Grouping notifications](grouping-notifications.md)
  Organize notifications into threads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-apps/customizing-your-long-look-interface)*