# TvShow.CastAndCrew

**Framework**: Apple TV Feed  
**Kind**: dictionary

Information about a cast or crew member, including translations of their name.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```swift
object TvShow.CastAndCrew
```

## Topics

### Related objects
- [object TvShow.CastAndCrew.Name](tvshow/castandcrew-data.dictionary/name-data.dictionary.md)
  A mapping of locale to localized names for the cast or crew member.

## Properties

- `birthday` (date): The birth date of the cast or crew member, in YYYY-MM-DD format.
- `character` (string): The name of the character played by a cast member.
- `name` (TvShow.CastAndCrew.Name): **(Required)** A mapping of locale to localized names for the cast or crew member.
- `role` (string): The role of the cast or crew member, for example, `Actor` or `Director`.

## See Also

- [object TvShow.Artworks](tvshow/artworks-data.dictionary.md)
  A mapping of locale to localized artwork.
- [object TvShow.Description](tvshow/description-data.dictionary.md)
  A mapping of locale to localized descriptions of the TV show.
- [object TvShow.ExternalContentId](tvshow/externalcontentid.md)
  Information about an external content ID.
- [object TvShow.Genre](tvshow/genre.md)
  A genre name and its structure.
- [object TvShow.Name](tvshow/name-data.dictionary.md)
  A mapping of locale to localized names for the TV show.
- [object TvShow.Prices](tvshow/prices-data.dictionary.md)
  A mapping of storefront to pricing information and availability.
- [object TvShow.Rating](tvshow/rating-data.dictionary.md)
  Information about a content rating.
- [object TvShow.Url](tvshow/url-data.dictionary.md)
  A mapping of locale to localized URLs for the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/tvshow/castandcrew-data.dictionary)*