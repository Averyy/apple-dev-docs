# WINetworkSharingProvider.AccessoryScanRequest

**Framework**: Wi-Fi Infrastructure  
**Kind**: struct

A request for the accessory to scan for available Wi-Fi networks.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
struct AccessoryScanRequest
```

#### Overview

An `AccessoryScanRequest` represents a system request for your accessory to perform a Wi-Fi scan and report discovered networks.

When you provide a scan closure to [`presentAskToShareUI(scanProvider:)`](winetworksharingprovider/presentasktoshareui(scanprovider:).md), the system calls your closure with scan request instances. Your accessory should perform a Wi-Fi scan and return the results in an [`WINetworkSharingProvider.AccessoryScanResponse`](winetworksharingprovider/accessoryscanresponse.md).

## Topics

### Identifying a scan request
- [WINetworkSharingProvider.AccessoryScanRequest.ID](winetworksharingprovider/accessoryscanrequest/id-swift.typealias.md)
  The type of value that uniquely identifies this scan request.
- [var id: WINetworkSharingProvider.AccessoryScanRequest.ID](winetworksharingprovider/accessoryscanrequest/id-swift.property.md)
  A stable identifier that uniquely identifies this scan request.

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
- [WINetworkSharingProvider.AccessoryScanResponse](winetworksharingprovider/accessoryscanresponse.md)
  A scan response from the accessory containing Wi-Fi scan results, if any.
- [WINetworkSharingProvider.AccessoryScanResult](winetworksharingprovider/accessoryscanresult.md)
  An access point that the accessory was able to discover in its Wi-Fi scans.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/accessoryscanrequest)*