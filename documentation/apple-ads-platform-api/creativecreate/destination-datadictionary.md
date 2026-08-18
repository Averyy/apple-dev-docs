# CreativeCreate.Destination

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The post-tap landing experience specified when creating an ad creative.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object CreativeCreate.Destination
```

#### Discussion

`destinationType` is immutable after creation and determines which fields `parameters` must include. For App Store destinations, provide `adamId` and optionally `productPageId`. See [`DestinationType`](destinationtype.md) and [`DestinationParameter`](destinationparameter.md) for details, and [`DestinationCreate`](destinationcreate.md) for the full field reference.

## Properties

- `destinationType` (DestinationCreate.DestinationType) *(required)*: The type of post-tap destination. See [`DestinationType`](destinationtype.md). Immutable after creation.
- `parameters` (DestinationCreate.Parameters): Destination-specific parameters. For App Store destinations, provide `adamId` and optionally `productPageId` to link to a Custom Product Page. See [`DestinationParameter`](destinationparameter.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/creativecreate/destination-data.dictionary)*