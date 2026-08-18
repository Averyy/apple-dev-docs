# Org & Me Endpoints

**Framework**: Apple Ads Platform API

Retrieve the authenticated user’s identity, organization details, and ad account access list.

**Availability**:
- apple-ads-platform-api 1.0+

#### Overview

This group exposes the following endpoints:

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/v1/me` | [`Get Me Details`](get-current-user-details.md) returns a `MeResponse` with the `userId` and `orgId` bound to the authenticated caller’s access token. |
| `GET` | `/v1/acls` | [`Get User ACL`](get-user-acls.md) returns a list of `UserAcl` entries identifying every ad account the token can access and the role assigned to each. |
| `GET` | `/v1/orgs/{id}` | [`Get Org by ID`](get-orgs-_id_.md) returns an `OrgResponse` with the organization’s name, currency, timezone, payment model, and system status. |

Call `GET /v1/me`, `GET /v1/acls`, and `GET /v1/orgs/{id}` in that order to confirm identity and discover accessible ad accounts. `GET /v1/acls` is the recommended starting point for determining which ad accounts a token can manage.

> **Note**: `GET /v1/me`, `GET /v1/acls`, and `GET /v1/orgs/{id}` do not require the `X-AP-Context` header. Supply `X-AP-Context` only for ad-account-scoped operations.

## Topics

- [Get Me Details](get-current-user-details.md)
  Return the user ID and organization ID of the authenticated API caller.
- [Get User ACL](get-user-acls.md)
  Return the ad accounts and roles accessible to the authenticated API caller.
- [Get Org by ID](get-orgs-_id_.md)
  Retrieve the details of a specific organization by its ID.

## See Also

- [Managing Ad Accounts and API Access](access-overview.md)
  Authenticate your requests, scope them to an ad account, and apply role-based access levels.
- [Ad Account Endpoints](ad-account-endpoints.md)
  Create, retrieve, and update ad accounts, and discover delegable advertiser resources.
- [Account Management Data Objects](account-management-data-objects.md)
  Reference the data objects for account management, access control, and organization resources.
- [Account Management Data Types](account-management-data-types.md)
  Reference the enumerations and scalar types for account management, access control, and organization resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/org-me)*