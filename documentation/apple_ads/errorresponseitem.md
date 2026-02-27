# ErrorResponseItem

**Framework**: Apple Ads  
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

## Properties

- `field` (string): The details regarding an error.
- `message` (string): A nonlocalized (U.S. English only) user-friendly string that describes the error.
- `messageCode` (string): A system-assigned error code.

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

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/errorresponseitem)*