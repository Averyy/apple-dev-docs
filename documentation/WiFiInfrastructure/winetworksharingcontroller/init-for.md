# init(for:)

**Framework**: Wi-Fi Infrastructure  
**Kind**: init

Creates a controller for a given accessory.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
init(for accessory: ASAccessory) async throws
```

#### Discussion

Use this initializer to create a network-sharing controller for the specified accessory. The accessory needs to be connected and using a secure transport when creating the controller.

> **Note**: A [`WINetworkSharingError`](winetworksharingerror.md) for various conditions: - [`WINetworkSharingError.accessoryTransportNotSecured`](winetworksharingerror/accessorytransportnotsecured.md): The accessory isn’t using a secure Bluetooth transport.
- [`WINetworkSharingError.accessoryNotConnected`](winetworksharingerror/accessorynotconnected.md): The accessory isn’t connected when your container app calls this method.
- [`WINetworkSharingError.wifiNetworkSharingUnsupported`](winetworksharingerror/wifinetworksharingunsupported.md): Network sharing isn’t supported on this device.

## Parameters

- `accessory`: The accessory to send requests to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingcontroller/init(for:))*