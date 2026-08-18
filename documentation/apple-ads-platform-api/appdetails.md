# AppDetails

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

Application details and metadata.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AppDetails
```

#### Discussion

`AppDetails` represents the App Store metadata for an app retrieved via [`Get App Details by Adam ID`](get-app-details-by-adam-id.md). The `id` field is the Adam ID, which is the same value used as `promotedObjectId` when targeting this app.

Use `deviceClasses` to verify that your campaign’s device-class targeting is compatible with the app before launching. Targeting an App Store country or region not in `availableStorefronts` will result in no impressions for that market.

##### Example

```json
{
  "id": "324684580",
  "appName": "AwayFinder - Travel Planner",
  "artistName": "AwayFinder Inc.",
  "primaryLanguage": "en-US",
  "primaryGenre": ">Mobile Software Applications>Travel",
  "secondaryGenre": ">Mobile Software Applications>Lifestyle",
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
```

## Properties

- `id` (string): App identifier (Adam ID). Read-only.
- `appName` (string): Application display name.
- `artistName` (string): Developer or company name.
- `primaryLanguage` (string): Primary language of the app (BCP-47 code, e.g., `"en-US"`).
- `primaryGenre` (string): The primary App Store genre category (e.g., `">Mobile Software Applications>Music"`).
- `secondaryGenre` (string): The secondary App Store genre category, if assigned.
- `deviceClasses` ([string]): Device families supported by the app. Possible values: `IPHONE`, `IPAD`.
- `iconPictureUrl` (uri): URL of the app’s icon image.
- `isPreorder` (boolean): Whether the app is currently available as a pre-order.
- `availableStorefronts` ([string]): List of ISO 3166-1 alpha-2 country codes where the app is available.

## See Also

- [object EligibilityQueryRequest](eligibilityqueryrequest.md)
  The request body for querying app eligibility.
- [object EligibilityQueryResponse](eligibilityqueryresponse.md)
  The paginated response object for an app eligibility query.
- [object RejectionReasonResponse](rejectionreasonresponse.md)
  The response object for a rejection reason operation.
- [object AppDetailsResponse](appdetailsresponse.md)
  The response object for a get app details operation.
- [object EligibilityResponse](eligibilityresponse.md)
  The response object describing an app’s eligibility for a specific supply placement, supply source, country or region, and device class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/appdetails)*