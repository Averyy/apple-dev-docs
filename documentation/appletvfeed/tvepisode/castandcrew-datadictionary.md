# TvEpisode.CastAndCrew

**Framework**: Apple TV Feed  
**Kind**: dictionary

Information about a cast or crew member, including translations of their name.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```swift
object TvEpisode.CastAndCrew
```

## Topics

### Related objects
- [object TvEpisode.CastAndCrew.Name](tvepisode/castandcrew-data.dictionary/name-data.dictionary.md)
  A mapping of locale to localized names for the cast or crew member.

## Properties

- `birthday` (date): The birth date of the cast or crew member, in YYYY-MM-DD format.
- `character` (string): The name of the character played by a cast member.
- `name` (TvEpisode.CastAndCrew.Name): **(Required)** A mapping of locale to localized names for the cast or crew member.
- `role` (string): The role of the cast or crew member, for example, `Actor` or `Director`.

## See Also

- [object TvEpisode.Artworks](tvepisode/artworks-data.dictionary.md)
  A mapping of locale to localized artwork.
- [object TvEpisode.Description](tvepisode/description-data.dictionary.md)
  A mapping of locale to localized descriptions of the TV episode.
- [object TvEpisode.ExternalContentId](tvepisode/externalcontentid.md)
  Information about an external content ID.
- [object TvEpisode.Genre](tvepisode/genre.md)
  A genre name and its structure.
- [object TvEpisode.Name](tvepisode/name-data.dictionary.md)
  A mapping of locale to localized names for the TV episode.
- [object TvEpisode.Prices](tvepisode/prices-data.dictionary.md)
  A mapping of storefront to pricing information and availability.
- [object TvEpisode.Rating](tvepisode/rating-data.dictionary.md)
  Information about a content rating.
- [object TvEpisode.Url](tvepisode/url-data.dictionary.md)
  A mapping of locale to localized URLs for the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/tvepisode/castandcrew-data.dictionary)*