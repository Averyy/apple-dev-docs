# Configuring Maps support

**Framework**: Xcode

Register your iOS routing app to provide point-to-point directions to Maps and other apps.

#### Overview

An iOS app that’s able to display point-to-point directions can register as a routing app and make those directions available to Maps along with all other apps on a user’s device. Registering as a routing app improves the user experience because other apps can access your app’s routing information, and these apps don’t need to provide their own routing directions. Because Maps displays apps in the App Store that provide directions, registering your iOS app as a routing app is a great way to let users know about it.

A routing app provides specific directions in addition to what Maps supports, such as subway routes, hiking trails, and bike paths. Before you can select the routing modes that your app supports, follow the steps in [`Add a capability`](adding-capabilities-to-your-app#Add-a-capability.md) to add the Maps capability to your app’s target.

![A screenshot of Xcode’s Capabilities library with a list of available capabilities on the left and an information pane on the right. The list shows a range of capabilities from Maps to Siri, and the Maps capability is in a selected state. The text on the information pane explains that, with MapKit, you can create routing apps that users can access from Maps. Your apps can provide specific directions beyond what the Maps app supports, including subway routes, hiking trails, or bike paths.](https://docs-assets.developer.apple.com/published/a05f851a0639bc61e3073396ffe1e82b/maps%402x.png)

> **Note**: This capability is only applicable to custom routing apps on iOS. You don’t need to add the Maps capability to a macOS app to be able to use the MapKit framework.

This capability is only applicable to custom routing apps on iOS. You don’t need to add the Maps capability to a macOS app to be able to use the MapKit framework.

##### Select the Supported Routing Modes

Before the system can distribute requests for directions to your routing app, you must inform it of the routing modes your app supports by following these
steps:

1. Select your project in Xcode’s Project navigator.
2. Select the app’s target from the Targets list.
3. Click the Signing & Capabilities tab in the project editor.
4. Find the Maps capability.
5. Select the relevant routing modes by checking the corresponding checkboxes.

![A screenshot of the Maps capability after you add it to a target. The Airplane, Bus, and Ferry routing modes are in an enabled state.](https://docs-assets.developer.apple.com/published/9609f68ccf2d2e3e7a374a7cf1db3cec/routing-modes%402x.png)

Xcode adds the [`MKDirectionsApplicationSupportedModes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/MKDirectionsApplicationSupportedModes) array to your app’s `Info.plist` file (if not already present) and uses the modes you select to populate the array with the necessary values.

After you select the necessary routing modes, there are additional configuration steps you must complete before your app can start providing point-to-point directions, such as specifying a directions request document type and declaring your app’s geographic region. For more information, see [`Configuring Your App to Accept Direction Requests`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/ProvidingDirections/ProvidingDirections.html#//apple_ref/doc/uid/TP40009497-CH8-SW8).

## See Also

- [Configuring background execution modes](configuring-background-execution-modes.md)
  Indicate the background services your app requires to continue executing in the background in iOS, iPadOS, tvOS, visionOS, and watchOS.
- [Configuring custom fonts](configuring-custom-fonts.md)
  Register your app as a provider or consumer of systemwide custom fonts.
- [Configuring game controllers](configuring-game-controllers.md)
  Enhance gameplay input by enabling the discovery, configuration, and use of physical game controllers.
- [Configuring Siri support](configuring-siri-support.md)
  Enable your app and its Intents extension to resolve, confirm, and handle user-driven Siri requests for your app’s services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/configuring-maps-support)*