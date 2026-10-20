# TvShow.Genre

**Framework**: Apple TV Feed  
**Kind**: dictionary  
**Role**: Object

A genre name and its structure.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```
object TvShow.Genre
```

## Properties

- `name` (string): The name of the genre.
- `path` ([string]): A list of genres in hierarchical order. Each item in the list is a subgenre of the previous item.

## See Also

### Related objects
- [object TvShow.Artworks](./artworks-data.dictionary.md)
  A mapping of locale to localized artwork.
- [object TvShow.CastAndCrew](./castandcrew-data.dictionary.md)
  Information about a cast or crew member, including translations of their name.
- [object TvShow.Description](./description-data.dictionary.md)
  A mapping of locale to localized descriptions of the TV show.
- [object TvShow.ExternalContentId](./externalcontentid.md)
  Information about an external content ID.
- [object TvShow.Name](./name-data.dictionary.md)
  A mapping of locale to localized names for the TV show.
- [object TvShow.Prices](./prices-data.dictionary.md)
  A mapping of storefront to pricing information and availability.
- [object TvShow.Rating](./rating-data.dictionary.md)
  Information about a content rating.
- [object TvShow.Url](./url-data.dictionary.md)
  A mapping of locale to localized URLs for the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/tvshow/genre)*