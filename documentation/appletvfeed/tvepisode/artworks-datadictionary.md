# TvEpisode.Artworks

**Framework**: Apple TV Feed  
**Kind**: dictionary

A mapping of locale to localized artwork.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```swift
object TvEpisode.Artworks
```

## Topics

### Related objects
- [object TvEpisode.Artworks.Artwork](tvepisode/artworks-data.dictionary/artwork-data.dictionary.md)
  The artwork related to this content.

## Properties

- `artwork` (TvEpisode.Artworks.Artwork): The artwork related to this content.
- `locale` (string): The IETF language tag format locale that serves as the key for the map of values. Note: The locale can contain a wildcard; for example, `-au` matches all languages for Australia, and `en-*` matches all countries that have English as a language.

## See Also

- [object TvEpisode.CastAndCrew](tvepisode/castandcrew-data.dictionary.md)
  Information about a cast or crew member, including translations of their name.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/tvepisode/artworks-data.dictionary)*