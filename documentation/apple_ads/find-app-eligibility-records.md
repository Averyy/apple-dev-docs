# Find App Eligibility Records

**Framework**: Apple Ads  
**Kind**: httpRequest

Fetches app eligibility records by adam ID.

**Availability**:
- Search Ads 5.0+

## Mentions

- [Apple Ads Campaign Management API 4](apple-search-ads-campaign-management-api-4.md)

#### Discussion

Use this endpoint to determine whether an app is eligible to promote in a campaign. Use a [`Selector`](selector.md) [`Condition`](condition.md) to search for a specific country or region, [`DeviceClass`](deviceclass.md), [`AgeCriteria`](agecriteria.md), or [`SupplySource`](supplysource.md).  See the [`EligibilityRecord`](eligibilityrecord.md) object for parameter descriptions and selector condition operators.

##### Payload Example Find App Eligibility Records

**Request**:

```None
POST https://api.searchads.apple.com/api/v5/apps/<adamId>/eligibilities/find

{
    "conditions": [
        {
            "field": "countryOrRegion",
            "operator": "IN",
            "values": ["US", "MX"]
        },
        {
            "field": "supplySource",
            "operator": "EQUALS",
            "values": ["APPSTORE_TODAY_TAB"]
        }
    ],
    "pagination": {
        "offset": 0,
        "limit": 2
    }
}
```

**Response**:

```json
{
    "data": [
        {
            "adamId": 123456789,
            "deviceClass": "IPHONE",
            "state": "ELIGIBLE",
            "minAge": 18,
            "countryOrRegion": "US",
            "supplySource": "APPSTORE_TODAY_TAB"
        },
        {
            "adamId": 123456789,
            "deviceClass": "IPAD",
            "state": "INELIGIBLE",
            "minAge": 18,
            "countryOrRegion": "US",
            "supplySource": "APPSTORE_TODAY_TAB"
        }
    ],
    "pagination": {
        "totalResults": 4,
        "startIndex": 0,
        "itemsPerPage": 2
    }
}
```

## Endpoint

`POST https://api.searchads.apple.com/api/v5/apps/{adamId}/eligibilities/find`

## Parameters

- `adamId` (string) *(required)*: A unique App Store app identifier.

## Request Body

The request body that includes the selector [`Condition`](condition.md). [`Selector`](selector.md) objects define what data the API returns when fetching resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/find-app-eligibility-records)*