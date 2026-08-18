# SportingEvent

**Framework**: Apple TV Feed  
**Kind**: dictionary

The data structure that represents a sporting event resource.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```swift
object SportingEvent
```

## Topics

### Related objects
- [object SportingEvent.Artworks](sportingevent/artworks-data.dictionary.md)
  A mapping of locale to localized artwork.
- [object SportingEvent.CastAndCrew](sportingevent/castandcrew-data.dictionary.md)
  Information about a cast or crew member, including translations of their name.
- [object SportingEvent.Competitor](sportingevent/competitor.md)
  Information about a competitor.
- [object SportingEvent.Description](sportingevent/description-data.dictionary.md)
  A mapping of locale to localized descriptions of the sporting event.
- [object SportingEvent.ExternalContentId](sportingevent/externalcontentid.md)
  Information about an external content ID.
- [object SportingEvent.LeagueAbbreviation](sportingevent/leagueabbreviation-data.dictionary.md)
  A mapping of locale to localized abbreviations for the league of the sporting event.
- [object SportingEvent.LeagueName](sportingevent/leaguename-data.dictionary.md)
  A mapping of locale to localized names for the league of the sporting event.
- [object SportingEvent.Name](sportingevent/name-data.dictionary.md)
  A mapping of locale to localized names for the sporting event.
- [object SportingEvent.Prices](sportingevent/prices-data.dictionary.md)
  A mapping of storefront to pricing information and availability.
- [object SportingEvent.Rating](sportingevent/rating-data.dictionary.md)
  Information about a content rating.
- [object SportingEvent.ShortName](sportingevent/shortname-data.dictionary.md)
  A mapping of locale to localized short versions of the sporting event name.
- [object SportingEvent.SportName](sportingevent/sportname-data.dictionary.md)
  A mapping of locale to localized names for the sport of the event.
- [object SportingEvent.Url](sportingevent/url-data.dictionary.md)
  A mapping of locale to localized URLs for the content.
- [object SportingEvent.VenueAddress](sportingevent/venueaddress-data.dictionary.md)
  A mapping of locale to localized addresses for the event venue.
- [object SportingEvent.VenueName](sportingevent/venuename-data.dictionary.md)
  A mapping of locale to localized names for the event venue.

## Properties

- `artworks` (SportingEvent.Artworks): **(Required)** A mapping of locale to localized artwork.
- `castAndCrew` ([SportingEvent.CastAndCrew]): **(Required)** A list of cast and crew for the event.
- `competitors` ([SportingEvent.Competitor]): **(Required)** A list of competitors in the event.
- `description` (SportingEvent.Description): **(Required)** A mapping of locale to localized descriptions of the event.
- `endTime` (date-time): The time, in ISO 8601 format, when the event ended.
- `externalContentIds` ([SportingEvent.ExternalContentId]): **(Required)** A list of unique identifiers for the sporting event in the catalog of another provider.
- `id` (string): **(Required)** The unique identifier for the sporting event.
- `lastModifiedTime` (date-time): The time, in ISO 8601 format, of the entity’s most recent update.
- `leagueAbbreviation` (SportingEvent.LeagueAbbreviation): A mapping of locale to localized abbreviations for the league of the event.
- `leagueName` (SportingEvent.LeagueName): A mapping of locale to localized names for the league of the event.
- `name` (SportingEvent.Name): **(Required)** A mapping of locale to localized names for the event.
- `prices` (SportingEvent.Prices): **(Required)** A mapping of storefront to pricing information and availability.
- `rating` ([SportingEvent.Rating]): **(Required)** A list of ratings for the event in different rating systems.
- `shortName` (SportingEvent.ShortName): A mapping of locale to localized short versions of the event name.
- `sportName` (SportingEvent.SportName): A mapping of locale to localized names for the sport of the event.
- `startTime` (date-time): The time, in ISO 8601 format, when the event started.
- `url` (SportingEvent.Url): **(Required)** A mapping of two-letter country code to URLs for the event.
- `venueAddress` (SportingEvent.VenueAddress): A mapping of locale to localized addresses for the event venue.
- `venueName` (SportingEvent.VenueName): A mapping of locale to localized names for the event venue.

## See Also

- [object Movie](movie.md)
  The data structure that represents a movie resource.
- [object TvEpisode](tvepisode.md)
  The data structure that represents a TV episode resource.
- [object TvSeason](tvseason.md)
  The data structure that represents a TV season resource.
- [object TvShow](tvshow.md)
  The data structure that represents a TV show resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/sportingevent)*