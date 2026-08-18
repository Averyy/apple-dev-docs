# App Eligibility Endpoints

**Framework**: Apple Ads Platform API

Check whether apps qualify to run ads and look up rejection reasons for creatives.

**Availability**:
- Apple Ads Platform API 1.0+

#### Overview

Not every app is eligible for promotion. Apple evaluates each app against a set of policy and technical criteria before it can serve ads, at a per-placement, per-country level of granularity. Each `EligibilityResponse` row reports a `state` of `ELIGIBLE` or `INELIGIBLE` for a given `adamId`, `supplyPlacement`, `supplySource`, `countryOrRegion`, and `deviceClass`, along with the `minAge` rating required in that market. To retrieve human-readable descriptions of any policy violations returned during ad creative review of App Store ad creatives, use the rejection reasons endpoints on this page.

This eligibility check applies to App Store app promotion (`promotedObjectType: APPSTORE_APP`) only. Apple Maps brand promotion (`promotedObjectType: BUSINESS_BRAND`) doesn’t use a dedicated eligibility query. Instead, the `eligibility` field on the [`Brand`](brand.md), [`Location`](location.md), [`BusinessCategory`](businesscategory.md), and [`LocationGroup`](locationgroup.md) objects reports serving eligibility directly, described in [`Eligibility`](eligibility.md). Apple Maps ad creative rejection reasons are also queried separately, with [`Query Rejection Reasons for Brands`](query-policy-assignments-(rejection-reasons)-for-external-consumers.md).

Use [`Search Apps Endpoints`](search-apps-endpoints.md) to find an app’s `adamId` and full app details, including via [`Get App Details by Adam ID`](get-app-details-by-adam-id.md), to check its eligibility. Once an app is eligible, use [`Product Pages Endpoints`](product-pages-endpoints.md) to discover its product pages to reference in an ad creative.

#### Explore the Endpoints

The following endpoints let you check eligibility and retrieve rejection reasons:

| Method | Path | Description |
| --- | --- | --- |
| `POST` | `/v1/eligibilities/apps/query` | [`Check App Eligibility`](find-apps-eligibilities.md) queries eligibility status for one or more apps across supply placements and countries or regions. |
| `POST` | `/v1/rejection-reasons/apps/query` | [`Query Rejection Reasons`](find-rejection-reasons.md) queries rejection reasons for ad creatives associated with an app. |
| `GET` | `/v1/rejection-reasons/apps/{rejectionReasonId}` | [`Get Rejection Reasons`](gets-rejection-reasons-by-id.md) retrieves a single rejection reason by ID. |

#### Interpret the Eligibility States

The following states apply to `EligibilityResponse.state` values returned by the `POST /v1/eligibilities/apps/query` endpoint:

| State | Description |
| --- | --- |
| `ELIGIBLE` | You can promote the app at this placement and country combination. |
| `INELIGIBLE` | You can’t promote the app at this placement and country combination. |

## Topics

- [Check App Eligibility](find-apps-eligibilities.md)
  Check whether apps are eligible to run on certain Apple Ads placements and in specific countries or regions.
- [Query Rejection Reasons](find-rejection-reasons.md)
  Query ad creative rejection reasons for apps and return why each ad creative failed approval.
- [Get Rejection Reasons](gets-rejection-reasons-by-id.md)
  Retrieve the details of an ad creative rejection reason by ID.

## See Also

- [Search Apps Endpoints](search-apps-endpoints.md)
  Browse the endpoints for searching apps and retrieving app details.
- [Product Pages Endpoints](product-pages-endpoints.md)
  Retrieve product pages and their localized details.
- [App Eligibility Data Objects](app-eligibility-data-objects.md)
  Reference the request and response objects used by the app eligibility and rejection reason endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/app-eligibility-endpoints)*