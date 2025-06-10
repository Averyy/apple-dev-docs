# Authenticating users on Apple Watch

**Framework**: watchOS apps

Create an account sign-up and sign-in strategy for your app.

#### Overview

Users can launch an independent watchOS app as soon as it downloads, even if they don’t have their iPhone. As a result, users must be able to set up the application directly on Apple Watch. If your app requires an account, users must be able to create it and sign in on the watch.

You have the following options for syncing or saving user data:

- Create an app that doesn’t require user accounts. Design your app so that it provides a full set of features without user accounts, or use CloudKit to sync and store your user’s data. Apps can access CloudKit data based on the user’s Apple ID without in-app sign-in. watchOS 6 and later also supports CloudKit subscriptions and notifications to let your app respond to changes from other devices.
- Authenticate users with Sign In with Apple. This feature authenticates users based on their Apple ID. For more information, see [`WKInterfaceAuthorizationAppleIDButton`](https://developer.apple.com/documentation/WatchKit/WKInterfaceAuthorizationAppleIDButton) and [`Authentication Services`](https://developer.apple.com/documentation/AuthenticationServices).
- Create custom sign-in and sign-up forms.

If you choose to create custom forms, watchOS 6 provides tools designed to fit the small screen size and to streamline data entry on Apple Watch.

##### Simplify Account Creation and Sign in

Create your sign-in and sign-up forms using text fields. In SwiftUI, use the [`TextField`](https://developer.apple.com/documentation/SwiftUI/TextField) and [`SecureField`](https://developer.apple.com/documentation/SwiftUI/SecureField) structures. In the storyboard, use the [`WKInterfaceTextField`](https://developer.apple.com/documentation/WatchKit/WKInterfaceTextField) class.

To streamline data entry, perform the following steps:

1. Set the text field’s content type. The text field’s content type modifies how the text input controller and Apple Continuity Keyboard behave. For SwiftUI, set the content type by calling the text field’s [`textContentType(_:)`](https://developer.apple.com/documentation/SwiftUI/View/textContentType(_:)-4dqqb) method. For the storyboard, set the content type using the Attributes inspector.
2. Provide a placeholder that describes the text field’s expected content. Effective placeholders help you get the most out of Apple Watch’s smaller screen. For SwiftUI, when instantiating the text field, the `title` property sets the placeholder. For the storyboard, set the placeholder using the Attributes inspector. Note that the system truncates placeholders if the text is too long, so keep your placeholders short.
3. Set up your app’s associated domains. If you have a website where users can sign in with the same username and password, associate the website’s domain with your app. An associated domain tells the Apple Continuity Keyboard to provide autofill suggestions for usernames and passwords from that domain. To learn how to set up your app’s associated domains, see [`Supporting associated domains`](https://developer.apple.com/documentation/Xcode/supporting-associated-domains).

##### Support Password Autofill

To support password autofill on Apple Watch, set the following [`WKTextContentType`](https://developer.apple.com/documentation/WatchKit/WKTextContentType) values.

| Credential | Content Type |
| --- | --- |
| User Name | [`username`](https://developer.apple.com/documentation/WatchKit/WKTextContentType/username) |
| Password | [`password`](https://developer.apple.com/documentation/WatchKit/WKTextContentType/password) |
| New Password | [`newPassword`](https://developer.apple.com/documentation/WatchKit/WKTextContentType/newPassword) |
| One-Time Code | [`oneTimeCode`](https://developer.apple.com/documentation/WatchKit/WKTextContentType/oneTimeCode) |

For [`TextField`](https://developer.apple.com/documentation/SwiftUI/TextField) and [`SecureField`](https://developer.apple.com/documentation/SwiftUI/SecureField), set the content type by calling the [`textContentType(_:)`](https://developer.apple.com/documentation/SwiftUI/View/textContentType(_:)-4dqqb) method.

```swift
var body: some View {
    VStack {
        TextField("User Name", text: $userName)
            .textContentType(.username)
            .multilineTextAlignment(.center)
        SecureField("Password", text: $password)
            .textContentType(.password)
            .multilineTextAlignment(.center)
        Button("Done") {
        }.disabled(userName.isEmpty || password.isEmpty)
    }
}
```

For [`WKInterfaceTextField`](https://developer.apple.com/documentation/WatchKit/WKInterfaceTextField), assign these values in Xcode by setting the Content Type attribute in the Attributes inspector.

![A screenshot showing the Content Type attribute in the Attributes inspector.](https://docs-assets.developer.apple.com/published/504418c9024b811f847d0371089764b4/authenticating-users-on-apple-watch-1%402x.png)

watchOS provides an autofill suggestion for [`oneTimeCode`](https://developer.apple.com/documentation/WatchKit/WKTextContentType/oneTimeCode) fields after receiving an SMS message that contains a one-time code.

If you place a [`username`](https://developer.apple.com/documentation/WatchKit/WKTextContentType/username) or [`emailAddress`](https://developer.apple.com/documentation/WatchKit/WKTextContentType/emailAddress) text field on the same screen as a [`password`](https://developer.apple.com/documentation/WatchKit/WKTextContentType/password) text field, the Apple Continuity Keyboard attempts to fill both fields. Similarly, if you put two [`newPassword`](https://developer.apple.com/documentation/WatchKit/WKTextContentType/newPassword) fields on the same screen, the keyboard automatically fills both when the user selects the suggested password.

For more information, see [`Password AutoFill`](https://developer.apple.com/documentation/Security/password-autofill).

## See Also

- [Setting up a watchOS project](setting-up-a-watchos-project.md)
  Create a new watchOS project or add a watch target to an existing iOS project.
- [Creating independent watchOS apps](creating-independent-watchos-apps.md)
  Set up a watchOS app that installs and runs without a companion iOS app.
- [Keeping your watchOS content up to date](keeping-your-watchos-app-s-content-up-to-date.md)
  Ensure that your app’s content is relevant and up to date.
- [Updating watchOS apps with timelines](updating-watchos-apps-with-timelines.md)
  Seamlessly schedule updates to your user interface, even while it’s inactive.
- [Responding to the Action button on Apple Watch Ultra](../AppIntents/ActionButtonArticle.md)
  Use App Intents to register actions for your app.
- [Enabling the double-tap gesture on Apple Watch](enabling-double-tap.md)
  Customize your app’s response to the double-tap gesture on Apple Watch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-apps/authenticating-users-on-apple-watch)*