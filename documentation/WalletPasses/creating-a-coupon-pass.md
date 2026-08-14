# Creating a coupon pass

**Framework**: Wallet Passes

Construct a digital pass for discounts and special offers.

#### Overview

Use coupon passes for coupons, special offers, and other discounts. Setting the coupon pass style provides data that Wallet displays automatically, such as business information, offer expiration date, terms and conditions, store locations, and other helpful information.

![An illustration showing a mock coupon pass for a food truck with a strip image.](/images/com.apple.walletpasses/coupon@2x.png)

#### Create Your Pass Type Identifier

Signing a pass requires a signing certificate for the pass type identifier. The pass type identifier is similar to a bundle identifier, or a class name. The value for the `passTypeIdentifier` key specifies the pass type identifier. You choose a string to define a class or category of passes; the string always begins with `pass`, and uses reverse DNS style—for example, `pass.com.example.winter-coupon`. Create your pass type identifier in the [`Certificates, Identifiers & Profiles`](https://developer.apple.comhttps://developer.apple.com/account/resources) area of your Apple Developer account. The pass type identifier must match the certificate used to sign the pass. For more information on creating Wallet certificates, see [`Create Wallet identifiers and certificates`](https://developer.apple.comhttps://developer.apple.com/help/account/capabilities/create-wallet-identifiers-and-certificates/).

Use a serial number to identify the pass uniquely within the scope of its pass type. The value for the `serialNumber` key in the pass specifies the serial number. You can assign a serial number in whatever way makes sense to you, such as by using an increasing integer or a UUID.

The difference between pass type identifiers and serial numbers is similar to the difference between classes and instances of a class: pass type identifiers designate something abstract, and serial numbers identify something specific, and concrete. For example, if a store creates passes for a summer sale and for its winter discount, the summer sale passes have the same pass type identifier, but each one has its own serial number. The winter discount passes have a different pass type identifier than the summer sale passes, because they’re a different type of pass.

PassKit uses the combination of pass type identifier and serial number to uniquely identify a pass. Two passes of the same type with the same serial number represent the same pass, even if other information on them differs. For example, when a pass updates, the new version has the same pass type identifier and serial number as the old version, so the new version replaces the old version.

For more information on creating your pass type identifier, see [`Create a Pass Type Identifier`](building-a-pass#Create-a-Pass-Type-Identifier.md).

#### Add the Coupon Pass Style

The pass’s style determines the overall visual appearance of the pass and the template for placement of information on the pass. The value of the pass style key is a dictionary containing fields that hold the pass content. You specify the pass style by providing the corresponding key at the top level of the `pass.json` file. Coupon passes use the key `coupon`. For more information on building your pass json file, see [`Building a Pass`](building-a-pass.md).

The following example shows a partial pass with top-level keys for a coupon pass.

```json
{
    "description": "Coupon for winter holiday event.",
    "formatVersion": 1,
    "passTypeIdentifier": "pass.com.example.coupon-pass",
    "serialNumber": "123A4b5Z7p",
    "coupon": { ... }
}
```

The pass style controls how Wallet lays out the pass fields and which images it shows on someone’s device. The following image shows a layout and placement of fields for the coupon pass style.

![An illustration showing a coupon pass layout with the pass fields for each section of the pass.](/images/com.apple.walletpasses/pass-fields-layout-coupon@2x.png)

The pass style determines the maximum number of pass fields that can appear on the front of a pass. A coupon can have up to three header fields, a single primary field, and up to four secondary and auxiliary fields combined. The text length in each pass field determines how many fields appear on the front of the pass. If text is too long, Wallet won’t display all of it. Space on the front of the pass is limited as well. You can use the primary pass field for a strip image that creates a banner across the pass, or for important business information. Use the secondary and auxiliary fields for information like expiration dates, store locations, and contact information.

The back of the pass can have as many fields as you need, and the contents of the fields can be longer if necessary to convey extra information about terms and conditions, and general information helpful for your pass viewers.

> ❗ **Important**: On the back of the pass, include contact information for the organization that signed the pass. If users interact with a different organization to redeem the pass, you may choose to provide two sets of contact information. For more information, see [`App Store Review Guidelines`](https://developer.apple.comhttps://developer.apple.com/app-store/review/guidelines/).

For more information on pass fields, see [`PassFields`](passfields.md). For more information on the coupon pass object, see [`Pass.Coupon`](pass/coupon-data.dictionary.md).

The following example shows a `pass.json` file with the `coupon` pass style and pass fields:

```json
{
    "formatVersion": 1,
    "passTypeIdentifier": "pass.com.example.coupon-pass",
    "serialNumber": "123A4b5Z7p",
    "teamIdentifier": "ABCD1234",
    "webServiceURL": "https://example.com/passes/",
    "authenticationToken": "xyz18vnkabn3789dtoBsk77v",
    "barcodes": {
        "message": "12345678",
        "format": "PKBarcodeFormatCode128",
        "messageEncoding": "iso-8859-1"
    },
    "organizationName": "My company name"
    "description": "Winter holiday coupon",
    "logoText": "My company",
    "foregroundColor": "rgb(245, 237, 95)",
    "backgroundColor": "rgb(34, 107, 72)",
    "coupon": {
        "primaryFields": [
            {
                "key": "offer",
                "label": "All holiday items.",
                "value": "25% off"
            }
        ],
        "auxiliaryFields": [
            {
                "key": "expires",
                "label": "EXPIRES",
                "value": "2026-03-01T10:00-05:00",
                "isRelative": true,
                "dateStyle": "PKDateStyleShort"
            }
        ],
        "backFields": [
            {
                "key": "customer-service",
                "label": "Customer service",
                "value": "(800) 555-5555"
            },
            {
                "key": "terms",
                "label": "Terms and Conditions",
                "value": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam
                        fermentum vestibulum est. Cras rhoncus. Pellentesque habitant morbi
                        tristique senectus et netus et malesuada fames ac turpis egestas. Sed
                        quis tortor. Donec non ipsum. Mauris condimentum, odio nec porta
                        tristique, ante neque malesuada massa, in dignissim eros velit at
                        tellus. Donec et risus in ligula eleifend consectetur. Donec volutpat
                        eleifend augue. Integer gravida sodales leo. Nunc vehicula neque ac
                        erat. Vivamus non nisl. Fusce ac magna. Suspendisse euismod libero eget
                        mauris"
            }
        ]
    }
}
```

> **Note**:  A pass viewed on an Apple Watch doesn’t show the strip image (banner image), thumbnail image, and back of pass information.

#### Provide Scannable Codes

Passes can work with Near Field Communication (NFC) readers and barcodes. Someone can hold a device near an NFC reader with the contactless symbol to use their pass. When employing NFC, the pass doesn’t need a barcode.

Alternatively, passes can use scannable barcodes to convey information. Wallet supports QR, PDF417, Aztec, Code128, Code 39, Codabar, EAN-13, and Interleaved 2 of 5 (ITF) barcode formats. Wallet optimizes the presentation of passes in order to facilitate a successful scan.

For more information on barcodes, see [`Pass.Barcodes`](pass/barcodes-data.dictionary.md) and the [`Add to Apple Wallet Guidelines`](https://developer.apple.comhttps://developer.apple.com/wallet/add-to-apple-wallet-guidelines/).

For design guidance about coupon passes, see Human Interface Guidelines > Wallet > Passes > [`Coupons`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/wallet#Coupons).

#### Debug the Pass

If the pass doesn’t display and add to Wallet, check the logs for a description of what went wrong. If you’re using Simulator to debug, you can drag your `.pkpass` file into the Simulator, then use the Console app on your Mac to view the Simulator device logs.

When testing on a device, errors are logged to the device’s console, which you can view from the Xcode organizer window. You can filter the logs by using your pass type ID or serial number to limit the device log output to a specific pass instance. See [`Acquiring crash reports and diagnostic logs`](https://developer.apple.com/documentation/xcode/acquiring-crash-reports-and-diagnostic-logs) for information on accessing a device’s console log, as well as downloading and installing the Wallet profile.

Common errors include malformed JSON files, misspelled keys or values, pass type identifiers that don’t match your certificate, and signatures that omit the Apple Worldwide Developer Relations Intermediate Certificate. For more information on common issues with pass creation, see [`Common Problems`](building-a-pass#Common-Problems.md).

## See Also

- [object Pass.Coupon](pass/coupon-data.dictionary.md)
  An object that represents the groups of fields that display the information for a coupon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/creating-a-coupon-pass)*