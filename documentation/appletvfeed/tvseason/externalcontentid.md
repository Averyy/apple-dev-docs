# TvSeason.ExternalContentId

**Framework**: Apple TV Feed  
**Kind**: dictionary  
**Role**: Object

Information about an external content ID.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```
object TvSeason.ExternalContentId
```

## Properties

- `catalogId` (string): **(Required)** The unique identifier for the external catalog. The possible values are `iTunes ADAM ID`, `TMS ID`, `TMDb`, `Gracenote TMS ID`, `atvtp (Apple TV+ ID)`.
- `id` (string): **(Required)** The unique identifier of the content in the specified catalog.

## See Also

### Related objects
- [object TvSeason.Artworks](./artworks-data.dictionary.md)
  A mapping of locale to localized artwork.
- [object TvSeason.CastAndCrew](./castandcrew-data.dictionary.md)
  Information about a cast or crew member, including translations of their name.
- [object TvSeason.Description](./description-data.dictionary.md)
  A mapping of locale to localized descriptions of the TV season.
- [object TvSeason.Genre](./genre.md)
  A genre name and its structure.
- [object TvSeason.Name](./name-data.dictionary.md)
  A mapping of locale to localized names for the TV season.
- [object TvSeason.Prices](./prices-data.dictionary.md)
  A mapping of storefront to pricing information and availability.
- [object TvSeason.Rating](./rating-data.dictionary.md)
  Information about a content rating.
- [object TvSeason.Url](./url-data.dictionary.md)
  A mapping of locale to localized URLs for the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/tvseason/externalcontentid)*