# Calling the Apple Ads Platform API

**Framework**: Apple Ads Platform API

Authenticate requests, structure endpoint calls, and interpret responses when using the Apple Ads Platform API.

**Availability**:
- Apple Ads Platform API 1.0+

#### Overview

Before you can call the API, you need to perform the implementation steps in [`Implementing OAuth for the Apple Ads Platform API`](implementing-oauth-for-the-apple-ads-platform-api.md).

To call the Apple Ads Platform API, pass your access token as `Bearer` in the authorization header of HTTP requests. The value tells the API that the caller holds a valid token authorized to access the API and perform the specified actions.

The following is an example call to the API:

```console
curl "https://api.ads.apple.com/v1/" \
-H "Authorization: Bearer {access_token}" \
-H "X-AP-Context: adAccountId={adAccountId}"
```

New to the API? See [`Managing Ad Accounts and API Access`](access-overview.md) for a complete walkthrough that shows where `{access_token}` and `{adAccountId}` come from, ending in a real request like the one above.

#### Include Required Headers

Include the following headers with every request:

| Header | Description |
| --- | --- |
| `Authorization` | **Required.** The authorization value is always `Bearer`. |
| `X-AP-Context` | **Required.** Scopes the request to a specific ad account. Format: `adAccountId={adAccountId}`. Required for all ad-account-scoped operations. **Note:** This isn’t a requirement when calling [`Get User ACL`](get-user-acls.md), [`Get Me Details`](get-current-user-details.md), [`Get Org by ID`](get-orgs-_id_.md), [`Get Advertiser Resources`](get-advertiser-resources.md), or [`Create Ad Accounts`](post-ad-accounts.md). |

To return the `userId` and `orgId` of an API caller, use [`Get Me Details`](get-current-user-details.md).

#### Confirm Product Feature and Delegation Requirements

The `productFeatures` array on an ad account determines whether it can run App Store or Apple Maps campaigns. App Store ad accounts carry `APPSTORE_APP_MANUAL`, and Apple Maps ad accounts carry `BUSINESS_BRAND_MANUAL`. An account authorized for App Store can’t run campaigns on Apple Maps, and vice versa.

In addition to `productFeatures`, the ad account must also have a `delegations` entry linking it to the appropriate advertiser resource. App Store accounts need a `CONTENT_PROVIDER` delegation with the CPID as `resourceId`, and Apple Maps accounts need a `BUSINESS_BRAND` delegation with the Brand ID as `resourceId`.

Both must be in place before campaigns can go live. See [`ProductFeatures`](productfeatures.md) for details.

#### Structure Endpoint Calls

The Apple Ads API uses a REST data model. To call endpoint resources, use CRUD (create, read, update, delete) and query functions. In some cases, the call may also include a query parameter. The Apple Ads Platform API has a hierarchy with most entities as top-level resources. For example, to get all keywords in an ad group, send the `adGroupId` as a filter to the keywords query endpoint, like this:

```json
POST /v1/keywords/query

{
  "filters": [
    {
      "field": "adGroupId",
      "operator": "EQUALS",
      "value": 542317095
    }
  ]
}
```

##### Perform Partial Updates

A partial update changes a subset of object properties instead of the entire set of object properties. The API supports partial updates for most PUT calls. Only include the fields you want to change. The API leaves unset fields unchanged. Array fields are an exception. When you include an array in a PUT request, it replaces the existing values entirely. To add a single item to an array field, retrieve the current array first and send the complete desired state.

For example, the following payload updates the `name` and `status` of a campaign:

```json
PUT /v1/campaigns/{id}

{
  "name": "Updated Campaign Name",
  "status": "PAUSED"
}
```

##### Perform Bulk Operations

Bulk endpoints accept multiple items in a single request. All bulk endpoints share the same request structure, with an `items` array where each element carries a `correlationId` and a `data` object containing the operation payload. The `correlationId` is a client-supplied integer that matches each result in the response back to its input item.

Set `allowPartialSuccess: true` in the request body to enable partial success semantics, as shown below. The API processes items that pass validation even if other items fail. When you omit `allowPartialSuccess` or set it to `false`, any single item failure rejects the entire batch.

```json
POST /v1/keywords/bulk-create

{
  "allowPartialSuccess": true,
  "items": [
    {
      "correlationId": 0,
      "data": {
        "adGroupId": 555666777,
        "text": "photo editor",
        "matchType": "EXACT"
      }
    }
  ]
}
```

