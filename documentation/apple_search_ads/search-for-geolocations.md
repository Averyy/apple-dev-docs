# Search for Geolocations

**Framework**: Apple Search Ads  
**Kind**: httpRequest

Fetches a list of geolocations for targeting.

**Availability**:
- Search Ads 5.0+

#### Discussion

Use this endpoint to obtain App Store locations you can use to refine your target audience. Specify the criteria for a geolocation search using the geotargeting criteria [`CountryCriteria`](countrycriteria.md), [`AdminAreaCriteria`](adminareacriteria.md), and [`LocalityCriteria`](localitycriteria.md), and then apply them to ad groups using [`Create an Ad Group`](create-an-ad-group.md) and [`Update an Ad Group`](update-an-ad-group.md) endpoints.

![A graphic depicting the search for geolocations workflow. First, run a get call for geo locations. Next, specify targeting criteria followed by applying the geo targeting in an ad group.](https://docs-assets.developer.apple.com/published/cfbf26de925c930d1bac7724045eb908/media-4465064%402x.png)

##### Payload Example Search for Geolocations

## See Also

- [Get a List of Geo Locations](get-a-list-of-geo-locations.md)
  Gets geolocation details using a geoidentifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_search_ads/search-for-geolocations)*