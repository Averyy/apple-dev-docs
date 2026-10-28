# Get Me Details

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetches details of an API caller.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Mentions

- [Apple Ads Campaign Management API 4](./apple-search-ads-campaign-management-api-4.md)

## Discussion

This endpoint returns the `userId` and `parentOrgId` of an API caller. See the [`MeDetail`](./medetail.md) object.

### Get Me Details Example

**Request**:

```
curl "https://api.searchads.apple.com/api/v5/me"
-H "Authorization: Bearer {access_token}" \
-H "X-AP-Context: orgId={orgId}"
```

**Response**:

```json
{
  "data": {
    "userId": 3962840,
    "parentOrgId": 27154130
  }
}
```

## Endpoint

`GET https://api.searchads.apple.com/api/v5/me`

## Responses

- `200` OK (`MeDetailResponse`, `application/json`): If the call succeeds, the API returns the [`MeDetail`](./medetail.md) object in the response payload with an HTTP status code of 200 (OK). If unsuccessful, the HTTP status code indicates the error with details in the error message.
- `401` Unauthorized (`ApiErrorResponse`, `application/json`): An unauthenticated call fails to get the requested response.
- `403` Forbidden (`ApiErrorResponse`, `application/json`): Insufficient rights to the resource.
- `429` (`ApiErrorResponse`, `application/json`): The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [Calling the Apple Ads API](./calling-the-apple-search-ads-api.md).
- `500` Internal Server Error (`ApiErrorResponse`, `application/json`): The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.

## See Also

### Access Control List
- [Get User ACL](./get-user-acl.md)
  Fetches roles and organizations that the API has access to.
- [object UserAcl](./useracl.md)
  The response to ACL requests.
- [object UserAclListResponse](./useracllistresponse.md)
  A container for ACL call responses.
- [object MeDetail](./medetail.md)
  The API caller identifiers.
- [object MeDetailResponse](./medetailresponse.md)
  The response from me detail calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-me-details)*