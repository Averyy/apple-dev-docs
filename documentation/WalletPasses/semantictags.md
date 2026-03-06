# SemanticTags

**Framework**: Wallet Passes  
**Kind**: dictionary

An object that contains machine-readable metadata the system uses to offer a pass and suggest related actions.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- watchOS 5.0+

## Declaration

```swift
object SemanticTags
```

## Mentions

- [Creating an airline boarding pass using semantic tags](creating-an-airline-boarding-pass-using-semantic-tags.md)
- [Creating a poster event pass using semantic tags](creating-an-event-pass-using-semantic-tags.md)
- [Supporting semantic tags in Wallet passes](supporting-semantic-tags-in-wallet-passes.md)

## Properties

- `additionalTicketAttributes` (localizable string): Additional ticket attributes that other tags or keys in the pass don’t include. Use this key for any type of event ticket.
- `admissionLevel` (localizable string): The level of admission the ticket provides, such as `general admission`, `VIP`, and so forth. Use this key for any type of event ticket.
- `admissionLevelAbbreviation` (localizable string): An abbreviation of the level of admission the ticket provides, such as `GA` or `VIP`. Use this key for any type of event ticket.
- `airlineCode` (localizable string): The IATA airline code, such as `EX` for `flightCode` `EX123`. Use this key only for airline boarding passes.
- `albumIDs` ([localizable string]): An array of the Apple Music persistent ID for each album corresponding to the event, in decreasing order of significance. Use this key for any type of event ticket.
- `artistIDs` ([localizable string]): An array of the Apple Music persistent ID for each artist performing at the event, in decreasing order of significance. Use this key for any type of event ticket.
- `attendeeName` (localizable string): The name of the person the ticket grants admission to. Use this key for any type of event ticket.
- `awayTeamAbbreviation` (localizable string): The unique abbreviation of the away team’s name. Use this key only for a sports event ticket.
- `awayTeamLocation` (localizable string): The home location of the away team. Use this key only for a sports event ticket.
- `awayTeamName` (localizable string): The name of the away team. Use this key only for a sports event ticket.
- `balance` (SemanticTagType.CurrencyAmount): The current balance redeemable with the pass. Use this key only for a store card pass.
- `boardingGroup` (localizable string): A group number for boarding. Use this key for any type of boarding pass.
- `boardingSequenceNumber` (localizable string): A sequence number for boarding. Use this key for any type of boarding pass.
- `boardingZone` (localizable string): A zone number for boarding. Don’t include the word *zone*.
- `carNumber` (localizable string): The number of the passenger car. A train car is also called a *carriage*, *wagon*, *coach*, or *bogie* in some countries. Use this key only for a train or other rail boarding pass.
- `confirmationNumber` (localizable string): A booking or reservation confirmation number. Use this key for any type of boarding pass.
- `currentArrivalDate` (ISO 8601 date as string): The updated date and time of arrival, if different from the originally scheduled date and time. Use this key for any type of boarding pass.
- `currentBoardingDate` (ISO 8601 date as string): The updated date and time of boarding, if different from the originally scheduled date and time. Use this key for any type of boarding pass.
- `currentDepartureDate` (ISO 8601 date as string): The updated departure date and time, if different from the originally scheduled date and time. Use this key for any type of boarding pass.
- `departureAirportCode` (localizable string): The IATA airport code for the departure airport, such as `MPM` or `LHR`. Use this key only for airline boarding passes.
- `departureAirportName` (localizable string): The full name of the departure airport, such as `Maputo International Airport`. Use this key only for airline boarding passes.
- `departureLocationSecurityPrograms` ([string]): A list of security programs that exist at the departure location. This only shows in the UI if a program is in `passengerEligibleSecurityPrograms` and at least one of `departureLocationSecurityPrograms` or `destinationLocationSecurityPrograms`.
- `departureLocationTimeZone` (string): The time zone of the departure location, such as `America/Chicago`. See the [`IANA Time Zone Database`](https://developer.apple.comhttps://www.iana.org/time-zones) for the full list of supported time zones.
- `departureCityName` (localizable string): The name of the departure city to display on the boarding pass, such as `London` or `Shanghai`.
- `departureGate` (localizable string): The gate number or letters of the departure gate, such as `1A`. Don’t include the word *gate*.
- `departureLocation` (SemanticTagType.Location): An object that represents the geographic coordinates of the transit departure location, suitable for display on a map. If possible, use precise locations, which are more useful to travelers; for example, the specific location of an airport gate. Use this key for any type of boarding pass.
- `departureLocationDescription` (localizable string): A brief description of the departure location. For example, for a flight departing from an airport that has a code of LHR, an appropriate description might be `London, Heathrow`. Use this key for any type of boarding pass.
- `departurePlatform` (localizable string): The name of the departure platform, such as `A`. Don’t include the word *platform*. Use this key only for a train or other rail boarding pass.
- `departureStationName` (localizable string): The name of the departure station, such as `1st Street Station`. Use this key only for a train or other rail boarding pass.
- `departureTerminal` (localizable string): The name or letter of the departure terminal, such as `A`. Don’t include the word *terminal*. Use this key only for airline boarding passes.
- `destinationAirportCode` (localizable string): The IATA airport code for the destination airport, such as `MPM` or `LHR`. Use this key only for airline boarding passes.
- `destinationAirportName` (localizable string): The full name of the destination airport, such as `London Heathrow`. Use this key only for airline boarding passes.
- `destinationLocationSecurityPrograms` ([string]): A list of security programs that exist at the destination location. This only shows in the UI if a program is in `passengerEligibleSecurityPrograms` and at least one of `departureLocationSecurityPrograms` or `destinationLocationSecurityPrograms`.
- `destinationLocationTimeZone` (string): The time zone of the destination location, such as `America/Los_Angeles`. See the [`IANA Time Zone Database`](https://developer.apple.comhttps://www.iana.org/time-zones) for the full list of supported time zones.
- `destinationCityName` (localizable string): The name of the destination city to display on the boarding pass, such as `London` or `Shanghai`.
- `destinationGate` (localizable string): The gate number or letter of the destination gate, such as `1A`. Don’t include the word *gate*. Use this key only for airline boarding passes.
- `destinationLocation` (SemanticTagType.Location): An object that represents the geographic coordinates of the transit departure location, suitable for display on a map. Use this key for any type of boarding pass.
- `destinationLocationDescription` (localizable string): A brief description of the destination location. For example, for a flight arriving at an airport that has a code of MPM, `Maputo` might be an appropriate description. Use this key for any type of boarding pass.
- `destinationPlatform` (localizable string): The name of the destination platform, such as `A`. Don’t include the word *platform*. Use this key only for a train or other rail boarding pass.
- `destinationStationName` (localizable string): The name of the destination station, such as `1st Street Station`. Use this key only for a train or other rail boarding pass.
- `destinationTerminal` (localizable string): The terminal name or letter of the destination terminal, such as `A`. Don’t include the word *terminal*. Use this key only for airline boarding passes.
- `duration` (number): The duration of the event or transit journey, in seconds. Use this key for any type of boarding pass and any type of event ticket.
- `entranceDescription` (localizable string): The long description of the entrance information. Use this key for any type of event ticket.
- `eventEndDate` (ISO 8601 date as string): The date and time the event ends. Use this key for any type of event ticket.
- `eventName` (localizable string): The full name of the event, such as the title of a movie. Use this key for any type of event ticket.
- `eventStartDate` (ISO 8601 date as string): The date and time the event starts. Use this key for any type of event ticket.
- `eventStartDateInfo` (SemanticTagType.EventDateInfo): An object that provides information for the date and time the event starts. Use this key for any type of event ticket.
- `eventType` (string): The type of event. Use this key for any type of event ticket.
- `flightCode` (localizable string): The IATA flight code, such as `EX123`. Use this key only for airline boarding passes.
- `flightNumber` (number): The numeric portion of the IATA flight code, such as `123` for `flightCode` `EX123`. Use this key only for airline boarding passes.
- `genre` (localizable string): The genre of the performance, such as `classical`. Use this key for any type of event ticket.
- `homeTeamAbbreviation` (localizable string): The unique abbreviation of the home team’s name. Use this key only for a sports event ticket.
- `homeTeamLocation` (localizable string): The home location of the home team. Use this key only for a sports event ticket.
- `homeTeamName` (localizable string): The name of the home team. Use this key only for a sports event ticket.
- `internationalDocumentsAreVerified` (boolean): An optional boolean that indicates whether the passenger’s international documents are verified. If set to `true` Wallet displays the badge on the boarding pass with the value from `internationalDocumentsVerifiedDeclarationName`.
- `internationalDocumentsVerifiedDeclarationName` (localizable string): The name of the declaration given once the passenger’s international documents are verified. Examples include `DOCS OK` or `Travel Ready`. If `internationalDocumentsAreVerified` is `true`, Wallet displays a badge on the boarding pass with this value.
- `leagueAbbreviation` (localizable string): The abbreviated league name for a sports event. Use this key only for a sports event ticket.
- `leagueName` (localizable string): The unabbreviated league name for a sports event. Use this key only for a sports event ticket.
- `loungePlaceIDs` ([string]): The `MapKit` `Place IDs` that reference the transit provider lounge locations. For more information, see [`Identifying unique locations with Place IDs`](https://developer.apple.com/documentation/MapKit/identifying-unique-locations-with-place-ids).
- `membershipProgramName` (localizable string): The name of a frequent flyer or loyalty program. Use this key for any type of boarding pass.
- `membershipProgramNumber` (localizable string): The ticketed passenger’s frequent flyer or loyalty number. Use this key for any type of boarding pass.
- `membershipProgramStatus` (localizable string): The ticketed passenger’s frequent flyer or loyalty program status. Use this key for any type of boarding pass.
- `originalArrivalDate` (ISO 8601 date as string): The originally scheduled date and time of arrival. Use this key for any type of boarding pass.
- `originalBoardingDate` (ISO 8601 date as string): The originally scheduled date and time of boarding. Use this key for any type of boarding pass.
- `originalDepartureDate` (ISO 8601 date as string): The originally scheduled date and time of departure. Use this key for any type of boarding pass.
- `passengerAirlineSSRs` ([string]): An array of airline-specific SSRs that apply to the ticketed passenger.
- `passengerCapabilities` ([string]): A list of capabilities the passenger has. Only use this key for airline boarding passes.
- `passengerEligibleSecurityPrograms` ([string]): A list of security programs the passenger is eligible for. This only shows in the UI if a program is in `passengerEligibleSecurityPrograms` and at least one of `departureLocationSecurityPrograms` or `destinationLocationSecurityPrograms`.
- `passengerInformationSSRs` ([string]): An array of IATA information SSRs that apply to the ticketed passenger. A comprehensive list of service SSRs can be found in the [`the IATA Airlines Developer Guide`](https://developer.apple.comhttps://guides.developer.iata.org/docs/21-1_ImplementationGuide.pdf) under A List of Information SSRs.
- `passengerName` (SemanticTagType.PersonNameComponents): An object that represents the name of the passenger. Use this key for any type of boarding pass.
- `passengerServiceSSRs` ([string]): An array of IATA SSRs that apply to the ticketed passenger. A comprehensive list of service SSRs can be found in [`the IATA Airlines Developer Guide`](https://developer.apple.comhttps://guides.developer.iata.org/docs/21-1_ImplementationGuide.pdf) under A List of Service SSRs.
- `performerNames` ([localizable string]): An array of the full names of the performers and opening acts at the event, in decreasing order of significance. Use this key for any type of event ticket.
- `playlistIDs` ([localizable string]): An array of the Apple Music persistent ID for each playlist corresponding to the event, in decreasing order of significance. Use this key for any type of event ticket.
- `priorityStatus` (localizable string): The priority status the ticketed passenger holds, such as `Gold` or `Silver`. Use this key for any type of boarding pass.
- `seats` ([SemanticTagType.Seat]): An array of objects that represent the details for each seat at an event or on a transit journey. Use this key for any type of boarding pass or event ticket.
- `securityScreening` (localizable string): The type of security screening for the ticketed passenger, such as `Priority`. Use this key for any type of boarding pass.
- `silenceRequested` (boolean): A Boolean value that determines whether the person’s device remains silent during an event or transit journey. The system may override the key and determine the length of the period of silence. Use this key for any type of boarding pass or event ticket.
- `sportName` (localizable string): The commonly used name of the sport. Use this key only for a sports event ticket.
- `tailgatingAllowed` (boolean): A Boolean value that indicates whether tailgating is allowed at the event. Use this key for any type of event ticket.
- `ticketFareClass` (localizable string): A localizable string that denotes the ticket class, such as `Saver`, `Economy`, `First`. This value displays as a badge on the boarding pass.
- `totalPrice` (SemanticTagType.CurrencyAmount): The total price for the pass. Use this key for any pass type.
- `transitProvider` (localizable string): The name of the transit company. Use this key for any type of boarding pass.
- `transitStatus` (localizable string): A brief description of the current boarding status for the vessel, such as `On Time` or `Delayed`. For delayed status, provide `currentBoardingDate`, `currentDepartureDate`, and `currentArrivalDate` where available. Use this key for any type of boarding pass.
- `transitStatusReason` (localizable string): A brief description that explains the reason for the current `transitStatus`, such as `Thunderstorms`. Use this key for any type of boarding pass.
- `vehicleName` (localizable string): The name of the vehicle to board, such as the name of a boat. Use this key for any type of boarding pass.
- `vehicleNumber` (localizable string): The identifier of the vehicle to board, such as the aircraft registration number or train number. Use this key for any type of boarding pass.
- `vehicleType` (localizable string): A brief description of the type of vehicle to board, such as the model and manufacturer of a plane or the class of a boat. Use this key for any type of boarding pass.
- `venueBoxOfficeOpenDate` (ISO 8601 date as string): The date when the box office opens. Use this key for any type of event ticket.
- `venueCloseDate` (ISO 8601 date as string): The date when the venue closes. Use this key for any type of event ticket.
- `venueDoorsOpenDate` (ISO 8601 date as string): The date the doors to the venue open. Use this key for any type of event ticket.
- `venueEntrance` (localizable string): The full name of the entrance, such as `Gate A`, to use to gain access to the ticketed event. Use this key for any type of event ticket.
- `venueEntranceDoor` (localizable string): The venue entrance door. Use this key for any type of event ticket.
- `venueEntranceGate` (localizable string): The venue entrance gate. Use this key for any type of event ticket.
- `venueEntrancePortal` (localizable string): The venue entrance portal. Use this key for any type of event ticket.
- `venueFanZoneOpenDate` (ISO 8601 date as string): The date the fan zone opens. Use this key for any type of event ticket.
- `venueGatesOpenDate` (ISO 8601 date as string): The date the gates to the venue open. Use this key for any type of event ticket.
- `venueLocation` (SemanticTagType.Location): An object that represents the geographic coordinates of the venue. Use this key for any type of event ticket.
- `venueName` (localizable string): The full name of the venue. Use this key for any type of event ticket.
- `venueOpenDate` (ISO 8601 date as string): The date when the venue opens. Use this if none of the more specific venue open tags apply. Use this key for any type of event ticket.
- `venueParkingLotsOpenDate` (ISO 8601 date as string): The date the parking lots open. Use this key for any type of event ticket.
- `venuePhoneNumber` (localizable string): The phone number for inquiries about the venue’s ticketed event. Use this key for any type of event ticket.
- `venueRegionName` (localizable string): The name of the city or hosting region of the venue. Use this key for any type of event ticket.
- `venueRoom` (localizable string): The full name of the room where the ticketed event is to take place. Use this key for any type of event ticket.
- `wifiAccess` ([SemanticTagType.WifiNetwork]): An array of objects that represent the Wi-Fi networks associated with the event; for example, the network name and password associated with a developer conference. Use this key for any type of pass.

## See Also

- [Supporting semantic tags in Wallet passes](supporting-semantic-tags-in-wallet-passes.md)
  Enable the system to offer suggestions for actions related to passes by adding machine-readable metadata.
- [object SemanticTagType](semantictagtype.md)
  A compilation of data object types for semantic tags.
- [Creating an airline boarding pass using semantic tags](creating-an-airline-boarding-pass-using-semantic-tags.md)
  Update your semantic tags to provide live and interactive passenger information for boarding passes.
- [object Pass.BoardingPass](pass/boardingpass-data.dictionary.md)
  An object that represents the groups of fields that display the information for a boarding pass.
- [object SemanticTagType](semantictagtype.md)
  A compilation of data object types for semantic tags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/semantictags)*