# WINetworkSharingProvider.AccessoryScanResult

**Framework**: Wi-Fi Infrastructure  
**Kind**: struct  
**Role**: Structure

An access point that the accessory was able to discover in its Wi-Fi scans.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+

## Declaration

```swift
struct AccessoryScanResult
```

## Overview

An `AccessoryScanResult` represents a single Wi-Fi access point your accessory detected during network scanning. Include signal strength information to help people select networks with good connectivity from your accessory’s location.

Provide signal strength as a normalized value between 0.0 (weakest) and 1.0 (strongest) to give people a consistent way to compare network quality across different accessory types.

## Topics

### Getting network definitions
- [let ssid: WISSID?](./accessoryscanresult/ssid.md)
  The SSID of the network.
### Getting network performance indicators
- [let signalStrength: Double](./accessoryscanresult/signalstrength.md)
  The signal strength the accessory measured for the access point.
### Getting network connection state
- [let isConnected: Bool](./accessoryscanresult/isconnected.md)
  A Boolean value that indicates whether the accessory currently has a connection to this Wi-Fi access point.
### Initializers
- [init(ssid: WISSID?, signalStrength: Double, isConnected: Bool)](./accessoryscanresult/init%28ssid,signalstrength,isconnected%29.md)
  Creates an accessory scan result.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Displaying network selection
- [func presentAskToShareUI(scanProvider: ((ASAccessory, WINetworkSharingProvider.AccessoryScanRequest) async -> WINetworkSharingProvider.AccessoryScanResponse?)?) async throws -> WINetworkSharingAskToShareState](./presentasktoshareui%28scanprovider%29.md)
  Presents system UI asking people to share available networks with an accessory.
- [WINetworkSharingProvider.AccessoryScanRequest](./accessoryscanrequest.md)
  A request for the accessory to scan for available Wi-Fi networks.
- [WINetworkSharingProvider.AccessoryScanResponse](./accessoryscanresponse.md)
  A scan response from the accessory containing Wi-Fi scan results, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/accessoryscanresult)*