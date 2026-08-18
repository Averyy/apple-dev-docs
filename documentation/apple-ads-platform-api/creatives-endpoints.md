# Creatives Endpoints

**Framework**: Apple Ads Platform API

Create, retrieve, update, and delete ad creatives through these endpoints.

**Availability**:
- Apple Ads Platform API 1.0+

#### Overview

You create a [`Creative`](creative.md) object at the ad account level, and an [`Ad`](ad.md) object references it to define what users see when your ad serves. Ad creatives are reusable; you can link the same ad creative to multiple ads across different ad groups.

#### Use the Creatives Endpoints

Use these endpoints to create, retrieve, update, and delete ad creatives:

| Method | Path | Description |
| --- | --- | --- |
| `POST` | `/v1/creatives` | [`Create an Ad Creative`](post-creatives.md) creates a new ad creative. |
| `POST` | `/v1/creatives/query` | [`Query Ad Creatives`](post-creatives-query.md) retrieves ad creatives matching the specified filters. |
| `GET` | `/v1/creatives/{id}` | [`Get an Ad Creative`](get-creatives-_id_.md) retrieves a single ad creative by its ID. |
| `PUT` | `/v1/creatives/{id}` | [`Update an Ad Creative`](put-creatives-_id_.md) updates an existing ad creative. |
| `DELETE` | `/v1/creatives/{id}` | [`Delete an Ad Creative`](delete-creatives-_id_.md) soft-deletes an ad creative by its ID. |

##### Understand Creative Types

The `creativeType` field determines the ad creative’s content source, how the pre-tap ad renders, and which placements it’s eligible for. You set the creative type at creation, and you can’t change it afterward. The following table summarizes each creative type, its pre-tap content source, and its post-tap destination:

| Creative Type | Pre-tap Content Source | Post-tap Destination |
| --- | --- | --- |
| `DEFAULT_PRODUCT_PAGE` | System-rendered from the app’s default App Store listing | Default App Store product page |
| `CUSTOM_PRODUCT_PAGE` | System-rendered from a custom product page in App Store Connect | Custom App Store product page |
| `LOCAL_ADS_SEARCH_CREATIVE` | Brand location assets or logo assembled in [`Creative.CreativeSpec`](creative/creativespec-data.dictionary.md) | Apple Maps place card |

##### Define the Pre Tap and Post Tap Experience

Every ad creative has two distinct content areas, `creativeSpec` and `destination`, each with a separate responsibility:

- **`creativeSpec`**: Defines the pre-tap experience, what users see before they interact with the ad. It contains the visual assets and copy rendered in the ad placement.
- **`destination`**: Defines the post-tap experience, where users land after they tap the ad. The [`Destination`](destination.md) object specifies the `destinationType` and destination-specific parameters.

These two fields operate independently. For product page ad creatives, `creativeSpec` is intentionally empty because App Store Connect controls the pre-tap rendering. Only `destination` carries meaningful data. For Apple Maps ad creatives, `creativeSpec` contains the Apple Maps creative spec with the brand’s visual content and promotional text.

##### Understand Product Page Creatives

For `DEFAULT_PRODUCT_PAGE` and `CUSTOM_PRODUCT_PAGE` creative types, `creativeSpec` is a product page creative spec object, which is intentionally empty. The pre-tap experience isn’t customizable through the API. All visual assets and copy come from App Store Connect.

The `destination` object carries all required parameters for product page ad creatives:

- `destinationType` is set to `APP_STORE_PRODUCT_PAGE`.
- `parameters.adamId` is the App Store app identifier, and it’s required for both ad creative types.
- `parameters.productPageId` is the custom product page identifier, and it’s required for `CUSTOM_PRODUCT_PAGE`. Omit it or leave it `null` for `DEFAULT_PRODUCT_PAGE`.

##### Understand Apple Maps Creatives

For `LOCAL_ADS_SEARCH_CREATIVE`, `creativeSpec` contains an Apple Maps creative spec with the brand’s visual content and promotional text. The spec includes the following fields:

| Apple Maps Creative Spec Field | Description |
| --- | --- |
| `brandId` | The brand identifier this ad creative belongs to |
| `creativeSubtype` | Asset format: `BUSINESS_LOGO` or `BUSINESS_ASSET` |
| `creativeAssets` | Array of creative asset references, each identified by `assetId` |
| `localizedText` | Localized promotional copy keyed by locale (for example, `"en-US": {"promoText": "Visit us today"}`) |

For Apple Maps ad creatives, the post-tap destination is always the Apple Maps place card. Set `destination.destinationType` to `LOCAL_ADS_PLACECARD` at creation. This destination type takes no `parameters`, since there’s no equivalent of `adamId` or `productPageId` to specify for a Maps place card.

##### Track System Status and Eligibility

Every ad creative has a `systemStatus` field that reflects whether the ad creative is ready to serve:

| systemStatus | Description |
| --- | --- |
| `VALID` | The ad creative passed all system validations and is eligible to serve. The ad creative may still be subject to additional review. |
| `INVALID` | The ad creative failed one or more validations. Check `systemStatusReasons`. |
| `PENDING` | The ad creative is undergoing system validation. |

