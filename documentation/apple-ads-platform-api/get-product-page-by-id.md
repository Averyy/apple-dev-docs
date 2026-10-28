# Get Product Page by ID

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Retrieves a specific Custom Product Page (CPP) by its unique UUID.

**Availability**:
- Apple Ads Platform API 1.0+

## Discussion

This endpoint retrieves a single App Store Custom Product Page (CPP) by its unique UUID. You create and manage product pages in App Store Connect. This endpoint reads the product page state as it appears to the Apple Ads Platform API.

The `state` field is `VISIBLE` for an available page or `HIDDEN` for a hidden page.

The `deepLink` field can use a custom URL scheme, and it is an empty string when the product page has no deep link configured. The response also includes the product page `name`, the associated `adamId` of the app, and `creationTime` and `modificationTime` timestamps.

Keep the following constraints in mind when fetching a product page:

| Constraint | Detail |
| --- | --- |
| X-AP-Context header | Required. Send `X-AP-Context: adAccountId=<id>`. Without it, the API returns `403 Forbidden`. |
| UUID format | `productPageId` is a UUID assigned by App Store Connect. It is not an integer. |
| Discovery | Use [`Query Product Pages`](./query-product-pages.md) to list all product pages for an app by `adamId` before fetching by ID. |

## Payload Examples

**Get Product Page**:

### Request

Retrieves a product page by its unique identifier.

```
GET /v1/product-pages/{productPageId}
```

### Response

```json
{
 "result": {
   "id": "133fc807-d4d5-4c77-92ae-1d6ffdf0c7dc",
   "adamId": 123456789,
   "name": "AwayFinder - Holiday Season CPP",
   "state": "VISIBLE",
   "deepLink": "https://apps.apple.com/us/app/awayfinder/id123456789?ppid=133fc807-d4d5-4c77-92ae-1d6ffdf0c7dc",
   "creationTime": "2025-04-10T08:00:00.000",
   "modificationTime": "2025-05-01T14:30:00.000"
 }
}
```

**Product Page Not Found**:

### Request

```
GET /v1/product-pages/{productPageId}
```

### Response

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

### Path Parameters

- `productPageId` (string) *(required)*

### Header Parameters

- `X-AP-Context` (string) *(required)*

## Responses

- `200` OK (`ProductPageDetailsResponse`, `application/json`)
- `400` Bad Request (`Error`, `application/json`)
- `401` Unauthorized (`Error`, `application/json`)
- `403` Forbidden (`Error`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` Too Many Requests (`Error`, `application/json`)
- `500` Internal Server Error (`Error`, `application/json`)

## See Also

- [Query Product Pages](./query-product-pages.md)
  Queries App Store product pages available to your account.
- [Query Product Page Locale Details](./query-product-page-locale-details.md)
  Queries the localized content of custom product pages (CPPs).
- [Query App Locale Details](./query-default-product-page-locale-details-by-adam-id.md)
  Returns the default product page locale details for an app identified by its adamId.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-product-page-by-id)*