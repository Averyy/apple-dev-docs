# Movie.CastAndCrew

**Framework**: Apple TV Feed  
**Kind**: dictionary

Information about a cast or crew member, including translations of their name.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```swift
object Movie.CastAndCrew
```

## Topics

### Related objects
- [object Movie.CastAndCrew.Name](movie/castandcrew-data.dictionary/name-data.dictionary.md)
  A mapping of locale to localized names for the cast or crew member.

## Properties

- `birthday` (date): The birth date of the cast or crew member, in YYYY-MM-DD format.
- `character` (string): The name of the character played by a cast member.
- `name` (Movie.CastAndCrew.Name): **(Required)** A mapping of locale to localized names for the cast or crew member.
- `role` (string): The role of the cast or crew member, for example, `Actor` or `Director`.

## See Also

- [object Movie.Artworks](movie/artworks-data.dictionary.md)
  A mapping of locale to localized artwork.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/movie/castandcrew-data.dictionary)*