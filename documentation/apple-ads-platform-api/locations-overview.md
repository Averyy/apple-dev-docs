# Understanding Locations

**Framework**: Apple Ads Platform API

Query and inspect the business locations associated with your brand for use in Apple Maps campaigns.

**Availability**:
- apple-ads-platform-api 1.0+

#### Overview

A location represents a physical place of business, such as a retail store, restaurant, or service center. Ads on Apple Maps promote these locations. See [`Managing Location Groups`](location-groups-overview.md) for how a location group organizes locations into a targetable set for an ad group.

Locations are read-only from the API perspective. Apple Business, not the Apple Ads Platform API, creates and maintains them. Use the location endpoints to discover locations associated with your brand, verify eligibility, and retrieve location IDs for use in location group construction.

#### Understand Key Concepts

Familiarize yourself with these concepts before you query locations or build location groups:

| Concept | Description |
| --- | --- |
| **Location** | A physical place of business associated with a brand. Each location belongs to one brand. |
| **ID** | The unique `id` that identifies a location. Use this value when building location groups. |
| **status** | Operational state: `OPEN`, `OPENING_SOON`, `CLOSED`, `MOVED`, or `TEMPORARILY_CLOSED`. Only `OPEN` locations are eligible for ad targeting. |
| **eligibility** | System-managed field that indicates whether ads can promote the location. See [`EligibilityStatus`](eligibilitystatus.md) for possible values. You can add only `ELIGIBLE` locations to location groups. |
| **Location group** | A named collection of location IDs. Ad groups reference location groups, not individual locations. See [`Managing Location Groups`](location-groups-overview.md). |

#### Follow the Location Workflow

Use location endpoints to discover and validate locations before building location groups for an Apple Maps campaign:

1. **Query locations for a brand.** Call [`Query for Locations`](query-locations.md) with a `brandId` filter to retrieve all locations associated with your brand. Note the `id` value of each location you want to target.
2. **Filter by status.** Add a `status EQUALS OPEN` filter to return only locations that are eligible for ad targeting. You can’t add closed or temporarily closed locations to location groups.
3. **Verify eligibility.** Check the `eligibility.status` field in each location object. A location must have `eligibility.status: ELIGIBLE` before you can add it to a location group and use it in a campaign.
4. **Retrieve a single location.** Call [`Get a Location`](get-location-by-id.md) by `id` to confirm address, coordinates, and eligibility before adding the location to a group.
5. **Build and manage location groups.** Once you’ve verified location IDs, see [`Managing Location Groups`](location-groups-overview.md) for the full group creation, targeting, and maintenance workflow.

#### Review Location Fields

Each location object returned by the API includes these read-only fields:

| Field | Type | Description |
| --- | --- | --- |
| `id` | string | Identifier for the location. **Read-only.** |
| `name` | string | Display name of the location. **Read-only.** |
| `brandId` | string | The brand this location belongs to. **Read-only.** |
| `status` | string | Operational status: `OPEN`, `OPENING_SOON`, `CLOSED`, `MOVED`, or `TEMPORARILY_CLOSED`. **Read-only.** |
| `countryOrRegion` | string | ISO 3166-1 alpha-2 country or region code for the location (e.g., `"US"`, `"GB"`). **Read-only.** |
| `categories` | array of strings | Business category identifiers. The first entry is the primary category. **Read-only.** |
| `address` | object | Full address with subfields for street, city, state, postal code, and country. **Read-only.** |
| `displayPoint` | object | Geographic coordinates of the location. **Read-only.** |
| `creationTime` | string | ISO-8601 creation timestamp. **Read-only.** |
| `modificationTime` | string | ISO-8601 last-modification timestamp. **Read-only.** |
| `eligibility` | object | System-managed eligibility status for ad targeting. See [`EligibilityStatus`](eligibilitystatus.md) for possible values. **Read-only.** |

## Topics

- [Query for Locations](query-locations.md)
  Retrieve a paginated list of business locations using filters and sorting.
- [Get a Location](get-location-by-id.md)
  Retrieve a single business location by its unique identifier.

## See Also

- [Ads on Apple Maps Endpoints](brands-endpoints.md)
  Query and retrieve brands, business categories, and creative rejection reasons.
- [Managing Location Groups](location-groups-overview.md)
  Organize business locations into named groups that define which locations an ad group’s targeting applies to in Apple Maps campaigns.
- [Brands Data Objects](brands-data-objects.md)
  Reference the request and response objects for brand, location, and location group endpoints.
- [Brands Data Types](brands-data-types.md)
  Look up the enumerations and metric types used in Apple Maps campaigns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/locations-overview)*