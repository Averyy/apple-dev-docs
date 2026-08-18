# TvEpisode.Rating

**Framework**: Apple TV Feed  
**Kind**: dictionary

Information about a content rating.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```swift
object TvEpisode.Rating
```

#### Overview

You can download a full list of rating systems and their ratings codes from the UMC Catalog Data Interface Specification at [`Content Advisories and Ratings`](https://developer.apple.comhttps://developer.apple.com/documentation/applemusicapi/get_a_catalog_resource_by_id).

## Properties

- `rating` (string): The rating of the content in the specified rating system, for example, `PG` or `TV-MA`.
- `systemCode` (string): The code for the rating system, for example, `MPAA` or `US-TV`.

## See Also

- [object TvEpisode.Artworks](tvepisode/artworks-data.dictionary.md)
  A mapping of locale to localized artwork.
- [object TvEpisode.CastAndCrew](tvepisode/castandcrew-data.dictionary.md)
  Information about a cast or crew member, including translations of their name.
- [object TvEpisode.Description](tvepisode/description-data.dictionary.md)
  A mapping of locale to localized descriptions of the TV episode.
- [object TvEpisode.ExternalContentId](tvepisode/externalcontentid.md)
  Information about an external content ID.
- [object TvEpisode.Genre](tvepisode/genre.md)
  A genre name and its structure.
- [object TvEpisode.Name](tvepisode/name-data.dictionary.md)
  A mapping of locale to localized names for the TV episode.
- [object TvEpisode.Prices](tvepisode/prices-data.dictionary.md)
  A mapping of storefront to pricing information and availability.
- [object TvEpisode.Url](tvepisode/url-data.dictionary.md)
  A mapping of locale to localized URLs for the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/tvepisode/rating-data.dictionary)*