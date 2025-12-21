# Building spatial experiences for business apps with enterprise APIs for visionOS

**Framework**: visionOS

Grant enhanced sensor access and increased platform control to your visionOS app by using entitlements.

#### Overview

> **Note**: This article is associated with WWDC25 session 223: [`Explore enhancements to your spatial business app`](https://developer.apple.comhttps://developer.apple.com/wwdc25/223/) and WWDC24 session 10139: [`Introducing enterprise APIs for visionOS`](https://developer.apple.comhttps://developer.apple.com/wwdc24/10139/).

You can use the entitlements that enterprise APIs for visionOS offer to create even more powerful enterprise solutions and spatial experiences for your visionOS app. The enterprise APIs for visionOS consist of two distinct categories.

The first category of APIs provides enhanced sensor access and improves the visual capabilities of Apple Vision Pro.

The second category focuses on platform control to help you get the most out of visionOS.

> **Note**: Each of these entitlements allows a device to operate outside the default configuration. When using these features, be aware that they may impact the performance of other apps.

##### Request the Entitlements

If you’re interested in using the enterprise APIs for visionOS in your app, the Account Holder of your Apple Developer Program and/or Apple Developer Enterprise Program can submit an [`entitlement request`](https://developer.apple.comhttps://developer.apple.com/go/?id=69613ca716fe11ef8ec848df370857f4).

To be eligible, your app needs to:

- Be for use in a business setting only
- Meet specific criteria associated with usage for each API

Enterprise APIs for visionOS are eligible for business use only. You can distribute apps that you develop with the enterprise APIs for visionOS privately as proprietary in-house apps or custom apps using Apple Business Manager. For more information on distributing custom apps, see [`Set distribution methods`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-your-apps-availability/set-distribution-methods).

You can also request access to the entitlements for  purposes. With this access, you can build and run apps on your registered test devices with development provisioning profiles.

##### Configure Your Apps Xcode Project

To use entitlements, you need to include both the entitlement file and a corresponding license file in your app. After Apple approves your app for one or more entitlements, you receive a license file, along with additional instructions.

You add the license file to your app’s Xcode project. Placing the license file within your project and adding it to your build target allows Xcode to compile it within your app and then validate it when checking your entitlements.

> **Note**: The license file comes with an expiration date, so you need to renew it before then to ensure your entitlements continue to function.

To add an entitlement in Xcode:

1. Select your project in the Project navigator.
2. Select the applicable target and then click the Signing & Capabilities tab.
3. Click the Add Capability button (+) and type the name of the entitlement you want to add, such as .
4. Double-click the entitlement to add it to the Signing section. This creates a `.entitlements` file with the relevant capability, such as `com.apple.developer.arkit.main-camera-access.allow` for “Main camera access”.

After you add the `.license` and `.entitlements` files, you can implement and test the APIs you have approval to use. For more information, see [`Adding capabilities to your app`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/adding-capabilities-to-your-app).

## See Also

- [Accessing the main camera](accessing-the-main-camera.md)
  Add camera-based features to enterprise apps.
- [Locating and decoding barcodes in 3D space](locating-and-decoding-barcodes-in-3d-space.md)
  Create engaging, hands-free experiences based on barcodes in a person’s surroundings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/building-spatial-experiences-for-business-apps-with-enterprise-apis)*