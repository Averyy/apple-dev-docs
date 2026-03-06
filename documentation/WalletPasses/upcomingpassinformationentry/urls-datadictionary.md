# UpcomingPassInformationEntry.URLs

**Framework**: Wallet Passes  
**Kind**: dictionary

An object with links to information about the upcoming pass information entry.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- watchOS 26.0+

## Declaration

```swift
object UpcomingPassInformationEntry.URLs
```

#### Discussion

Use as deep a link as possible for each URL.

## Properties

- `accessibilityURL` (string): A URL that links to your or the venue’s accessiblity content.
- `addOnURL` (string): A URL that links to experiences that you can add on to your ticket or that allows you to access your existing prepurchased or preloaded add-on experiences, including any necessary QR or barcode links to access the experience. For example, loaded value or upgrades for an experience.
- `bagPolicyURL` (string): A URL that links out to the bag policy of the venue.
- `contactVenueEmail` (string): The preferred email address to contact the venue, event, or issuer.
- `contactVenuePhoneNumber` (string): The preferred phone number to contact the venue, event, or issuer.
- `contactVenueWebsite` (string): A URL that links the user to the website of the venue, event, or issuer.
- `directionsInformationURL` (string): A URL that links to content you have about getting to the venue.
- `merchandiseURL` (string): A URL that links to order merchandise for the specific event. This can be a ship-to-home ecommerce site, a pre-order to pickup at the venue, or other appropriate merchandise flow. This link can also be updated throughout the user’s journey to provide more accurately tailored links at certain times. For example, before versus after a user enters an event. This can be done through a pass update. For more information on updating a pass, see [`Distributing and updating a pass`](distributing-and-updating-a-pass.md).
- `orderFoodURL` (string): A URL that links out to the food-ordering page for the venue. This can be in-seat food delivery, pre-order for pickup at a vendor, or other appropriate food-ordering service.
- `parkingInformationURL` (string): A URL that links to any information you have about parking.
- `purchaseParkingURL` (string): A URL that links to your experience to buy or access prepaid parking or general parking information.
- `sellURL` (string): A URL that launches the user into the issuer’s flow for selling their current ticket. Provide as deep a link as possible into the sale flow.
- `transferURL` (string): A URL that launches the user into the issuer’s flow for transferring the current ticket. Provide as deep a link as possible into the transfer flow.
- `transitInformationURL` (string): A URL that links to documentation you have about public or private transit to the venue.

## See Also

- [object UpcomingPassInformationEntry.AdditionalInfoFields](upcomingpassinformationentry/additionalinfofields-data.dictionary.md)
  The fields of information that display in the Additional Info section below a pass.
- [object UpcomingPassInformationEntry.BackFields](upcomingpassinformationentry/backfields-data.dictionary.md)
  The fields of information displayed in the details view  of the upcoming pass information entry.
- [object UpcomingPassInformationEntry.DateInformation](upcomingpassinformationentry/dateinformation-data.dictionary.md)
  Information about the start and end time of the upcoming pass information entry.
- [object UpcomingPassInformationEntry.Images](upcomingpassinformationentry/images-data.dictionary.md)
  A collection of image names used to populate images in the details view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/upcomingpassinformationentry/urls-data.dictionary)*