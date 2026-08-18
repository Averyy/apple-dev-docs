# Geo Targeting Endpoints

**Framework**: Apple Ads Platform API

Retrieve geographic location metadata used for geo targeting.

**Availability**:
- Apple Ads Platform API 1.0+

#### Overview

Geo targeting lets you focus ad delivery on specific countries, regions, cities, or postal codes associated with where the ad viewer is located.

- The API doesn’t use precise location for either channel: App Store campaigns use the device’s location, and Apple Maps campaigns use either the current map view or the device’s location.
- Whether device location is available depends on whether the user has location services enabled for the app.
- Apple Maps campaigns discover users based on their location while they’re using Apple Maps, not based on the business locations the ads promote.
- The API provides dedicated endpoints for discovering valid location identifiers, which you then reference in ad group targeting dimensions.

##### Query Geo Location Metadata

App Store and Apple Maps campaigns both use the Geo Search endpoints (`GET` and `POST /v1/search/geo`). The `supplySource` parameter controls which entity types appear in the results and scopes eligibility evaluation to the relevant campaign context.

Use the two geo search endpoints to retrieve geographic location metadata:

- Use `GET /v1/search/geo` to perform a text search by name or wildcard. It requires the `supplySource` query parameter, and it accepts optional parameters `query` (minimum two characters, or `*` to return all), `entity`, `countrycode`, `eligible`, `offset`, and `pageSize`.
- Use `POST /v1/search/geo` to look up locations by ID. It accepts a `GeoSearchPostRequest` body with a `geoRequest` array of (`entity ID`, `type`) or (`legacyID`, `type`) pairs, and it also requires `supplySource`.

| `supplySource` | Entity types returned | Excludes | Notes |
| --- | --- | --- | --- |
| `APPSTORE` | `Country` (a country or region), `AdminArea` (a state or province within a country), `Locality` (a city or metropolitan area) | `PostalCode` | Postal-code geo is only available with `MAPS`. |
| `MAPS` | `AdminArea` (a state or province within a country), `Locality` (a city or metropolitan area), `PostalCode` (a postal code) | `Country` | Results are restricted to the US and Canada. |

Each result includes `id`, `legacyId` (pipe-delimited hierarchy, e.g. `US|CA|San Francisco`), `entity`, `displayName`, `countryOrRegion`, `adminArea`, `locality`, `postalCode`, and an `eligibility` object scoped to the requested supply source.

By default, the API includes soft-blocked geos (low search volume, sparse coverage) with eligibility data. Pass `eligible=true` on the GET endpoint to exclude them from results.

##### Target Apple Maps Campaigns By Geography

For Apple Maps campaigns, geo targeting controls where the ad viewer is located when the ad is shown, not which advertiser business locations the ad group promotes. To reach users in specific geographic areas on Maps, use the `postalCode`, `locality`, and `adminArea` targeting dimensions.

To find valid locality and postal code identifiers for Maps campaigns, use `GET /v1/search/geo` with `supplySource=MAPS`. The API restricts results to the US and Canada. You can only use the `PostalCode` entity type under `supplySource=MAPS`.

You can view location-level reporting for Apple Maps campaigns by grouping or filtering the Apple Maps report endpoints (`POST /v1/reports/business-brands/{campaigns,adgroups,ads,keywords,searchterms}/query`) by `locationId`, rather than through a dedicated locations-report endpoint.

> **Note**: The `locationGroup` targeting field controls which of the advertiser’s business locations the ad group promotes. It isn’t a geo targeting dimension and doesn’t filter by the ad viewer’s location. Manage location groups via the [`Managing Location Groups`](location-groups-overview.md).

##### Apply Geo Targeting Dimensions to an Ad Group

You apply geo targeting through the `targeting` field on an ad group, alongside the ad group’s other audience and placement dimensions. See [`AdGroupTargeting`](adgrouptargeting.md) for the full set of available dimensions. Each geo dimension uses a [`TargetingData`](targetingdata.md) object with `include` and `exclude` arrays of location identifiers.

The following geo targeting dimensions are available:

| Dimension | Scope | Description |
| --- | --- | --- |
| `country` | Apps | Reach users in specific countries or regions. Use a country ID from the Geo Search endpoint. |
| `adminArea` | Apps & Maps | Reach users in specific states or provinces. Use identifiers from the Geo Search endpoint. |
| `locality` | Apps & Maps | Reach users in specific cities. Use identifiers from the Geo Search endpoint. |
| `postalCode` | Maps | Reach users by postal code. Use identifiers from the Geo Search endpoint with `supplySource=MAPS`. |

Dimensions can be combined. For example, target a country while excluding specific cities within it. Use `exclude` arrays to suppress delivery in locations that overlap with a broader inclusion.

> **Note**: The `locationGroup` field isn’t a geo targeting dimension. It specifies which of the advertiser’s business locations to promote and doesn’t filter by the ad viewer’s location. See [`Managing Location Groups`](location-groups-overview.md).

##### Check Supported Languages By Market

This applies to App Store campaigns only. To retrieve the languages supported for App Store advertising in each country or region, use `POST /v1/metadata/apps/supported-languages/query`. The response includes `adsSupportedLanguages` and `adsDefaultLanguages` per country code. To validate creative language selection before targeting a new market, use this data.

##### Report on Performance By Geography

Both Apps and Apple Maps reports support geographic breakdowns via the `groupBy` parameter. The following table lists which geographic dimensions each report type supports:

| Dimension | Apps | Apple Maps |
| --- | --- | --- |
| `countryOrRegion` | Supported on campaign, ad group, keyword, search term, and ad reports | N/A |
| `countryCode` | Supported on campaign and ad group reports | N/A |
| `adminArea` | Supported on campaign and ad group reports | N/A |
| `locality` | Supported on campaign and ad group reports | N/A |
| `locationId` | N/A | Supported on campaign, ad group, keyword, search term, and ad reports |

For Apple Maps, `locationId` groups report rows by individual business location, enabling per-location performance analysis across the full campaign hierarchy.

#### Use the Geo Search Endpoints

Use these endpoints to retrieve and search geographic location metadata:

| Method | Path | Description |
| --- | --- | --- |
| `POST` | `/v1/search/geo` | [`Query Geo Locations`](gets-a-list-of-geo-locations.md) retrieves geographic location metadata by entity ID for geo targeting. |
| `GET` | `/v1/search/geo` | [`Search Geo Locations`](searches-for-a-list-of-geo-locations.md) searches geographic locations by name or wildcard text. |
| `POST` | `/v1/metadata/apps/supported-languages/query` | [`Query Supported App Languages`](query-supported-app-languages.md) returns the languages supported for app advertising in each country or region. |

## Topics

- [Query Geo Locations](gets-a-list-of-geo-locations.md)
  Search for geographic locations by entity type and ID for use in ad group geo targeting.
- [Search Geo Locations](searches-for-a-list-of-geo-locations.md)
  Search for geographic locations for use in ad group geo targeting.

## See Also

- [Geo Targeting Data Objects](geo-targeting-data-objects.md)
  Reference the request and response objects for geo targeting.
- [Geo Targeting Data Types](geo-targeting-data-types.md)
  Reference the enumerations and scalar types for geo targeting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/geo-targeting-endpoints)*