# Movie.Description

**Framework**: Apple TV Feed  
**Kind**: dictionary  
**Role**: Object

A mapping of locale to localized descriptions of the movie.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```
object Movie.Description
```

## Properties

- `locale` (string): The IETF language tag format locale that serves as the key for the map of values.
- `short` (string): The short-form localized description of the content.
- `standard` (string): The full localized description of the content.

## See Also

### Related objects
- [object Movie.Artworks](./artworks-data.dictionary.md)
  A mapping of locale to localized artwork.
- [object Movie.CastAndCrew](./castandcrew-data.dictionary.md)
  Information about a cast or crew member, including translations of their name.
- [object Movie.ExternalContentId](./externalcontentid.md)
  Information about an external content ID.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/movie/description-data.dictionary)*