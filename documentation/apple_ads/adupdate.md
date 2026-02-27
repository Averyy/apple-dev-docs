# AdUpdate

**Framework**: Apple Ads  
**Kind**: dictionary

The request to update an ad.

**Availability**:
- Search Ads 4.0+

## Declaration

```swift
object AdUpdate
```

## Mentions

- [Apple Ads Campaign Management API 4](apple-search-ads-campaign-management-api-4.md)

## Properties

- `creativeId` (int64): The unique identifier for a creative.
- `adGroupId` (int64): The unique identifier for an [`AdGroup`](adgroup.md). You can use the `EQUALS` and `IN` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Find Ads`](find-ads.md).
- `campaignId` (int64): The unique identifier for a campaign.
- `creationTime` (date-time): The date and time of the creation of the `AdUpdate` object. You can use the `EQUALS`, `LESS_THAN`, and `GREATER_THAN` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Find Ads`](find-ads.md).
- `creativeType` (string): The type of creative. See [`CreativeType`](creativetype.md) for value descriptions. You can create one [`Creative`](creative.md) per custom product page per organization. You can use the `EQUALS` [`Selector`](selector.md) [`Condition`](condition.md) operator with [`Find Ads`](find-ads.md).
- `deleted` (boolean): Indicates whether an [`Ad`](ad.md) is deleted. You can use the `EQUALS` and `IN` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Find Ads`](find-ads.md).
- `id` (int64): An `adId` is a unique identifier that represents the assignment relationship between an ad group and an ad. You can use the `EQUALS` and `IN` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Find Ads`](find-ads.md).
- `modificationTime` (date-time): The date and time of the most recent modification of the [`Ad`](ad.md). You can use the `EQUALS`, `LESS_THAN`, and `GREATER_THAN` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Find Ads`](find-ads.md).
- `name` (string): The unique name of the [`Ad`](ad.md) assigned to an [`AdGroup`](adgroup.md). This field is required in requests and is updatable. You can use the `EQUALS`, `LESS_THAN`, and `GREATER_THAN` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Find Ads`](find-ads.md).
- `orgId` (int64): The identifier of the organization that owns the campaign. Your `orgId` is the same as your account in [`Apple Ads`](https://developer.apple.comhttps://ads.apple.com/).
- `servingStateReasons` ([string]): A list of reasons that displays when an [`Ad`](ad.md) isn’t running. For example, if the [`DeviceClass`](deviceclass.md) changes, the `servingStateReasons` may change. See [`AdServingStateReasons`](adservingstatereasons.md) for value descriptions.
- `servingStatus` (string): The indicator of the status of an ad assignment with an [`AdGroup`](adgroup.md). See [`AdServingStatus`](adservingstatus.md) for value descriptions.
- `status` (string): The status of the [`Ad`](ad.md). This field is required in requests and is updatable. You can use the `EQUALS` and `IN` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Find Ads`](find-ads.md).

## See Also

- [object Ad](ad.md)
  The assignment of a creative to an ad group.
- [object AdCreate](adcreate.md)
  The request to create an ad, and assign a creative to an ad group.
- [object AdResponse](adresponse.md)
  The response to an ad request.
- [object AdListResponse](adlistresponse.md)
  The response to a request that returns a list of ads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/adupdate)*