The response returns a `result` array with one entry per input item. Each entry includes `correlationId`, `operation`, `success`, and either the entity you created or updated or per-item error details.

For supported entities and endpoint paths, see [`Bulk Operations Endpoints`](bulk-operations-endpoints.md).

#### Query the Api

The Apple Ads Platform API uses a common query parameter structure in all `/query` endpoints. Define filtering, sort order, and pagination for a query. The API doesn’t return deleted entities unless the user specifically filters to include them.

To return all records and values for supported endpoints, use the `/query` endpoint with an empty payload.

The `/query` request structure resembles the following:

```None
POST /v1/campaigns/query

{
  "filters": [
    {
      "field": "status",
      "operator": "EQUALS",
      "value": "ENABLED"
    }
  ],
  "sorting": [
    {
      "field": "name",
      "order": "ASC"
    }
  ],
  "pagination": {
    "offset": 0,
    "pageSize": 10,
    "fetchTotalCount": true
  }
}
```

For more illustrative examples, see [`Managing Reports`](reports.md).

#### Structure the Query Request

The API performs all querying via POST requests to `/query` endpoints, not GET with query parameters. The pattern is consistent across every entity type.

The table below details the **query request fields**:

| Field | Type | Description |
| --- | --- | --- |
| `filters` | array | Filter field conditions. If the request has no filters, the API returns all non-deleted entities within the current ad account scope. It returns deleted entities only when the filters specify them. |
| `sorting` | array | Sort entities in ascending or descending order. The default behavior is to sort by ID, ascending. |
| `pagination` | pagination | Controls pagination settings for results using offset and size. |

The table below details the **filters objects**:

| Field | Type | Description |
| --- | --- | --- |
| `field` | string | To filter on a field, use its name (for example, id or name). |
| `operator` | string | Comparison operator. Supported operators vary by endpoint. See [`QueryFilterOperator`](queryfilteroperator.md) for the full list and per-operator behavior. `IS_NULL` and `IS_NOT_NULL` take no `value`. For case-insensitive matching with any string operator, set `ignoreCase` to `true` instead of using a separate operator. |
| `value` | scalar or array | One or more filter conditions applied to the result set. |
| `ignoreCase` | boolean | When `true`, the filter comparison is case-insensitive. |

The table below details the **sorting objects**:

| Field | Type | Description |
| --- | --- | --- |
| `field` | string | To sort on a field, use its name (for example, id or name). |
| `order` | string | The sort direction for the specified field: `ASC` or `DESC`. |

The table below details the **request pagination objects**:

| Field | Type | Description |
| --- | --- | --- |
| `offset` | integer | The starting position for pagination. |
| `pageSize` | integer | The number of items per page. |
| `fetchTotalCount` | boolean | When `true`, includes the total count of matching records in the response pagination metadata. Defaults to `false`. |

#### Explore the Query Objects

The following objects support querying:

- [`QueryRequest`](queryrequest.md): Drives the query. Contains optional filters, sorting, and pagination.
- [`QueryFilter`](queryfilter.md): A single filter condition. Contains field, operator (see QueryFilterOperator), value, and optional ignoreCase flag.
- [`QueryFilterOperator`](queryfilteroperator.md): The comparison operators supported in query filters.
- [`QuerySort`](querysort.md): Defines the sort order for a single field. Contains the field and order (see `QuerySortOrder`).
- [`QuerySortOrder`](querysortorder.md): The enumeration controlling the sort direction of `ASC` or `DESC`.
- [`QueryPagination`](querypagination.md): Controls the page size and offset for the result set. Contains `pageSize`, `offset`, and `fetchTotalCount`.
- [`QueryResponse`](queryresponse.md): The paginated response wrapper that contains a paginated result array of entity objects and pagination metadata.
- [`QueryPaginationResult`](querypaginationresult.md): Reflects the pagination state of the response. Contains `pageSize`, `offset`, and `totalCount`.
- [`Error`](error.md): The top-level error returned when the query fails (for example, an invalid filter field).
- [`ErrorDetail`](errordetail.md): Granular error detail with code and message.

#### Interpret Api Responses

In API responses, the `result` field is the main result object across all responses.

The response object fields are as follows:

| Field | Type | Description |
| --- | --- | --- |
| `result` | object or array | A container for the successful payload when a request succeeds |
| `pagination` | pagination | Pagination metadata on successful list responses |
| `error` | error | The primary error container |

