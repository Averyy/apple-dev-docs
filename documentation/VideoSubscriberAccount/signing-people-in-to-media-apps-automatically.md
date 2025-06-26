# Signing people in to their media accounts automatically

**Framework**: Video Subscriber Account

Implement single sign-on for media-streaming apps by managing a sign-in token on a person’s Apple Account.

#### Overview

The Automatic Sign-In feature offers a single sign-on experience for media-streaming apps that have the [`com.apple.smoot.subscriptionservice`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.smoot.subscriptionservice) entitlement. The first time a person signs in to your media streaming service, your app prompts them to opt in to Automatic Sign-In. If they agree, your app generates a  token. You provide the token to the framework, which stores it on the person’s Apple Account to sign the person in across all of their devices. When your app launches again, the framework provides the token if it exists on the person’s Apple Account, which your app uses to bypass the sign-in prompt and give the person quick access to the media streaming features in your app.

In addition, the feature creates a single sign-on experience when a person:

- Acquires a new Apple TV, iPhone, or iPad and restores app purchases
- Downloads your media-streaming app later on another device

Only your app interprets the value to authenticate the person, for example, by ensuring it represents an account with a valid subscription. The framework only manages  for your app. In addition to storing the token value on the person’s Apple Account, the framework also records the token , that is, the choice a person makes on the prompt. If the person dismisses the prompt without approving, your app proceeds to enable streaming without creating a token value.

> ❗ **Important**: If your app supports tvOS and other platforms, including iOS and iPadOS, use Automatic Sign-In to share a unified code base on Apple platforms for your media streaming apps. Because iCloud Keychain isn’t available on tvOS, Automatic Sign-In provides a cross-platform solution to implement single sign-on for iOS, iPadOS, and tvOS apps. Automatic Sign-In doesn’t replace iCloud Keychain for storing generic secrets, such as those that enable a person to manage their account, or view their personal information.

#### Generate an Automatic Sign in Token

When your app launches with the person signed out, check for an Automatic Sign-In token ([`autoSignInToken`](vsuseraccountmanager/autosignintoken-swift.property.md)) to use for signing them in.

If the token is undefined ([`value`](vsuseraccountmanager/autosignintoken-swift.struct/value.md) is `nil` or [`authorization`](vsuseraccountmanager/autosignintoken-swift.struct/authorization.md) is  [`VSUserAccountManager.AutoSignInAuthorization.notDetermined`](vsuseraccountmanager/autosigninauthorization/notdetermined.md)), prompt the person to sign in to your media streaming service:

```swift
// Access the static shared user account manager. 
let accountManager = VSUserAccountManager.shared
let autoSignInToken = try? await accountManager.autoSignInToken

if autoSignInToken?.value == nil || autoSignInToken?.authorization == .notDetermined {      
    // Prompt the person to sign in. 
```

After the person signs in successfully, prompt them to opt in to Automatic Sign-In. Call [`requestAutoSignInAuthorization()`](vsuseraccountmanager/requestautosigninauthorization().md) to present a sheet that asks for their approval:

```swift
// Media streaming service sign-in success:  
if case .success = newSignInResult {
    // Prompt to opt-in to Automatic Sign-In.
    if let context = try? await accountManager.requestAutoSignInAuthorization() {
        // Generate the token. 
    }
}
```

If the person dismisses the prompt without approving, the system leaves the [`authorization`](vsuseraccountmanager/autosignintokenupdatecontext/authorization.md) status [`VSUserAccountManager.AutoSignInAuthorization.notDetermined`](vsuseraccountmanager/autosigninauthorization/notdetermined.md) and the framework doesn’t prompt them again until the app calls [`requestAutoSignInAuthorization()`](vsuseraccountmanager/requestautosigninauthorization().md) once more.

If the person approves the prompt, the method returns an [`VSUserAccountManager.AutoSignInTokenUpdateContext`](vsuseraccountmanager/autosignintokenupdatecontext.md) instance with an [`authorization`](vsuseraccountmanager/autosignintokenupdatecontext/authorization.md) set to [`VSUserAccountManager.AutoSignInAuthorization.granted`](vsuseraccountmanager/autosigninauthorization/granted.md). Generate a token [`value`](vsuseraccountmanager/autosignintoken-swift.struct/value.md) and pass it to the framework using [`updateAutoSignInToken(_:updateContext:)`](vsuseraccountmanager/updateautosignintoken(_:updatecontext:).md):

```swift
let newToken = await generateNewAutoSignInToken() // Your implementation.
try? await accountManager.updateAutoSignInToken(newToken, updateContext: context) 
```

The system stores the token value and its authorization status to the person’s Apple Account, where the framework can find it from your app across the their other devices.

#### Sign in with an Automatic Sign in Token

If your app launches signed out but the Automatic Sign-In token ([`autoSignInToken`](vsuseraccountmanager/autosignintoken-swift.property.md)) has a valid [`value`](vsuseraccountmanager/autosignintoken-swift.struct/value.md), consume the token and sign them in:

```swift
let accountManager = VSUserAccountManager.shared
let autoSignInToken = try? await accountManager.autoSignInToken
if let token = autoSignInToken?.value {
    // Consume the token to bypass the sign-in screen, if appropriate.
}
```

> ❗ **Important**: Only use an Automatic Sign-In token to enable media streaming, and provide access to streaming features, like watchlists. Consider other mechanisms to secure a person’s account itself, or to enable the app to display their personal information.

#### Manage the Token on Device or From a Web Server

You might revoke an Automatic Sign-In token if:

- Your app provides its own UI that lets the person opt out of Automatic Sign-In.
- The person changes their password and wants to sign out from all of their devices.
- Your app implements conditions to invalidate a token, such as if a person flags a specific log in as unauthorized.

To revoke an Automatic Sign-In token, call [`deleteAutoSignInToken()`](vsuseraccountmanager/deleteautosignintoken().md), and the framework sets the token:

- [`value`](vsuseraccountmanager/autosignintoken-swift.struct/value.md) to `nil`
- [`authorization`](vsuseraccountmanager/autosignintoken-swift.struct/authorization.md) to [`VSUserAccountManager.AutoSignInAuthorization.notDetermined`](vsuseraccountmanager/autosigninauthorization/notdetermined.md).

The [`Automatic Sign-In API`](https://developer.apple.com/documentation/automaticsigninapi) enables you to manage tokens on your web sever. For example, you might allow the person to opt out of Automatic Sign-In from your website.

To remove the current token value from your web server, call the [`Delete Sign-In Token`](https://developer.apple.com/documentation/automaticsigninapi/delete-this-token-for-all-associated-users) endpoint:

```other
https://api.storekit.itunes.apple.com/account/v1/autoSignIn/delete
```

In addition, you can update the current token value from your web server by calling [`Update Sign-In Token`](https://developer.apple.com/documentation/automaticsigninapi/update-this-token-for-all-associated-users):

```other
https://api.storekit.itunes.apple.com/account/v1/autoSignIn/update
```

## See Also

- [class VSUserAccountManager](vsuseraccountmanager.md)
  The object that coordinates your app’s user account actions.
- [struct VSUserAccount](vsuseraccount-swift.struct.md)
  An object that represents a user’s account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/signing-people-in-to-media-apps-automatically)*