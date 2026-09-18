# Creating a Poster Generic Pass

**Framework**: Wallet Passes

Construct a digital pass with information that enables people to take action.

#### Overview

In iOS and watchOS 27, you can present passes such as, membership, loyalty, coupon, rewards, gift card, and other pass types in a poster-style format designed to highlight prominent artwork, modern typography, and thoughtful customer notifications. This style also supports up to two Featured Action links, giving users quick access to helpful information right from the pass.

The Poster Generic template builds on the same presentation style used for event ticket posters, but without the event-specific semantic requirements, giving you flexibility over the content you choose to surface. When you set the Poster Generic Pass style, Wallet automatically displays relevant details such as business information, a barcode, terms and conditions, store locations, and other helpful information.

![An illustration of a Poster Generic Pass for a museum with poster artwork. The poster shows the skull of a Tyrannosaurus rex surrounded by ferns, butterflies, and a nautilus. The pass also displays a QR code and information about the pass holder, including the member name, expiration, and type of pass.](/images/com.apple.walletpasses/poster-generic-pass-natural-history-museum@2x.png)

#### Create Your Pass Type Identifier

Signing a pass requires a signing certificate for the *pass type identifier*, which is similar to a bundle identifier, or a class name. The value for the `passTypeIdentifier` key specifies the pass type identifier. You choose a string to define a class or category of passes; the string always begins with `pass`, and uses reverse DNS style—for example, `pass.com.example.membership-card`. Create your pass type identifier in the [`Certificates, Identifiers & Profiles`](https://developer.apple.comhttps://developer.apple.com/account/resources) area of your Apple Developer account. The pass type identifier must match the certificate used to sign the pass. For more information on creating Wallet certificates, see [`Create Wallet identifiers and certificates`](https://developer.apple.comhttps://developer.apple.com/help/account/capabilities/create-wallet-identifiers-and-certificates/).

> **Note**:  Generic passes don’t auto-expire based on the signing date. Use `expirationDate` in your `pass.json` to explicitly control the expiration date.

Use a serial number to identify the pass uniquely within the scope of its pass type. The value for the `serialNumber` key in the pass specifies the serial number. You can assign a serial number using a method that makes sense to you, such as by using an increasing integer or a UUID.

The difference between pass type identifiers and serial numbers is similar to the difference between classes and instances of a class: pass type identifiers designate something abstract, and serial numbers identify something specific, and concrete. For example, if a store creates passes for a locker rental and for its membership card program, the locker rental passes have the same pass type identifier, but each one has its own serial number. The membership cards have a different pass type identifier than the locker rental passes, because they’re a different type of pass.

PassKit uses the combination of pass type identifier and serial number to uniquely identify a pass. Two passes of the same type with the same serial number represent the same pass, even if other information on them differs. For example, when a pass updates, the new version has the same pass type identifier and serial number as the old version, so the new version replaces the old version.

For more information on creating your pass type identifier, see [`Create a Pass Type Identifier`](building-a-pass#Create-a-Pass-Type-Identifier.md).

#### Add the Poster Generic Pass Style

The pass’s style determines the overall visual appearance of the pass and the template for placement of information on the pass. The value of the pass style key is a dictionary containing fields that hold the pass content. Specify the pass style by providing the corresponding key at the top level of the `pass.json` file; Poster Generic Passes use the key `posterGeneric`. For more information on building your `pass.json` file, see [`Building a Pass`](building-a-pass.md).

The following example shows a partial Poster Generic Pass with top-level keys.

```json
{
    "description": "A museum membership pass",
    "formatVersion": 1,
    "passTypeIdentifier": "pass.com.example.membership-pass",
    "serialNumber": "123A4b5Z7p",
    "posterGeneric": { ... }
}
```

The pass style controls how Wallet lays out the pass fields and which images it shows on someone’s device. The following figures show the different layout options and the placement of fields for a Poster Generic Pass and a generic pass. The Poster Generic Pass layout has a *headerFields*, *primaryFields*, *footerFields*, *backFields*, and *additionalInfoFields* with a square QR code. The generic pass layout has a separate *secondary* and *auxiliary* section with a rectangular barcode.

| Poster Generic Pass layout | Generic pass layout |
| --- | --- |
| ![An illustration showing a Poster Generic Pass layout option with primary fields and a QR code.](/images/com.apple.walletpasses/pass-fields-layout-poster-generic@2x.png) | ![An illustration showing the generic pass layout option with separate secondary and auxiliary sections and a rectangular barcode](/images/com.apple.walletpasses/pass-fields-layout-generic-pass@2x.png) |

The pass style determines the maximum number of pass fields that can appear on the front of a pass. A Poster Generic Pass can have a header field, up to four primary fields, two footer fields, back fields, and additional info field.

A generic pass can have up to three header fields, a single primary field, a thumbnail field, and up to four secondary and auxiliary fields combined. The text length in each pass field determines how many fields appear on the front of the pass. If the text is too long, Wallet won’t display all of it.

Space on the front of the pass is limited, as well. You can use the primary pass field for important business information, the thumbnail field for a thumbnail image, and the secondary and auxiliary fields for information like expiration dates, store locations, and contact information.

The back of the pass can have as many fields as you need, and the contents of the fields can be longer if necessary to convey extra information about terms and conditions, and general information helpful for your pass viewers.

> ❗ **Important**: On the back of the pass, include contact information for the organization that signed the pass. If users interact with a different organization to redeem the pass, you may choose to provide two sets of contact information. For more information, see [`App Store Review Guidelines`](https://developer.apple.comhttps://developer.apple.com/app-store/review/guidelines/).

For more information on pass fields, see [`PassFields`](passfields.md) and Human Interface Guide > Wallet > [`Pass field types`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/wallet#Pass-field-types). For more information on the generic pass object, see [`Pass.Generic`](pass/generic-data.dictionary.md).

#### Ensure Backward Compatibility

To ensure your pass is backward compatible, include an additional style dictionary on the same pass, for example, `storeCard`, `generic`, `eventTicket`, or `coupon`. Wallet’s style resolution prioritizes `posterGeneric` when present, so newer devices display the generic pass with the poster, and older devices display the legacy style they recognize.

![An illustration of a generic pass for a gym membership that displays text, including the membership type, name, and ID, on a single background color.](/images/com.apple.walletpasses/generic-pass@2x.png)

The following example shows a `pass.json` file with the `posterGeneric` pass style as the main pass style for devices viewing the pass on iOS and watchOS 27 or later and the `generic` pass style as a fallback when the pass is viewed on devices devices with an older iOS or watchOS version:

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
    "organizationName": "Museum"
    "description": "Museum pass",
    "logoText": "My gym",
    "foregroundColor": "rgb(0, 0, 0)",
    "backgroundColor": "rgb(245, 197, 67)",
    "posterGeneric": {
        "headerFields": [
            {
                "key": "memberNumber.",
                "label": "Guest No.",
                "value": "102035"
            }
        ],
        "primaryFields": [
            {
                "key": "memberName",
                "label": "Name",
                "value": "Ryan Notch"
            },
            {
                "key": "memberType",
                "label": "Family",
                "value": "Family Pass",
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
                "value": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            }
        ]
    }, 
    // Legacy fields for backwards compatibility.
    "generic": {
            "primaryFields": [
                {
                    "key": "memberName",
                    "label": "Name",
                    "value": "Ryan Notch"
                }
            ],
            "secondaryFields": [
                {
                    "key": "memberNumber",
                    "label": "Guest No.",
                    "value": "102035",
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
                    "value": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                }
            ]
        }
}
```

> **Note**:  A pass viewed on an Apple Watch doesn’t show the strip image (banner image), thumbnail image, or the information on the back of the pass.

#### Provide Scannable Codes

Passes can work with Near Field Communication (NFC) readers and barcodes type. Someone can hold a device near an NFC reader with the contactless symbol to use their pass. When employing NFC, the pass doesn’t need a barcode.

Alternatively, passes can use scannable barcodes to convey information. Wallet supports QR, PDF417, Aztec, Code128, Code 39, Codabar, EAN-13, and Interleaved 2 of 5 (ITF) barcode formats. Wallet optimizes the presentation of passes in order to facilitate a successful scan.

For more information on barcodes, see [`Pass.Barcodes`](pass/barcodes-data.dictionary.md) and the [`Add to Apple Wallet Guidelines`](https://developer.apple.comhttps://developer.apple.com/wallet/add-to-apple-wallet-guidelines/).

For design guidance about generic passes, see Human Interface Guidelines > Wallet > Passes > [`Generic passes`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/wallet#Generic-passes).

#### Add Featured Actions

With iOS and watchOS 27 and later, you can include Featured Actions with your pass. These actions display as cards when someone views your pass in the Wallet app, and you can use them for quick calls to action for the viewer. Featured Actions make it easy for someone to find relevant information related to your pass quickly, such as directions to a business location, music related to a live performance, or links to book tickets.

![An illustration of a Poster Generic Pass for a museum. The pass shows an image of the skull of a Tyrannosaurus rex surrounded by ferns, butterflies, and a nautilus. The pass also displays two Featured Action options: View Membership Benefits and Go to Location.](/images/com.apple.walletpasses/featured-actions-with-pass@2x.png)

Each Featured Action includes an icon, string, and action. Define your icon from available SF Symbols; be sure to pick one that accurately represents the action, and that viewers can understand at a glance. When choosing a symbol, prefer circular, filled icons.

Your string is a brief call to action, and your action label informs people what happens when they click the link; for example, your pass may redirect them to a website or the Maps app.

![An image of a Featured Action icon with labels.](/images/com.apple.walletpasses/featured-actions-anatomy@2x.png)

For a list of available Featured Actions, see [`Add Featured Actions`](defining-the-metadata-of-your-wallet-pass#Add-Featured-Actions.md)

#### Add Notifications

With notifications you can inform customers in thoughtful ways to increase visits, sales, and overall engagement. Use notifications to broadcast program updates to all of your customers or provide specific updates to each customer based on their engagement with your program. These updates and notifications can be triggered via relevant time and relevant location functionality held directly in the pass. For best practices and design guidance on notifications, see [`Human Interface Guide > Components > System Experiences > Notifications`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/notifications#best-practices).

#### Debug the Pass

If the pass doesn’t display and add to Wallet, check the logs for a description of what went wrong. If you’re using Simulator to debug, you can drag your `.pkpass` file into the Simulator, then use the Console app on your Mac to view the Simulator device logs.

When testing on a device, errors are logged to the device’s console, which you can view from the Xcode organizer window. You can filter the logs by using your pass type ID or serial number to limit the device log output to a specific pass instance. See [`Diagnosing issues using crash reports and device logs`](https://developer.apple.com/documentation/xcode/diagnosing-issues-using-crash-reports-and-device-logs) for information on accessing a device’s console log, as well as downloading and installing the Wallet profile.

Common errors include malformed JSON files, misspelled keys or values, pass type identifiers that don’t match your certificate, and signatures that omit the Apple Worldwide Developer Relations Intermediate Certificate. For more information on common issues with pass creation, see [`Common Problems`](building-a-pass#Common-Problems.md).

## See Also

- [Creating a pass with Pass Designer](creating-a-pass-with-pass-designer.md)
  Construct and customize a variety of pass styles with this easy-to-use tool.
- [Creating the Source for a Pass](creating-the-source-for-a-pass.md)
  Create the directory structure and add source files and images to define a pass.
- [Building a Pass](building-a-pass.md)
  Build a distributable pass.
- [Defining the metadata of your Wallet Pass](defining-the-metadata-of-your-wallet-pass.md)
  Provide customizable information for your Wallet Pass.
- [Distributing and updating a pass](distributing-and-updating-a-pass.md)
  Distribute a pass to your users or update an existing pass.
- [object Pass](pass.md)
  An object that represents a pass.
- [object PassFields](passfields.md)
  An object that represents the groups of fields that display information on the front and back of a pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/creating-a-poster-generic-pass)*