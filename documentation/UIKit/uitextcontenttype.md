# UITextContentType

**Framework**: UIKit  
**Kind**: struct

Constants that identify the semantic meaning for a text-entry area.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct UITextContentType
```

#### Overview

Use these constants with the [`textContentType`](uitextinputtraits/textcontenttype.md) property.

## Topics

### Defining web addresses
- [static let URL: UITextContentType](uitextcontenttype/url.md)
  A property that defines the content in a text input area as a URL.
### Identifying contacts
- [static let namePrefix: UITextContentType](uitextcontenttype/nameprefix.md)
  A property that defines the content in a text input area as a prefix or title, such as .
- [static let name: UITextContentType](uitextcontenttype/name.md)
  A property that defines the content in a text input area as a name.
- [static let nameSuffix: UITextContentType](uitextcontenttype/namesuffix.md)
  A property that defines the content in a text input area as a suffix, such as .
- [static let givenName: UITextContentType](uitextcontenttype/givenname.md)
  A property that defines the content in a text input area as a first name.
- [static let middleName: UITextContentType](uitextcontenttype/middlename.md)
  A property that defines the content in a text input area as a middle name.
- [static let familyName: UITextContentType](uitextcontenttype/familyname.md)
  A property that defines the content in a text input area as a family name, or last name.
- [static let nickname: UITextContentType](uitextcontenttype/nickname.md)
  A property that defines the content in a text input area as a nickname.
- [static let organizationName: UITextContentType](uitextcontenttype/organizationname.md)
  A property that defines the content in a text input area as an organization name.
- [static let jobTitle: UITextContentType](uitextcontenttype/jobtitle.md)
  A property that defines the content in a text input area as a job title.
### Setting location data
- [static let location: UITextContentType](uitextcontenttype/location.md)
  A property that defines the content in a text input area as a location, such as a point of interest, an address, or another identifier for a location.
- [static let fullStreetAddress: UITextContentType](uitextcontenttype/fullstreetaddress.md)
  A property that defines the content in a text input area as a street address that fully identifies a location.
- [static let streetAddressLine1: UITextContentType](uitextcontenttype/streetaddressline1.md)
  A property that defines the content in a text input area as the first line of a street address.
- [static let streetAddressLine2: UITextContentType](uitextcontenttype/streetaddressline2.md)
  A property that defines the content in a text input area as the second line of a street address.
- [static let addressCity: UITextContentType](uitextcontenttype/addresscity.md)
  A property that defines the content in a text input area as a city name.
- [static let addressCityAndState: UITextContentType](uitextcontenttype/addresscityandstate.md)
  A property that defines the content in a text input area as a city name with a state name.
- [static let addressState: UITextContentType](uitextcontenttype/addressstate.md)
  A property that defines the content in a text input area as a state name.
- [static let postalCode: UITextContentType](uitextcontenttype/postalcode.md)
  A property that defines the content in a text input area as a postal code.
- [static let sublocality: UITextContentType](uitextcontenttype/sublocality.md)
  A property that defines the content in a text input area as a sublocality.
- [static let countryName: UITextContentType](uitextcontenttype/countryname.md)
  A property that defines the content in a text input area as a country or region name.
### Managing accounts
- [static let username: UITextContentType](uitextcontenttype/username.md)
  A property that defines the content in a text input area as an account or login name.
- [static let password: UITextContentType](uitextcontenttype/password.md)
  A property that defines the content in a text input area as a password.
- [static let newPassword: UITextContentType](uitextcontenttype/newpassword.md)
  A property that defines the content in a text input area as a new password.
### Securing accounts
- [static let oneTimeCode: UITextContentType](uitextcontenttype/onetimecode.md)
  A property that defines the content in a text input area as a one-time code.
### Setting communication details
- [static let emailAddress: UITextContentType](uitextcontenttype/emailaddress.md)
  A property that defines the content in a text input area as an email address.
- [static let telephoneNumber: UITextContentType](uitextcontenttype/telephonenumber.md)
  A property that defines the content in a text input area as a telephone number.
- [static let cellularEID: UITextContentType](uitextcontenttype/cellulareid.md)
  A property that defines the content in a text input area to contain an embedded identity document number for an eSIM.
- [static let cellularIMEI: UITextContentType](uitextcontenttype/cellularimei.md)
  A property that defines the content in a text input area to contain an international mobile equipment identity number for an eSIM.
### Accepting payment
- [static let creditCardNumber: UITextContentType](uitextcontenttype/creditcardnumber.md)
  A property that defines the content in a text input area as a credit card number.
- [static let creditCardExpiration: UITextContentType](uitextcontenttype/creditcardexpiration.md)
  A property that defines the content in a text input area as an expiration date on a credit card.
- [static let creditCardExpirationMonth: UITextContentType](uitextcontenttype/creditcardexpirationmonth.md)
  A property that defines the content in a text input area as the month component of an expiration date on a credit card.
- [static let creditCardExpirationYear: UITextContentType](uitextcontenttype/creditcardexpirationyear.md)
  A property that defines the content in a text input area as the year component of an expiration date on a credit card.
- [static let creditCardSecurityCode: UITextContentType](uitextcontenttype/creditcardsecuritycode.md)
  A property that defines the content in a text input area as a credit card security code.
- [static let creditCardType: UITextContentType](uitextcontenttype/creditcardtype.md)
  A property that defines the content in a text input area as a credit card type.
- [static let creditCardName: UITextContentType](uitextcontenttype/creditcardname.md)
  A property that defines the content in a text input area as a name on a credit card.
- [static let creditCardGivenName: UITextContentType](uitextcontenttype/creditcardgivenname.md)
  A property that defines the content in a text input area as a first name on a credit card.
- [static let creditCardMiddleName: UITextContentType](uitextcontenttype/creditcardmiddlename.md)
  A property that defines the content in a text input area as a middle name on a credit card.
- [static let creditCardFamilyName: UITextContentType](uitextcontenttype/creditcardfamilyname.md)
  A property that defines the content in a text input area as a family name, or last name, on a credit card.
### Getting birthday information
- [static let birthdate: UITextContentType](uitextcontenttype/birthdate.md)
  A property that defines the content in a text input area as a date of birth.
- [static let birthdateDay: UITextContentType](uitextcontenttype/birthdateday.md)
  A property that defines the content in a text input area as the day component of a birthdate.
- [static let birthdateMonth: UITextContentType](uitextcontenttype/birthdatemonth.md)
  A property that defines the content in a text input area as the month component of a birthdate.
- [static let birthdateYear: UITextContentType](uitextcontenttype/birthdateyear.md)
  A property that defines the content in a text input area as the year component of a birthdate.
### Scheduling events
- [static let dateTime: UITextContentType](uitextcontenttype/datetime.md)
  A property that defines the content in a text input area as a date, time, or duration.
### Tracking events
- [static let flightNumber: UITextContentType](uitextcontenttype/flightnumber.md)
  A property that defines the content in a text input area as an airline flight number.
- [static let shipmentTrackingNumber: UITextContentType](uitextcontenttype/shipmenttrackingnumber.md)
  A property that defines the content in a text input area as a parcel tracking number.
### Creating a text content type
- [init(rawValue: String)](uitextcontenttype/init(rawvalue:).md)
  Creates a text content type with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var keyboardType: UIKeyboardType](uitextinputtraits/keyboardtype.md)
  The keyboard type for the text object.
- [enum UIKeyboardType](uikeyboardtype.md)
  Constants that specify the type of keyboard to display for a text-based view.
- [var keyboardAppearance: UIKeyboardAppearance](uitextinputtraits/keyboardappearance.md)
  The appearance style of the keyboard for the text object.
- [enum UIKeyboardAppearance](uikeyboardappearance.md)
  Constants that specify the appearance of the keyboard for a text-based view.
- [var returnKeyType: UIReturnKeyType](uitextinputtraits/returnkeytype.md)
  The visible title of the Return key.
- [enum UIReturnKeyType](uireturnkeytype.md)
  Constants that specify the text string that displays in the Return key of a keyboard.
- [var textContentType: UITextContentType!](uitextinputtraits/textcontenttype.md)
  The semantic meaning for a text input area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextcontenttype)*