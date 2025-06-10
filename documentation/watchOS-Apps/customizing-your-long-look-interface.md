# Customizing your long-look interface

**Framework**: watchOS apps

Create custom interfaces for your watchOS app’s notifications.

#### Overview

To customize the appearance of your app’s notifications, you can provide a [`Scene`](https://developer.apple.com/documentation/SwiftUI/Scene) to your [`App`](https://developer.apple.com/documentation/SwiftUI/App) for each notification category. The scene defines either a  or a  interface.

Use the interactive controls to update or even reload the notification’s interface. In general, keep your action methods simple. Complex, multi-step tasks aren’t a good fit for interactive notifications.

##### Create a Notification Scene

The following code creates a notification scene using the [`WKNotificationScene`](https://developer.apple.com/documentation/SwiftUI/WKNotificationScene) struct, specifying both the notification controller’s class and the notification’s category.

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

When the system receives a notification with a matching category, it displays a dynamic view specified by the notification controller. By default, the view isn’t interactive; however, you can make the view interactive by returning [`true`](https://developer.apple.com/documentation/swift/true) from the notification controller’s [`isInteractive`](https://developer.apple.com/documentation/SwiftUI/WKUserNotificationHostingController/isInteractive) property.

```swift
// Create a dynamic, interactive notification interface.
override class var isInteractive: Bool {
    return true
}
```

##### Customize the Interface

To display a custom interface, override the notification controller’s [`didReceive(_:)`](https://developer.apple.com/documentation/WatchKit/WKUserNotificationInterfaceController/didReceive(_:)) method to extract information from the incoming notification.

```swift
override func didReceive(_ notification: UNNotification) {
    content = notification.request.content
    date = notification.date
}
```

Then, override the [`body`](https://developer.apple.com/documentation/SwiftUI/WKUserNotificationHostingController/body) property to create the notification view using the notification’s content.

```swift
override var body: NotificationView {
    return NotificationView(content: content, date: date)
}
```

The navigation view is a standard SwiftUI view. In the view’s [`body`](https://developer.apple.com/documentation/SwiftUI/View/body-8kl5o), you lay out the content from your notification.

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