When `systemStatus` is `INVALID`, the `systemStatusReasons` array contains one or more of the following values. Reasons marked **Apple Maps ad creatives only** or **Product page ad creatives only** apply exclusively to that creative type. Unless marked, a reason applies to both App Store and Apple Maps ad creatives:

| Reason | Description |
| --- | --- |
| `ASSET_DELETED` | A referenced asset no longer exists. **Apple Maps ad creatives only**, since only `LOCAL_ADS_SEARCH_CREATIVE` carries asset references in `creativeSpec`. |
| `CREATIVE_ASSET_PENDING_AVAILABILITY` | The advertiser uploaded a creative asset, but it isn’t yet available. **Apple Maps ad creatives only**. |
| `CREATIVE_ASSET_UNAVAILABLE` | A required creative asset is unavailable. **Apple Maps ad creatives only**. |
| `PRODUCT_PAGE_DELETED` | The developer deleted the linked product page in App Store Connect. **Product page ad creatives only** (`DEFAULT_PRODUCT_PAGE`, `CUSTOM_PRODUCT_PAGE`), since Apple Maps ad creatives don’t reference a product page. |
| `PRODUCT_PAGE_HIDDEN` | The developer hid the linked product page in App Store Connect. **Product page ad creatives only**. |
| `PRODUCT_PAGE_UNAVAILABLE` | The linked product page is temporarily unavailable. **Product page ad creatives only**. |
| `DELETED_BY_USER` | The advertiser deleted the ad creative. |
| `PAUSED_BY_USER` | The advertiser paused the ad creative. |
| `POLICY_PROHIBITED` | The ad creative violates advertising policy and can’t serve. |
| `NEEDS_REVIEW` | The ad creative requires manual review before it can serve. |
| `POLICY_UNDEFINED` | The system hasn’t yet made a policy determination for the ad creative. |
| `MISSING_ASSET` | One or more required assets are missing from the ad creative. **Apple Maps ad creatives only**. |
| `PENDING_ASSET_CHECKS` | Asset checks are in progress and the ad creative is awaiting the outcome. **Apple Maps ad creatives only**. |
| `FAILED_ASSET_RATIO_COMPATIBILITY` | One or more assets don’t meet the required aspect ratio for the targeted placement. **Apple Maps ad creatives only**. |

Each ad creative also carries an `eligibility` field of type [`CreativeEligibility`](creativeeligibility.md). The system returns eligibility data for ad creatives of every `creativeType`, including App Store product page ad creatives (`DEFAULT_PRODUCT_PAGE`, `CUSTOM_PRODUCT_PAGE`) and Apple Maps ad creatives (`LOCAL_ADS_SEARCH_CREATIVE`). It summarizes whether the ad creative meets the requirements to serve on each supported ad placement.

##### Query Ad Creatives

The [`Query Ad Creatives`](post-creatives-query.md) endpoint supports filtering ad creatives by `creativeType`, `systemStatus`, `name`, and `eligibility.status` using dot-notation, with observed values `ELIGIBLE` and `INELIGIBLE`.

##### Look Up Rejection Reasons

For product page ad creatives (`DEFAULT_PRODUCT_PAGE`, `CUSTOM_PRODUCT_PAGE`), detailed rejection information is available as [`CreativeRejectionReason`](creativerejectionreason.md) records. These records are queried and fetched through endpoints documented under Apps > App Eligibility rather than under Creatives: see [`Query Rejection Reasons`](find-rejection-reasons.md) (`POST /v1/rejection-reasons/apps/query`) and [`Get Rejection Reasons`](gets-rejection-reasons-by-id.md) (`GET /v1/rejection-reasons/apps/{rejectionReasonId}`).

For Apple Maps ad creatives (`LOCAL_ADS_SEARCH_CREATIVE`), rejection information is available as policy assignment records instead, queried through the Brands endpoint: see [`Query Rejection Reasons for Brands`](query-policy-assignments-(rejection-reasons)-for-external-consumers.md) (`POST /v1/rejection-reasons/business-brands/query`), filtered by the brand’s `promotedObjectId`.

## Topics

- [Create an Ad Creative](post-creatives.md)
  Add a new ad creative that defines the visual presentation and tap destination for an ad.
- [Query Ad Creatives](post-creatives-query.md)
  Retrieve ad creatives that match structured filter, sort, and pagination criteria.
- [Get an Ad Creative](get-creatives-_id_.md)
  Fetch a single ad creative by its unique identifier.
- [Update an Ad Creative](put-creatives-_id_.md)
  Change an ad creative’s name or creative spec by its unique identifier.
- [Delete an Ad Creative](delete-creatives-_id_.md)
  Remove an ad creative by its unique identifier.

## See Also

- [Ad Creatives Data Objects](creatives-data-objects.md)
  Reference the request and response payloads used by ad creative endpoints.
- [Ad Creative Data Types](creative-data-types.md)
  Look up the allowed values for creative type, status, and destination type fields.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/creatives-endpoints)*