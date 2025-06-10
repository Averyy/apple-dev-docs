# Retrieve the latest version of an order

**Framework**: Wallet Orders  
**Kind**: httpRequest

Retrieves the latest signed and compressed version of an order.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+

#### Discussion

The device uses this endpoint for both initial and subsequent attempts to retrieve an order. Make sure you support standard HTTP caching on this endpoint.

## See Also

- [Creating the source for an order](creating-the-source-for-an-order.md)
  Define an order by creating the directory structure, and adding source files and images.
- [Building a distributable order package](building-a-distributable-order-package.md)
  Prepare an order for distribution by building, signing, and compressing the source files.
- [Retrieve the registrations for a device](retrieve-the-registrations-for-a-device.md)
  Retrieves the identifiers of the orders that the device registered for.
- [object Order](order.md)
  The order’s details, including information about the products or services rendered, customer service, and fulfillment.
- [Example Order Packages](example-order-packages.md)
  Edit, build, and add example order packages to Wallet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletorders/retrieve-the-latest-version-of-an-order)*