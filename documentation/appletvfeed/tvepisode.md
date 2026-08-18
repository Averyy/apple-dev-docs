# TvEpisode

**Framework**: Apple TV Feed  
**Kind**: dictionary

The data structure that represents a TV episode resource.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```swift
object TvEpisode
```

## Topics

### Related objects
- [object TvEpisode.Artworks](tvepisode/artworks-data.dictionary.md)
  A mapping of locale to localized artwork.
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

## Properties

- `artworks` (TvEpisode.Artworks): **(Required)** A mapping of locale to localized artwork.
- `castAndCrew` ([TvEpisode.CastAndCrew]): **(Required)** A list of cast and crew for the TV episode.
- `description` (TvEpisode.Description): **(Required)** A mapping of locale to localized descriptions of the TV episode.
- `durationInMillis` (int64): The length of the episode in milliseconds.
- `episodeNumber` (integer): The sequence number of the TV episode in the TV season it belongs to.
- `externalContentIds` ([TvEpisode.ExternalContentId]): **(Required)** A list of unique identifiers for the TV episode in the catalog of another provider.
- `genres` ([TvEpisode.Genre]): **(Required)** A list of genres associated with the TV episode.
- `id` (string): **(Required)** The unique identifier for the TV episode.
- `lastModifiedTime` (date-time): The time, in ISO 8601 format, of the entity’s most recent update.
- `name` (TvEpisode.Name): **(Required)** A mapping of locale to localized names for the TV episode.
- `originalAirDate` (string): The date when the episode first aired in YYYY-MM-DD format.
- `prices` (TvEpisode.Prices): **(Required)** A mapping of storefront to pricing information and availability.
- `rating` ([TvEpisode.Rating]): **(Required)** A list of ratings for the TV episode in different rating systems.
- `seasonId` (string): The unique identifier for the TV season that the episode belongs to.
- `seasonNumber` (integer): The sequence number of the TV season.
- `showId` (string): The unique identifier for the TV show that the episode belongs to.
- `url` (TvEpisode.Url): **(Required)** A mapping of two-letter country code to URLs for the TV episode.

## See Also

- [object Movie](movie.md)
  The data structure that represents a movie resource.
- [object TvSeason](tvseason.md)
  The data structure that represents a TV season resource.
- [object TvShow](tvshow.md)
  The data structure that represents a TV show resource.
- [object SportingEvent](sportingevent.md)
  The data structure that represents a sporting event resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/tvepisode)*