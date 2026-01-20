# Creating a generic pass

**Framework**: Wallet Passes

Construct a digital pass with information that enables people to take action.

#### Overview

The generic pass style is for passes that don’t fit into the boarding, coupon, event, or store card pass categories. You might use the generic pass style for a gym membership card, library card, valet claim ticket, or other kind of pass. Setting the generic pass style provides data that Wallet displays automatically, such as business information, a barcode, terms and conditions, store locations, and other helpful information.

![An illustration showing an example generic pass for a mock gym membership.](https://docs-assets.developer.apple.com/published/2f8c9366433d611399132b3075659cba/generic-pass-design%402x.png)

#### Create Your Pass Type Identifier

Signing a pass requires a signing certificate for the , which is similar to a bundle identifier, or a class name. The value for the `passTypeIdentifier` key specifies the pass type identifier. You choose a string to define a class or category of passes; the string always begins with `pass`, and uses reverse DNS style—for example, `pass.com.example.membership-card`. Create your pass type identifier in the [`Certificates, Identifiers & Profiles`](https://developer.apple.comhttps://developer.apple.com/account/resources) area of your Apple Developer account. The pass type identifier must match the certificate used to sign the pass. For more information on creating Wallet certificates, see [`Create Wallet identifiers and certificates`](https://developer.apple.comhttps://developer.apple.com/help/account/capabilities/create-wallet-identifiers-and-certificates/).

Use a serial number to identify the pass uniquely within the scope of its pass type. The value for the `serialNumber` key in the pass specifies the serial number. You can assign a serial number in whatever way makes sense to you, such as by using an increasing integer or a UUID.

The difference between pass type identifiers and serial numbers is similar to the difference between classes and instances of a class: pass type identifiers designate something abstract, and serial numbers identify something specific, and concrete. For example, if a store creates passes for a locker rental and for its membership card program, the locker rental passes have the same pass type identifier, but each one has its own serial number. The membership cards have a different pass type identifier than the locker rental passes, because they’re a different type of pass.

PassKit uses the combination of pass type identifier and serial number to uniquely identify a pass. Two passes of the same type with the same serial number represent the same pass, even if other information on them differs. For example, when a pass updates, the new version has the same pass type identifier and serial number as the old version, so the new version replaces the old version.

For more information on creating your pass type identifier, see [`Create a Pass Type Identifier`](building-a-pass#Create-a-Pass-Type-Identifier.md).

#### Add the Generic Pass Style

The pass’s style determines the overall visual appearance of the pass and the template for placement of information on the pass. The value of the pass style key is a dictionary containing fields that hold the pass content. Specify the pass style by providing the corresponding key at the top level of the `pass.json` file; generic passes use the key `generic`. For more information on building your pass json file, see [`Building a Pass`](building-a-pass.md).

The following example shows a partial generic pass with top-level keys.

```json
{
    "description": "A gym membership pass.",
    "formatVersion": 1,
    "passTypeIdentifier": "pass.com.example.membership-pass",
    "serialNumber": "123A4b5Z7p",
    "generic": { ... }
}
```

The pass style controls how Wallet lays out the pass fields and which images it shows on someone’s device. The following images shows options for the layout and placement of fields for the generic pass style.

The following images show the different layout options for a generic pass. Layout one has a separate  and  section with a rectangular barcode. Layout two shows a combined  and  section with a square barcode.

| Generic pass layout 1 | Generic pass layout 2 |
| --- | --- |
| ![An illustration showing the generic pass layout option with separate secondary and auxiliary sections and a rectangular barcode](https://docs-assets.developer.apple.com/published/0ea8eaf5a48417f07aed39a2e317710e/generic-passfield-layout-1%402x.png) | ![An illustration showing a generic pass layout option with a combined secondary and auxiliary section and a square barcode.](https://docs-assets.developer.apple.com/published/17f44895905b4c1e99b22bdab5c2842f/generic-passfield-layout-2%402x.png) |

The pass style determines the maximum number of pass fields that can appear on the front of a pass. A generic pass can have up to three header fields, a single primary field, a thumbnail field, and up to four secondary and auxiliary fields combined. The text length in each pass field determines how many fields appear on the front of the pass. If the text is too long, Wallet won’t display all of it.

Space on the front of the pass is limited, as well. You can use the primary pass field for important business information, the thumbnail field for a thumbnail image, and the secondary and auxiliary fields for information like expiration dates, store locations, and contact information.

The back of the pass can have as many fields as you need, and the contents of the fields can be longer if necessary to convey extra information about terms and conditions, and general information helpful for your pass viewers.

> ❗ **Important**: On the back of the pass, include contact information for the organization that signed the pass. If users interact with a different organization to redeem the pass, you may choose to provide two sets of contact information. For more information, see [`App Store Review Guidelines`](https://developer.apple.comhttps://developer.apple.com/app-store/review/guidelines/).

For more information on pass fields, see [`PassFields`](passfields.md). For more information on the generic pass object, see [`Pass.Generic`](pass/generic-data.dictionary.md).

The following example shows a `pass.json` file with the `generic` pass style and pass fields:

```json
{
    "formatVersion": 1,
    "passTypeIdentifier": "pass.com.example.membership-pass",
    "serialNumber": "123A4b5Z7p",
    "teamIdentifier": "ABCD1234",
    "webServiceURL": "https://example.com/passes/",
    "authenticationToken": "xyz18vnkabn3789dtoBsk77v",
    "barcodes": {
        "message": "12345678",
        "format": "PKBarcodeFormatCode128",
        "messageEncoding": "iso-8859-1"
    },
    "organizationName": "My gym name"
    "description": "Gym membership pass",
    "logoText": "My gym",
    "foregroundColor": "rgb(0, 0, 0)",
    "backgroundColor": "rgb(245, 197, 67)",
    "generic": {
        "primaryFields": [
            {
                "key": "memberName",
                "label": "Name",
                "value": "Maria Ruiz"
            }
        ],
        "secondaryFields": [
            {
                "key": "memberNumber",
                "label": "Member Number",
                "value": "7337",
            }
        ],
        "auxiliaryFields" : [
          {
            "key" : "memberSince",
            "dateStyle" : "PKDateStyleShort",
            "label" : "Joined",
            "value" : "2026-01-02T00:00-7:00"
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
                "label": "Membership Terms and Conditions",
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

> **Note**:  A pass viewed on an Apple Watch doesn’t show the strip image (banner image), thumbnail image, or the information on the back of the pass.

#### Provide Scannable Codes

Passes can work with Near Field Communication (NFC) readers and barcodes. Someone can hold a device near an NFC reader with the contactless symbol to use their pass. When employing NFC, the pass doesn’t need a barcode.

Alternatively, passes can use scannable barcodes to convey information. Wallet supports 2D barcodes using QR, Aztec, and PDF417 formats. Wallet optimizes the presentation of passes in order to facilitate a successful scan.

For more information on barcodes, see [`Pass.Barcodes`](pass/barcodes-data.dictionary.md) and the [`Add to Apple Wallet Guidelines`](https://developer.apple.comhttps://developer.apple.com/wallet/add-to-apple-wallet-guidelines/).

For design guidance about generic passes, see Human Interface Guidelines > Wallet > Passes > [`Generic passes`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/wallet#Generic-passes).

#### Debug the Pass

If the pass doesn’t display and add to Wallet, check the logs for a description of what went wrong. If you’re using Simulator to debug, you can drag your `.pkpass` file into the Simulator, then use the Console app on your Mac to view the Simulator device logs.

When testing on a device, errors are logged to the device’s console, which you can view from the Xcode organizer window. You can filter the logs by using your pass type ID or serial number to limit the device log output to a specific pass instance. See [`Acquiring crash reports and diagnostic logs`](https://developer.apple.com/documentation/Xcode/acquiring-crash-reports-and-diagnostic-logs#Access-device-console-logs) for information on accessing a device’s console log, as well as downloading and installing the Wallet profile.

Common errors include malformed JSON files, misspelled keys or values, pass type identifiers that don’t match your certificate, and signatures that omit the Apple Worldwide Developer Relations Intermediate Certificate. For more information on common issues with pass creation, see [`Common Problems`](building-a-pass#Common-Problems.md).

## See Also

- [object Pass.Generic](pass/generic-data.dictionary.md)
  An object that represents the groups of fields that display the information for a generic pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/creating-a-generic-pass)*