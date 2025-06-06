# Inspecting tvOS

**Framework**: Safari Developer Features

Inspect JavaScript and TVML content on tvOS from a Mac on the same network.

#### Overview

JavaScript and TVML in your apps can be inspected from a Mac on the same network as your Apple TV. You can also use simulators on macOS to debug your JavaScript and TVML without having to use a physical device. To learn more about getting simulators for device, see [`Installing Xcode and Simulators`](installing-xcode-and-simulators.md).

#### Enabling Inspecting Your Device From a Mac on the Same Network

Unlike iOS and iPadOS devices, Apple TV does not have a way to connect physically to your Mac. Instead you must pair the Apple TV over the network:

1. Make sure both your Mac and Apple TV are connected to the same network, either wirelessly or using a network cable.
2. On your Apple TV, open , then choose  > . The Apple TV is now available for pairing from any Mac on the network.
3. In Safari, go to the  menu and find your Apple TV in the list of devices.
4. From the device’s submenu, choose .
5. Enter the six digit PIN code shown on the Apple TV into the PIN field shown on your Mac.

Once paired, you can inspect content on the device like any other device. In Safari, the device appears in the [`Develop menu`](develop-menu.md).

Alternatively, you can also [`pair with the device using Xcode`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/devbc48d1bad).

##### Tvos Simulators

 is always enabled for simulators, and currently booted simulators will appear in the  menu just like connected devices. You do not need to pair simulators.

#### Inspecting Javascript and Tvml in Apps

[`JSContext`](https://developer.apple.com/documentation/JavaScriptCore/JSContext)s in apps can be made inspectable, allowing any user who enables  on the device to inspect them. When content in an application is inspectable it will appear in a submenu for the connected device of the  menu of Safari on a connected Mac. webpages (and other content) is separated by app, making it easier to find the webpage you want to inspect.

Learn more about [`Enabling inspecting content in your apps`](enabling-inspecting-content-in-your-apps.md).

Additionally, TVML content in developer-provisions apps can be inspected to debug layout and design issues.

## See Also

- [Inspecting Safari on macOS](inspecting-safari-macos.md)
  Inspect webpages, Service Workers, and extensions in Safari on macOS.
- [Inspecting iOS and iPadOS](inspecting-ios.md)
  Inspect webpages, Service Workers, Home Screen web apps, extensions, and content inside apps on iOS and iPadOS devices and simulators from a connected Mac.
- [Inspecting visionOS](inspecting-visionos.md)
  Inspect webpages, service workers, extensions, and content inside apps in visionOS from a Mac on the same network.
- [Enabling inspecting content in your apps](enabling-inspecting-content-in-your-apps.md)
  Enable the inspection of webpages and JavaScript in apps you develop when inspected from a connected Mac.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-developer-tools/inspecting-tvos)*