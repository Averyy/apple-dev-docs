# Creating a store card pass

**Framework**: Wallet Passes

Construct a digital pass for store loyalty and gift cards.

#### Overview

Use store card passes for discount, gift, and store loyalty cards. Setting the store card pass style provides data that Wallet displays automatically, such as store points, rewards balance, terms and conditions, and other helpful information.

![An illustration showing an example store card pass for a mock coffee shop with a points and rewards earned balance.](https://docs-assets.developer.apple.com/published/f81fefc86a3b46a8052c2164131d2583/store-card%402x.png)

#### Create Your Pass Type Identifier

Signing a pass requires a signing certificate for the *pass type identifier*, which is similar to a bundle identifier, or a class name. The value for the `passTypeIdentifier` key specifies the pass type identifier. You choose a string to define a class or category of passes; the string always begins with `pass`, and uses reverse DNS style—for example, `pass.com.example.loyalty-card`. Create your pass type identifier in the [`Certificates, Identifiers & Profiles`](https://developer.apple.comhttps://developer.apple.com/account/resources) area of your Apple Developer account. The pass type identifier must match the certificate used to sign the pass. For more information on creating Wallet certificates, see [`Create Wallet identifiers and certificates`](https://developer.apple.comhttps://developer.apple.com/help/account/capabilities/create-wallet-identifiers-and-certificates/).

Use a serial number to identify the pass uniquely within the scope of its pass type. The value for the `serialNumber` key in the pass specifies the serial number. You can assign a serial number in whatever way makes sense to you, such as by using an increasing integer or a UUID.

The difference between pass type identifiers and serial numbers is similar to the difference between classes and instances of a class: pass type identifiers designate something abstract, and serial numbers identify something specific, and concrete. For example, if a store creates passes for loyalty cards and for gift cards, the loyalty card passes have the same pass type identifier, but each one has its own serial number. The gift cards have a different pass type identifier than the loyalty card passes, because they’re a different type of pass.

PassKit uses the combination of pass type identifier and serial number to uniquely identify a pass. Two passes of the same type with the same serial number represent the same pass, even if other information on them differs. For example, when a pass updates, the new version has the same pass type identifier and serial number as the old version, so the new version replaces the old version.

For more information on creating your pass type identifier, see [`Create a Pass Type Identifier`](building-a-pass#Create-a-Pass-Type-Identifier.md).

#### Add the Store Card Pass Style

The pass’s style determines the overall visual appearance of the pass and the template for placement of information on the pass. The value of the pass style key is a dictionary containing fields that hold the pass content. Specify the pass style by providing the corresponding key at the top level of the `pass.json` file; store card passes use the key `storeCard`. For more information on building your pass json file, see [`Building a Pass`](building-a-pass.md).

The following example shows a partial store card pass with top-level keys.

```json
{
    "description": "Coffee shop loyalty card.",
    "formatVersion": 1,
    "passTypeIdentifier": "pass.com.example.loyalty-card",
    "serialNumber": "123A4b5Z7p",
    "storeCard": { ... }
}
```

The pass style controls how Wallet lays out the pass fields and which images it shows on someone’s device. The following image shows options for the layout and placement of fields for the store card pass style. Typically, your store identifies an account someone has with your company, which can be used to make payments or receive discounts. When the account carries a balance, show the current balance on the pass.

![An illustration showing a store card pass layout option with combined secondary and auxiliary sections and a rectangular barcode.](https://docs-assets.developer.apple.com/published/7b648e914e0e99562fcf512efb115175/store-card-layout%402x.png)

The pass style determines the maximum number of pass fields that can appear on the front of a pass. A store card pass can display logo and strip images and a barcode, and it can have up to four secondary and auxiliary fields, all displayed on one row. The text length in each pass field determines how many fields appear on the front of the pass. If the text is too long, Wallet won’t display all of it.

Space on the front of the pass is limited, as well. You can use the primary pass field for a strip image that creates a banner across the pass, or for business information to which you want to call attention. Use the secondary and auxiliary fields for information about store points, rewards balances, and contact details.

The back of the pass can have as many fields as you need, and the contents of the fields can be as long as necessary to convey additional information about terms and conditions, and general information helpful for your pass viewers.

> ❗ **Important**: On the back of the pass, include contact information for the organization that signed the pass. If users interact with a different organization to redeem the pass, you may choose to provide two sets of contact information. For more information, see [`App Store Review Guidelines`](https://developer.apple.comhttps://developer.apple.com/app-store/review/guidelines/).

For more information on pass fields, see [`PassFields`](passfields.md). For more information on the store card pass object, see [`Pass.StoreCard`](pass/storecard-data.dictionary.md).

The following example shows a `pass.json` file with the `storeCard` pass style and pass fields:

```json
{
    "formatVersion": 1,
    "passTypeIdentifier": "pass.com.example.loyalty-card",
    "serialNumber": "123A4b5Z7p",
    "teamIdentifier": "ABCD1234",
    "webServiceURL": "https://example.com/passes/",
    "authenticationToken": "xyz18vnkabn3789dtoBsk77v",
    "barcodes": {
        "message": "12345678",
        "format": "PKBarcodeFormatCode128",
        "messageEncoding": "iso-8859-1"
    },
    "organizationName": "My coffee company"
    "description": "Coffee shop loyalty card.",
    "logoText": "My coffee shop",
    "foregroundColor": "rgb(222, 173, 40)",
    "backgroundColor": "rgb(24, 44, 82)",
    "storeCard": {
        "primaryFields": [
            {
                "key": "rewardsBalance",
                "label": "Rewards Value",
                "value": "10",
                "currencyCode": "USD"
            }
        ],
        "auxiliaryFields" : [
            {   "key": "status",
                "label": "Coffee Status"
                "value": "Coffee Champ"
            },
            {
                "key" : "totalPoints",
                "label": "Points",
                "value" : "75"
            }
        ],
        "backFields": [
            {
                "key": "terms",
                "label": "Rewards Terms and Conditions",
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

For design guidance about store cards, see Human Interface Guidelines > Wallet > Passes > [`Store cards`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/wallet#Store-cards).

#### Debug the Pass

If the pass doesn’t display and add to Wallet, check the logs for a description of what went wrong. If you’re using Simulator to debug, you can drag your `.pkpass` file into the Simulator, then use the Console app on your Mac to view the Simulator device logs.

When testing on a device, errors are logged to the device’s console, which you can view from the Xcode organizer window. You can filter the logs by using your pass type ID or serial number to limit the device log output to a specific pass instance. See [`Acquiring crash reports and diagnostic logs`](https://developer.apple.com/documentation/Xcode/acquiring-crash-reports-and-diagnostic-logs#Access-device-console-logs) for information on accessing a device’s console log, as well as downloading and installing the Wallet profile.

Common errors include malformed JSON files, misspelled keys or values, pass type identifiers that don’t match your certificate, and signatures that omit the Apple Worldwide Developer Relations Intermediate Certificate. For more information on common issues with pass creation, see [`Common Problems`](building-a-pass#Common-Problems.md).

## See Also

- [object Pass.StoreCard](pass/storecard-data.dictionary.md)
  An object that represents groups of fields that show the information for a store card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/creating-a-store-card-pass)*