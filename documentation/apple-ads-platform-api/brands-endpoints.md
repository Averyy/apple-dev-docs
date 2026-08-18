# Ads on Apple Maps Endpoints

**Framework**: Apple Ads Platform API

Query and retrieve brands, business categories, and creative rejection reasons.

**Availability**:
- Apple Ads Platform API 1.0+

#### Overview

Use the Apple Ads Platform API to create and manage Apple Maps campaigns that promote business locations on Apple Maps. Ads on Apple Maps help users find businesses; you can reach people before they search, at the top of the Suggested Places list on Search home, or after they search for something specific, on Search results. For a full end-to-end walkthrough, see [`Advertising Your Business on Apple Maps`](journey-apple-maps-brand-ads.md).

#### Review the Prerequisites

Ads on Apple Maps require an Apple Ads profile and a validated brand in Apple Ads. A brand must have `eligibility.status: ELIGIBLE` before you can use it in a campaign. Your ad account must also have `productFeatures: ["BUSINESS_BRAND_MANUAL"]` and a `BUSINESS_BRAND` delegation with the Brand ID as `resourceId` before campaigns can go live. See [`ProductFeatures`](productfeatures.md) for full delegation requirements. All API calls require a Bearer token and the `X-AP-Context: adAccountId` header.

#### Understand the Campaign Structure

App Store campaigns use three objects: Campaign, Ad Group, and Ad, plus a Creative. Apple Maps campaigns add two more, [`Understanding Locations`](locations-overview.md) and [`Managing Location Groups`](location-groups-overview.md), that sit between the Brand and the Ad Group. The dependency chain is:

- **Brand**: the root object for the account. Every Maps campaign’s `promotedObjectId` is a brand ID. - **Location**: a physical place of business belonging to one brand. Locations are read-only and come from Apple Business. You can’t create or edit locations through this API. - **Location Group**: a named collection of a brand’s location IDs. Ad groups target a location group, not individual locations. You must build a location group before an ad group can use location-based targeting.
- **Asset**: an uploaded image tied to the brand through `promotedObjectId`. Assets must reach `eligibility.status: ELIGIBLE` before use. - **Creative**: combines a brand asset, promotional text, and the Apple Maps place card destination into the ad unit. A creative references the brand and one or more assets.

A Campaign references the Brand directly. Its Ad Groups reference a Location Group for targeting, and its Ads reference a Creative. Both the Location Group and the Creative must exist, and be in a valid state, before the Ad Group and Ad that depend on them can serve.

#### Follow the Campaign Workflow

Follow these steps, in order, to launch an Apple Maps campaign once your brand and assets are ready:

