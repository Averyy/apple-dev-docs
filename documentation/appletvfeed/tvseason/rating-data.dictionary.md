# TvSeason.Rating

**Framework**: Apple TV Feed  
**Kind**: dictionary  
**Role**: Object

Information about a content rating.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```
object TvSeason.Rating
```

#### Overview

You can download a full list of rating systems and their ratings codes from the UMC Catalog Data Interface Specification at [Content Advisories and Ratings](../../AppleMusicAPI/get_a_catalog_resource_by_id.md).

## Properties

- `rating` (string): The rating of the content in the specified rating system, for example, `PG` or `TV-MA`.
- `systemCode` (string): The code for the rating system, for example, `MPAA` or `US-TV`.

## See Also

### Related objects
- [object TvSeason.Artworks](./artworks-data.dictionary.md)
  A mapping of locale to localized artwork.
- [object TvSeason.CastAndCrew](./castandcrew-data.dictionary.md)
  Information about a cast or crew member, including translations of their name.
- [object TvSeason.Description](./description-data.dictionary.md)
  A mapping of locale to localized descriptions of the TV season.
- [object TvSeason.ExternalContentId](./externalcontentid.md)
  Information about an external content ID.
- [object TvSeason.Genre](./genre.md)
  A genre name and its structure.
- [object TvSeason.Name](./name-data.dictionary.md)
  A mapping of locale to localized names for the TV season.
- [object TvSeason.Prices](./prices-data.dictionary.md)
  A mapping of storefront to pricing information and availability.
- [object TvSeason.Url](./url-data.dictionary.md)
  A mapping of locale to localized URLs for the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/tvseason/rating-data.dictionary)*