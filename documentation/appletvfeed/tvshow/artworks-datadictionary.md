# TvShow.Artworks

**Framework**: Apple TV Feed  
**Kind**: dictionary

A mapping of locale to localized artwork.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```swift
object TvShow.Artworks
```

## Topics

### Related objects
- [object TvShow.Artworks.Artwork](tvshow/artworks-data.dictionary/artwork-data.dictionary.md)
  The artwork related to this content.

## Properties

- `artwork` (TvShow.Artworks.Artwork): The artwork related to this content.
- `locale` (string): The IETF language tag format locale that serves as the key for the map of values. Note: The locale can contain a wildcard; for example, `-au` matches all languages for Australia, and `en-*` matches all countries that have English as a language.

## See Also

- [object TvShow.CastAndCrew](tvshow/castandcrew-data.dictionary.md)
  Information about a cast or crew member, including translations of their name.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/tvshow/artworks-data.dictionary)*