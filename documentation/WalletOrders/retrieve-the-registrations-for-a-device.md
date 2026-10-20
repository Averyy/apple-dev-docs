# Retrieve the registrations for a device

**Framework**: Wallet Orders  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Retrieves the identifiers of the orders that the device registered for.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+

## Endpoint

`GET https://your-web-service.com/v1/devices/{deviceIdentifier}/registrations/{orderTypeIdentifier}?ordersModifiedSince={lastModified}`

## Parameters

### Path Parameters

- `orderTypeIdentifier` (string) *(required)*: The order type identifier of the order. This value corresponds to the value of the `orderTypeIdentifier` key of the [`Order`](./order.md).
- `deviceIdentifier` (string) *(required)*: A unique identifier used to recognize and authenticate the device.

### Query Parameters

- `lastModified` (string): The value of the `lastModified` key from the response to a previous request. This value limits the results of the current request to the orders modified since the previous request.

## Responses

- `200` Matching Orders (`OrderIdentifiers`, `application/json`): The request was successful and the response includes the identifiers for the matching orders.
- `204` No Matching Orders: There are no matching orders.

## See Also

### Essentials
- [Creating the source for an order](./creating-the-source-for-an-order.md)
  Define an order by creating the directory structure, and adding source files and images.
- [Building a distributable order package](./building-a-distributable-order-package.md)
  Prepare an order for distribution by building, signing, and compressing the source files.
- [Retrieve the latest version of an order](./retrieve-the-latest-version-of-an-order.md)
  Retrieves the latest signed and compressed version of an order.
- [object Order](./order.md)
  The order’s details, including information about the products or services rendered, customer service, and fulfillment.
- [Example Order Packages](./example-order-packages.md)
  Edit, build, and add example order packages to Wallet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletorders/retrieve-the-registrations-for-a-device)*