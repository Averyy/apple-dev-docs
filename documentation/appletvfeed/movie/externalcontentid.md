# Movie.ExternalContentId

**Framework**: Apple TV Feed  
**Kind**: dictionary  
**Role**: Object

Information about an external content ID.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```
object Movie.ExternalContentId
```

## Properties

- `catalogId` (string): **(Required)** The unique identifier for the external catalog. The possible values are `iTunes ADAM ID`, `TMS ID`, `TMDb`, `Gracenote TMS ID`, `atvtp (Apple TV+ ID)`.
- `id` (string): **(Required)** The unique identifier of the content in the specified catalog.

## See Also

### Related objects
- [object Movie.Artworks](./artworks-data.dictionary.md)
  A mapping of locale to localized artwork.
- [object Movie.CastAndCrew](./castandcrew-data.dictionary.md)
  Information about a cast or crew member, including translations of their name.
- [object Movie.Description](./description-data.dictionary.md)
  A mapping of locale to localized descriptions of the movie.
- [object Movie.Genre](./genre.md)
  A genre name and its structure.
- [object Movie.Name](./name-data.dictionary.md)
  A mapping of locale to localized names for the movie.
- [object Movie.OriginalReleaseDate](./originalreleasedate-data.dictionary.md)
  A mapping of locale to localized release date.
- [object Movie.Prices](./prices-data.dictionary.md)
  A mapping of storefront to pricing information and availability.
- [object Movie.Rating](./rating-data.dictionary.md)
  Information about a content rating.
- [object Movie.Url](./url-data.dictionary.md)
  A mapping of locale to localized URLs for the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/movie/externalcontentid)*