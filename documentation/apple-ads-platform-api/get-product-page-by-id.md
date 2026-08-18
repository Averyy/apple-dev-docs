# Get Product Page by ID

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieves a specific Product Page (DPP, CPP, or PPO) by its unique UUID.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint retrieves a single App Store product page (DPP, CPP, or PPO) by its unique UUID. You create and manage product pages in App Store Connect. This endpoint reads the product page state as it appears to the Apple Ads Platform API.

The `state` field is a plain string reflecting the product page’s current distribution status, and it is not a closed enum. The typical value once a page is live is `PUBLISHED`, though App Store Connect may surface other states (such as `READY_FOR_DISTRIBUTION`) before a page finishes propagating.

The `deepLink` field provides the URL used when the product page is set as a creative destination. The response also includes the product page `name`, the associated `adamId` of the app, and `creationTime` / `modificationTime` timestamps.

Keep the following constraints in mind when fetching a product page:

| Constraint | Detail |
| --- | --- |
| UUID format | `productPageId` is a UUID assigned by App Store Connect. It is not an integer. |
| Discovery | Use [`Query Product Pages`](query-product-pages.md) to list all product pages for an app by `adamId` before fetching by ID. |

#### Payload Examples

**Get Product Page**:

##### Request

Retrieves a product page by its unique identifier.

```None
GET https://api.ads.apple.com/v1/product-pages/133fc807-d4d5-4c77-92ae-1d6ffdf0c7dc
```

##### Response

```json
{
 "result": {
   "id": "133fc807-d4d5-4c77-92ae-1d6ffdf0c7dc",
   "adamId": 123456789,
   "name": "AwayFinder - Holiday Season CPP",
   "state": "PUBLISHED",
   "deepLink": "https://apps.apple.com/us/app/my-productivity-app/id123456789?ppid=133fc807-d4d5-4c77-92ae-1d6ffdf0c7dc",
   "creationTime": "2025-04-10T08:00:00.000",
   "modificationTime": "2025-05-01T14:30:00.000"
 }
}
```

**Product Page Not Found**:

##### Request

```None
GET https://api.ads.apple.com/v1/product-pages/00000000-0000-0000-0000-000000000000
```

##### Response

```json
{
 "error": {
   "code": "ENTITY_NOT_FOUND",
   "message": "Product page not found",
   "details": [
     {
       "code": "RESOURCE_NOT_FOUND_ENTITY",
       "message": "Product page not found",
       "info": {
         "field": "productPageId"
       }
     }
   ]
 }
}
```

## Endpoint

`GET https://api.ads.apple.com/v1/product-pages/{productPageId}`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Query Product Pages](query-product-pages.md)
  Queries App Store product pages available to your account.
- [Query Product Page Locale Details](query-product-page-locale-details.md)
  Queries the localized content associated with a custom product page.
- [Query App Locale Details](query-default-product-page-locale-details-by-adam-id.md)
  Return the default product page locale details for an app identified by its adamId.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-product-page-by-id)*