# Understanding webhook events

**Framework**: Apple School Manager and Apple Business APIs  
**Role**: Article

Learn how to authenticate and process webhook notifications from Apple Business and the data each event contains.

### Overview

Webhooks notify your systems when something changes in your organization so you don’t have to poll the API. When a subscribed event occurs, Apple sends an HTTPS POST with a JSON payload to the URL you specify. When you create or update a webhook, use `eventTypes` to choose the events it receives. For the available values, see [`WebhookEventType`](../AppleBusinessAPI/webhookeventtype.md).

Each notification is a [`WebhookDelivery`](../AppleBusinessAPI/webhookdelivery.md) that links to a [`WebhookEvent`](../AppleBusinessAPI/webhookevent.md). The event’s `eventType` attribute identifies the kind of event, and its `payload` attribute contains the event data as a JSON string. To review the deliveries for a webhook, see [`Get All Deliveries for a Webhook`](../AppleBusinessAPI/get-all-deliveries-for-a-webhook.md). To retry a delivery, see [`Create a WebhookDelivery`](../AppleBusinessAPI/create-a-webhookdelivery.md).

### Set up notification authentication

Secure your webhook by verifying that a request to your endpoint comes from Apple Business. The security protocol for webhooks is hash-based message authentication code (HMAC), which requires that you:

- Share a secret phrase with the request sender (Apple Business).
- Verify that each POST to your endpoint has the HMAC header and validate it with your secret.

When you create or update a webhook, you define the secret phrase using the `secret` attribute in [`WebhookCreateRequest`](../AppleBusinessAPI/webhookcreaterequest.md) or [`WebhookUpdateRequest`](../AppleBusinessAPI/webhookupdaterequest.md). You need to choose a string value for `secret` that’s difficult to guess. Apple Business then creates a hash signature using the secret and includes it in each POST. The signature resides in the request header as `x-apple-signature`. You verify the signature by implementing code in your webhook endpoint that:

1. Creates a hash from the payload body using your secret.
2. Compares the hash to the one Apple Business sends in the header to ensure they match.

For example, applying HMAC-SHA256 to the secret “This is my secret” and payload body “Hello, World!” produces this hash:

```
7f062172b01cb00b53ca068614674a3d982a34062a0f5d37687d5e3377e54657
```

This result verifies a POST is authentic (the sender knows the secret) if the request contains the header:

```
x-apple-signature: hmacsha256=7f062172b01cb00b53ca068614674a3d982a34062a0f5d37687d5e3377e54657
```

