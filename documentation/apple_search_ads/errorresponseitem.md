# ErrorResponseItem

**Framework**: Apple Search Ads  
**Kind**: dictionary

The error response details in the response body.

**Availability**:
- Search Ads 2.0+

## Declaration

```swift
object ErrorResponseItem
```

#### Discussion

```json
{
   "errors": [
     {
       "messageCode": "404",
       "message": "Not Found: The API can’t locate the resource.",
       "field": "null"
     },
   ...
   ]
}

```

## See Also

- [object ApiErrorResponse](apierrorresponse.md)
  A parent object of the error response body.
- [object ErrorResponseBody](errorresponsebody.md)
  A parent object of the error response.
- [object IntegerResponse](integerresponse.md)
  A common integer type response.
- [object VoidResponse](voidresponse.md)
  A default generic null response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_search_ads/errorresponseitem)*