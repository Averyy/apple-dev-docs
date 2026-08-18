# Managing Location Groups

**Framework**: Apple Ads Platform API

Organize business locations into named groups that define which locations an ad group’s targeting applies to in Apple Maps campaigns.

**Availability**:
- apple-ads-platform-api 1.0+

#### Overview

A location group is a named collection of business locations associated with a brand. Instead of targeting every location a brand operates, you can define groups (such as all locations in a metro area, a specific region, or a custom set for a promotional push) and apply that group to an ad group’s targeting configuration. The location group only scopes which locations are in play. You set the schedule, creatives, and bids on the ad group or ad itself, not per location group.

A location group doesn’t affect which viewers see the ad or how close they are to any given location. Geo and radius targeting on the ad group control that separately.

#### Understand Key Concepts

The following terms explain how location groups fit into your targeting strategy:

| Concept | Description |
| --- | --- |
| **Location group** | A named set of location IDs scoped to a single brand. |
| **Location ID** | The identifier for a physical location (`location.id`). |
| **Ad group targeting** | Associate a location group with an ad group to restrict delivery to those locations. |
| **systemStatus** | System-managed state: `VALID`, `INVALID`, `PENDING`, or `DELETED`. You can’t update or delete groups with `INVALID` or `PENDING` status. |

#### Follow the Workflow

Use location groups to build a targeted geographic strategy for an Apple Maps campaign:

1. **Discover locations.** Call [`Query for Locations`](query-locations.md) with a `brandId` filter to retrieve locations for your brand. Note the `id` values of the locations you want to group.
2. **Create the group.** Call [`Create Location Group`](create-location-group.md) with a `name`, the `brandId`, and an array of `locationIds`. `STATIC` groups (built from an explicit `locationIds` list) are `VALID` immediately. `DYNAMIC` groups (built from `rules`) start in `PENDING` state while the system evaluates membership. Wait for `systemStatus: VALID` before using a `DYNAMIC` group in targeting.
3. **Verify the group.** Call [`Get Location Group`](get-location-group-by-id.md) to confirm the group was created correctly and all location IDs are present.
4. **Target the group.** Reference the location group ID in the targeting parameters of an ad group. That restricts delivery for the ad group to the locations in the group.
5. **Maintain the group.** As brand footprint changes (new store openings, closures, seasonal popups), update the group using [`Update Location Group`](update-location-group.md) to add or remove location IDs without rebuilding your campaign structure. For `DYNAMIC` groups, the system automatically adds new locations that satisfy the group’s rules, so they don’t require a manual update.
6. **Remove unused groups.** When a group is no longer needed, call [`Delete Location Group`](delete-location-group.md) to clean up. Deletion is permanent. Ad groups targeting a deleted group lose that targeting constraint immediately and continue to serve only if they also target other location groups.

#### Review Location Group Fields

A location group object exposes the following fields:

| Field | Type | Description |
| --- | --- | --- |
| `id` | string | System-assigned group identifier. |
| `name` | string | Display name for the group. |
| `brandId` | string | The brand this group belongs to. |
| `adAccountId` | string | The ad account that owns this location group. |
| `groupType` | string | Type of location grouping: `STATIC` or `DYNAMIC`. |
| `systemStatus` | string | System-managed status: `VALID`, `INVALID`, `PENDING`, or `DELETED`. **Read-only.** You can’t update or delete groups with `INVALID` or `PENDING` status. |
| `query` | string | RSQL query generated from `rules` for `DYNAMIC` groups. **Read-only.** |
| `rules` | array | Rule objects defining membership criteria for `DYNAMIC` groups. |
| `locationIds` | array of strings | Location IDs included in the group (`STATIC` groups). |
| `isAllLocationsGroup` | boolean | `true` for the system-created “All Locations” group for a brand. **Read-only.** |
| `description` | string | Optional description of the group. |
| `groupTotal` | integer (int64) | Total number of locations in the group. **Read-only.** |
| `eligibility` | object | Ad serving eligibility for this group. **Read-only.** |
| `creationTime` | string (ISO 8601) | When the group was created. |
| `modificationTime` | string (ISO 8601) | When the group was last modified. |

#### Note Group Size Limits

Location groups enforce the following limits on size and structure:

- An organization can have a maximum of 5000 location groups across all its brands.
- An ad group can target a maximum of 25 location groups.
- A dynamic location group can include a maximum of 25 rules.
- There’s no limit on the number of locations a static location group can include, or on the number of locations attached to a campaign through location groups. Locations are defined at the brand level, so any location added to a brand is available to include in that brand’s groups.

## Topics

- [Create Location Group](create-location-group.md)
  Create a named group of locations for geographic targeting.
- [Query Location Groups](query-location-groups.md)
  Retrieve a paginated list of location groups using filters and sorting.
- [Get Location Group](get-location-group-by-id.md)
  Retrieve a single location group by its unique identifier.
- [Update Location Group](update-location-group.md)
  Update an existing location group’s name, rules, or location membership.
- [Delete Location Group](delete-location-group.md)
  Delete a location group by its unique identifier.

## See Also

- [Ads on Apple Maps Endpoints](brands-endpoints.md)
  Query and retrieve brands, business categories, and creative rejection reasons.
- [Understanding Locations](locations-overview.md)
  Query and inspect the business locations associated with your brand for use in Apple Maps campaigns.
- [Brands Data Objects](brands-data-objects.md)
  Reference the request and response objects for brand, location, and location group endpoints.
- [Brands Data Types](brands-data-types.md)
  Look up the enumerations and metric types used in Apple Maps campaigns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/location-groups-overview)*