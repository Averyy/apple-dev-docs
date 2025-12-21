# Building a Pass

**Framework**: Wallet Passes

Build a distributable pass.

#### Overview

The pass you distribute to a user is a signed [`Bundle`](https://developer.apple.com/documentation/Foundation/Bundle) that contains the JSON description of the pass, images, and optional localizations.

To build a pass, you:

- Create the source files for a pass. To learn more, see [`Creating the Source for a Pass`](creating-the-source-for-a-pass.md).
- Create a pass type identifier.
- Generate a signing certificate.
- Create a digital signature for the pass.
- Create the signed bundle.

##### Create a Pass Type Identifier

You build one or more groups of related passes, such as the tickets for different events. Each group has a unique pass type identifier, a reverse DNS string that identifies your organization, the kind of pass, and the group, such as `com.example-company.passes.ticket.event-4631A`.

Identify the individual passes in a group by assigning each a serial number. Each combination of pass identifier and serial number is one unique pass. Adding a pass with the same pass identifier and serial number as one that already exists on a users’ device overwrites the old one.

Create your pass type identifier in the Certificates, Identifiers & Profiles area of your Apple Developer account:

- Select Identifiers and then click Add (+).
- On the next screen, choose Pass Type IDs and click Continue.
- Enter a description and the reverse DNS string to create the identifier.

For more information on signing in to your account and creating identifiers, see [`Developer Account Help`](https://developer.apple.comhttps://developer.apple.com/help/account/).

Set the `passTypeIdentifier` of [`Pass`](pass.md) in the `pass.json` file to the identifier. Set the `serialNumber` key to the unique serial number for that identifier.

##### Generate a Signing Certificate

Signing a pass requires a signing certificate for the pass type identifier. Before you can generate a signing certificate you need a certificate signing request (CSR). To learn how to generate a CSR, see [`Create a certificate signing request`](https://developer.apple.comhttps://developer.apple.com/help/account/create-certificates/create-a-certificate-signing-request).

Generate the signing certificate in the Certificates, Identifiers & Profiles area of the Apple Developer portal.

- Select Certificates, and then click Add (+).
- On the next screen, choose Pass Type ID Certificate and click Continue.
- Enter a name for the certificate and select the pass type ID from the dropdown menu.
- Click continue and upload the certificate signing request (CSR).

After uploading the CSR, generate the certificate and download it to the machine used for signing the pass.

For more information on signing into your account and creating signing certificates, see [`Developer Account Help`](https://developer.apple.comhttps://developer.apple.com/help/account/).

##### Sign the Pass and Create the Bundle

To sign the pass, follow these steps:

1. Generate a manifest of the source files for a pass.
2. Write the manifest object to a new file called `manifest.json` in the top-level directory of the source for the pass.
3. Create a PKCS #7 detached signature for the manifest that uses the private key of the pass identifier signing certificate.
4. Add the signature to the top level of the pass in a file called `signature`.
5. Zip the resulting directory.
6. Change the file extension of the resulting archive from `.zip` to `.pkpass`.

> **Note**:  Don’t include metadata files that aren’t part of the pass format, such as the `.DS_Store` file in the manifest or distributable pass.

The manifest is a JSON object that contains a dictionary of the SHA1 hashes for each of the source files for the pass. The dictionary key is the pathname of the file relative to the top level of the pass, and the value is the SHA1 hash. For example, the code below shows the manifest.json file for a pass that’s localized for English and Simplified Chinese:

```other
{
   "icon.png" : "2a1625e1e1b3b38573d086b5ec158f72f11283a0",
   "icon@2x.png" : "7321a3b7f47d1971910db486330c172a720c3e4b",
   "icon@3x.png" : "7321a3b7f47d1971910db486330c172a720c3e4b",
   "pass.json" : "ef3f648e787a16ac49fff2c0daa8615e1fa15df9",
   "strip.png" : "25b737727194b5c7b26a86d57e859a054eada240",
   "en.lproj\/logo.png" : "cff02680b9041b7bf637960f9f2384738c935347",
   "en.lproj\/logo@2x.png" : "0e12af882204c3661fd937f6594c6b5ffc6b8a49",
   "en.lproj\/logo@3x.png" : "1f103c8a07fb979ea33adfbfd031e26305fd616b",
   "en.lproj\/pass.strings" : "aaf7d9598f6a792755be71f492a3523d507bc212",
   "zh-Hans.lproj\/logo.png" : "eca86d8a474ccd33978f6aaf98a564669d45c7ae",
   "zh-Hans.lproj\/logo@2x.png" : "b6556bc2fa795d11262f17cdff04f80350398f5f",
   "zh-Hans.lproj\/logo@3x.png" : "124f8381721b44b2b57bf33e30b8a9a2e0404bce",
   "zh-Hans.lproj\/pass.strings" : "b0b4499ba7369e4cc15bad45c251e7b9bbcad6a4",
}
```

Test your pass by dropping it onto an iPhone that’s running on Simulator. Wallet shows the add pass dialog if it’s valid.

![A graphic that show the add pass sheet on an iPhone 12 running in Simulator. ](https://docs-assets.developer.apple.com/published/b81267345d99cafb42bae4aac6f02c4d/media-3737826%402x.png)

##### Common Problems

If your pass doesn’t build correctly, check whether the following are all true:

- The `pass.json` file contains all the required keys.
- The value of the `passTypeIdentifier` key in the `pass.json` file matches the pass type identifier of the signing certificate.
- The value of the `teamIdentifier` key in the `pass.json` file matches the Apple Developer account of the signing certificate.
- The machine signing the pass has a copy of the signing certificate.
- The certificate isn’t expired.
- The `manifest.json` contains all the source files, including those in subdirectories.
- The source contains all required images.
- The images are in the correct format.
- The `pass.json` and `manifest.json` files use the correct JSON syntax.
- Strings that require value formats are correct, such as the `value` and `attributedValue` keys of [`PassFieldContent`](passfieldcontent.md) which require an ISO 8601 date.
- The names of localization folders use the correct language and region identifiers.
- Each localization folder contains all localized image files.
- Each localization folder contain the `pass.strings` file for passes with localized strings.
- The `pass.strings` files use the correct syntax.
- The keys for localized strings in the `pass.json` file match those used in the `pass.strings` files.
- Each pass.strings file contains the same number of localized strings and uses the same keys.

## See Also

- [Creating the Source for a Pass](creating-the-source-for-a-pass.md)
  Create the directory structure and add source files and images to define a pass.
- [Distributing and updating a pass](distributing-and-updating-a-pass.md)
  Distribute a pass to your users or update an existing pass.
- [object Pass](pass.md)
  An object that represents a pass.
- [object PassFields](passfields.md)
  An object that represents the groups of fields that display information on the front and back of a pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/building-a-pass)*