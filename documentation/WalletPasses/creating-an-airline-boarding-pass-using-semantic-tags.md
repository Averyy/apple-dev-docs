# Creating an airline boarding pass using semantic tags

**Framework**: Wallet Passes

Update your semantic tags to provide live and interactive passenger information for boarding passes.

#### Overview

Beginning with iOS and watchOS 26, you can update airline boarding passes with live information using semantic tags. This experience builds on the existing [`PKPass`](https://developer.apple.com/documentation/PassKit/PKPass) bundle in Wallet and maintains backward compatibility. If you can’t use semantic tags for some reason, Wallet falls back to the legacy boarding pass. For existing boarding passes, you can update your legacy boarding pass by using semantic tags to enable up-to-date flight information, real-time updates, and interactive features in Wallet. For more information on semantic tags, see [`Supporting semantic tags in Wallet passes`](supporting-semantic-tags-in-wallet-passes.md).

By adding semantic tags to your boarding pass, you provide structured data that Wallet uses to automatically display information like flight status, gate changes, and baggage information, as well as an overall more dynamic and helpful experience for passengers. After you meet the minimum requirements to display a boarding pass using semantic tags, you can optimize a passenger’s experience by adding badges to highlight travel attributes and ticket add-ons.

To display a semantic boarding pass, you need to meet the following minimum requirements:

- Add `semanticBoardingPass` to the `preferredStyleSchemes`.
- Set the `transitType` in the `boardingPass` top-level style dictionary to `PKTransitTypeAir`. For more information, see [`Pass.BoardingPass`](pass/boardingpass-data.dictionary.md).
- Provide the required semantic tags to populate the pass and certain dashboard content.

> **Note**: Use the semantic boarding pass style only for airline boarding passes.

#### Set the Preferred Style Scheme

The preferred style scheme is a top-level key that you provide. It takes an array of strings that correspond to schemes that the system resolves into a style. For semantic boarding passes, the scheme is `semanticBoardingPass`. Wallet recognizes this scheme and runs the appropriate validation to designate the pass as a semantic boarding pass, or falls back to the legacy boarding pass (`boardingPass`).

The following is an example of the preferred style scheme structure:

```json
  "preferredStyleSchemes": [
    "semanticBoardingPass",
    "boardingPass"
]
```

> **Note**:  To automatically suppress the Wallet-based Live Activity, list your App Store Identifier (Adam ID) in the `associatedStoreIdentifiers` array in the `pass.json` file of the boarding pass.

#### Set the Top Level Style Dictionary

The style dictionary determines the pass type. To provide the upgraded boarding pass experience, set the `transitType` to `PKTransitTypeAir` in the `boardingPass` top-level style dictionary key.

#### Add the Required Semantic Tags

Semantic tags are objects that contain machine-readable metadata the system uses to offer a pass and suggest related actions. For the semantic boarding pass style, the following list of semantic tags is required. If you omit any of the tags, your pass falls back to the legacy boarding pass style. For more information on semantic tags, see [`SemanticTags`](semantictags.md).

| Required tags | Description |
| --- | --- |
| `airlineCode` | The IATA airline code, such as `EX` for `flightCode EX123`. Use this key only for airline boarding passes. |
| `flightNumber` | The numeric portion of the IATA flight code, such as `123` for `flightCode EX123`. Use this key only for airline boarding passes. |
| `departureAirportCode` | The IATA airport code for the departure airport, such as `MPM` or `LHR`. Use this key only for airline boarding passes. |
| `departureCityName` | The name of the departure city to display on the boarding pass, such as `London` or `Shanghai`. |
| `departureLocationTimeZone` | The time zone of the departure location, such as `America/Chicago`. See the [`IANA Time Zone Database`](https://developer.apple.comhttps://www.iana.org/time-zones) for the full list of supported time zones. |
| `destinationAirportCode` | The IATA airport code for the destination airport, such as `MPM` or `LHR`. Use this key only for airline boarding passes. |
| `destinationCityName` | The name of the destination city to display on the boarding pass, such as `London` or `Shanghai`. |
| `destinationLocationTimeZone` | The time zone of the destination location, such as `America/Los_Angeles`. See the [`IANA Time Zone Database`](https://developer.apple.comhttps://www.iana.org/time-zones) for the full list of supported time zones. |
| `originalArrivalDate` | The originally scheduled date and time of arrival. Use this key for any type of boarding pass. |
| `originalBoardingDate` | The originally scheduled date and time of boarding. Use this key for any type of boarding pass. |
| `originalDepartureDate` | The originally scheduled date and time of departure. Use this key for any type of boarding pass. |
| `passengerName` | An object that represents the name of the passenger. Use this key for any type of boarding pass. |

#### Include Recommended and Optional Semantic Tags

The following list of semantic tags are optional, but recommended for optimal pass design:

| Recommended tags | Description |
| --- | --- |
| `departureAirportName` | The full name of the departure airport, such as `Maputo International Airport`. Use this key only for airline boarding passes. |
| `departureLocation` | An object that represents the geographic coordinates of the transit departure location, suitable for display on a map. If possible, use precise locations, which are more useful to travelers; for example, the specific location of an airport gate. Use this key for any type of boarding pass. |
| `departureLocationSecurityPrograms` | A list of security programs that exist at the departure location. This only shows in the UI if a program is in `passengerEligibleSecurityPrograms` and at least one of `departureLocationSecurityPrograms` or `destinationLocationSecurityPrograms`. |
| `destinationAirportName` | The full name of the destination airport, such as `London Heathrow`. Use this key only for airline boarding passes. |
| `destinationLocation` | An object that represents the geographic coordinates of the transit departure location, suitable for display on a map. Use this key for any type of boarding pass. |
| `destinationLocationSecurityPrograms` | A list of security programs that exist at the destination location. This only shows in the UI if a program is in `passengerEligibleSecurityPrograms` and at least one of `departureLocationSecurityPrograms` or `destinationLocationSecurityPrograms`. |
| `passengerEligibleSecurityPrograms` | A list of security programs the passenger is eligible for. This only shows in the UI if a program is in `passengerEligibleSecurityPrograms` and at least one of `departureLocationSecurityPrograms` or `destinationLocationSecurityPrograms`. |
| `transitProvider` | The name of the transit company. Use this key for any type of boarding pass. |

The following list of semantic tags are optional:

| Optional tags | Description |
| --- | --- |
| `boardingGroup` | A group number for boarding. Use this key for any type of boarding pass. |
| `boardingSequenceNumber` | A sequence number for boarding. Use this key for any type of boarding pass. |
| `boardingZone` | A zone number for boarding. Don’t include the word . |
| `currentArrivalDate` | The updated date and time of arrival, if different from the originally scheduled date and time. Use this key for any type of boarding pass. |
| `currentBoardingDate` | The updated date and time of boarding, if different from the originally scheduled date and time. Use this key for any type of boarding pass. |
| `currentDepartureDate` | The updated date and time of departure, if different from the originally scheduled date and time. Use this key for any type of boarding pass. |
| `departureGate` | The gate number or letters of the departure gate, such as `1A`. Don’t include the word . |
| `departureTerminal` | The name or letter of the departure terminal, such as `A`. Don’t include the word . Use this key only for airline boarding passes. |
| `destinationGate` | The gate number or letter of the destination gate, such as `1A`. Don’t include the word . Use this key only for airline boarding passes. |
| `destinationTerminal` | The terminal name or letter of the destination terminal, such as `A`. Don’t include the word . Use this key only for airline boarding passes. |
| `internationalDocumentsAreVerified` | An optional Boolean value that indicates whether the system verifies the passenger’s international documents. When `true`, Wallet displays the badge on the boarding pass with the value from `internationalDocumentsVerifiedDeclarationName`. |
| `internationalDocumentsVerifiedDeclarationName` | The name of the declaration the system provides after it verifies the passenger’s international documents. Examples include `DOCS OK` or `Travel Ready`. When `internationalDocumentsAreVerified` is `true`, Wallet displays a badge on the boarding pass with this value. |
| `loungePlaceIDs` | The MapKit Place IDs that reference the transit provider lounge locations. For more information, see [`Identifying unique locations with Place IDs`](https://developer.apple.com/documentation/MapKit/identifying-unique-locations-with-place-ids). |
| `membershipProgramName` | The name of a frequent flyer or loyalty program. Use this key for any type of boarding pass. |
| `membershipProgramNumber` | The ticketed passenger’s frequent flyer or loyalty program number. Use this key for any type of boarding pass. |
| `membershipProgramStatus` | The ticketed passenger’s frequent flyer or loyalty program status. Use this key for any type of boarding pass. |
| `passengerAirlineSSRs` | An array of airline-specific SSRs that apply to the ticketed passenger. Use this key only for airline boarding passes. |
| `passengerCapabilities` | A list of capabilities the passenger has. Use this key only for airline boarding passes. |
| `passengerInformationSSRs` | An array of IATA SSRs that apply to the ticketed passenger related to passenger information. Find a comprehensive list of information SSRs in the [`IATA Airlines Developer Guide`](https://developer.apple.comhttps://guides.developer.iata.org/docs/21-1_ImplementationGuide.pdf) under the section titled, . Use this key only for airline boarding passes. |
| `passengerServiceSSRs` | An array of IATA SSRs that apply to the ticketed passenger related to available services. Find a comprehensive list of service SSRs in the [`IATA Airlines Developer Guide`](https://developer.apple.comhttps://guides.developer.iata.org/docs/21-1_ImplementationGuide.pdf) under the section titled, . Use this key only for airline boarding passes. |
| `priorityStatus` | The priority status the ticketed passenger holds, such as `Gold` or `Silver`. Use this key for any type of boarding pass. |
| `seats` | An array of objects that represent the details for each seat at an event or on a transit journey. Use this key for any type of boarding pass or event ticket. |
| `ticketFareClass` | A localizable string that denotes the ticket class, such as `Saver`, `Economy`, `First`. This value displays as a badge on the boarding pass. |

#### Ensure Backward Compatibility

To ensure your pass is backward compatible, continue to provide the [`PassFields.PrimaryFields`](passfields/primaryfields-data.dictionary.md), [`PassFields.SecondaryFields`](passfields/secondaryfields-data.dictionary.md), and [`PassFields.AuxiliaryFields`](passfields/auxiliaryfields-data.dictionary.md) so the system presents the legacy boarding pass style, if necessary. Semantic boarding passes add keys and assets to the existing `PKPass` bundle that legacy boarding passes use. By building on the legacy pass bundle, Wallet automatically generates the appropriate device experience for iOS and watchOS.

When someone adds a pass to a device, that pass automatically syncs to all devices linked to the same Apple Account. When a supported device with iOS or watchOS 26 or later syncs to a device that doesn’t support semantic tags, Wallet recognizes the pass as a legacy boarding pass. The possible scenarios are:

- The legacy fields aren’t present. This means there is no content on the pass.
- The legacy fields are present but invalid. This means the ingestion fails on all devices.
- The legacy fields are present and valid. This means Wallet shows a fully populated legacy boarding pass.

If someone adds a pass to an unsupported device and syncs it to a supported device with iOS or watchOS 26 or later, Wallet displays the semantic boarding pass information after you meet the minimum requirements by setting the top-level style dictionary and adding the required semantic tags. If you don’t meet the requirements, Wallet displays a legacy boarding pass.

#### Offer Additional Flight Information

Populate an airline and services page to provide additional information related to a flight. The system uses metadata you provide to display an airline and services page in Wallet. Below the boarding pass, passengers can select a quick action link to navigate to a separate page within Wallet with useful information related to their flight and airport experience. Depending on the information you provide, you can populate links for the following:

| Flight information | Semantic tag |
| --- | --- |
| Add checked bag | `purchaseAdditionalBaggageURL` |
| Airline email | `transitProviderEmail` |
| Airline phone | `transitProviderPhoneNumber` |
| Airline website | `transitProviderWebsiteURL` |
| Business chat | `businessChatIdentifier` |
| Change seat | `changeSeatURL` |
| Entertainment | `entertainmentURL` |
| Inflight Wi-Fi | `purchaseWifiURL` |
| Management options for the boarding pass | `managementURL` |
| Meal ordering | `orderFoodURL` |
| Purchase lounge access | `purchaseLoungeAccessURL` |
| Report lost bags to the airline | `reportLostBagURL` |
| Track bags through the airline’s app | `trackBagsURL` |
| Upgrade seat | `upgradeURL` |

#### Provide Live Flight Information

Boarding passes use semantic tags to correlate which flight the pass belongs to. With semantic tags, Wallet subscribes to updates for flight and surface functionalities, like Share Flight Tracker, which allows passengers to share flight information from Wallet through iMessage or iPhone nearby interactivity.

If live flight information isn’t available for the current flight, Wallet provides the following information:

| Flight information | Semantic tag |
| --- | --- |
| Arrival baggage claim | From the live data in Wallet. |
| Arrival gate | `destinationGate` |
| Arrival terminal | `destinationTerminal` |
| Arrival time | `originalArrivalDate` and `currentArrivalDate` |
| Departure city | `departureCityName` |
| Departure gate | `departureGate` |
| Departure terminal | `departureTerminal` |
| Departure time | `originalDepartureDate` and `currentDepartureDate` |
| Destination city | `destinationCityName` |

You provide the following information through semantic tags, and Wallet doesn’t supersede it:

| Flight information | Semantic tag |
| --- | --- |
| Boarding group | `boardingGroup` |
| Boarding time | `originalBoardingDate` |
| Passenger name | `passengerName` |
| Seat | `seats` |
| Sequence Number | `boardingSequenceNumber` |

For the full list of semantic tags, see [`SemanticTags`](semantictags.md).

> **Note**:  The information you provide determines the boarding time. Wallet calculates the boarding time by applying the time difference between your `originalDepartureDate` and `originalBoardingDate` to the known live departure time.

## See Also

- [object Pass.BoardingPass](pass/boardingpass-data.dictionary.md)
  An object that represents the groups of fields that display the information for a boarding pass.
- [object SemanticTags](semantictags.md)
  An object that contains machine-readable metadata the system uses to offer a pass and suggest related actions.
- [object SemanticTagType](semantictagtype.md)
  A compilation of data object types for semantic tags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/creating-an-airline-boarding-pass-using-semantic-tags)*