# TvShow.ExternalContentId

**Framework**: Apple TV Feed  
**Kind**: dictionary  
**Role**: Object

Information about an external content ID.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```
object TvShow.ExternalContentId
```

## Properties

- `catalogId` (string): **(Required)** The unique identifier for the external catalog. The possible values are `iTunes ADAM ID`, `TMS ID`, `TMDb`, `Gracenote TMS ID`, `atvtp (Apple TV+ ID)`.
- `id` (string): **(Required)** The unique identifier of the content in the specified catalog.

## See Also

### Related objects
- [object TvShow.Artworks](./artworks-data.dictionary.md)
  A mapping of locale to localized artwork.
- [object TvShow.CastAndCrew](./castandcrew-data.dictionary.md)
  Information about a cast or crew member, including translations of their name.
- [object TvShow.Description](./description-data.dictionary.md)
  A mapping of locale to localized descriptions of the TV show.
- [object TvShow.Genre](./genre.md)
  A genre name and its structure.
- [object TvShow.Name](./name-data.dictionary.md)
  A mapping of locale to localized names for the TV show.
- [object TvShow.Prices](./prices-data.dictionary.md)
  A mapping of storefront to pricing information and availability.
- [object TvShow.Rating](./rating-data.dictionary.md)
  Information about a content rating.
- [object TvShow.Url](./url-data.dictionary.md)
  A mapping of locale to localized URLs for the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/tvshow/externalcontentid)*