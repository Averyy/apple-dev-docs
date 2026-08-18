# Creative.Destination

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Post-tap destination entity defining where users go after tapping the ad.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object Creative.Destination
```

#### Discussion

Destination is the post-tap experience for the ad creative. `destinationType` is immutable after creation, and the system computes the read-only `url` field from `destinationType` and `parameters`.

## Properties

- `destinationType` (Destination.DestinationType): The type of post-tap destination. See [`DestinationType`](destinationtype.md). Immutable after creation.
- `parameters` (Destination.Parameters): Destination-specific parameters. Sub-fields: adamId (App Store app identifier, required), productPageId (UUID of a Custom Product Page created in App Store Connect, nullable string UUID, omit to use the default product page). Immutable after creation.
- `url` (string): The resolved destination URL. Read-only, computed by the system from `destinationType` and `parameters`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/creative/destination-data.dictionary)*