# Movie.Rating

**Framework**: Apple TV Feed  
**Kind**: dictionary

Information about a content rating.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```swift
object Movie.Rating
```

#### Overview

You can download a full list of rating systems and their ratings codes from the UMC Catalog Data Interface Specification at [`Content Advisories and Ratings`](https://developer.apple.comhttps://developer.apple.com/documentation/applemusicapi/get_a_catalog_resource_by_id).

## Properties

- `rating` (string): The rating of the content in the specified rating system, for example, `PG` or `TV-MA`.
- `systemCode` (string): The code for the rating system, for example, `MPAA` or `US-TV`.

## See Also

- [object Movie.Artworks](movie/artworks-data.dictionary.md)
  A mapping of locale to localized artwork.
- [object Movie.CastAndCrew](movie/castandcrew-data.dictionary.md)
  Information about a cast or crew member, including translations of their name.
- [object Movie.Description](movie/description-data.dictionary.md)
  A mapping of locale to localized descriptions of the movie.
- [object Movie.ExternalContentId](movie/externalcontentid.md)
  Information about an external content ID.
- [object Movie.Genre](movie/genre.md)
  A genre name and its structure.
- [object Movie.Name](movie/name-data.dictionary.md)
  A mapping of locale to localized names for the movie.
- [object Movie.OriginalReleaseDate](movie/originalreleasedate-data.dictionary.md)
  A mapping of locale to localized release date.
- [object Movie.Prices](movie/prices-data.dictionary.md)
  A mapping of storefront to pricing information and availability.
- [object Movie.Url](movie/url-data.dictionary.md)
  A mapping of locale to localized URLs for the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/movie/rating-data.dictionary)*