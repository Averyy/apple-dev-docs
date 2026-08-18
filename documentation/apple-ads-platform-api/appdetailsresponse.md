# AppDetailsResponse

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The response object for a get app details operation.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AppDetailsResponse
```

#### Discussion

The [`Get App Details by Adam ID`](get-app-details-by-adam-id.md) endpoint returns `AppDetailsResponse` as a single-item envelope. It follows the standard `Response` pattern used across the Apple Ads Platform API: on success, `result` contains the retrieved `AppDetails` object. On failure, `result` is absent and `error` contains the structured error details.

Unlike paginated query responses, `AppDetailsResponse` returns exactly one app record (or none). Because the API accepts a single Adam ID in the path, there is no ambiguity about which app the result belongs to, and the response includes no pagination metadata.

##### Understand the Result Field

On a 404, the response contains an `ENTITY_NOT_FOUND` error in the `error` field and `result` is absent. Always check the HTTP status code first, then inspect `error` for machine-readable detail.

The returned `AppDetails` object includes App Store metadata such as app name, developer, supported device classes, and available App Store countries or regions. `GET /v1/apps/{adamId}` accepts only the `adamId` path parameter and the `X-Ap-Context` header.

##### Understand the Error Field

Inspect `error.details` for a structured list of error codes and messages. Common failure cases include:

- **400**: malformed Adam ID or unsupported query parameter
- **401**: missing or expired OAuth token
- **403**: the authenticated account does not have access to the requested app
- **404**: no app exists for the supplied Adam ID
- **429**: rate limit exceeded. Use exponential backoff before retrying
- **500**: transient server error. The request may succeed on retry

##### Understand the Relationship to Appdetails

`AppDetailsResponse` is a thin wrapper. All substantive app metadata lives in the `AppDetails` object inside `result`. The wrapper exists to provide a uniform envelope that carries both success data and error information in a single response shape, consistent with every other API response object in this documentation.

##### Example

```json
{
  "result": {
    "id": "324684580",
    "appName": "AwayFinder - Travel Planner",
    "artistName": "AwayFinder Inc.",
    "primaryLanguage": "en-US",
    "primaryGenre": "Travel",
    "secondaryGenre": "Productivity",
    "deviceClasses": [
      "IPHONE",
      "IPAD"
    ],
    "iconPictureUrl": "https://is5-ssl.mzstatic.com/image/thumb/Purple126/v4/aa/bb/cc/AppIcon-1024x1024.png",
    "isPreorder": false,
    "availableStorefronts": [
      "US",
      "GB",
      "DE",
      "JP",
      "AU"
    ]
  }
}
```

## Properties

- `result` (AppDetails): On success, contains the `AppDetails` for the requested app. Absent when the app is not found or an error occurred. See [`AppDetails`](appdetails.md) for details. Read-only.
- `error` (Error): Populated only when the request fails. Absent on success. See [`Error`](error.md) for details. Read-only.

## See Also

- [object EligibilityQueryRequest](eligibilityqueryrequest.md)
  The request body for querying app eligibility.
- [object EligibilityQueryResponse](eligibilityqueryresponse.md)
  The paginated response object for an app eligibility query.
- [object RejectionReasonResponse](rejectionreasonresponse.md)
  The response object for a rejection reason operation.
- [object AppDetails](appdetails.md)
  Application details and metadata.
- [object EligibilityResponse](eligibilityresponse.md)
  The response object describing an app’s eligibility for a specific supply placement, supply source, country or region, and device class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/appdetailsresponse)*