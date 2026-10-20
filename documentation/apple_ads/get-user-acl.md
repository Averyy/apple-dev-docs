# Get User ACL

**Framework**: Apple Ads  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetches roles and organizations that the API has access to.

**Availability**:
- Search Ads 5.0+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

#### Discussion

The API uses a user access control list (ACL) for policy-based authorization to determine access to resources. The Get User ACL call fetches roles in all organizations. Each role has access to all organizations or a subset of them.

##### Get user ACL example

**Request**:

```
GET https://api.searchads.apple.com/api/v5/acls
```

**Response**:

```json
{
  "data": {
    "orgName": "Trip Trek",
    "orgId": 40669820,
    "currency": "USD",
    "timeZone": "America/Los_Angeles",
    "paymentModel": "PAYG",
    "roleNames": [
      "Admin"
    ],
    "parentOrgId": "27154130",
    "displayName": "Trip Trek"
  },
  "pagination": null,
  "error": null
}
```

##### Campaign Groups

The API treats your `orgId` like a campaign group. If you need to manage Apple Ads for multiple clients, or if you need to restrict user access to a subset of your campaigns, you can create additional campaign groups within your account. Otherwise, you can create and manage all your campaigns under your default `orgId` and campaign group.

## Endpoint

`GET https://api.searchads.apple.com/api/v5/acls`

## Responses

- `200` OK (`UserAclListResponse`, `application/json`): If successful, the API returns a list of ACL objects in the response payload with an HTTP status code of `200 (OK)`. If unsuccessful, the HTTP status code indicates the error with details in the error message.
- `401` Unauthorized (`ApiErrorResponse`, `application/json`): An unauthenticated call fails to get the requested response.
- `403` Forbidden (`ApiErrorResponse`, `application/json`): Insufficient rights to the resource.
- `429` (`ApiErrorResponse`, `application/json`): The API calls exceed rate-limit thresholds. See the Rate Limits subsection of [Calling the Apple Ads API](./calling-the-apple-search-ads-api.md).
- `500` Internal Server Error (`ApiErrorResponse`, `application/json`): The Apple Ads server is temporarily down or unreachable. The request may be valid, but you need to retry it later.

## See Also

### Access Control List
- [object UserAcl](./useracl.md)
  The response to ACL requests.
- [object UserAclListResponse](./useracllistresponse.md)
  A container for ACL call responses.
- [Get Me Details](./get-me-details.md)
  Fetches details of an API caller.
- [object MeDetail](./medetail.md)
  The API caller identifiers.
- [object MeDetailResponse](./medetailresponse.md)
  The response from me detail calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/get-user-acl)*