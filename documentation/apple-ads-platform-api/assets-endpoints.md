# Assets Endpoints

**Framework**: Apple Ads Platform API

Upload, query, retrieve, and delete Apple Maps creative assets.

**Availability**:
- Apple Ads Platform API 1.0+

#### Overview

You use assets to build creative for your campaigns. Uploading new assets through this API is available only for Apple Maps brands, but querying and retrieving assets covers both App Store apps and Apple Maps brands. Each asset carries metadata about its type, dimensions, eligibility status, and any rejection reasons.

#### Use the Endpoints

The Assets API provides four endpoints for uploading, querying, retrieving, and deleting assets:

| Method | Path | Description |
| --- | --- | --- |
| `POST` | `/v1/assets/upload` | [`Upload Asset`](upload-asset.md) uploads a new creative asset for use in Apple Maps campaigns. |
| `POST` | `/v1/assets/query` | [`Query Assets`](query-assets.md) retrieves assets matching the specified filters. |
| `GET` | `/v1/assets/{id}` | [`Get Asset`](get-asset-by-id.md) retrieves a single asset by its ID. |
| `DELETE` | `/v1/assets/{id}` | [`Delete Asset`](delete-asset-by-id.md) soft-deletes an uploaded asset by its ID. |

##### Identify the Asset Type

Every asset has an `assetType` field, which identifies the kind of media it contains. Currently, `IMAGE` is the only supported value, and it represents a static image file. See [`ImageType`](imagetype.md) for the full list of supported formats.

##### Upload Assets

Assets enter the system through a single upload method. Send a multipart form to `POST /v1/assets/upload` containing the binary image file (`file`), `promotedObjectId`, and `promotedObjectType: BUSINESS_BRAND`. The endpoint accepts PNG, JPG, and HEIC formats.

This endpoint only supports asset uploads for Apple Maps (`BUSINESS_BRAND`) assets, and it doesn’t accept any other value for `promotedObjectType`. The uploaded asset belongs to the ad account identified by the `X-AP-Context` header and becomes part of that account’s asset library.

After upload, the asset begins processing. Poll using [`Get Asset`](get-asset-by-id.md) until the `eligibility.status` indicates the asset is ready before referencing it in a creative.

##### Query Assets

To find assets, use `POST /v1/assets/query` with the following filterable fields:

| Filterable Field | Operators | Description |
| --- | --- | --- |
| `promotedObjectId` | `EQUALS`, `IN` | Filter by the promoted object’s identifier (`adamId` for an App Store app, `brandId` for an Apple Maps brand). |
| `promotedObjectType` | `EQUALS` | Filter by promoted object type: `APPSTORE_APP` or `BUSINESS_BRAND`. |
| `providerAssetId` | `EQUALS`, `IN` | Filter by the provider-assigned asset identifier. |
| `assetType` | `EQUALS`, `IN` | Filter by asset type: `IMAGE`. |

##### Review the Shared Response Fields

Every asset response includes the following fields:

| Field | Description |
| --- | --- |
| `id` | Unique asset identifier (UUID). Read-only. |
| `name` | User-facing asset name or description. |
| `assetType` | The media type of the asset. See [`AssetType`](assettype.md). |
| `providerAssetId` | Asset identifier assigned by the provider system. |
| `promotedObjectId` | Identifier of the promoted object (`adamId` for an app, `brandId` for a brand). |
| `promotedObjectType` | The type of the promoted object: `APPSTORE_APP` or `BUSINESS_BRAND`. |
| `providerAssetMetadata` | Provider-specific metadata. Structure varies by provider type. |
| `assetDetails` | Type-specific media metadata. For `IMAGE` assets, contains [`AssetImage`](assetimage.md) fields, including `format` (see [`ImageType`](imagetype.md)) and `orientation` (see [`Orientation`](orientation.md)). |
| `parentAssetId` | Identifier of the parent asset if this asset is a variant. |
| `variantIds` | Identifiers for asset variants (e.g., different sizes or localizations). |
| `eligibility` | Eligibility data. See [`AssetEligibility`](asseteligibility.md) for the `status` field (see [`AssetEligibilityStatus`](asseteligibilitystatus.md)) and the `blockedGroups`/`allowedGroups` constraint fields (see [`AssetConstraintGroup`](assetconstraintgroup.md)). Always returned unless excluded via a `fields` projection parameter. |
| `creationTime` | Timestamp when the asset was created (ISO 8601). Read-only. |
| `modificationTime` | Timestamp of the last modification (ISO 8601). Read-only. |

##### Delete Assets

You can only delete assets you’ve uploaded. A call to [`Get Asset`](get-asset-by-id.md) still returns a deleted asset and marks it with `deleted: true`, but [`Query Assets`](query-assets.md) excludes deleted assets from results by default.

## Topics

- [Upload Asset](upload-asset.md)
  Upload a binary image file to create a new asset.
- [Query Assets](query-assets.md)
  Retrieve a paginated list of creative assets using filters and sorting.
- [Get Asset](get-asset-by-id.md)
  Retrieve a single asset by its UUID.
- [Delete Asset](delete-asset-by-id.md)
  Soft-delete an asset by its UUID.

## See Also

- [Assets Data Objects](assets-data-objects.md)
  Reference the request and response objects for asset endpoints.
- [Assets Data Types](assets-data-types.md)
  Look up the enumerations and scalar types used for assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/assets-endpoints)*