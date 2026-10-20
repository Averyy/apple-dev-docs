# Retrieve the latest version of an order

**Framework**: Wallet Orders  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Retrieves the latest signed and compressed version of an order.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+

#### Discussion

The device uses this endpoint for both initial and subsequent attempts to retrieve an order. Make sure you support standard HTTP caching on this endpoint.

## Endpoint

`GET https://your-web-service.com/v1/orders/{orderTypeIdentifier}/{orderIdentifier}`

## Parameters

### Path Parameters

- `orderIdentifier` (string) *(required)*: The order identifier. This value corresponds to the value of the `orderIdentifier` key of the [`Order`](./order.md).
- `orderTypeIdentifier` (string) *(required)*: The order type identifier of the order. This value corresponds to the value of the `orderTypeIdentifier` key of the [`Order`](./order.md).

### Header Parameters

- `Authorization` (string) *(required)*: The authentication for an order. The scheme is `AppleOrder` with the [`Order`](./order.md)’s value for the `authenticationToken` key as parameter. For example, `AppleOrder {authenticationToken}`.

  **Allowed Values**: `AppleOrder {authenticationToken}`
- `If-Modified-Since` (string): If available, the most recent `If-Modified` value.

## Responses

- `200` OK (`application/vnd.apple.finance.order`): The request was successful and the response includes the [`Order`](./order.md) data as payload.
- `304` Not Modified: The request wasn’t modified since it was last loaded.
- `401` Request Not Authorized: The request isn’t authorized.

## See Also

### Essentials
- [Creating the source for an order](./creating-the-source-for-an-order.md)
  Define an order by creating the directory structure, and adding source files and images.
- [Building a distributable order package](./building-a-distributable-order-package.md)
  Prepare an order for distribution by building, signing, and compressing the source files.
- [Retrieve the registrations for a device](./retrieve-the-registrations-for-a-device.md)
  Retrieves the identifiers of the orders that the device registered for.
- [object Order](./order.md)
  The order’s details, including information about the products or services rendered, customer service, and fulfillment.
- [Example Order Packages](./example-order-packages.md)
  Edit, build, and add example order packages to Wallet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletorders/retrieve-the-latest-version-of-an-order)*