# Configuring Sign in with Apple support

**Framework**: Xcode

Allow users to create an account and sign in to your app with their Apple Account.

#### Overview

Sign in with Apple gives your users the option to sign in to your app with their existing Apple Account instead of creating a separate username and password. All Apple devices support Sign in with Apple. For information about using this feature in the browser, see doc://com.apple.documentation/documentation/sign_in_with_apple/sign_in_with_apple_js.

To use Sign in with Apple in your app, add the capability by configuring your app’s target in Xcode, set up the user interface and necessary authorizations, and register your domain with Apple’s relay service to ensure you can send emails to your users’ personal inboxes.

> **Note**: If your app targets an OS version that predates the availability of Sign in with Apple, use the JavaScript library to provide the same functionality. For more information, see doc://com.apple.documentation/documentation/sign_in_with_apple/sign_in_with_apple_js/incorporating_sign_in_with_apple_into_other_platforms.

##### Add the Sign in with Apple Capability to Your App

Follow the instructions in the [`Add a capability`](adding-capabilities-to-your-app#Add-a-capability.md) section of [`Adding capabilities to your app`](adding-capabilities-to-your-app.md). When you reach the Capabilities library, choose Sign in with Apple. For watchOS apps with separate WatchKit extensions, add the capability to the WatchKit Extension’s target.

![A screenshot of Xcode’s Capabilities library. At the top is a filter button next to a search field that contains the placeholder text Capabilities. Below that, in the left pane, there’s a list of capabilities, such as Network Extensions, Wallet, and Sign in with Apple. The Sign in with Apple capability is in a selected state. On the right, there’s an information pane that contains the text Enabling Sign in with Apple allows your users to authenticate with their Apple Account.](https://docs-assets.developer.apple.com/published/143aa5f00cf1ae88b7a3ef75cb88d5ec/sign-in-with-apple%402x.png)

After you add the capability, Xcode updates the target’s entitlements to include the [`Sign in with Apple Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.applesignin) — an array that contains a single string of `Default`, the value that represents normal operation. If you configure Xcode to automatically manage app signing, then at this point, Xcode also enables Sign in with Apple for your app’s App ID in your developer account.

> **Note**: If you later remove the Sign in with Apple capability in Xcode, you must manually update your App ID’s configuration in your developer account to disable Sign in with Apple.

Users must provide their consent before Apple shares any information with your app. If you have a number of related apps — for example, an iOS app and a macOS app — group their App IDs so the user only needs to provide consent on the first device they use to access your app. For more information, see [`Group Apps for Sign in with Apple`](https://developer.apple.comhttps://developer.apple.com/help/account/configure-app-capabilities/group-apps-for-sign-in-with-apple/).

##### Prompt the User to Sign in with Their Apple Account

After you add the Sign in with Apple capability to your Xcode project, update your app’s user interface to enable users to sign in with their Apple Account. For a reference implementation of the following steps, see the sample code [`Implementing User Authentication with Sign in with Apple`](https://developer.apple.com/documentation/AuthenticationServices/implementing-user-authentication-with-sign-in-with-apple).

- Add a Sign in with Apple button to your app’s user interface using [`ASAuthorizationAppleIDButton`](https://developer.apple.com/documentation/AuthenticationServices/ASAuthorizationAppleIDButton) or [`WKInterfaceAuthorizationAppleIDButton`](https://developer.apple.com/documentation/WatchKit/WKInterfaceAuthorizationAppleIDButton).
- Add a handler for the button that creates an instance of [`ASAuthorizationAppleIDRequest`](https://developer.apple.com/documentation/AuthenticationServices/ASAuthorizationAppleIDRequest). Make sure you set the request’s [`requestedScopes`](https://developer.apple.com/documentation/AuthenticationServices/ASAuthorizationOpenIDRequest/requestedScopes) property. For more information, see [`ASAuthorization.Scope`](https://developer.apple.com/documentation/AuthenticationServices/ASAuthorization/Scope).
- Perform the authorization request with [`ASAuthorizationController`](https://developer.apple.com/documentation/AuthenticationServices/ASAuthorizationController), prompting the user to sign in with their Apple Account and consent to Apple sharing their details with your app.
- Implement the [`ASAuthorizationControllerDelegate`](https://developer.apple.com/documentation/AuthenticationServices/ASAuthorizationControllerDelegate) protocol to determine the outcome of the authorization request and, if successful, receive the  — an instance of [`ASAuthorizationAppleIDCredential`](https://developer.apple.com/documentation/AuthenticationServices/ASAuthorizationAppleIDCredential) that contains details about the user.

If your app stores account information on a remote server, send the credential’s contents to that server. The remote server verifies the data’s legitimacy with the Apple Account servers before creating or updating a user account. For more information, see doc://com.apple.documentation/documentation/sign_in_with_apple/sign_in_with_apple_rest_api/authenticating_users_with_sign_in_with_apple.

##### Receive Updates About Apple Account Changes

If your app uses a remote server to manage user accounts, turn on server-to-server notifications so that the Apple Account servers notify you when users make changes to their Apple Account. The Apple Account servers send notifications when users change their mail forwarding preferences, delete their app account, or permanently delete their Apple Account. Use these notifications to maintain a canonical list of users. For more information, see [`Enabling Server to Server Notifications`](https://developer.apple.comhttps://developer.apple.com/help/account/configure-app-capabilities/enabling-server-to-server-notifications/).

##### Send Emails to Users Hidden Inboxes

If you include the [`email`](https://developer.apple.com/documentation/AuthenticationServices/ASAuthorization/Scope/email) scope when you prompt the user for authorization, the system provides an option for that user to hide their real email address and instead use a unique, random forwarding email address that Apple provides. To help prevent spam and ensure that emails to users originate from your registered domains and email addresses, follow these steps:

- Register the domains and subdomains that you use for email communication.
- Register a list of unique email addresses that you use to send email.
- Authenticate your registered domains using the Sender Policy Framework (SPF) and DomainKeys Identified Mail (DKIM) protocol.

You must complete these steps before you can send emails to your users’ hidden inboxes. For more information, see [`Configure Private Email Relay Service`](https://developer.apple.comhttps://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service/).

## See Also

- [Configuring Apple Pay support](configuring-apple-pay-support.md)
  Process payments in your app using the payment information the user stores on their device.
- [Configuring Wallet support](configuring-wallet-support.md)
  Access the user’s Wallet to add, update, and display your app’s passes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/configuring-sign-in-with-apple)*