# WINetworkSharingProvider.AccessoryScanResponse

**Framework**: Wi-Fi Infrastructure  
**Kind**: struct

A scan response from the accessory containing Wi-Fi scan results, if any.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
struct AccessoryScanResponse
```

#### Overview

An `AccessoryScanResponse` contains the Wi-Fi networks your accessory discovered during scanning. The system uses these results to enhance the network selection interface, showing signal strength and compatibility information to help people choose the best networks to share.

Create responses that correspond to specific scan requests and include all relevant networks your accessory found. Include signal strength information to help people select networks with good connectivity from your accessory’s perspective.

## Topics

### Identifying a scan response
- [WINetworkSharingProvider.AccessoryScanResponse.ID](winetworksharingprovider/accessoryscanresponse/id-swift.typealias.md)
  The type of value that uniquely identifies this scan response.
- [var id: WINetworkSharingProvider.AccessoryScanResponse.ID](winetworksharingprovider/accessoryscanresponse/id-swift.property.md)
  A stable identifier that uniquely identifies this scan response.
### Getting the originating scan request
- [let scanRequest: WINetworkSharingProvider.AccessoryScanRequest](winetworksharingprovider/accessoryscanresponse/scanrequest.md)
  The original scan request that prompted this response.
### Getting the scan results from the Accessory
- [let results: [WINetworkSharingProvider.AccessoryScanResult]](winetworksharingprovider/accessoryscanresponse/results.md)
  An array of scan results containing access points the accessory has discovered.
### Initializers
- [init(scanRequest: WINetworkSharingProvider.AccessoryScanRequest, results: [WINetworkSharingProvider.AccessoryScanResult])](winetworksharingprovider/accessoryscanresponse/init(scanrequest:results:).md)
  Creates an accessory scan response.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func presentAskToShareUI(scanProvider: ((ASAccessory, WINetworkSharingProvider.AccessoryScanRequest) async -> WINetworkSharingProvider.AccessoryScanResponse?)?) async throws -> WINetworkSharingAskToShareState](winetworksharingprovider/presentasktoshareui(scanprovider:).md)
  Presents system UI asking people to share available networks with an accessory.
- [WINetworkSharingProvider.AccessoryScanRequest](winetworksharingprovider/accessoryscanrequest.md)
  A request for the accessory to scan for available Wi-Fi networks.
- [WINetworkSharingProvider.AccessoryScanResult](winetworksharingprovider/accessoryscanresult.md)
  An access point that the accessory was able to discover in its Wi-Fi scans.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/accessoryscanresponse)*