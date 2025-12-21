# Wi-Fi Infrastructure

**Framework**: Wi-Fi Infrastructure  
**Kind**: module

Share Wi-Fi network credentials securely between devices and connected accessories.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

#### Overview

Companion apps that have paired an accessory with [`AccessorySetupKit`](https://developer.apple.comhttps://developer.apple.com/documentation/accessorysetupkit/) can use the Wi-Fi™️ Infrastructure framework to share networks with their paired accessory over a local Bluetooth 4.2 Secure connection.

The Wi-Fi™️ Infrastructure framework enables your app to share Wi-Fi network credentials from an iOS device to paired accessories automatically and securely. Use this framework to avoid manually entering network passwords on accessories with limited input capabilities, such as smartwatches, Internet of Things (IoT) devices, or other connected hardware that travels with people across different networks.

The framework provides a secure, encrypted sharing mechanism that respects privacy and choice. People can authorize different levels of sharing, from automatic network sharing to manual approval for each network. All network sharing occurs only when accessories are connected via Bluetooth, ensuring that the credentials a person shares are only shared when devices are physically together.

With the Wi-Fi Infrastructure framework, you can:

- Request authorization to share Wi-Fi networks with paired accessories.
- Automatically share networks when the iOS device joins them.
- Prompt people through your app to share specific networks with their accessories.
- Receive shared network credentials in your app extension.
- Present system-provided network picker interfaces.
- Handle network-sharing failures and retry with alternative networks.

> ❗ **Important**: You may develop and test Wi-Fi Infrastructure apps on devices in all regions. People using your app must have an account registered in the European Union (EU), and their device must be located within the EU.

## Topics

### Essentials
- [com.apple.developer.wifi-infrastructure](../BundleResources/Entitlements/com.apple.developer.wifi-infrastructure.md)
  The entitlement the system requires for an app to use the Wi-Fi Infrastructure framework.
- [Sharing Wi-Fi network credentials](sharing-wi-fi-network-credentials.md)
  Use Wi-Fi Infrastructure to automatically share Wi-Fi network credentials after establishing a Bluetooth connection.
### Network sharing
- [class WINetworkSharingController](winetworksharingcontroller.md)
  A controller that enables your container app to control network-sharing functions with connected accessories.
- [class WINetworkSharingProvider](winetworksharingprovider.md)
  A provider that delivers updated Wi-Fi network information to your app extension.
- [enum WINetworkSharingAskToShareState](winetworksharingasktosharestate.md)
  The authorization state for sharing the current Wi-Fi network with an accessory.
### Common data
- [struct WISSID](wissid.md)
  The Service Set Identifier (SSID) for a Wi-Fi network, from which applications derive the human-readable network name.
### Errors
- [enum WINetworkSharingError](winetworksharingerror.md)
  Error codes for Wi-Fi network-sharing functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/WiFiInfrastructure)*