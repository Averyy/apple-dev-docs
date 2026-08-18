# TvShow.Rating

**Framework**: Apple TV Feed  
**Kind**: dictionary

Information about a content rating.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```swift
object TvShow.Rating
```

#### Overview

You can download a full list of rating systems and their ratings codes from the UMC Catalog Data Interface Specification at [`Content Advisories and Ratings`](https://developer.apple.comhttps://developer.apple.com/documentation/applemusicapi/get_a_catalog_resource_by_id).

## Properties

- `rating` (string): The rating of the content in the specified rating system, for example, `PG` or `TV-MA`.
- `systemCode` (string): The code for the rating system, for example, `MPAA` or `US-TV`.

## See Also

- [object TvShow.Artworks](tvshow/artworks-data.dictionary.md)
  A mapping of locale to localized artwork.
- [object TvShow.CastAndCrew](tvshow/castandcrew-data.dictionary.md)
  Information about a cast or crew member, including translations of their name.
- [object TvShow.Description](tvshow/description-data.dictionary.md)
  A mapping of locale to localized descriptions of the TV show.
- [object TvShow.ExternalContentId](tvshow/externalcontentid.md)
  Information about an external content ID.
- [object TvShow.Genre](tvshow/genre.md)
  A genre name and its structure.
- [object TvShow.Name](tvshow/name-data.dictionary.md)
  A mapping of locale to localized names for the TV show.
- [object TvShow.Prices](tvshow/prices-data.dictionary.md)
  A mapping of storefront to pricing information and availability.
- [object TvShow.Url](tvshow/url-data.dictionary.md)
  A mapping of locale to localized URLs for the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/tvshow/rating-data.dictionary)*