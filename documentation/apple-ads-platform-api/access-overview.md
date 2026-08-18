# Managing Ad Accounts and API Access

**Framework**: Apple Ads Platform API

Authenticate your requests, scope them to an ad account, and apply role-based access levels.

**Availability**:
- Apple Ads Platform API 1.0+

#### Overview

Obtain an access token via the Apple Ads OAuth2 flow. Pass it as:

```None
Authorization: Bearer <access_token>
```

See [`Implementing OAuth for the Apple Ads Platform API`](implementing-oauth-for-the-apple-ads-platform-api.md) for the full OAuth setup walkthrough.

All ad account scoped endpoints require an `X-AP-Context` header that identifies the ad account you’re accessing:

```None
X-AP-Context: adAccountId=<id>
```

You don’t need the header for `GET /v1/me`, `GET /v1/acls`, `GET /v1/orgs/{id}`, `GET /v1/advertiser-resources`, or `POST /v1/ad-accounts`.

#### Explore the Account Management Endpoints

The following endpoints handle authentication, ad account management, and access control:

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/v1/me` | [`Get Me Details`](get-current-user-details.md) returns the userId and orgId for the authenticated caller. |
| `POST` | `/v1/ad-accounts` | [`Create Ad Accounts`](post-ad-accounts.md) creates a new ad account under a specified org. |
| `GET` | `/v1/ad-accounts/{id}` | [`Get Ad Account by ID`](get-ad-accounts-_id_.md) retrieves full details for a specific ad account. |
| `PUT` | `/v1/ad-accounts/{id}` | [`Update Ad Accounts`](put-ad-accounts-_id_.md) updates an ad account’s name or delegations. |
| `GET` | `/v1/advertiser-resources` | [`Get Advertiser Resources`](get-advertiser-resources.md) retrieves the advertiser resources (brands, content providers) eligible to be delegated to an ad account. |
| `GET` | `/v1/acls` | [`Get User ACL`](get-user-acls.md) returns a list of ad accounts and roles accessible to the authenticated caller. |
| `GET` | `/v1/orgs/{id}` | [`Get Org by ID`](get-orgs-_id_.md) retrieves the details of a specific organization by its ID. |

#### Make Your First Api Call

This walkthrough takes you from an access token to a real ad account response, start to finish.

##### Get an Access Token

Request a token from the authorization server using the client credentials you set up in [`Implementing OAuth for the Apple Ads Platform API`](implementing-oauth-for-the-apple-ads-platform-api.md):

```console
curl -X POST "https://appleid.apple.com/auth/oauth2/token" \
  -H "Host: appleid.apple.com" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials" \
  -d "client_id={client_id}" \
  -d "client_secret={client_secret}" \
  -d "scope=searchadsorg"
```

The server returns:

```json
{
  "access_token": "{access_token}",
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "searchadsorg"
}
```

Save `access_token`. Every call below sends it as `Authorization: Bearer {access_token}`.

##### Confirm Your User and Org

The `GET /v1/me` endpoint doesn’t require an `X-AP-Context` header, so you can call it right after you get your token:

```console
curl "https://api.ads.apple.com/v1/me" \
  -H "Authorization: Bearer {access_token}"
```

The response includes your `userId` and `orgId`:

```json
{
  "result": {
    "userId": 3962840,
    "orgId": 27154130
  }
}
```

##### Discover Your Ad Accounts

The `GET /v1/acls` endpoint also doesn’t require an `X-AP-Context` header. It returns every ad account your token can access and your role on each one:

```console
curl "https://api.ads.apple.com/v1/acls" \
  -H "Authorization: Bearer {access_token}"
```

The response lists each accessible ad account alongside your roles:

```json
{
  "result": {
    "acls": [
      {
        "adAccount": {
          "id": 123456789,
          "name": "AwayFinder",
          "orgId": 27154130
        },
        "roles": ["Admin"]
      }
    ]
  }
}
```

Save the `adAccount.id` you want to work with. That value is your `adAccountId`.

If `acls` comes back empty, your org has no ad accounts yet. See “Create an Ad Account” further down this page, then return here with the new account’s `id` before continuing to Make Your First Ad Account Scoped Call.

##### Make Your First Ad Account Scoped Call

The `GET /v1/ad-accounts/{id}` endpoint is ad account scoped, so it requires the `X-AP-Context` header set to the `adAccountId` from Discover Your Ad Accounts, above:

```console
curl "https://api.ads.apple.com/v1/ad-accounts/123456789" \
  -H "Authorization: Bearer {access_token}" \
  -H "X-AP-Context: adAccountId=123456789"