Use an implementation of HMAC hex digest to generate the hash. For more information, see GitHub’s [Validating webhook deliveries](https://docs.github.com/en/webhooks/using-webhooks/validating-webhook-deliveries).

### Parse webhook notifications

When Apple Business sends a notification to your webhook, it does so in the form of an HTTP POST. When you receive a notification, check its type to process it accordingly. The action you perform depends on the notification type. Each type has a specific dataset, or schema, composed of attributes that drive the different actions you take. For the types of events and their schemas, see the sections below.

### Process a specific notification

This example uses the notification type `orgDeviceRelationshipAssignedServerChanged`. The attributes include the serial number of the device and the ID of the device management service it’s now assigned to. The payload includes a relationship to the device (`instance`) and one to the new device management service (`newAssignedServer`). Use this information to read more about the device using [`Get Device Information`](../AppleBusinessAPI/get-orgdevice-information.md), and about the device management service using [`Get Device Management Service Information`](../AppleBusinessAPI/get-mdmserver-information.md).

```json
{
  "data": {
    "type": "orgDeviceRelationshipAssignedServerChanged",
    "id": "812ada8f-d313-4148-b9db-2f0b50a7b009",
    "version": 1,
    "attributes": {
      "orgDeviceSerialNumber": "XABC123DEF4",
      "newMdmServerId": "1F97349736CF4614A94F624E705841AD"
    },
    "relationships": {
      "instance": {
        "data": {
          "type": "orgDevices",
          "id": "XABC123DEF4"
        },
        "links": {
          "self": "https://api-business.apple.com/v1/orgDevices/XABC123DEF4"
        }
      },
      "newAssignedServer": {
        "data": {
          "type": "mdmServers",
          "id": "1F97349736CF4614A94F624E705841AD"
        },
        "links": {
          "self": "https://api-business.apple.com/v1/mdmServers/1F97349736CF4614A94F624E705841AD"
        }
      }
    }
  }
}
```

### Events

> **Note**: The example payloads in this article use placeholder values.

Every event payload has the same structure:

- `type` is the event type, in a format that matches the `eventType` value.
- `id` is the opaque ID that uniquely identifies the event.
- `version` is the version of the event’s schema.
- `attributes` contains the event-specific values.
- `relationships` links to the resources the event relates to. The `instance` relationship always refers to the resource that changed.

#### Webhook ping

Verify your server is receiving notifications.

After you create a webhook and set up your server to receive notifications, send a test ping to verify that your server is receiving them. Call [`Create a WebhookPing`](../AppleBusinessAPI/create-a-webhookping.md) with a payload like this, where the `id` for type `webhooks` is the unique identifier from the response to [`Create a Webhook`](../AppleBusinessAPI/create-a-webhook.md), [`Get Webhooks`](../AppleBusinessAPI/get-webhooks.md), or [`Get Webhook Information`](../AppleBusinessAPI/get-webhook-information.md):

```json
{
  "data": {
    "type": "webhookPings",
    "relationships": {
      "webhook": {
        "data": {
          "type": "webhooks",
          "id": "string"
        }
      }
    }
  }
}
```

Apple Business then sends a `webhookPingCreated` event to the webhook’s URL. You can’t subscribe to this event type, so it doesn’t appear in [`WebhookEventType`](../AppleBusinessAPI/webhookeventtype.md). The `isPingEvent` attribute of the [`WebhookEvent`](../AppleBusinessAPI/webhookevent.md) is `true`.

| Field | Type | Description |
| --- | --- | --- |
| `attributes.createdDateTime` | DateTime | The date and time the ping was created. |

```json
{
  "data": {
    "type": "webhookPingCreated",
    "id": "9be761ff-131c-4652-9df8-b779e8adee29",
    "version": 1,
    "attributes": {
      "createdDateTime": "2026-10-14T17:24:54.096092003Z"
    }
  }
}
```

To check whether the ping reached your server, review the webhook’s past deliveries with [`Get All Deliveries for a Webhook`](../AppleBusinessAPI/get-all-deliveries-for-a-webhook.md). Each delivery’s `deliveryState` is `SUCCEEDED`, `FAILED`, or `PENDING`. If a delivery fails:

- `errorMessage` describes the system error when your server returned no HTTP response, such as when the host couldn’t be resolved.
- `response.httpStatusCode` and `response.body` describe your server’s response. The `body` is present only when the status code isn’t 2xx.

After you fix the problem, use [`Create a WebhookDelivery`](../AppleBusinessAPI/create-a-webhookdelivery.md) to request a redelivery of a past delivery.

#### Device attribute changed

Event type: `ORG_DEVICE_ATTRIBUTE_CHANGED`

Sent when an attribute of a device in your organization changes.

| Field | Type | Description |
| --- | --- | --- |
| `attributes.orgDeviceSerialNumber` | String | The serial number of the device whose attributes changed. |
| `relationships.instance` | Relationship to `orgDevices` | The device that changed. |

```json
{
  "data": {
    "type": "orgDeviceAttributeChanged",
    "id": "813ef0fa-ce41-4c3f-88dc-b97096670b26",
    "version": 1,
    "attributes": {
      "orgDeviceSerialNumber": "XABC123DEF4"
    },
    "relationships": {
      "instance": {
        "data": {
          "type": "orgDevices",
          "id": "XABC123DEF4"
        },
        "links": {
          "self": "https://api-business.apple.com/v1/orgDevices/XABC123DEF4"
        }
      }
    }
  }
}
```

#### Device migration details changed

Event type: `ORG_DEVICE_ATTRIBUTE_MIGRATION_DETAILS_CHANGED`

Sent when the device management service migration details of a device change.

| Field | Type | Description |
| --- | --- | --- |
| `attributes.orgDeviceSerialNumber` | String | The serial number of the device whose migration details changed. |
| `relationships.instance` | Relationship to `orgDevices` | The device that changed. |

```json
{
  "data": {
    "type": "orgDeviceAttributeMigrationDetailsChanged",
    "id": "e00313e9-d0ee-41d4-b13f-f23a23495941",
    "version": 1,
    "attributes": {
      "orgDeviceSerialNumber": "XABC123DEF4"
    },
    "relationships": {
      "instance": {
        "data": {
          "type": "orgDevices",
          "id": "XABC123DEF4"
        },
        "links": {
          "self": "https://api-business.apple.com/v1/orgDevices/XABC123DEF4"
        }
      }
    }
  }
}
```

#### Device assigned server changed

Event type: `ORG_DEVICE_RELATIONSHIP_ASSIGNED_SERVER_CHANGED`

Sent when the device management service assigned to a device changes.

| Field | Type | Description |
| --- | --- | --- |
| `attributes.orgDeviceSerialNumber` | String | The serial number of the device whose associated AppleCare coverage changed. |
| `attributes.newMdmServerId` | String | The ID of the device management service that the device is now assigned to. |
| `relationships.instance` | Relationship to `orgDevices` | The device that changed. |
| `relationships.newAssignedServer` | Relationship to `mdmServers` | The device management service that the device is now assigned to. |

```json
{
  "data": {
    "type": "orgDeviceRelationshipAssignedServerChanged",
    "id": "812ada8f-d313-4148-b9db-2f0b50a7b009",
    "version": 1,
    "attributes": {
      "orgDeviceSerialNumber": "XABC123DEF4",
      "newMdmServerId": "1F97349736CF4614A94F624E705841AD"
    },
    "relationships": {
      "instance": {
        "data": {
          "type": "orgDevices",
          "id": "XABC123DEF4"
        },
        "links": {
          "self": "https://api-business.apple.com/v1/orgDevices/XABC123DEF4"
        }
      },
      "newAssignedServer": {
        "data": {
          "type": "mdmServers",
          "id": "1F97349736CF4614A94F624E705841AD"
        },
        "links": {
          "self": "https://api-business.apple.com/v1/mdmServers/1F97349736CF4614A94F624E705841AD"
        }
      }
    }
  }
}
```

#### Device warranty changed

Event type: `ORG_DEVICE_RELATIONSHIP_WARRANTY_CHANGED`

Sent when the AppleCare coverage of a device changes.

| Field | Type | Description |
| --- | --- | --- |
| `attributes.orgDeviceSerialNumber` | String | The serial number of the device for which an associated AppleCare changed. |
| `attributes.appleCareCoverageId` | String | The ID of the AppleCare coverage that changed. |
| `relationships.instance` | Relationship to `orgDevices` | The device that changed. |

```json
{
  "data": {
    "type": "orgDeviceRelationshipWarrantyChanged",
    "id": "7de7d1dd-5830-4104-b03e-d861faa1fd1a",
    "version": 1,
    "attributes": {
      "orgDeviceSerialNumber": "XABC123DEF4",
      "appleCareCoverageId": "H2WN4ZX7QK"
    },
    "relationships": {
      "instance": {
        "data": {
          "type": "orgDevices",
          "id": "XABC123DEF4"
        },
        "links": {
          "self": "https://api-business.apple.com/v1/orgDevices/XABC123DEF4"
        }
      }
    }
  }
}
```

## See Also

### Webhooks
- [Get Webhooks](../AppleBusinessAPI/get-webhooks.md)
  Get a list of webhooks in an organization.
- [Get Webhook Information](../AppleBusinessAPI/get-webhook-information.md)
  Get information about a specific webhook in an organization.
- [Create a Webhook](../AppleBusinessAPI/create-a-webhook.md)
  Create a new webhook in an organization.
- [Update a Webhook](../AppleBusinessAPI/update-a-webhook.md)
  Update an existing webhook in an organization.
- [Delete a Webhook](../AppleBusinessAPI/delete-a-webhook.md)
  Delete a webhook from an organization.
- [Get All Deliveries for a Webhook](../AppleBusinessAPI/get-all-deliveries-for-a-webhook.md)
  Get a list of deliveries for a webhook.
- [Create a WebhookDelivery](../AppleBusinessAPI/create-a-webhookdelivery.md)
  Create a new webhook delivery based on an existing delivery.
- [Create a WebhookPing](../AppleBusinessAPI/create-a-webhookping.md)
  Send a ping event to a webhook to test that it receives notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-school-and-business-manager-api/understanding-apple-business-api-webhook-events)*