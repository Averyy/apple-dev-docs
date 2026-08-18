# Response

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Base response wrapper used by all response types.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object Response
```

#### Discussion

`Response` is the base response wrapper used across all response types in the Apple Ads Platform API.

##### Example

```json
{
  "result": {
    "id": "123456789",
    "name": "AwayFinder Campaign"
  }
}
```

## Topics

### Dictionaries
- [object Response.Result](response/result-data.dictionary.md)
  Placeholder for the response payload, whose actual shape depends on each endpoint’s concrete result type.

## Properties

- `result` (Response.Result): The response payload. Type depends on the specific response subtype. See [`Response.Result`](response/result-data.dictionary.md). Absent when the request fails.
- `error` (Error): Error details if the request failed. Absent on success. See [`Error`](error.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/response)*