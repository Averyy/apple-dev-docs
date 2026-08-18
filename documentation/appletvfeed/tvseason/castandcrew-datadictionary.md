# TvSeason.CastAndCrew

**Framework**: Apple TV Feed  
**Kind**: dictionary

Information about a cast or crew member, including translations of their name.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```swift
object TvSeason.CastAndCrew
```

## Topics

### Related objects
- [object TvSeason.CastAndCrew.Name](tvseason/castandcrew-data.dictionary/name-data.dictionary.md)
  A mapping of locale to localized names for the cast or crew member.

## Properties

- `birthday` (date): The birth date of the cast or crew member, in YYYY-MM-DD format.
- `character` (string): The name of the character played by a cast member.
- `name` (TvSeason.CastAndCrew.Name): **(Required)** A mapping of locale to localized names for the cast or crew member.
- `role` (string): The role of the cast or crew member, for example, `Actor` or `Director`.

## See Also

- [object TvSeason.Artworks](tvseason/artworks-data.dictionary.md)
  A mapping of locale to localized artwork.
- [object TvSeason.Description](tvseason/description-data.dictionary.md)
  A mapping of locale to localized descriptions of the TV season.
- [object TvSeason.ExternalContentId](tvseason/externalcontentid.md)
  Information about an external content ID.
- [object TvSeason.Genre](tvseason/genre.md)
  A genre name and its structure.
- [object TvSeason.Name](tvseason/name-data.dictionary.md)
  A mapping of locale to localized names for the TV season.
- [object TvSeason.Prices](tvseason/prices-data.dictionary.md)
  A mapping of storefront to pricing information and availability.
- [object TvSeason.Rating](tvseason/rating-data.dictionary.md)
  Information about a content rating.
- [object TvSeason.Url](tvseason/url-data.dictionary.md)
  A mapping of locale to localized URLs for the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/tvseason/castandcrew-data.dictionary)*