# Building a distributable order package

**Framework**: Walletorders

Prepare an order for distribution by building, signing, and compressing the source files.

#### Overview

A distributable order package is a signed and compressed order ready for donating to Wallet. The order package you distribute contains the JSON description of the order, images, optional localizations, and a signature certifying the authenticity and integrity of the package.

To build an order package, you:

- Create the source files for an order. To learn more, see [`Creating the source for an order`](creating-the-source-for-an-order.md).
- Create an order type identifier.
- Generate a signing certificate.
- Create and write the manifest.
- Sign and compress the order package.

Donate the distributable order package to Wallet by setting the [`orderDetails`](https://developer.apple.com/documentation/PassKit/PKPaymentAuthorizationResult/orderDetails) property on [`PKPaymentAuthorizationResult`](https://developer.apple.com/documentation/PassKit/PKPaymentAuthorizationResult).

##### Create an Order Type Identifier

An order type identifier is a unique identifier for your company or brand. Create your order type identifier in the Certificates, Identifiers & Profiles area of the Apple Developer portal:

1. Select Identifiers and then click Add (+).
2. On the next screen, choose Order Type ID and click Continue.
3. Enter a description and the reverse DNS string to create the order type identifier.

For more information about signing in to your account and creating identifiers, see [`Developer Account Help`](https://developer.apple.comhttps://help.apple.com/developer-account/).

Set the `orderTypeIdentifier` in your `order.json` file to the identifier. Set the `orderIdentifier` key to a unique order identifier. The order identifier, in combination with the order type identifier, uniquely identifies an order within the system. For more information, see the top-level [`Order`](order.md) object.

##### Generate a Signing Certificate

Signing an order package requires a signing certificate for the order type identifier. Before you can generate a signing certificate, you need a certificate signing request (CSR). To learn how to generate a CSR, see [`Create a certificate signing request`](https://developer.apple.comhttps://help.apple.com/developer-account/#/devbfa00fef7).

Generate the signing certificate in the Certificates, Identifiers & Profiles area of the Apple Developer portal.

1. Select Certificates and then click Add (+).
2. On the next screen, choose Order Type ID Certificate and click Continue.
3. Select the Order Type ID from the dropdown menu.
4. Click Continue and upload the certificate signing request (CSR).

Install the generated certificate on the server you use for signing the order package. For more information about signing in to your account and creating signing certificates, see [`Developer Account Help`](https://developer.apple.comhttps://help.apple.com/developer-account/).

##### Create and Write the Manifest

The manifest is a JSON object that contains a dictionary of the SHA-256 hashes for each of the source files for the order. The dictionary key is the pathname of the file relative to the top level of the order, and the value is the SHA-256 hash.

Write the manifest object to a new file called `manifest.json` in the top-level directory of the source for the order. For example, the code below shows the `manifest.json` file for an order package that’s localized for English and Simplified Chinese:

```other
{
    "icon.png" : "2a1625e1e1b3b38573d086b5ec158f72f11283a0",
    "icon@2x.png" : "7321a3b7f47d1971910db486330c172a720c3e4b",
    "icon@3x.png" : "7321a3b7f47d1971910db486330c172a720c3e4b",
    "order.json" : "ef3f648e787a16ac49fff2c0daa8615e1fa15df9",
    "strip.png" : "25b737727194b5c7b26a86d57e859a054eada240",
    "en.lproj/logo.png" : "cff02680b9041b7bf637960f9f2384738c935347",
    "en.lproj/logo@2x.png" : "0e12af882204c3661fd937f6594c6b5ffc6b8a49",
    "en.lproj/logo@3x.png" : "1f103c8a07fb979ea33adfbfd031e26305fd616b",
    "en.lproj/order.strings" : "aaf7d9598f6a792755be71f492a3523d507bc212",
    "zh-Hans.lproj/logo.png" : "eca86d8a474ccd33978f6aaf98a564669d45c7ae",
    "zh-Hans.lproj/logo@2x.png" : "b6556bc2fa795d11262f17cdff04f80350398f5f",
    "zh-Hans.lproj/logo@3x.png" : "124f8381721b44b2b57bf33e30b8a9a2e0404bce",
    "zh-Hans.lproj/order.strings" : "b0b4499ba7369e4cc15bad45c251e7b9bbcad6a4",
}
```

> **Note**:  Don’t include metadata files that aren’t part of the order format, such as the `.DS_Store` file, in the manifest or distributable order package.

##### Sign and Compress the Order Package

To sign the order package, follow these steps:

1. Create a PKCS #7 detached signature for the manifest that uses the private key of the order type identifier signing certificate. Generating a PKCS #7 detached signature is a function of common cryptography libraries. For more information, see [`RFC 5652`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc5652).
2. Add the signature to the top level of the order in a file called `signature`.
3. Compress the resulting directory into a zip file.
4. Change the file extension of the resulting archive from `.zip` to `.order`.

Test your signed order package by sharing the file to an iPhone with AirDrop. Wallet shows the Add Order dialog if the order package is valid.

##### Troubleshoot Issues

If your order package doesn’t build correctly, check whether the following are all true:

- The `order.json` file contains all the required keys. For more information about required keys, see the top-level [`Order`](order.md) object.
- The value of the `orderTypeIdentifer` key in the `order.json` file matches the order type identifier of the signing certificate.
- The value of the `merchantIdentifier` key in the `order.json` file matches the Apple Developer account of the signing certificate.
- The server signing the order has a copy of the signing certificate and the [`WWDR Intermediate Certificates`](https://developer.apple.comhttps://www.apple.com/certificateauthority/).
- The certificate isn’t expired.
- The `manifest.json` contains all the source files, including those in subdirectories.
- The images are in the correct format.
- The `order.json` and `manifest.json` files use the correct JSON syntax.
- Strings that require value formats are correct, such as the `createdAt` and `updatedAt` keys of [`Order`](order.md), which require an RFC 3339 format, or `pickupWindowDuration,` which requires an ISO 8601-1 duration format.
- `updatedAt` is equal to `createdAt` if there are no updates, and `updatedAt` is monotonically increasing.
- Strings that require values from a finite set are correct, such as `Order.status` and `Order.ShippingFulfillment.status`.
- The names of localization folders use the correct language and region identifiers. For more information about language identifiers, see [`Choosing localization regions and scripts`](https://developer.apple.com/documentation/Xcode/choosing-localization-regions-and-scripts).
- Each localization folder contains all localized image files.
- Each localization folder contains the `order.strings` file for the order with localized strings.
- The keys for localized strings in the `order.json` file match those in the `order.strings` files.
- Each `order.strings` file contains the same number of localized strings and uses the same keys.

## See Also

- [Creating the source for an order](creating-the-source-for-an-order.md)
  Define an order by creating the directory structure, and adding source files and images.
- [Retrieve the registrations for a device](retrieve-the-registrations-for-a-device.md)
  Retrieves the identifiers of the orders that the device registered for.
- [Retrieve the latest version of an order](retrieve-the-latest-version-of-an-order.md)
  Retrieves the latest signed and compressed version of an order.
- [object Order](order.md)
  The order’s details, including information about the products or services rendered, customer service, and fulfillment.
- [Example Order Packages](example-order-packages.md)
  Edit, build, and add example order packages to Wallet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/WalletOrders/building-a-distributable-order-package)*