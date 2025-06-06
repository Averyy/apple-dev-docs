# Configuring Apple Pay support

**Framework**: Xcode

Process payments in your app using the payment information the user stores on their device.

#### Overview

Apple Pay lets the user store payment information on their device and then use it to quickly purchase goods and services in your app. Your app creates a payment request that Apple Pay transfers between your app, the Apple Pay servers, and your payment provider. Apple Pay leverages the device’s Secure Element to help protect the user’s payment information.

To use Apple Pay in your app, add the capability to configure your app’s target with the necessary entitlements, and create a merchant identifier and payment processing certificate to help secure transaction data. For more detailed information about these steps, see the video [`Configuring Your Developer Account for Apple Pay`](https://developer.apple.comhttps://developer.apple.com/videos/play/tutorials/configuring-your-developer-account-for-apple-pay/).

Before you create a merchant identifier or select an existing one, follow the instructions in the [`Add a capability`](adding-capabilities-to-your-app#Add-a-capability.md) section of [`Adding capabilities to your app`](adding-capabilities-to-your-app.md). When you reach the Capabilities library, choose Apple Pay. For watchOS apps with separate WatchKit extensions, add the capability to the WatchKit Extension’s target. The Apple Pay capability isn’t available for tvOS apps.

![A screenshot of Xcode’s Capabilities library. At the top is a filter button next to a search field that contains the placeholder text Capabilities. Below that, in the left pane, there’s a list of capabilities, such as Associated Domains, ClassKit, and Apple Pay. The Apple Pay capability is in a selected state. On the right, there’s an information pane that contains the text Apple Pay allows users to easily and securely pay for physical goods and services such as groceries, clothing, tickets, and reservations in apps using payment information stored in their device.](https://docs-assets.developer.apple.com/published/f10e8e0f52d4a3a1aeb32f13f5db24fa/apple-pay%402x.png)

After you add the Apple Pay capability, Xcode updates your target’s entitlements file to include the [`Merchant IDs Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.in-app-payments), which is an array that contains the merchant identifiers you select. If you configure Xcode to automatically manage app signing, then at this point, Xcode also enables Apple Pay for your app’s App ID in your developer account.

> **Note**: If you later remove the Apple Pay capability in Xcode, you must manually update your App ID’s configuration in your developer account to disable Apple Pay.

If you later remove the Apple Pay capability in Xcode, you must manually update your App ID’s configuration in your developer account to disable Apple Pay.

##### Select or Create a Merchant Identifier

A  uniquely identifies you to Apple Pay as a merchant that’s able to accept payments. To allow your app to submit payment requests, specify at least one merchant identifier in your project’s configuration. After you add the Apple Pay capability, Xcode retrieves any existing merchant identifiers from your developer account and displays them in the capability’s Merchant IDs list. To fetch an updated list of your account’s merchant identifiers, click the refresh button below the list.

![A screenshot of the Apple Pay capability after you add it to your target. The Merchant IDs list contains two existing merchant IDs, neither of which are in an enabled state.](https://docs-assets.developer.apple.com/published/87dea7fefaead07d2ee0a2ff1e374a7b/fetched-merchant-ids%402x.png)

Enable one or more merchant identifiers in the list using their checkboxes. Conversely, uncheck a merchant identifier’s checkbox to disallow your app from using it. Xcode updates the Merchant IDs array — `com.apple.developer.in-app-payments` — in your target’s entitlements file to reflect any changes you make, and associates the selected merchant identifiers with the app’s App ID in your developer account.

> **Note**: To avoid breaking a live version of your app that relies on the identifier association, Xcode doesn’t automatically dissociate a merchant identifier from your App ID when you deselect it in the capability.

To avoid breaking a live version of your app that relies on the identifier association, Xcode doesn’t automatically dissociate a merchant identifier from your App ID when you deselect it in the capability.

To create a new merchant identifier, perform the following steps:

1. Select your project in Xcode’s Project navigator.
2. Select the app’s target in the Targets list.
3. Click the Signing & Capabilities tab in the project editor.
4. Find the Apple Pay capability.
5. Click the Add button (+) below the Merchant IDs list.
6. Enter a merchant identifier in the dialog that appears. It’s preferrable to prefix a merchant identifier with `merchant.` and then append a custom string in reverse DNS notation.
7. Click OK to save the new merchant identifier.

![A screenshot of the Add a new Merchant ID dialog that appears after you click the Add button. The dialog’s text explains that Xcode will create a new merchant ID if the named merchant ID doesn’t already exist, and that Xcode also adds the new merchant ID to both your App ID and the app’s entitlements file.](https://docs-assets.developer.apple.com/published/c871b531adb8c96dd4ab8610b13e33fa/add-new-merchant-id%402x.png)

Xcode automatically registers the merchant identifier in your developer account, adds it to your target’s entitlements file, and selects it in the Merchant IDs list, indicating that your app is now able to use the new merchant identifier.

![A screenshot of the Apple Pay capability after you add it to your target. The Merchant IDs list contains three merchant IDs, and the new merchant ID is in an enabled state.](https://docs-assets.developer.apple.com/published/b4588e259da91b1ef23b4666dc65d2df/selected-merchant-id%402x.png)

##### Create a Payment Processing Certificate

Before you can use your merchant identifier, you must generate a  — a digital certificate that secures transaction data and proves its origin. The Apple Pay servers use the certificate’s public key to encrypt payment data, and you or your payment service provider use the certificate’s private key to decrypt the data and process the payment. For more information on creating the certificate, see [`Create a payment processing certificate`](https://developer.apple.comhttps://developer.apple.com/help/account/configure-app-capabilities/configure-apple-pay#create-a-payment-processing-certificate).

> **Note**: If you use an e-commerce platform or payment service provider, please contact them for information about using their service with Apple Pay. For a list of supported platforms and providers, see [`Payment Platforms`](https://developer.apple.comhttps://developer.apple.com/apple-pay/payment-platforms/).

If you use an e-commerce platform or payment service provider, please contact them for information about using their service with Apple Pay. For a list of supported platforms and providers, see [`Payment Platforms`](https://developer.apple.comhttps://developer.apple.com/apple-pay/payment-platforms/).

After you create your merchant identifier and payment processing certificate, use the PassKit framework to enable the collection of payments from within your app. For more information, see the [`Apple Pay`](https://developer.apple.com/documentation/PassKit/apple-pay) documentation and the sample code [`Offering Apple Pay in Your App`](https://developer.apple.com/documentation/PassKit/offering-apple-pay-in-your-app).

## See Also

- [Configuring Sign in with Apple support](configuring-sign-in-with-apple.md)
  Allow users to create an account and sign in to your app with their Apple Account.
- [Configuring Wallet support](configuring-wallet-support.md)
  Access the user’s Wallet to add, update, and display your app’s passes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/configuring-apple-pay-support)*