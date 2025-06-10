# Configuring HomeKit access

**Framework**: Xcode

Discover compatible accessories and communicate with configured accessories and services to perform actions.

#### Overview

Apps that integrate with HomeKit can securely connect to a user’s home automation network and access compatible accessories. After an app connects to an accessory, it can read and update that accessory’s state, for example, by changing the ambient color of a smart light bulb.

To enable your app to control the user’s compatible accessories, you must add the HomeKit capability to your app’s target and include a short description of the app’s functionality in its target’s `Info.plist` file.

##### Add the Homekit Capability to Your Target

Follow the steps in [`Add a capability`](adding-capabilities-to-your-app#Add-a-capability.md) to add the capability to your app’s target; be sure to select the HomeKit capability from Xcode’s Capabilities library. For watchOS apps with separate WatchKit extensions, you must add the capability to the WatchKit Extension target. The capability isn’t available for macOS.

![A screenshot of Xcode’s Capabilities library with a list of available capabilities on the left and an information pane on the right. The list shows a range of capabilities from HomeKit to Multipath, and the HomeKit capability is in a selected state. The text on the information pane explains that, by enabling HomeKit, your app can interact with HomeKit accessories and create home configurations.](https://docs-assets.developer.apple.com/published/ead28854e6fa05b5326e440a170aabf5/homekit%402x.png)

After you add the HomeKit capability, Xcode links the `HomeKit` framework to your target and updates its entitlements file to include the [`HomeKit Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.homekit). If Xcode automatically manages the signing of your app, it also enables HomeKit for your app’s App ID.

##### Request Access to a Home Automation Network

To help protect the security and privacy of the user’s home automation network, your app requires the user’s explicit permission before it can control HomeKit accessories on that network. The system prompts the user for their permission the first time your app uses the HomeKit framework, which is when you initialize [`HMHomeManager`](https://developer.apple.com/documentation/HomeKit/HMHomeManager).

The App Store requires your app to include a , which accurately and concisely describes the reasons the app needs access to the user’s network. The system displays this information to the user when requesting their permission, which helps them make an informed decision. Follow these steps to add the purpose string to your target:

1. In the Project navigator, select your target’s `Info.plist` file.
2. Move the mouse pointer over the “Information Property List” key.
3. Click the Add button (+) that appears.
4. Choose “Privacy - HomeKit Usage Description” from the drop-down menu.
5. Double-click the Value column to the right of the key and enter your app’s purpose string.

![A screenshot of a target’s Info.plist file open in Xcode’s Property List Editor. The file contains the Privacy - HomeKit Usage Description key and an example purpose string as its value.](https://docs-assets.developer.apple.com/published/a32536c027e35c8bca348465786e9e5b/homekit-purpose-string%402x.png)

> ❗ **Important**: Apps that enable Homekit but don’t include a purpose string crash when attempting to use the framework’s APIs.

Remember that the user can revoke their permission at any time in the Settings app, and your app must respond to this accordingly. You can check your app’s current authorization status by accessing the [`authorizationStatus`](https://developer.apple.com/documentation/HomeKit/HMHomeManager/authorizationStatus) property. HomeKit also returns a [`homeAccessNotAuthorized`](https://developer.apple.com/documentation/HomeKit/HMError/homeAccessNotAuthorized) error if your app attempts to make an unauthorized call to any of the framework’s APIs.

##### Install the Homekit Accessory Simulator

Integrating with HomeKit doesn’t require you to have physical access to each of the accessories that your app supports. Instead, you can install the HomeKit Accessory Simulator and simulate each of those accessories. To install the simulator, follow these steps:

1. Open the Signing & Capabilities tab in your target’s project editor.
2. Find the HomeKit capability.
3. Click the Download HomeKit Simulator button.
4. On the [`More Downloads`](https://developer.apple.comhttps://developer.apple.com/download/all) webpage that opens, find and download the latest “Additional Tools for Xcode” DMG file. Your browser may ask you to sign in to your Apple developer account first.
5. After the DMG file downloads, double-click it to mount the disk image in Finder.
6. Open the Hardware folder.
7. Drag the HomeKit Accessory Simulator app to your Mac’s Applications folder.

![A screenshot of Finder showing the contents of the Hardware folder from the downloaded disk image. The HomeKit Accessory Simulator is in a selected state.](https://docs-assets.developer.apple.com/published/468df0b637e9332a52220c7369fbd819/homekit-simulator%402x.png)

Use the simulator to add and remove simulated HomeKit accessories, services, and characteristics, and to simulate networked cameras and video doorbells by leveraging your Mac’s camera. For more information, see the Add Accessories, Services, and Characteristics section of [`Testing Your App with the HomeKit Accessory Simulator`](https://developer.apple.comhttps://developer.apple.com/documentation/homekit/testing_your_app_with_the_homekit_accessory_simulator#3087266).

## See Also

- [Configuring HealthKit access](configuring-healthkit-access.md)
  Read and write health and activity data in the Health app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/configuring-homekit-access)*