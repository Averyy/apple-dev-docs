# Configuring Wallet support

**Framework**: Xcode

Access the user’s Wallet to add, update, and display your app’s passes.

#### Overview

The Wallet app on iOS and watchOS allows users to organize their  — tickets, gift cards, loyalty cards, boarding passes, and the payment cards they use with Apple Pay. By integrating with [`PassKit (Apple Pay and Wallet)`](https://developer.apple.com/documentation/PassKit), your app can access any related passes and allow the user to manage them.

To use Wallet in your app, add the capability by configuring your app’s target in Xcode and, optionally, specify which pass types your app supports. Follow the instructions in the [`Add a capability`](adding-capabilities-to-your-app#Add-a-capability.md) section of [`Adding capabilities to your app`](adding-capabilities-to-your-app.md). When you reach the Capabilities library, choose Wallet. For watchOS apps with separate WatchKit extensions, add the capability to the WatchKit Extension’s target. The capability isn’t available for macOS or tvOS.

![A screenshot of Xcode’s Capabilities library. At the top is a filter button next to a search field that contains the placeholder text Capabilities. Below that, in the left pane, there’s a list of capabilities, such as Network Extensions, Siri, and Wallet. The Wallet capability is in a selected state. On the right, there’s an information pane that contains the text Wallet gives users a way to organize passes, tickets, gift cards, credit cards and loyalty cards. Use the PassKit framework APIs to display, add, or update items in your users’ Wallets.](https://docs-assets.developer.apple.com/published/82b23f93b839a1ee3d5d8904cf391802/wallet%402x.png)

After you add the Wallet capability, Xcode updates your target’s entitlements file to include the [`Pass Type IDs Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.pass-type-identifiers) — an array containing the single wildcard value `$(TeamIdentifierPrefix)*`. This value allows your app to access passes of every pass type that you define in your developer account; use the configuration options of the capability to narrow the scope of accessible pass types to only those your app requires.

> ❗ **Important**: The capability fetches and displays the pass type identifiers you register in your developer account; Xcode doesn’t provide a way to register them locally. For more information, see [`Create Wallet identifiers and certificates`](https://developer.apple.comhttps://developer.apple.com/help/account/configure-app-capabilities/create-wallet-identifiers-and-certificates).

##### Restrict Your App to a Subset of Pass Types

To minimize potential security risks and help protect the user’s privacy, follow these steps to provide your app with access to only the pass type identifiers it requires to function properly:

1. Select your project in Xcode’s Project navigator.
2. Select the app’s target from the Targets list.
3. Click the Signing & Capabilities tab in the project editor.
4. Find the Wallet capability.
5. Select the “Enable subset of pass types” option.
6. Xcode enables all pass type identifiers by default; disable individual identifiers by unchecking their checkboxes.

![A screenshot of the Wallet capability after you add it to an app’s target. The Allow subset of pass types option is in an enabled state, as are two of the three listed pass type identifiers.](https://docs-assets.developer.apple.com/published/d40f513c0ae43a77a40ec87f2187f868/subset-of-pass-types%402x.png)

Xcode updates the `com.apple.developer.pass-type-identifiers` array in the app’s entitlements file to include only the enabled pass type identifiers, and if present, removes the wildcard value.

After enabling the required pass type identifiers, use the [`passes()`](https://developer.apple.com/documentation/PassKit/PKPassLibrary/passes()) method of [`PKPassLibrary`](https://developer.apple.com/documentation/PassKit/PKPassLibrary) to retrieve the passes accessible to your app, or [`pass(withPassTypeIdentifier:serialNumber:)`](https://developer.apple.com/documentation/PassKit/PKPassLibrary/pass(withPassTypeIdentifier:serialNumber:)) to fetch a specific pass. For more information on creating, distributing, and updating passes, see [`Wallet Passes`](https://developer.apple.com/documentation/WalletPasses).

## See Also

- [Configuring Apple Pay support](configuring-apple-pay-support.md)
  Process payments in your app using the payment information the user stores on their device.
- [Configuring Sign in with Apple support](configuring-sign-in-with-apple.md)
  Allow users to create an account and sign in to your app with their Apple Account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/configuring-wallet-support)*