# Configuring custom fonts

**Framework**: Xcode

Register your app as a provider or consumer of systemwide custom fonts.

#### Overview

In iOS 13 and later, your iOS app can contribute fonts for systemwide use and leverage fonts that other apps install.

When an app attempts the install one or more fonts systemwide, iOS prompts the user for their permission. If the user agrees, the installed fonts become accessible in Settings > General > Fonts. If your app provides installable fonts, include a UI that allows the user to browse those fonts and manage their registration.

You must store installable fonts in the app bundle or deliver them using On-Demand Resources, because the system prohibits an app from installing arbitrary fonts. Provide fonts in the TTF, OTF, or TTC formats or any of their modern variants, and package large font libraries as asset catalogs.

The system limits the number of installed fonts, and it derives that limit from the available system resources. If the user deletes your app, the system automatically removes any of the app’s installed fonts.

To register your app as a provider or consumer of systemwide custom fonts, follow the steps in [`Add a capability`](adding-capabilities-to-your-app#Add-a-capability.md) to add the Fonts capability to your app’s target.

![A screenshot of Xcode’s Capabilities library with a list of available capabilities on the left and an information pane on the right. The list shows a range of capabilities from Fonts to In-App Purchase, and the Fonts capability is in a selected state. The text on the information pane explains that the Fonts capability allows your app, with the user’s permission, to install and make use of custom fonts.](https://docs-assets.developer.apple.com/published/e2e14e643f2606c5d2ceb0f8501dc351/fonts%402x.png)

> **Note**: The Fonts capability is only available to use with iOS apps that target iOS 13 and later.

##### Select the Required Privileges

Before your iOS app can install one or more custom fonts or use fonts that other apps provide, you must enable the necessary privileges by performing the following:

1. Select your project in Xcode’s Project navigator.
2. Select the iOS app’s target from the Targets list.
3. Click the Signing & Capabilities tab in the project editor.
4. Find the Fonts capability.
5. Select the required privileges using the corresponding checkboxes.

![A screenshot of the Fonts capability after you add it to an iOS target. The Install Fonts and Use Installed Fonts privileges are in an enabled state.](https://docs-assets.developer.apple.com/published/7537b87aaffa33681a478a748a9bf357/fonts-consumer-provider%402x.png)

> 💡 **Tip**: Fonts privileges aren’t exclusive; your iOS app can provide fonts for use in other apps and consume fonts that other apps install systemwide.

Xcode adds the `com.apple.developer.user-fonts` array to your app’s entitlements file, if not already present, and uses the privileges you enable to populate that array with the corresponding values.

After enabling the required privileges, update your app to perform one or more of the following:

- Register fonts systemwide using one of these registration methods: - [`CTFontManagerRegisterFontURLs(_:_:_:_:)`](https://developer.apple.com/documentation/CoreText/CTFontManagerRegisterFontURLs(_:_:_:_:))
- [`CTFontManagerRegisterFontDescriptors(_:_:_:_:)`](https://developer.apple.com/documentation/CoreText/CTFontManagerRegisterFontDescriptors(_:_:_:_:))
- [`CTFontManagerRegisterFontsWithAssetNames(_:_:_:_:_:)`](https://developer.apple.com/documentation/CoreText/CTFontManagerRegisterFontsWithAssetNames(_:_:_:_:_:))
- Remove installed fonts using one of these unregister methods: - [`CTFontManagerUnregisterFontURLs(_:_:_:)`](https://developer.apple.com/documentation/CoreText/CTFontManagerUnregisterFontURLs(_:_:_:))
- [`CTFontManagerUnregisterFontDescriptors(_:_:_:)`](https://developer.apple.com/documentation/CoreText/CTFontManagerUnregisterFontDescriptors(_:_:_:))
- Query all installed fonts using [`CTFontManagerRequestFonts(_:_:)`](https://developer.apple.com/documentation/CoreText/CTFontManagerRequestFonts(_:_:))
- Listen for font change notifications using [`kCTFontManagerRegisteredFontsChangedNotification`](https://developer.apple.com/documentation/CoreText/kCTFontManagerRegisteredFontsChangedNotification)

For more information, see the WWDC session video [`Font Management and Text Scaling`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2019/227).

## See Also

- [Configuring background execution modes](configuring-background-execution-modes.md)
  Indicate the background services your app requires to continue executing in the background in iOS, iPadOS, tvOS, visionOS, and watchOS.
- [Configuring game controllers](configuring-game-controllers.md)
  Enhance gameplay input by enabling the discovery, configuration, and use of physical game controllers.
- [Configuring Maps support](configuring-maps-support.md)
  Register your iOS routing app to provide point-to-point directions to Maps and other apps.
- [Configuring Siri support](configuring-siri-support.md)
  Enable your app and its Intents extension to resolve, confirm, and handle user-driven Siri requests for your app’s services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Xcode/configuring-custom-fonts)*