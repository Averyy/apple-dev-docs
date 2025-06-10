# Preparing your app to be the default web browser

**Framework**: Xcode

Configure your browser app so users can set it as the default on their device instead of Safari.

#### Overview

In iOS 14 and later, users can select an app to be their default web browser. To make your app a choice, confirm that your app meets the requirements below, then request a managed entitlement.

##### Configure Your App to Be a Default Browser

The system invokes the default web browser in iOS whenever the user opens an HTTP or HTTPS link. Because this app becomes the user’s primary gateway to the internet, Apple requires that web browsing apps meet specific functional criteria to protect user privacy and ensure proper access to internet resources.

Apps express their capability to be a default web browser by using the [`com.apple.developer.web-browser`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.web-browser) managed entitlement.

> ❗ **Important**:  Request the default browser entitlement by filling out the [`Default browser entitlement request form`](https://developer.apple.comhttps://developer.apple.com/contact/request/default-browser-entitlement/). In that form you can also request the [`com.apple.developer.browser.app-installation`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.browser.app-installation) entitlement. If you do that and your request for the default browser entitlement is accepted you get both the default browser entitlement and the app-installation entitlement for your browser app.

##### Fulfill Default Browser Requirements

Apps that register as a default web browser option must satisfy the following criteria:

- Your app must specify the HTTP and HTTPS schemes in its `Info.plist` file.
- Your app can’t use [`UIWebView`](https://developer.apple.com/documentation/UIKit/UIWebView).
- On launch, the app must provide a text field for entering a URL, search tools for finding relevant links on the internet, or curated lists of bookmarks.

When opening an HTTP or HTTPS URL in its default configuration:

- The app must navigate directly to the specified destination and render the expected web content. Apps that redirect to unexpected locations or render content not specified in the destination’s source code don’t meet the requirements of a default web browser.
- Apps designed to operate in a parental controls or locked down mode may restrict navigation to comply with those goals.
- Your app may present a “Safe Browsing” or other warning for content suspected of phishing or other problems.
- Your app may offer a native authentication UI for a site that also offers a native web sign-in flow.

##### Use Default Browser Capabilities

Apps that use the [`com.apple.developer.web-browser`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.web-browser) managed entitlement can:

- Be an option for the user to choose as their default browser.
- Load pages from all domains with full script access.
- Use Service Workers in [`WKWebView`](https://developer.apple.com/documentation/WebKit/WKWebView) instances.
- Offer the Add to Home Screen action in a share sheet by including the current [`WKWebView`](https://developer.apple.com/documentation/WebKit/WKWebView) in the `activityItems` array when creating a [`UIActivityViewController`](https://developer.apple.com/documentation/UIKit/UIActivityViewController).

##### Adhere to Browser Restrictions

Apps that have the [`com.apple.developer.web-browser`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.web-browser) managed entitlement may not claim to respond to Universal Links for specific domains. The system will ignore any such claims. Apps with the entitlement can still open Universal Links to other apps as usual.

Because of their privileged position in a user’s web browsing, browser apps should avoid unnecessary access to personal data. Apps that use any of the following `Info.plist` keys while using the [`com.apple.developer.web-browser`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.web-browser) managed entitlement will be rejected:

- [`NSPhotoLibraryUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSPhotoLibraryUsageDescription) — For saving images, your app should only specify [`NSPhotoLibraryAddUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSPhotoLibraryAddUsageDescription). [`WKWebView`](https://developer.apple.com/documentation/WebKit/WKWebView) can still upload photos and files without your app needing access to a user’s entire photo library. To access individual photos your app should use [`PHPickerViewController`](https://developer.apple.com/documentation/PhotosUI/PHPickerViewController) which doesn’t require [`NSPhotoLibraryUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSPhotoLibraryUsageDescription), instead of [`UIImagePickerController`](https://developer.apple.com/documentation/UIKit/UIImagePickerController).
- [`NSLocationAlwaysUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSLocationAlwaysUsageDescription), [`NSLocationAlwaysAndWhenInUseUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSLocationAlwaysAndWhenInUseUsageDescription) — For determining the user’s location, request while in-use authorization instead ([`NSLocationWhenInUseUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSLocationWhenInUseUsageDescription)). Browsers are restricted from always-on location access.
- [`NSHomeKitUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSHomeKitUsageDescription) — Browsers can’t access the user’s HomeKit database.
- [`NSBluetoothAlwaysUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSBluetoothAlwaysUsageDescription) — Browsers can’t poll for Bluetooth devices when the app is in the background. Browsers should use `NSBluetoothWhileInUseUsageDescription` for Bluetooth features.
- [`NSHealthShareUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSHealthShareUsageDescription), [`NSHealthUpdateUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSHealthUpdateUsageDescription) — Browsers can’t access the user’s health database.

> **Note**: [`NSLocationAlwaysUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSLocationAlwaysUsageDescription) was deprecated in iOS 10. For more information, see [`Choosing the  Location Services Authorization to Request`](https://developer.apple.com/documentation/BundleResources/choosing-the-location-services-authorization-to-request).

##### Check If Your App Is the Default Browser

To test whether someone configured your app as the default browser in iOS, call [`isDefault(_:)`](https://developer.apple.com/documentation/UIKit/UIApplication/isDefault(_:)) (Swift) or [`defaultStatusForCategory:error:`](https://developer.apple.com/documentation/UIKit/UIApplication/defaultStatusForCategory:error:) (Objective-C), with the category [`UIApplication.Category.webBrowser`](https://developer.apple.com/documentation/UIKit/UIApplication/Category/webBrowser).

This method is rate-limited: if your app calls it too frequently, the method throws an error. The value for the key [`retryAvailableDateErrorKey`](https://developer.apple.com/documentation/UIKit/UIApplication/CategoryDefaultError/retryAvailableDateErrorKey) in the error’s user info dictionary is the date at which your app can next check whether it’s the default browser.

##### Ship an Alternative Browser Engine

If your iOS browser app includes an alternative browser engine, which includes using a version of WebKit other than the framework supplied in the operating system, you need to design your browser as an app that hosts extensions to access system resources and process untrusted data. For more information, see [`BrowserEngineKit`](https://developer.apple.com/documentation/BrowserEngineKit).


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/preparing-your-app-to-be-the-default-browser)*