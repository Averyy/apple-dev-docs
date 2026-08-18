# Location.Address

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

The postal address of a brand location.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object Location.Address
```

#### Discussion

`address` is sourced from Apple Maps and is read-only. Use `countryOrRegion` to verify country or region targeting compatibility, and `fullAddress` for a single formatted display string.

## Properties

- `countryOrRegion` (string): ISO 3166-1 alpha-2 country code, e.g. `"US"`, `"GB"`. Read-only.
- `adminArea` (string): State or province name, e.g. `"California"`. Read-only.
- `adminAreaCode` (string): Abbreviated state or province code, e.g. `"CA"`. Read-only.
- `locality` (string): City or town name. Read-only.
- `subLocality` (string): Neighborhood or district within a city. Read-only.
- `subAdminArea` (string): County or sub-administrative area. Read-only.
- `postalCode` (string): Postal or ZIP code. Read-only.
- `thoroughfare` (string): Street name. Read-only.
- `subThoroughfare` (string): Street number. Read-only.
- `fullThoroughfare` (string): Combined street number and street name. Read-only.
- `fullAddress` (string): Complete formatted address string. Read-only.
- `unit` (string): Suite or unit number, e.g. `"Suite 100"`. Read-only.
- `floor` (string): Floor number, e.g. `"1"`. Read-only.
- `building` (string): Building name, e.g. `"Main Building"`. Read-only.
- `dependentLocality` ([string]): Array of additional locality components. Read-only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/location/address-data.dictionary)*