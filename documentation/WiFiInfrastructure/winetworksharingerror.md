# WINetworkSharingError

**Framework**: Wi-Fi Infrastructure  
**Kind**: enum

Error codes for Wi-Fi network-sharing functionality.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
enum WINetworkSharingError
```

#### Overview

The Wi-Fi network-sharing API throws `WINetworkSharingError` instances when there are issues with accessories, network availability, permissions, or system state.

## Topics

### Checking for general errors
- [WINetworkSharingError.error](winetworksharingerror/error.md)
  Indicates a general error occurred.
### Checking for timeouts
- [WINetworkSharingError.timeout](winetworksharingerror/timeout.md)
  Indicates the requested operation timed out.
### Checking for app issues
- [WINetworkSharingError.appNotPermitted](winetworksharingerror/appnotpermitted.md)
  Indicates the person hasn’t granted your app permission to use the shared networks API for the accessory.
- [WINetworkSharingError.appNotInForeground](winetworksharingerror/appnotinforeground.md)
  Indicates your app can’t perform the requested operation because it isn’t running in the foreground.
### Checking for unsupported host capabilities
- [WINetworkSharingError.wifiNetworkSharingUnsupported](winetworksharingerror/wifinetworksharingunsupported.md)
  Indicates the device doesn’t support Wi-Fi network sharing.
### Checking for communication failures
- [WINetworkSharingError.communicationFailure](winetworksharingerror/communicationfailure.md)
  Indicates the app failed to communicate with the shared network system.
### Checking for no available networks
- [WINetworkSharingError.noAvailableNetworks](winetworksharingerror/noavailablenetworks.md)
  Indicates the system found no sharable networks nearby.
### Checking for excessive requests
- [WINetworkSharingError.tooManyRequests](winetworksharingerror/toomanyrequests.md)
  Indicates the accessory exceeded the maximum number of requests.
### Checking for accessory issues
- [WINetworkSharingError.accessoryNotConfigured](winetworksharingerror/accessorynotconfigured.md)
  Indicates the person hasn’t configured the accessory on this system.
- [WINetworkSharingError.accessoryNotAuthorized](winetworksharingerror/accessorynotauthorized.md)
  Indicates the person didn’t grant the accessory authorization to access network information.
- [WINetworkSharingError.accessoryNotConnected](winetworksharingerror/accessorynotconnected.md)
  Indicates the accessory isn’t connected to the host.
- [WINetworkSharingError.noAccessoryScanResponse](winetworksharingerror/noaccessoryscanresponse.md)
  Indicates the accessory didn’t send a scan response.
- [WINetworkSharingError.accessoryTransportNotSecured](winetworksharingerror/accessorytransportnotsecured.md)
  Indicates the accessory doesn’t use the required transport security, such as Bluetooth Secure Connections.
- [WINetworkSharingError.noMatchingAccessoryScanRequest](winetworksharingerror/nomatchingaccessoryscanrequest.md)
  Indicates the system found no matching scan request pending for the accessory.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingerror)*