# Movie.Artworks

**Framework**: Apple TV Feed  
**Kind**: dictionary

A mapping of locale to localized artwork.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```swift
object Movie.Artworks
```

## Topics

### Related objects
- [object Movie.Artworks.Artwork](movie/artworks-data.dictionary/artwork-data.dictionary.md)
  The artwork related to this content.

## Properties

- `artwork` (Movie.Artworks.Artwork): The artwork related to this content.
- `locale` (string): The IETF language tag format locale that serves as the key for the map of values. Note: The locale can contain a wildcard; for example, `-au` matches all languages for Australia, and `en-*` matches all countries that have English as a language.

## See Also

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
- [object Movie.Rating](movie/rating-data.dictionary.md)
  Information about a content rating.
- [object Movie.Url](movie/url-data.dictionary.md)
  A mapping of locale to localized URLs for the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/movie/artworks-data.dictionary)*