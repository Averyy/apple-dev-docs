# Movie.Genre

**Framework**: Apple TV Feed  
**Kind**: dictionary  
**Role**: Object

A genre name and its structure.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```
object Movie.Genre
```

## Properties

- `name` (string): The name of the genre.
- `path` ([string]): A list of genres in hierarchical order. Each item in the list is a subgenre of the previous item.

## See Also

### Related objects
- [object Movie.Artworks](./artworks-data.dictionary.md)
  A mapping of locale to localized artwork.
- [object Movie.CastAndCrew](./castandcrew-data.dictionary.md)
  Information about a cast or crew member, including translations of their name.
- [object Movie.Description](./description-data.dictionary.md)
  A mapping of locale to localized descriptions of the movie.
- [object Movie.ExternalContentId](./externalcontentid.md)
  Information about an external content ID.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/movie/genre)*