Some endpoints instead return a dedicated `ErrorResponse` envelope on failure, which wraps a single `error` field containing the `Error` object (see [`Error`](error.md)) rather than embedding `error` alongside `result` and `pagination`. See [`ErrorResponse`](errorresponse.md) for details.

The response pagination object fields are as follows:

| Field | Type | Description |
| --- | --- | --- |
| `offset` | integer | The starting position for pagination |
| `pageSize` | integer | The number of items per page |
| `totalCount` | integer | The total number of items in the response |

The error object fields are as follows:

| Field | Type | Description |
| --- | --- | --- |
| `code` | string | The reason the API rejected the request |
| `message` | string, nullable | A human-readable error summary of what went wrong at the request level |
| `details` | array[ErrorDetail] | An array of zero or more error details objects |

The error detail object fields are as follows:

| Field | Type | Description |
| --- | --- | --- |
| `code` | string | A granular reason about one part of the error |
| `message` | string, nullable | Explicit detail about why the API rejected this part of the request |

**Successful Response**

A successful response example:

```json
{
  "result": [
    {
      "id": 542370549,
      "name": "AwayFinder_Brand"
    },
    {
      "id": 542370539,
      "name": "AwayFinder_Category"
    }
  ],
  "pagination": {
    "offset": 0,
    "pageSize": 10,
    "totalCount": 12
  }
}
```

The table below details the **error responses**:

| HTTP status code | Error message | Description |
| --- | --- | --- |
| `400` | `bad_request` | The request is malformed or contains invalid parameters. |
| `401` | `unauthorized` | The token is invalid or expired. |
| `403` | `forbidden` | The request requires higher privileges than the access token provides. |
| `404` | `not_found` | The requested resource does not exist. |
| `429` | `rate_limit_exceeded` | Too many requests in a short time. Use exponential backoff before retrying. |
| `500` | `internal_server_error` | An unexpected server-side error occurred. |

A detailed error message example:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Validation errors found",
    "details": [
      {
        "code": "DUPLICATE_NAME",
        "message": "AdGroup name already exists under this Campaign."
      }
    ]
  }
}
```

##### Handle Rate Limits

Every response, successful or not, includes a set of `RateLimit-*` headers you can use to pace requests and avoid a `429`. See [`Applying Rate Limits`](rate-limits.md) for the full header reference and a sample backoff implementation.

## Topics

### Query Objects
- [object QueryRequest](queryrequest.md)
  The standard request body used across all query endpoints, supporting filters, sorting, pagination, and field selection.
- [object QueryFilter](queryfilter.md)
  A single filter condition in a query request, specifying a field, comparison operator, and one or more values to match against.
- [object QuerySort](querysort.md)
  A sort directive in a query request, specifying a field and direction.
- [object QueryPagination](querypagination.md)
  Controls the page size and starting offset for query results.
- [object QueryResponse](queryresponse.md)
  Response wrapper for paginated query results.
- [object QueryPaginationResult](querypaginationresult.md)
  Pagination metadata returned in query responses, including page size, offset, and optional total count.
### Type Aliases
- [type QueryFilterOperator](queryfilteroperator.md)
  Enumeration of the comparison operators supported in query filters.
- [type QuerySortOrder](querysortorder.md)
  Enumeration of the sort directions available when ordering query results.
### Response
- [object Response](response.md)
  Base response wrapper used by all response types.
### Error Responses
- [object Error](error.md)
  The standard error envelope that the API returns when a request fails.
- [object ErrorDetail](errordetail.md)
  Field-level or request-level detail for a specific part of a failed API request.
- [object ErrorResponse](errorresponse.md)
  Certain endpoints return this envelope, which wraps an `Error` object, when a request fails.

## See Also

- [Implementing OAuth for the Apple Ads Platform API](implementing-oauth-for-the-apple-ads-platform-api.md)
  Generate a key pair and request an access token to authenticate with the Apple Ads Platform API.
- [Using Client Libraries](client-libraries.md)
  Integrate the Apple Ads Platform API using an Apple-maintained client library instead of a custom HTTP client.
- [Applying Rate Limits](rate-limits.md)
  Track your remaining quota and pace requests.
- [Advertising Your App on the App Store](journey-app-store-ads.md)
  Set up and launch an App Store campaign, from account verification through keyword targeting to performance reporting.
- [Advertising Your Business on Apple Maps](journey-apple-maps-brand-ads.md)
  Identify your brand, upload creative assets, build location groups, and create campaigns, ad groups, creatives, and ads to promote it on Apple Maps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/calling-apple-ads-platform-api)*