# Query Product Pages

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Queries App Store product pages available to your account.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint queries product pages available to your ad account, returning Default Product Pages (DPPs), Custom Product Pages (CPPs), and Product Page Optimization (PPO) variants. Product pages come from App Store Connect and reflect the current publishing state of your product pages.

Filter by `adamId` to list all product pages for a specific app. This is the recommended starting point when building a `CUSTOM_PRODUCT_PAGE` creative: use this endpoint to discover the available `productPageId` values for an app, then fetch locale details or pass the ID directly to the creative creation endpoint.

Changes made in App Store Connect, such as publishing, hiding, or editing a product page, appear in this endpoint’s results after a short propagation delay.

The `filters` array supports the following fields:

| Field | Supported Operators | Notes |
| --- | --- | --- |
| `adamId` | `EQUALS` | Filter to all product pages for a specific app. |
| `state` | `EQUALS` | Filter by page state. `state` is a plain nullable string with no fixed enum. The typical value is `PUBLISHED`. |

Keep the following constraints in mind when querying product pages:

| Constraint | Detail |
| --- | --- |
| Filter by adamId | Always filter by `adamId` for targeted results. Omitting it may return product pages across all accessible apps. |
| App Store Connect source | Product page data originates in App Store Connect. This endpoint is read-only. |

#### Payload Examples

##### Request

```json
{
 "filters": [
   {
     "field": "adamId",
     "operator": "EQUALS",
     "value": 123456789
   }
 ],
 "pagination": {
   "offset": 0,
   "pageSize": 20
 }
}
```

##### Response

```json
{
 "result": [
   {
     "id": "133fc807-d4d5-4c77-92ae-1d6ffdf0c7dc",
     "adamId": 123456789,
     "name": "AwayFinder - Holiday Season CPP",
     "state": "PUBLISHED",
     "deepLink": "https://apps.apple.com/us/app/my-productivity-app/id123456789?ppid=133fc807-d4d5-4c77-92ae-1d6ffdf0c7dc",
     "creationTime": "2025-04-10T08:00:00.000",
     "modificationTime": "2025-05-01T14:30:00.000"
   },
   {
     "id": "a4b2c3d4-e5f6-7890-abcd-ef1234567890",
     "adamId": 123456789,
     "name": "AwayFinder - Back to School CPP",
     "state": "PUBLISHED",
     "deepLink": "https://apps.apple.com/us/app/my-productivity-app/id123456789?ppid=a4b2c3d4-e5f6-7890-abcd-ef1234567890",
     "creationTime": "2025-07-15T09:00:00.000",
     "modificationTime": "2025-07-20T11:00:00.000"
   }
 ],
 "pagination": {
   "totalCount": 2,
   "offset": 0,
   "pageSize": 20
 }
}
```

## Endpoint

`POST https://api.ads.apple.com/v1/product-pages/query`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Get Product Page by ID](get-product-page-by-id.md)
  Retrieves a specific Product Page (DPP, CPP, or PPO) by its unique UUID.
- [Query Product Page Locale Details](query-product-page-locale-details.md)
  Queries the localized content associated with a custom product page.
- [Query App Locale Details](query-default-product-page-locale-details-by-adam-id.md)
  Return the default product page locale details for an app identified by its adamId.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/query-product-pages)*