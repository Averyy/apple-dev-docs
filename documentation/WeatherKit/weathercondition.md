# WeatherCondition

**Framework**: WeatherKit  
**Kind**: enum

A description of the current weather condition.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
enum WeatherCondition
```

## Topics

### Creating the object
- [init?(rawValue: String)](weathercondition/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Getting visibility properties
- [WeatherCondition.blowingDust](weathercondition/blowingdust.md)
  Blowing dust or sandstorm.
- [WeatherCondition.clear](weathercondition/clear.md)
  Clear.
- [WeatherCondition.cloudy](weathercondition/cloudy.md)
  Cloudy, overcast conditions.
- [WeatherCondition.foggy](weathercondition/foggy.md)
  Fog.
- [WeatherCondition.haze](weathercondition/haze.md)
  Haze.
- [WeatherCondition.mostlyClear](weathercondition/mostlyclear.md)
  Mostly clear.
- [WeatherCondition.mostlyCloudy](weathercondition/mostlycloudy.md)
  Mostly cloudy.
- [WeatherCondition.partlyCloudy](weathercondition/partlycloudy.md)
  Partly cloudy.
- [WeatherCondition.smoky](weathercondition/smoky.md)
  Smoky.
### Getting wind properties
- [WeatherCondition.breezy](weathercondition/breezy.md)
  Breezy, light wind.
- [WeatherCondition.windy](weathercondition/windy.md)
  Windy.
### Getting precipitation properties
- [WeatherCondition.drizzle](weathercondition/drizzle.md)
  Drizzle or light rain.
- [WeatherCondition.heavyRain](weathercondition/heavyrain.md)
  Heavy rain.
- [WeatherCondition.isolatedThunderstorms](weathercondition/isolatedthunderstorms.md)
  Thunderstorms covering less than 1/8 of the forecast area.
- [WeatherCondition.rain](weathercondition/rain.md)
  Rain.
- [WeatherCondition.sunShowers](weathercondition/sunshowers.md)
  Rain with visible sun.
- [WeatherCondition.scatteredThunderstorms](weathercondition/scatteredthunderstorms.md)
  Numerous thunderstorms spread across up to 50% of the forecast area.
- [WeatherCondition.strongStorms](weathercondition/strongstorms.md)
  Notably strong thunderstorms.
- [WeatherCondition.thunderstorms](weathercondition/thunderstorms.md)
  Thunderstorms.
### Getting hazardous properties
- [WeatherCondition.frigid](weathercondition/frigid.md)
  Frigid conditions, low temperatures, or ice crystals.
- [WeatherCondition.hail](weathercondition/hail.md)
  Hail.
- [WeatherCondition.hot](weathercondition/hot.md)
  High temperatures.
### Getting winter precipitation properties
- [WeatherCondition.flurries](weathercondition/flurries.md)
  Flurries or light snow.
- [WeatherCondition.sleet](weathercondition/sleet.md)
  Sleet.
- [WeatherCondition.snow](weathercondition/snow.md)
  Snow.
- [WeatherCondition.sunFlurries](weathercondition/sunflurries.md)
  Snow flurries with visible sun.
- [WeatherCondition.wintryMix](weathercondition/wintrymix.md)
  Wintry mix.
### Getting hazardous winter properties
- [WeatherCondition.blizzard](weathercondition/blizzard.md)
  Blizzard.
- [WeatherCondition.blowingSnow](weathercondition/blowingsnow.md)
  Blowing or drifting snow.
- [WeatherCondition.freezingDrizzle](weathercondition/freezingdrizzle.md)
  Freezing drizzle or light rain.
- [WeatherCondition.freezingRain](weathercondition/freezingrain.md)
  Freezing rain.
- [WeatherCondition.heavySnow](weathercondition/heavysnow.md)
  Heavy snow.
### Getting tropical hazard properties
- [WeatherCondition.hurricane](weathercondition/hurricane.md)
  Hurricane.
- [WeatherCondition.tropicalStorm](weathercondition/tropicalstorm.md)
  Tropical storm.
### Describing the weather condition
- [var accessibilityDescription: String](weathercondition/accessibilitydescription.md)
  A localized accessibility description describing the weather condition.
- [var description: String](weathercondition/description.md)
  A localized string describing the current condition.
### Instance Properties
- [var rawValue: String](weathercondition/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [WeatherCondition.AllCases](weathercondition/allcases-swift.typealias.md)
  A type that can represent a collection of all values of this type.
- [WeatherCondition.RawValue](weathercondition/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static var allCases: [WeatherCondition]](weathercondition/allcases-swift.type.property.md)
  A collection of all values of this type.
### Default Implementations
- [Equatable Implementations](weathercondition/equatable-implementations.md)
- [RawRepresentable Implementations](weathercondition/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum Precipitation](precipitation.md)
  The form of precipitation.
- [enum PressureTrend](pressuretrend.md)
  The atmospheric pressure change over time.
- [struct UVIndex](uvindex.md)
  The expected intensity of ultraviolet radiation from the sun.
- [struct Wind](wind.md)
  Contains wind data of speed, direction, and gust.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weathercondition)*