# VoidResponse

**Framework**: Apple Ads  
**Kind**: dictionary  
**Role**: Object

A default generic null response.

**Availability**:
- Search Ads 2.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Declaration

```
object VoidResponse
```

## Topics

### Objects
- [object VoidResponse.Data](./voidresponse/data-data.dictionary.md)
  A default generic null response that triggers when no data returns.

## Properties

- `data` (VoidResponse.Data): Response data that the API provides.
- `error` (ErrorResponseBody)
- `pagination` (PageDetail)

## See Also

### Error Responses
- [object ApiErrorResponse](./apierrorresponse.md)
  A parent object of the error response body.
- [object ErrorResponseBody](./errorresponsebody.md)
  A parent object of the error response.
- [object ErrorResponseItem](./errorresponseitem.md)
  The error response details in the response body.
- [object IntegerResponse](./integerresponse.md)
  A common integer type response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/voidresponse)*