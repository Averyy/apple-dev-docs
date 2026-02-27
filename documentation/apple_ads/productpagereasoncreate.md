# ProductPageReasonCreate

**Framework**: Apple Ads  
**Kind**: dictionary

The ad creative rejection reason based on a product page.

## Declaration

```swift
object ProductPageReasonCreate
```

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
- **`SUBTITLE_NOT_ELIGIBLE`**: The app’s subtitle doesn’t comply with Apple Ads advertising requirements.
- **`SUBTITLE_PRICING_OFFERS_OR_RANKING_CLAIMS`**: Pricing, offers, ranking, or other incentivized promotions aren’t allowed in the app subtitle.

## Properties

- `adamId` (int64) *(required)*: Your unique App Store app identifier.
- `assetGenId` (string): The unique identifier for an app preview or screenshot.
- `comment` (string): Custom comments from Apple about the rejection reason.
- `countryOrRegion` (string) *(required)*: The App Store geoterritories where you’re promoting your app.
- `id` (int64): The unique identifier for a creative.
- `languageCode` (string) *(required)*: The ISO 639-1 language code appended to the ISO 3166-1 alpha-2 country code, such as `en-US`.
- `productPageId` (string) *(required)*: The custom product page identifier associated with the ad creative rejection reason. This field is nullable.
- `reasonCode` (string) *(required)*: Contains one of the `RejectionReason` enumerations in the Discussion section below.
- `reasonLevel` (string): The level at which the system applies the rejection reason. See [`ReasonLevel`](reasonlevel.md) for enumerations.
- `reasonType` (string) *(required)*: The reason type has a value of `REJECTION_REASON`.
- `supplySource` (string) *(required)*: The ad placement associated with the ad creative rejection reason.

## See Also

- [object LocaleInfo](localeinfo.md)
  The supported languages and language codes.
- [object CountryOrRegion](countryorregion.md)
  The supported locales of a product page.
- [object CountriesOrRegionsListResponse](countriesorregionslistresponse.md)
  A container for product page responses.
- [object MediaAppVideoAsset](mediaappvideoasset.md)
  The app preview or screenshot asset detail.
- [object ProductPageLocaleDetail](productpagelocaledetail.md)
  The product page locale metadata on App Store Connect.
- [object ProductPageDetail](productpagedetail.md)
  The product page metadata.
- [object ProductPageDetailWithAssets](productpagedetailwithassets.md)
  The product page asset metadata.
- [object ProductPageLocaleDetailListResponse](productpagelocaledetaillistresponse.md)
  A container for product page responses.
- [object ProductPageDetailResponse](productpagedetailresponse.md)
  A container for product page responses.
- [object ProductPageDetailWithAssetInfoResponse](productpagedetailwithassetinforesponse.md)
  A container for product page responses.
- [object ProductPageDetailListResponse](productpagedetaillistresponse.md)
  A container for product page responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/productpagereasoncreate)*