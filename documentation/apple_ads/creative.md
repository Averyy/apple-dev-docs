# Creative

**Framework**: Apple Ads  
**Kind**: dictionary

The creative object.

**Availability**:
- Search Ads 4.0+

## Declaration

```swift
object Creative
```

## Mentions

- [Apple Ads Campaign Management API 4](apple-search-ads-campaign-management-api-4.md)

## Properties

- `adamId` (int64): Your unique App Store app identifier. Use [`Get a Campaign`](get-a-campaign.md) or [`Get all Campaigns`](get-all-campaigns.md) to obtain your `adamId`. This field is required in requests to [`Create a Creative`](create-a-creative.md). You can use the `EQUALS` and `IN` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Find Creatives`](find-creatives.md).
- `creationTime` (date-time): The date and time of the creation of the [`Creative`](creative.md) object. You can use the `EQUALS`, `LESS_THAN`, and `GREATER_THAN` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Find Creatives`](find-creatives.md).
- `id` (int64): The `creativeId` is a unique identifier for a creative. You can use the `EQUALS` and `IN` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Find Creatives`](find-creatives.md).
- `modificationTime` (date-time): The date and time of the most recent modification of the object. You can use the `EQUALS`, `LESS_THAN`, and `GREATER_THAN` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Find Creatives`](find-creatives.md).
- `name` (string): The name of a creative. This field is required in requests to [`Create a Creative`](create-a-creative.md). You can use the `EQUALS` and `CONTAINS` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Find Creatives`](find-creatives.md).
- `orgId` (int64): The identifier of the organization that owns a campaign. Your `orgId` is the same as your account in the [`Apple Search Ads UI`](https://developer.apple.comhttps://searchads.apple.com/advanced).
- `state` (string): The system state of the creative. See [`CreativeState`](creativestate.md) for value descriptions.
- `stateReasons` ([string]): The detailed explanation of the system state. See [`CreativeStateReason`](creativestatereason.md) for value descriptions.
- `type` (string): The type of creative. This field is required in requests to [`Create a Creative`](create-a-creative.md). See [`CreativeType`](creativetype.md) for value descriptions. You can use the `EQUALS` and `IN` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Find Creatives`](find-creatives.md).

## See Also

- [object AppPreviewDevicesMappingResponse](apppreviewdevicesmappingresponse.md)
  The app preview device mapping response to display name and size mapping requests.
- [object CreativeLocalization](creativelocalization.md)
  The localized creative metadata.
- [object CreativeLocalizationWithAssets](creativelocalizationwithassets.md)
  The localized creative metadata with app preview.
- [object CustomProductPageCreative](customproductpagecreative.md)
  The creative details of a product page.
- [object CreativeResponse](creativeresponse.md)
  The response details of a creative request.
- [object CreativeListResponse](creativelistresponse.md)
  A container for response details of a creative request.
- [object DefaultProductPageCreative](defaultproductpagecreative.md)
  The default product page object.
- [object MediaAppAsset](mediaappasset.md)
  The asset details of app preview or app screenshots.
- [object MediaAppAssetsDetail](mediaappassetsdetail.md)
  The app asset details of a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/creative)*