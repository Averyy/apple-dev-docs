# init(for:)

**Framework**: Wi-Fi Infrastructure  
**Kind**: init

Creates a provider for the specified accessory.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
init(for accessory: ASAccessory) async throws
```

#### Return Value

A new [`WINetworkSharingProvider`](winetworksharingprovider.md) configured for the specified accessory.

#### Discussion

Use this initializer to establish a connection with the system for sharing networks with your accessory.

> **Note**: A [`WINetworkSharingError`](winetworksharingerror.md) for various conditions: - [`WINetworkSharingError.accessoryTransportNotSecured`](winetworksharingerror/accessorytransportnotsecured.md): The accessory doesn’t use a secure Bluetooth transport.
- [`WINetworkSharingError.accessoryNotAuthorized`](winetworksharingerror/accessorynotauthorized.md): The person hasn’t authorized network data sharing to the accessory.
- [`WINetworkSharingError.accessoryNotConnected`](winetworksharingerror/accessorynotconnected.md): The accessory isn’t connected when making this request.
- [`WINetworkSharingError.wifiNetworkSharingUnsupported`](winetworksharingerror/wifinetworksharingunsupported.md): The device doesn’t support network sharing.

## Parameters

- `accessory`: The accessory that receives the shared networks list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/init(for:))*