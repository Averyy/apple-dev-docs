# Creating the source for an order

**Framework**: Walletorders

Define an order by creating the directory structure, and adding source files and images.

#### Overview

An order is a self-contained package that represents a purchase a user makes, and the current state of any fulfillments and tracking metadata. The source for your order includes all the information the system needs to show it to the user, such as:

- Product images for line items and your merchant logo.
- An `order.json` file that contains the strings the system displays to describe the order, and the current state of any fulfillments and tracking metadata.
- Optional localization information.

Create the source in a directory that you use to create the final distributable order package. For information about building the order package and donating to Wallet, see [`Building a distributable order package`](building-a-distributable-order-package.md).

##### Create the Directory and Add Files and Images

Create a directory to hold all the source files. Add the `order.json` file that contains the information and metadata for the order. For more information about the contents of this file, see the top-level [`Order`](order.md) object.

Create a visually rich order by providing product images of line items and a merchant logo to represent your company or brand. The system displays product images in notifications, including on the Lock Screen, when you publish relevant updates to the order.

##### Add Localization

You can expand your audience by localizing the strings and images of your order for different languages and regions. Add a directory at the top-level source directory of each order for each localization. The name of the directory identifies the language and an optional region.

```other
[language identifier]-[region identifier].lproj
```

For example, the name for the French localization directory is `fr.lproj`, and the name for the Simplified Chinese directory is `zh-Hans.lproj`. For more information about language identifiers, see [`Choosing localization regions and scripts`](https://developer.apple.com/documentation/Xcode/choosing-localization-regions-and-scripts).

Localize an image by adding the location-specific image files to each localization directory. For example, to add localized versions of a merchant logo, add the English version of `logo@2x.png` and `logo@3x.png` files to the `en.lprojfolder`, and the Simplified Chinese version of the `logo@2x.png` and `logo@3x.png` files to the `zh-Hans.lproj` folder. Reference your image in the `order.json` by the filename `logo`. Be sure to provide the same number of resolutions for each localization.

> **Note**:  Adding an image of the same name to the top-level folder of the order file overrides any localized versions.

##### Localize the Strings

The system localizes the strings in your order using a strings file that contains a list of keys and associated localized strings. For more information about fields that are localizable, see the top-level [`Order`](order.md) object.

Add localized strings to your order using the following steps:

1. Set the value of a displayed string in `order.json` to a key, such as `LineItemTitle` for the title of a line item.
2. Add an `order.strings` file to the localization folder.
3. Add a line to each `order.strings` file that sets a key you create in `order.json` to the localized term.

For example, to localize a line item from English to German, set the value of the strings in the `order.json` to keys.

```other
...  
"lineItems": [
    {
        "title": "LineItemTitle", 
        "subtitle": "LineItemSubtitle",
        "quantity": "2" 
    }
]
...
```

Define the values for the keys in the English strings in `en.lproj/order.strings`.

```other
/* English Localization */
"LineItemTitle" = "Water Bowl";
"LineItemSubtitle" = "Green";
```

Then define the values for the keys in the German strings in `de.lproj/order.strings`.

```other
/* German Localization */
"LineItemTitle" = "Wasserschale";
"LineItemSubtitle" = "Grün";
```

> **Note**:  Use UTF-16 encoding for non-ASCII characters.

The system localizes fields that contain dates and times that use standard formats in the `order.json` file. The system always displays localized versions of these values, even when your order doesn’t contain localization folders for the language.

> ❗ **Important**:  The system doesn’t perform currency conversion on fields that contain monetary values. Monetary values display in the provided currency.

## See Also

- [Building a distributable order package](building-a-distributable-order-package.md)
  Prepare an order for distribution by building, signing, and compressing the source files.
- [Retrieve the registrations for a device](retrieve-the-registrations-for-a-device.md)
  Retrieves the identifiers of the orders that the device registered for.
- [Retrieve the latest version of an order](retrieve-the-latest-version-of-an-order.md)
  Retrieves the latest signed and compressed version of an order.
- [object Order](order.md)
  The order’s details, including information about the products or services rendered, customer service, and fulfillment.
- [Example Order Packages](example-order-packages.md)
  Edit, build, and add example order packages to Wallet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/WalletOrders/creating-the-source-for-an-order)*