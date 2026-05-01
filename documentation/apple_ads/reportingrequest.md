# ReportingRequest

**Framework**: Apple Ads  
**Kind**: dictionary

The report request body.

**Availability**:
- Search Ads 2.0+

## Declaration

```swift
object ReportingRequest
```

## Mentions

- [Apple Ads Campaign Management API 2](apple-search-ads-campaign-management-api-2.md)

## Properties

- `endTime` (string) *(required)*: The date and time the report coverage ends. The format is `YYYY-MM-DD`.
- `granularity` (string): The report data organized by hour, day, week, and month. > **Note**: For [`Get Search Term-Level Reports`](get-search-term-level-reports.md), if you specify `granularity` in the payload, make sure `returnRowTotals` and `returnGrandTotals` are `false`. - **`HOURLY`**: The `startTime` and `endTime` are ≤ 7 days apart, and the `startTime` is ≤ 30 days in the past. Use: `"granularity":"HOURLY"`, The hour, `00` to `23`, appends to the date string as `HH`. > **Note**: `HOURLY` isn’t available to use in [`Get Search Term-Level Reports`](get-search-term-level-reports.md) or [`Get Ad-Level Reports`](get-ad-level-reports.md).
- **`DAILY`**: The `startTime` and `endTime` are ≤ 90 days apart, and the `startTime` is ≤ 90 days in the past.
- **`WEEKLY`**: The `date` value is the Monday of the designated week. The `startTime` and `endTime` are > 14 days and ≤ 365 days apart, and the `startTime` is ≤ 24 months in the past.
- **`MONTHLY`**: The `date` value is the first day of the designated month. The `startTime` and `endTime` are > 3 months apart, and the `startTime` is ≤ 24 months in the past.
- `groupBy` ([string]): Use the `groupBy` field to group responses by selected dimensions. If `groupBy` specifies age, gender, and geodimensions, `returnRowTotals` and `returnGrandTotals` must be `false`. > **Note**: The API groups `ageRange`, `countryCode`, [`Gender`](gender.md), `adminArea`, and `locality` records with fewer than 100 impressions in the API response as `other`. The following `groupBy` descriptions include supported values per dimension: - **`adminArea`**: The `adminArea` dimension is a group of states or the equivalent according to its associated `country`. Use [`Search for Geolocations`](search-for-geolocations.md) to retrieve geolocations. In [`Get Ad Group-Level Reports`](get-ad-group-level-reports.md), you need to use the `adminArea` dimension with `countryCode`. The `locality` dimension is optional.
- **`ageRange`**: The `ageRange` dimension is a group of the user demographic age ranges. In [`Get Ad Group-Level Reports`](get-ad-group-level-reports.md), the `ageRange` dimension is available to use with [`DeviceClass`](deviceclass.md).
- **`countryCode`**: The `countryCode` dimension is a group of country codes that indicate the country or region to serve ads in. In [`Get Ad Group-Level Reports`](get-ad-group-level-reports.md), the `countryCode` dimension is available to use with [`DeviceClass`](deviceclass.md), `adminArea`, and `locality`.
- **[`CountryOrRegion`](countryorregion.md)**: The [`CountryOrRegion`](countryorregion.md) dimension is a group of countries and regions. In [`Get Campaign-Level Reports`](get-campaign-level-reports.md), [`Get Ad Group-Level Reports`](get-ad-group-level-reports.md), [`Get Keyword-Level Reports`](get-keyword-level-reports.md),  and [`Get Search Term-Level Reports`](get-search-term-level-reports.md), the [`CountryOrRegion`](countryorregion.md) dimension is available to use with [`DeviceClass`](deviceclass.md).
- **[`DeviceClass`](deviceclass.md)**: The [`DeviceClass`](deviceclass.md) dimension is a group of device classes that the promoted app supports. In [`Get Ad Group-Level Reports`](get-ad-group-level-reports.md), the [`DeviceClass`](deviceclass.md) dimension is available to use with any other dimension.
- **[`Gender`](gender.md)**: The [`Gender`](gender.md) dimension is a group of user-demographic genders. In [`Get Ad Group-Level Reports`](get-ad-group-level-reports.md), the [`Gender`](gender.md) dimension is available to use with [`DeviceClass`](deviceclass.md).
- **`locality`**: The `locality` dimension is the city or group of cities equivalent according to its associated `adminArea`. See [`Search for Geolocations`](search-for-geolocations.md) to retrieve geolocations. In [`Get Ad Group-Level Reports`](get-ad-group-level-reports.md), the `locality` dimension with higher dimensions is available to use with `countryCode` and `adminArea`.
- `returnGrandTotals` (boolean): Returns the total of all the rows in the result set. If you don’t specify `granularity`, `returnRowTotals` must be `true`. If you specify `granularity` in the payload, `returnGrandTotals` must be `false`. The default is `false`.
- `returnRecordsWithNoMetrics` (boolean): Specifies whether the API returns records without metrics. The default is `false`.
- `returnRowTotals` (boolean): Specifies whether to return the totals of each row. If you don’t specify `granularity`, `returnRowTotals` must be `true`. If you specify `granularity` in the payload, `returnGrandTotals` must be `false`. The default is `false`. For example: ```console
"granularity": "DAILY",
"returnRowTotals": false,
"returnGrandTotals": false
```
- `selector` (Selector) *(required)*: [`Selector`](selector.md) objects define what data the API returns when fetching resources. [`Selector`](selector.md) objects are available to use with Find and Reports endpoints. - **[`Condition`](condition.md)**: Additional types of filters to perform deeper filtering of the data. For available conditions per field for each report type, see [`ReportingCampaign`](reportingcampaign.md), [`ReportingAdGroup`](reportingadgroup.md), [`ReportingKeyword`](reportingkeyword.md), [`ReportingSearchTerm`](reportingsearchterm.md), and [`ReportingAd`](reportingad.md).
- **`orderBy`**: Specify a field name and grouping to sort the records by `ASCENDING` or `DESCENDING`. This sorts on all `groupBy` dimensions and most metadata. See [`ExtendedSpendRow`](extendedspendrow.md). Only one `orderBy` field is available to use per payload.
- **[`Pagination`](pagination.md)**: Specify how many records to return per page. The default is `20`.
- `startTime` (string) *(required)*: The date and time the report coverage starts. The format is `YYYY-MM-DD`.
- `timeZone` (string): You set the default `timeZone` during account creation through [`Apple Ads`](https://developer.apple.comhttps://ads.apple.com). `ORTZ` (organization time zone) is the default.

## See Also

- [object ReportingResponseBody](reportingresponsebody.md)
  The container object for the report response body.
- [object ReportingResponse](reportingresponse.md)
  The container object of report metrics.
- [object ReportingDataResponse](reportingdataresponse.md)
  The total metrics for a report.
- [object GrandTotalsRow](grandtotalsrow.md)
  The summary of cumulative metrics.
- [object SpendRow](spendrow.md)
  The reporting response metrics.
- [object ExtendedSpendRow](extendedspendrow.md)
  The descriptions of metrics with dates.
- [object Row](row.md)
  The report metrics by time granularity.
- [object ReportingCampaign](reportingcampaign.md)
  The response to a request to fetch campaign-level reports.
- [object ReportingAdGroup](reportingadgroup.md)
  The response to a request to fetch ad group-level reports.
- [object ReportingKeyword](reportingkeyword.md)
  The response to a request to fetch keyword-level reports.
- [object ReportingSearchTerm](reportingsearchterm.md)
  The response to a request to fetch search term-level reports.
- [object ReportingAd](reportingad.md)
  The response to a request to fetch ad-level reports.
- [object CampaignAppDetail](campaignappdetail.md)
  The app data to fetch from campaign-level reports.
- [object InsightsObject](insightsobject.md)
  The container object for bid recommendations.
- [object KeywordInsights](keywordinsights.md)
  The object that contains bid recommendations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/reportingrequest)*