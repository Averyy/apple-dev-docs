# AdSystemStatusReason

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

A reason code explaining why an ad is not currently running.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string AdSystemStatusReason
```

## Possible Values

- `PROCESSING`: General processing state during system evaluation.
- `PAUSED_BY_USER`: A user paused the ad.
- `PAUSED_BY_SYSTEM`: The platform automatically paused the ad.
- `DELETED_BY_USER`: A user soft-deleted the ad.
- `AD_APPROVAL_PENDING`: The ad is awaiting Apple review.
- `AD_APPROVAL_REJECTED`: Apple rejected the ad during review.
- `AD_APPROVAL_CREATIVE_DOC_EXPIRED`: A required creative approval document has expired and must be resubmitted.
- `AD_APPROVAL_CREATIVE_DOC_NOT_SUBMITTED`: A required creative approval document has not been submitted.
- `AD_APPROVAL_CREATIVE_DOC_PENDING`: A required creative approval document is awaiting review.
- `AD_APPROVAL_CREATIVE_DOC_REJECTED`: Apple rejected a required creative approval document.
- `CREATIVE_SET_INVALID`: The ad’s creative set configuration is invalid.
- `CREATIVE_SET_UNSUPPORTED`: This ad configuration does not support the associated ad creative type.
- `CREATIVE_INVALID`: The associated ad creative is invalid.
- `CREATIVE_PENDING`: The associated ad creative is pending validation.
- `PRODUCT_PAGE_DELETED`: The App Store product page linked to this ad has been deleted.
- `PRODUCT_PAGE_HIDDEN`: The App Store product page is hidden and not publicly available.
- `PRODUCT_PAGE_INSUFFICIENT_ASSETS`: The App Store product page does not have enough assets to render the ad.
- `PRODUCT_PAGE_UNAVAILABLE`: The App Store product page is unavailable.
- `PRODUCT_PAGE_INCOMPATIBLE`: The product page is incompatible with this ad’s targeting.
- `CREATIVE_LOCALE_INCOMPATIBLE`: The ad creative locale does not match the targeted market.

#### Discussion

One or more `AdSystemStatusReason` values appear in the `systemStatusReasons` array on an [`Ad`](./ad.md) when `systemStatus` is `NOT_RUNNING`. These codes are read-only and system-applied. They provide the specific cause behind a non-running state and indicate what action, if any, is required to resume delivery.

## See Also

- [type AdStatus](./adstatus.md)
  Enumeration of advertiser-configurable serving states for an ad.
- [type AdSystemStatus](./adsystemstatus.md)
  Enumeration of system-evaluated delivery states for an ad.
- [type AdDisplayStatus](./addisplaystatus.md)
  Rolled-up delivery state for an ad, combining advertiser settings and system conditions into a single user-facing label.
- [type AdSystemLimitedStatusReason](./adsystemlimitedstatusreason.md)
  A reason code indicating that an ad is running but at reduced delivery capacity due to a policy condition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/adsystemstatusreason)*