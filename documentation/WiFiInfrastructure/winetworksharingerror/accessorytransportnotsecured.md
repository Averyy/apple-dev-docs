# WINetworkSharingError.accessoryTransportNotSecured

**Framework**: Wi-Fi Infrastructure  
**Kind**: case  
**Role**: Case

Indicates the accessory doesn’t use the required transport security, such as Bluetooth Secure Connections.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+

## Declaration

```swift
case accessoryTransportNotSecured
```

## See Also

### Checking for accessory issues
- [WINetworkSharingError.accessoryNotConfigured](./accessorynotconfigured.md)
  Indicates the person hasn’t configured the accessory on this system.
- [WINetworkSharingError.accessoryNotAuthorized](./accessorynotauthorized.md)
  Indicates the person didn’t grant the accessory authorization to access network information.
- [WINetworkSharingError.accessoryNotConnected](./accessorynotconnected.md)
  Indicates the accessory isn’t connected to the host.
- [WINetworkSharingError.noAccessoryScanResponse](./noaccessoryscanresponse.md)
  Indicates the accessory didn’t send a scan response.
- [WINetworkSharingError.noMatchingAccessoryScanRequest](./nomatchingaccessoryscanrequest.md)
  Indicates the system found no matching scan request pending for the accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingerror/accessorytransportnotsecured)*