1. **Find and validate your brand.** Query the Brands API to retrieve your brand’s identifier, filtering by `eligibility.status: ELIGIBLE`. Campaign creation requires both `promotedObjectType: BUSINESS_BRAND` and `promotedObjectId` (the brand ID), and both remain immutable afterward. Confirm the correct brand before creating a campaign.
2. **Upload and prepare assets.** Upload images directly with [`Upload Asset`](upload-asset.md). The multipart request body must include the binary image file alongside `promotedObjectId` and `promotedObjectType: BUSINESS_BRAND`. To check the `eligibility.status` field, use [`Get Asset`](get-asset-by-id.md). Assets must reach `ELIGIBLE` before you can reference them in a creative.
3. **Create location groups.** Location groups let you group the business locations you want to promote together under an ad group, rather than requiring you to set each one individually. Location groups don’t control who sees the ad or how close they are to a location. Geo and radius targeting on the ad group handle that separately. - Create a group with [`Create Location Group`](create-location-group.md), supplying `name`, `brandId`, `adAccountId`, `groupType` (`STATIC` or `DYNAMIC`), and the Apple Maps location IDs for `STATIC` groups.
- To look up valid location IDs, use [`Query for Locations`](query-locations.md), filtering by country, name, or status.
- Groups with `groupType: DYNAMIC` start in `systemStatus: PENDING` while Apple Ads evaluates the rules. Wait for `systemStatus: VALID` before referencing the group in ad group targeting.
4. **Choose placements and markets.** Set the campaign’s `targeting` to a `supplySource` of `MAPS`, one or both Apple Maps placements (`MAPS_SEARCH_RESULTS` for Search results, `MAPS_SEARCH_HOME` for Search home), and a `countryOrRegion` list that includes only the markets where your brand is eligible. You can combine both placements in one campaign, or create separate campaigns per placement for independent budget control and reporting. All three targeting dimensions remain mutable after you create the campaign.
5. **Create a creative.** A creative assembles an asset, promotional text, and the tap destination (always the Apple Maps place card) into the ad unit shown on Apple Maps. Apple Ads may review creatives before they can serve. To monitor approval status, use [`Query Ad Creatives`](post-creatives-query.md). If Apple Ads rejects a creative or brand entity, query rejection reason details with [`Query Rejection Reasons for Brands`](query-policy-assignments-(rejection-reasons)-for-external-consumers.md).
6. **Create a campaign.** Create the campaign with a POST to `/v1/campaigns`. - Set `promotedObjectType: BUSINESS_BRAND` and your brand ID as `promotedObjectId`.
- Set the `targeting` object you configured in step 4.
- Set a `dailyBudget` with an amount and currency.
- If your ad account is on monthly invoicing (`paymentModel: LOC`), you can later use [`Budget Orders Endpoints`](budget-orders-endpoints.md) to cap total spend across a group of campaigns, on top of each campaign’s `dailyBudget`. Accounts on `PAYG` can’t use budget orders.
- Both `promotedObjectType` and `promotedObjectId` become immutable after creation.
7. **Create an ad group.** Ad groups sit under a campaign. Reference the location group from step 3 in `targeting.locationGroup.include` to restrict delivery to your chosen locations. This array accepts more than one location group. Apple Maps ad groups also support admin area, locality, postal code, radius, and daypart targeting. You can also add keywords with `PHRASE` or `CATEGORY` match types for the Search results placement.
8. **Create an ad.** Link the creative to the ad group by creating an Ad object that references the `creativeId`, `campaignId`, and `adGroupId`. Ads go through Apple review before serving.
9. **Pull reports.** Apple Maps campaigns use the fixed `business-brands` path segment in all report endpoints (`/v1/reports/business-brands/campaigns/query`, `/adgroups/query`, `/ads/query`, `/keywords/query`, and `/searchterms/query`). These endpoints support `timeZone: "ORTZ"` to align timestamps to your organization’s configured time zone. There’s no dedicated location-level report endpoint. Instead, group or filter any of these by `locationId` to see performance broken down by individual map location.

## Topics

- [Query Brands](query-brands.md)
  Retrieve a paginated list of brands using filters and sorting.
- [Get Brand by ID](get-brand-by-id.md)
  Retrieve a single brand by its unique identifier.
- [Query Business Categories](query-categories.md)
  Retrieve a paginated list of business categories using filters and sorting.
- [Get Business Category](get-category-by-id.md)
  Retrieve a single business category by its identifier.
- [Query Rejection Reasons for Brands](query-policy-assignments-(rejection-reasons)-for-external-consumers.md)
  Query paginated policy assignment rejection reason details.

## See Also

- [Managing Location Groups](location-groups-overview.md)
  Organize business locations into named groups that define which locations an ad group’s targeting applies to in Apple Maps campaigns.
- [Understanding Locations](locations-overview.md)
  Query and inspect the business locations associated with your brand for use in Apple Maps campaigns.
- [Brands Data Objects](brands-data-objects.md)
  Reference the request and response objects for brand, location, and location group endpoints.
- [Brands Data Types](brands-data-types.md)
  Look up the enumerations and metric types used in Apple Maps campaigns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/brands-endpoints)*