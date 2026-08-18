# Ads Endpoints

**Framework**: Apple Ads Platform API

Create, retrieve, update, and delete ads using these endpoints.

**Availability**:
- Apple Ads Platform API 1.0+

#### Overview

An [`Ad`](ad.md) object connects a [`Creative`](creative.md) to an ad group. The ad is the serving unit: It tells the system which ad creative to show when the ad group wins an auction. An ad group can contain multiple ads, but only one ad per ad group can be `ENABLED` at a time. Enabling a different ad requires pausing the one currently serving.

Creating an ad requires a `name`, a `status`, the `adGroupId` of the target ad group, and a `creativeId` referencing an existing [`Creative`](creative.md). Create the ad creative first, then reference its `id` here. The `campaignId`, `adAccountId`, and other system fields are read-only, and the system populates them automatically at creation.

#### Use the Ads Endpoints

Use these endpoints to create, retrieve, update, and delete ads:

| Method | Path | Description |
| --- | --- | --- |
| `POST` | `/v1/ads` | [`Create an Ad`](post-ads.md) creates a new ad. |
| `POST` | `/v1/ads/query` | [`Query Ads`](post-ads-query.md) retrieves ads matching the specified filters. |
| `GET` | `/v1/ads/{id}` | [`Get an Ad`](get-ads-_id_.md) retrieves a single ad by its ID. |
| `PUT` | `/v1/ads/{id}` | [`Update an Ad`](put-ads-_id_.md) updates an existing ad. |
| `DELETE` | `/v1/ads/{id}` | [`Delete an Ad`](delete-ads-_id_.md) soft-deletes an ad by its ID. |

##### Track Ad Status and System Status

Ads have three status fields that together determine whether an ad is serving:

- `status`: The advertiser-controlled field. Set it to `ENABLED` to let the ad serve, or `PAUSED` to stop delivery without deleting the ad. You can only update `status` and `name` after creation.
- `systemStatus`: A system-computed field that reflects whether the ad is actually running. A value of `RUNNING` means the ad is active and eligible to serve, and a value of `NOT_RUNNING` means the system identified a condition that’s preventing delivery.
- `displayStatus`: A system-computed field that represents a rolled-up label combining `status` and `systemStatus` into a single delivery state. See [`AdDisplayStatus`](addisplaystatus.md) for all values.

When `systemStatus` is `NOT_RUNNING`, the system populates the `systemStatusReasons` array with one or more values explaining why. Reasons marked **App Store-specific** apply only to App Store ads. Unless marked, a reason applies to both App Store and Apple Maps ads:

| Reason | Description |
| --- | --- |
| `AD_APPROVAL_PENDING` | The ad is awaiting Apple review. |
| `AD_APPROVAL_REJECTED` | Apple reviewed and rejected the ad. |
| `AD_APPROVAL_CREATIVE_DOC_NOT_SUBMITTED` | The advertiser hasn’t submitted the required creative documentation for review. |
| `AD_APPROVAL_CREATIVE_DOC_PENDING` | Apple is reviewing the submitted creative documentation. |
| `AD_APPROVAL_CREATIVE_DOC_REJECTED` | Apple rejected the creative documentation during review. |
| `AD_APPROVAL_CREATIVE_DOC_EXPIRED` | The previously approved creative documentation has expired. |
| `PROCESSING` | General processing state. The ad isn’t yet ready to serve. |
| `PAUSED_BY_USER` | The advertiser set the ad’s `status` to `PAUSED`. |
| `PAUSED_BY_SYSTEM` | The system paused the ad due to a policy or account condition. |
| `DELETED_BY_USER` | The advertiser deleted the ad. |
| `CREATIVE_SET_INVALID` | The associated ad creative is invalid. |
| `CREATIVE_SET_UNSUPPORTED` | The current placement doesn’t support the associated ad creative type. |
| `CREATIVE_INVALID` | The associated ad creative is invalid and can’t serve. |
| `CREATIVE_PENDING` | The associated ad creative is pending validation or Apple review. |
| `CREATIVE_LOCALE_INCOMPATIBLE` | The ad creative locale doesn’t match the targeted market. |
| `PRODUCT_PAGE_DELETED` | **App Store-specific.** The developer deleted the linked product page in App Store Connect. |
| `PRODUCT_PAGE_HIDDEN` | **App Store-specific.** The developer hid the linked product page in App Store Connect. |
| `PRODUCT_PAGE_INCOMPATIBLE` | **App Store-specific.** The product page is incompatible with the current campaign configuration. |
| `PRODUCT_PAGE_INSUFFICIENT_ASSETS` | **App Store-specific.** The product page doesn’t have enough assets to render the ad. |
| `PRODUCT_PAGE_UNAVAILABLE` | **App Store-specific.** The product page is temporarily unavailable. |

##### Interpret System Status Limiting Reasons

When an ad is running but delivering at reduced capacity, the system populates the `systemStatusLimitingReasons` array. Unlike `systemStatusReasons`, these reasons don’t stop delivery. Instead, they constrain reach. There’s one possible value, `CREATIVE_POLICY_ISSUES`, which means the ad creative associated with the ad has policy conditions that limit but don’t fully stop delivery.

##### Understand Apple Review Requirements

Apple must approve ads before they can serve. For App Store ads, the review covers the ad creative content and product page. For Apple Maps ads, the review covers the brand ad creative instead.

The `CREATIVE_PENDING` and `CREATIVE_INVALID` reasons reflect this review state. While an ad is under review, `systemStatus` is `NOT_RUNNING` and `systemStatusReasons` includes `AD_APPROVAL_PENDING` or `CREATIVE_PENDING`. Once Apple approves the ad, `systemStatus` changes to `RUNNING` unless the advertiser sets `status` to `PAUSED` or schedules a future start date.

## Topics

- [Create an Ad](post-ads.md)
  Creates a new ad that links an ad creative to an ad group for delivery.
- [Query Ads](post-ads-query.md)
  Searches and filters ads using structured query criteria including field filters, sorting, and pagination.
- [Get an Ad](get-ads-_id_.md)
  Retrieves a single ad by its unique identifier.
- [Update an Ad](put-ads-_id_.md)
  Updates the name or status of an existing ad by its unique identifier.
- [Delete an Ad](delete-ads-_id_.md)
  Soft-deletes an ad by its unique identifier, stopping delivery and removing it from active results.

## See Also

- [Ads Data Objects](ads-data-objects.md)
  Reference the request and response objects used by ad endpoints.
- [Ads Data Types](ads-data-types.md)
  Reference the enumerations and scalar types used by ad objects and endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/ads-endpoints)*