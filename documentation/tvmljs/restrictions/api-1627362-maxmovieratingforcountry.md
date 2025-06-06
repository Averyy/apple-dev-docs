# maxMovieRatingForCountry

**Framework**: TVMLKit JS  
**Kind**: instm

The maximum movie rating allowed for the specified country or region.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
String maxMovieRatingForCountry(
    in String countryCode
);
```

#### Return_value

A string representing the maximum allowed rating for a movie in the specified country or region; for example, PG-13.

## Parameters

- `countryCode`: An object containing the valid country code. If the code is invalid, the current country or region based on location is used.

## See Also

- [allowsExplicit](restrictions/1627425-allowsexplicit.md)
  A boolean value that indicates whether any explicit media is allowed.
- [maxMovieRank](restrictions/1627305-maxmovierank.md)
  The maximum allowed ranking for a movie.
- [maxTVShowRank](restrictions/1627434-maxtvshowrank.md)
  The maximum allowed ranking for a television show.
- [maxTVShowRatingForCountry](restrictions/1627442-maxtvshowratingforcountry.md)
  The maximum television show rating allowed for the specified country or region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/restrictions/1627362-maxmovieratingforcountry)*