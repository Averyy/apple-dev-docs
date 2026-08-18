# Get App Details by Adam ID

**Framework**: Apple Ads Platform API  
**Kind**: httpRequest

Retrieve application details for a specific Adam ID.

**Availability**:
- apple-ads-platform-api 1.0+

#### Discussion

This endpoint retrieves the full details of a specific app by its Adam identifier, including its name, genre, and supported device classes.

Obtain the app’s Adam ID from a search or from existing campaign targeting data before calling this endpoint. The endpoint returns a single `AppDetails` object in the `result` field, or a `null` result with an `ENTITY_NOT_FOUND` error if no app matches the supplied Adam ID.

Use the returned `deviceClasses` and `availableStorefronts` values to confirm that an app’s supported devices and countries or regions align with a campaign’s targeting settings before creating an ad group.

#### Payload Examples

##### Request

Retrieves the full details of a specific app by its Adam identifier, including its name, genre, and supported device classes.

```None
GET https://api.ads.apple.com/v1/apps/324684580
```

##### Response

```json
{
 "result": {
   "id": "324684580",
   "appName": "My Productivity App",
   "artistName": "My Developer",
   "primaryLanguage": "en-US",
   "primaryGenre": "Productivity",
   "secondaryGenre": "Travel",
   "deviceClasses": [
     "IPHONE",
     "IPAD"
   ],
   "iconPictureUrl": "https://is1-ssl.mzstatic.com/image/thumb/Purple/v4/example.jpg",
   "isPreorder": false,
   "availableStorefronts": [
     "US",
     "GB",
     "CA"
   ]
 }
}
```

## Endpoint

`GET https://api.ads.apple.com/v1/apps/{adamId}`

## Parameters

- `X-Ap-Context` (string) *(required)*

## See Also

- [Search for Apps](searches-for-a-list-of-apps.md)
  Search the App Store for apps matching the supplied criteria and return app details.
- [Query Supported App Languages](query-supported-app-languages.md)
  Query countries and regions to discover the ad-supported languages available in each market.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/get-app-details-by-adam-id)*