# WINetworkSharingProvider.AccessoryScanResponse

**Framework**: Wi-Fi Infrastructure  
**Kind**: struct  
**Role**: Structure

A scan response from the accessory containing Wi-Fi scan results, if any.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+

## Declaration

```swift
struct AccessoryScanResponse
```

## Overview

An `AccessoryScanResponse` contains the Wi-Fi networks your accessory discovered during scanning. The system uses these results to enhance the network selection interface, showing signal strength and compatibility information to help people choose the best networks to share.

Create responses that correspond to specific scan requests and include all relevant networks your accessory found. Include signal strength information to help people select networks with good connectivity from your accessory’s perspective.

## Topics

### Identifying a scan response
- [WINetworkSharingProvider.AccessoryScanResponse.ID](./accessoryscanresponse/id-swift.typealias.md)
  The type of value that uniquely identifies this scan response.
- [var id: WINetworkSharingProvider.AccessoryScanResponse.ID](./accessoryscanresponse/id-swift.property.md)
  A stable identifier that uniquely identifies this scan response.
### Getting the originating scan request
- [let scanRequest: WINetworkSharingProvider.AccessoryScanRequest](./accessoryscanresponse/scanrequest.md)
  The original scan request that prompted this response.
### Getting the scan results from the Accessory
- [let results: [WINetworkSharingProvider.AccessoryScanResult]](./accessoryscanresponse/results.md)
  An array of scan results containing access points the accessory has discovered.
### Initializers
- [init(scanRequest: WINetworkSharingProvider.AccessoryScanRequest, results: [WINetworkSharingProvider.AccessoryScanResult])](./accessoryscanresponse/init%28scanrequest,results%29.md)
  Creates an accessory scan response.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Identifiable](../../Swift/identifiable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Displaying network selection
- [func presentAskToShareUI(scanProvider: ((ASAccessory, WINetworkSharingProvider.AccessoryScanRequest) async -> WINetworkSharingProvider.AccessoryScanResponse?)?) async throws -> WINetworkSharingAskToShareState](./presentasktoshareui%28scanprovider%29.md)
  Presents system UI asking people to share available networks with an accessory.
- [WINetworkSharingProvider.AccessoryScanRequest](./accessoryscanrequest.md)
  A request for the accessory to scan for available Wi-Fi networks.
- [WINetworkSharingProvider.AccessoryScanResult](./accessoryscanresult.md)
  An access point that the accessory was able to discover in its Wi-Fi scans.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/accessoryscanresponse)*