```

The response returns the full ad account record:

```json
{
  "result": {
    "id": 123456789,
    "name": "AwayFinder Ad Account",
    "orgId": 27154130,
    "timezone": "America/New_York",
    "currency": "USD",
    "paymentModel": "PAYG",
    "systemStatus": "ACTIVE",
    "systemStatusReasons": [],
    "productFeatures": ["APPSTORE_APP_MANUAL"],
    "delegations": [
      {
        "resourceId": "12345678",
        "resourceType": "CONTENT_PROVIDER",
        "resourceName": "AwayFinder Apps"
      }
    ],
    "creationTime": "2025-01-10T08:00:00.000",
    "modificationTime": "2025-01-10T08:00:00.000"
  }
}
```

You now have a `userId`, `orgId`, and `adAccountId`, and you’ve made a real, authenticated, ad account scoped call. From here:

- To find the brands or content providers available across your org and identify which one to delegate to an account, use `GET /v1/advertiser-resources?resourceType=<type>`.
- Every response above also includes `RateLimit-*` headers you can use to pace requests before hitting a `429`. See [`Applying Rate Limits`](rate-limits.md) for the full header reference and a sample backoff implementation.
- Ready to build a campaign? Follow the [`Advertising Your App on the App Store`](journey-app-store-ads.md) or [`Advertising Your Business on Apple Maps`](journey-apple-maps-brand-ads.md) journey guide next.

#### Understand the Organization Hierarchy

An Org (organization) is the top-level owner. Each Org can have multiple Ad Accounts. Delegations attach advertiser resources (brands, content providers) to ad accounts.

The API uses a three-level hierarchy: **Org** → **Ad Accounts** → **Campaigns**. Each ad account belongs to exactly one org, and that relationship is immutable.

#### Understand Ad Account Product Features

Each ad account carries a `productFeatures` array that determines whether its campaigns can target App Store or Apple Maps.

App Store ad accounts carry the `APPSTORE_APP_MANUAL` feature. Apple Maps ad accounts carry the `BUSINESS_BRAND_MANUAL` feature. An account authorized for App Store can’t run campaigns on Apple Maps, and vice versa.

See [`ProductFeatures`](productfeatures.md) for a full description of each value.

#### Create an Ad Account

To create an ad account, make a POST request to `/v1/ad-accounts`. See [`AdAccountCreate`](adaccountcreate.md) for the required parameters. To link the account to an App Store or Apple Maps resource, use `delegations`.

A newly created account receives a `systemStatus` of `ACTIVE` or `INACTIVE`. When the status is `INACTIVE`, the `systemStatusReasons` array identifies the blocking condition. Campaigns under an inactive account don’t serve until you resolve the blocking condition.

#### Update an Ad Account

To update an ad account, make a PUT request to `/v1/ad-accounts/{id}` with an [`AdAccountUpdate`](adaccountupdate.md) body. The request updates only the fields you include in the body.

All array fields use full-replacement semantics. If you send a partial array, the system removes any items not included in the request. To add a single item to an array field, retrieve the current array first, then send the complete desired state.

#### Find Advertiser Resources

Advertiser resources are brands and content providers available across your organization that you can delegate to an ad account. To retrieve the advertiser resources available in your organization, filtered by resource type, use `GET /v1/advertiser-resources`. The `resourceType` query parameter is required. Omitting it returns a validation error.

#### Retrieve Access Control Lists Acls

Call `GET /v1/acls` to retrieve the `UserAccessResult` for the authenticated user. Each acl entry (`UserAcl`) contains:

- `adAccount`: the ad account this entry covers
- `roles`: the list of role names the user holds for that account

See [`Get User ACL`](get-user-acls.md) for full request and response details.

#### Look Up Available Roles

For the full list of `roles` values and their access levels, see [`User ACL`](useracl.md).

## See Also

- [Org & Me Endpoints](org-me.md)
  Retrieve the authenticated user’s identity, organization details, and ad account access list.
- [Ad Account Endpoints](ad-account-endpoints.md)
  Create, retrieve, and update ad accounts, and discover delegable advertiser resources.
- [Account Management Data Objects](account-management-data-objects.md)
  Reference the data objects for account management, access control, and organization resources.
- [Account Management Data Types](account-management-data-types.md)
  Reference the enumerations and scalar types for account management, access control, and organization resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/access-overview)*