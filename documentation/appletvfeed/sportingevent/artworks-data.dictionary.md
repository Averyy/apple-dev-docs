# SportingEvent.Artworks

**Framework**: Apple TV Feed  
**Kind**: dictionary  
**Role**: Object

A mapping of locale to localized artwork.

**Availability**:
- AppleTVFeed 1.0+

## Declaration

```
object SportingEvent.Artworks
```

## Topics

### Related objects
- [object SportingEvent.Artworks.Artwork](./artworks-data.dictionary/artwork-data.dictionary.md)
  The artwork related to this content.

## Properties

- `artwork` (SportingEvent.Artworks.Artwork): The artwork related to this content.
- `locale` (string): The IETF language tag format locale that serves as the key for the map of values.

  Note: The locale can contain a wildcard; for example, `-au` matches all languages for Australia, and `en-*` matches all countries that have English as a language.

## See Also

### Related objects
- [object SportingEvent.CastAndCrew](./castandcrew-data.dictionary.md)
  Information about a cast or crew member, including translations of their name.
- [object SportingEvent.Competitor](./competitor.md)
  Information about a competitor.
- [object SportingEvent.Description](./description-data.dictionary.md)
  A mapping of locale to localized descriptions of the sporting event.
- [object SportingEvent.ExternalContentId](./externalcontentid.md)
  Information about an external content ID.
- [object SportingEvent.LeagueAbbreviation](./leagueabbreviation-data.dictionary.md)
  A mapping of locale to localized abbreviations for the league of the sporting event.
- [object SportingEvent.LeagueName](./leaguename-data.dictionary.md)
  A mapping of locale to localized names for the league of the sporting event.
- [object SportingEvent.Name](./name-data.dictionary.md)
  A mapping of locale to localized names for the sporting event.
- [object SportingEvent.Prices](./prices-data.dictionary.md)
  A mapping of storefront to pricing information and availability.
- [object SportingEvent.Rating](./rating-data.dictionary.md)
  Information about a content rating.
- [object SportingEvent.ShortName](./shortname-data.dictionary.md)
  A mapping of locale to localized short versions of the sporting event name.
- [object SportingEvent.SportName](./sportname-data.dictionary.md)
  A mapping of locale to localized names for the sport of the event.
- [object SportingEvent.Url](./url-data.dictionary.md)
  A mapping of locale to localized URLs for the content.
- [object SportingEvent.VenueAddress](./venueaddress-data.dictionary.md)
  A mapping of locale to localized addresses for the event venue.
- [object SportingEvent.VenueName](./venuename-data.dictionary.md)
  A mapping of locale to localized names for the event venue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appletvfeed/sportingevent/artworks-data.dictionary)*