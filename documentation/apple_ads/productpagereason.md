# ProductPageReason

**Framework**: Apple Ads  
**Kind**: dictionary

The ad creative rejection reason based on a product page.

**Availability**:
- Search Ads 4.8+

## Declaration

```swift
object ProductPageReason
```

## Mentions

- [Apple Ads Campaign Management API 4](apple-search-ads-campaign-management-api-4.md)

#### Discussion

Descriptions of reason codes include the following:

- **`APP_ICON_GRAPHIC_OR_ADULT_THEMED_CONTENT`**: Violent, offensive, sexually explicit, or otherwise inappropriate images aren’t allowed in the app icon.
- **`APP_ICON_NOT_ELIGIBLE`**: The app icon doesn’t comply with Apple advertising guidelines.
- **`APP_NAME_LANGUAGE_CONFLICT`**: The language in the app name needs to match the language selected in [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com).
- **`APP_NAME_GRAPHIC_OR_ADULT_THEMED_CONTENT`**: Violent, offensive, sexually explicit, or otherwise inappropriate wording isn’t allowed in the app name.
- **`APP_NAME_NOT_ELIGIBLE`**: The app name doesn’t comply with Apple advertising guidelines.
- **`APP_NOT_ELIGIBLE_AT_THIS_TIME`**: The app isn’t eligible for promotion on the Today tab.
- **`MIMICS_APP_STORE_TODAY_CARD`**: The phrases *Game of the Day* and *App of the Day* aren’t allowed in the app icon, name, or subtitle.
- **`PRODUCT_PAGE_OPTIMIZATION_EXPERIMENT_APP_ICON_NOT_ELIGIBLE`**: The app icon from a product page optimization (PPO) experiment doesn’t comply with Apple Advertising guidelines.
- **`SUBTITLE_GRAPHIC_OR_ADULT_THEMED_CONTENT`**: Violent, offensive, sexually explicit, or otherwise inappropriate wording isn’t allowed in the app subtitle.
- **`SUBTITLE_LANGUAGE_CONFLICT`**: The language in the app subtitle needs to match the language of the primary locale in [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com).
- **`SUBTITLE_NOT_ELIGIBLE`**: The app’s subtitle doesn’t comply with Apple Search Ads advertising requirements.
- **`SUBTITLE_PRICING_OFFERS_OR_RANKING_CLAIMS`**: Pricing, offers, ranking, or other incentivized promotions aren’t allowed in the app subtitle.

## Properties

- `adamId` (int64): Your unique App Store app identifier. Use [`Get a Campaign`](get-a-campaign.md) or [`Get all Campaigns`](get-all-campaigns.md) to obtain your `adamId`. You can use the `EQUALS` and `IN` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Find Ad Creative Rejection Reasons`](find-ad-creative-rejection-reasons.md).
- `assetGenId` (string): The unique identifier for an app preview or screenshot. You can use the `EQUALS` and `IN` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Find Ad Creative Rejection Reasons`](find-ad-creative-rejection-reasons.md).
- `comment` (string): Custom comments from Apple about the rejection reason.
- `countryOrRegion` (string): The App Store geoterritories where you’re promoting your app. You can use the `EQUALS` and `IN` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Find Ad Creative Rejection Reasons`](find-ad-creative-rejection-reasons.md).
- `id` (int64): The rejection reason identifier. You can use the `EQUALS` and `IN` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Find Ad Creative Rejection Reasons`](find-ad-creative-rejection-reasons.md).
- `languageCode` (string): The ISO 639-1 language code appended to the ISO 3166-1 alpha-2 country code, such as `en-US`. You can use the `EQUALS` and `IN` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Find Ad Creative Rejection Reasons`](find-ad-creative-rejection-reasons.md).
- `productPageId` (string): The custom product page identifier associated with the ad creative rejection reason. This field is nullable. You can use the `EQUALS` and `IN` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Find Ad Creative Rejection Reasons`](find-ad-creative-rejection-reasons.md).
- `reasonCode` (string): Contains one of the `RejectionReason` enumerations in the Discussion section below. You can use the `EQUALS` and `IN` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Find Ad Creative Rejection Reasons`](find-ad-creative-rejection-reasons.md).
- `reasonLevel` (string): The level at which the system applies the rejection reason. See [`ReasonLevel`](reasonlevel.md) for enumerations. You can use the `EQUALS` and `IN` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Find Ad Creative Rejection Reasons`](find-ad-creative-rejection-reasons.md).
- `reasonType` (string): The reason type has a value of `REJECTION_REASON`. You can use the `EQUALS` and `IN` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Find Ad Creative Rejection Reasons`](find-ad-creative-rejection-reasons.md).
- `supplySource` (string): The ad placement associated with the ad creative rejection reason. You can use the `EQUALS` and `IN` [`Selector`](selector.md) [`Condition`](condition.md) operators with [`Find Ad Creative Rejection Reasons`](find-ad-creative-rejection-reasons.md).

## Relationships

### Inherited By
- [ProductPageReasonResponse](productpagereasonresponse.md)

## See Also

- [object AppAsset](appasset.md)
  The app assets associated with an adam ID.
- [object AppAssetListResponse](appassetlistresponse.md)
  The response to a request that returns a list of app assets.
- [object ProductPageReasonListResponse](productpagereasonlistresponse.md)
  The response to a request that returns a list of product page rejection reasons.
- [object ProductPageReasonResponse](productpagereasonresponse.md)
  A container for product page reasons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/productpagereason)*