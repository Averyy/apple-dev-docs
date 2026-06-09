# Creating a pass with Pass Designer

**Framework**: Wallet Passes

Construct and customize a variety of pass styles with this easy-to-use tool.

#### Overview

With Pass Designer, you can easily visualize and design effective passes for Apple Wallet using a simple macOS app.  Start with one of the templates provided for inspiration or use your own template to design passes that reflect your business or brand personality.

![An illustration showing an example of the Pass Designer tool layout with an event pass.](https://docs-assets.developer.apple.com/published/417a74d22b27ff500016539e3951a51a/pass-designer-overview%402x.png)

Using the Pass Designer app, you can both design and preview passes in real time, seeing exactly how your passes appear to people. The Wallet app makes it easy for people to access their passes right when they need them, and Pass Designer makes it easy to create passes that look great and reflect the personality of an issuer’s brand. For example, a music venue can customize passes to display album cover art for the artist who’s performing.

To use the Pass Designer app on Mac:

- [`Download`](https://developer.apple.comhttps://developer.apple.com/download/all/?q=pass%20designer) the app.
- Make sure you have macOS 27.0 or later installed.

#### Choose a Pass Type

There are six primary types of passes you can create using the Pass Designer app, detailed below. You can easily visualize the appearance of each pass in each version of the software, so you can design a pass that looks great no matter what system a person is viewing it in. You can even create a blank pass or create one completely from scratch.

**Boarding pass**:

Use the boarding pass style for train tickets, airline boarding passes, and other types of transit passes. Typically, each pass corresponds to a single trip with a specific starting and ending point.

![An illustration of two airline boarding passes, one as viewed in iOS 26 and later, and the other as viewed in earlier iOS versions.](https://docs-assets.developer.apple.com/published/0c4e6d08916a6742a5966d4407222316/pass-designer-pass-types-boarding-pass-airline%402x.png)

**Coupon pass**:

Use the coupon pass style for coupons, special offers, and other discounts.

![An illustration of a coupon pass for a food truck.](https://docs-assets.developer.apple.com/published/9f91c26ece2ff9161073ef14d9cefd96/pass-designer-pass-types-coupon%402x.png)

**Generic pass**:

Use the generic style for a pass that doesn’t fit into the other categories, such as a gym membership card or coat-check claim ticket.

![An illustration of a generic pass with a depiction of a gym membership.](https://docs-assets.developer.apple.com/published/4453272999df940237dd088810aef9e2/pass-designer-pass-types-generic%402x.png)

**Store card pass**:

Use the store card style for store loyalty cards, discount cards, points cards, and gift cards. If an account related to a store card carries a balance, the pass usually shows the current balance.

![An illustration of a Store Card pass for a coffee shop.](https://docs-assets.developer.apple.com/published/8c9f0d6bc420749481a3cf4d4091a48a/pass-designer-pass-types-store-card%402x.png)

**Event pass**:

Use the event ticket pass style to give people entry into events like concerts, movies, plays, and sporting events. Typically, each pass corresponds to a specific event, but you can also use a single pass for several events, as with a season ticket.

![An illustration of an event pass for a concert.](https://docs-assets.developer.apple.com/published/e8fa49aaf4a7e6b3e29c0ed080799ec1/pass-designer-pass-types-event-ticket%402x.png)

**Poster generic pass**:

Use the poster generic pass style for an updated version of the generic pass. This style is for passes that don’t fit into the other categories, such as a gym membership card or coat-check claim ticket.

![An illustration of a poster generic pass of a museum ticket.](https://docs-assets.developer.apple.com/published/e19eb5ef4bf3de39bc42d6b991902de2/pass-designer-pass-types-poster-generic%402x.png)

When you first open the app and create a new document, Pass Designer presents you with the Template Picker, which you  use to select the style of pass you want to build. Pick a specific template, and the app preloads your pass with all the relevant text fields and image placements, which you can then customize for your design.

![An image of the Template Picker with the Boarding Pass option selected.](https://docs-assets.developer.apple.com/published/3928dabaddce2536ad4704da211a67a8/pass-designer-template-picker%402x.png)

#### Set Up Your Workspace

The left-hand sidebar contains all the components for a specific pass. Click on a component to open an editor panel from which you can customize each section of your pass. The right-hand side of the app shows you previews of your pass designs.

![A screenshot of the Pass Designer workspace layout with callouts for each section of the tool.](https://docs-assets.developer.apple.com/published/8406f8aadfedcaff3fd32b5d62d32d71/pass-designer-workspace-layout%402x.png)

To select the background color for your canvas, use the canvas background setting. Depending on the colors you’re using, this feature can make it easier to see the design. For example, if you’re working on a pass with a white background, setting the background color of the app to black can make seeing your pass design easier.

![A screenshot of the background color selection section of the Pass Designer tool.](https://docs-assets.developer.apple.com/published/4b96bade6025e7432a45acc5cb26a24d/pass-designer-canvas-color-picker%402x.png)

#### Customize Your Pass Components

Each pass is composed of a number of components, each of which is responsible for helping define a different aspect of your pass design. The components section of the Pass Designer tool is where you can customize all of your components to tailor your pass to your target audience.

![A screenshot of the component section of the Pass Designer tool, highlighting the Identity & Signing section.](https://docs-assets.developer.apple.com/published/ed06fafe217405478ea53605069b149c/pass-designer-components-overview%402x.png)

#### Configure the Identity and Signing

In the Identity & Signing section, you can add information about your business or company. This metadata becomes available to people in the pass information.

If you’ve already created a Pass Type ID certificate, you can easily import all the information directly from the certificate. For more information on creating a Pass Type ID certificate, see [`Create Wallet identifiers and certificates`](https://developer.apple.comhttps://developer.apple.com/help/account/capabilities/create-wallet-identifiers-and-certificates/).

![A screenshot of the Identity & Signing component.](https://docs-assets.developer.apple.com/published/b97908267ee6bbf5ddf624331978d3b8/pass-designer-identity-and-signing-overview%402x.png)

#### Select the Pass Style

In the Style section, you can select the type of pass you want to create. For boarding passes, you can also select other categories like Transit Type, where you can choose between Air, Train, Boat, Bus, or Generic as the travel mode.

> **Note**: Only the air travel boarding pass supports the new Semantic Pass designs available in iOS 26 and later.

![A screenshot of the Style component.](https://docs-assets.developer.apple.com/published/ae1f0ca60cbb4bb06992eb3f965c4c75/pass-designer-style-overview%402x.png)

You can also select the colors used throughout your pass design. Ensure the colors you pick for labels are accessible and easy for people to read, especially when using background images in your pass. For design guidance on optimizing color choices, see the [`Designing passes`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/wallet#Designing-passes) section of the Human Interface Guidelines.

![A screenshot of the Colors section of the Style component.](https://docs-assets.developer.apple.com/published/2280cb61de3f013ffcc0d655621ccdd5/pass-designer-style-overview-color%402x.png)

The graphic below shows which section of the pass each color field refers to:

![An illustration of a pass with the color fields called out. component.](https://docs-assets.developer.apple.com/published/cd66a7fd7184f6578d68c665386bb78c/pass-designer-color-layout%402x.png)

#### Add Images to Your Pass

Each style of Wallet pass has different types of images you can use to help create a dynamic pass, ranging from small iconography to large background images.

![An screenshot of the Pass Designer images types.](https://docs-assets.developer.apple.com/published/954a8108fdd43fb524c7c9420b6016aa/pass-designer-images-overview%402x.png)

Provide each image to Pass Designer in PNG format at its 2x and 3x sizes to ensure that it renders properly no matter what device someone is viewing it on. The Pass Designer tool tells you which images are needed for each pass.

To learn more about which images are available for each pass type and how to construct them, see the following table:

| Pass type | Boarding pass | Coupon | Event ticket | Store card | Generic pass | Poster generic pass |
| --- | --- | --- | --- | --- | --- | --- |
| `Icon` | All | All | All | All | All | All |
| `Logo` | < iOS 26 and earlier and non-airline | < iOS 26 | < iOS 18 | < iOS 26 | < iOS 26 | iOS 27+ |
| `Primary logo` | iOS 27+ | iOS 27+ | iOS 18+ | NA | NA | iOS 27+ |
| `Secondary logo` | NA | NA | iOS 18+ | NA | NA | NA |
| `Strip image` | NA | < iOS 26 | NA | <iOS 26 | NA | NA |
| `Thumbnail image` | NA | NA | < iOS 26 | NA | < iOS 26 | NA |
| `Background` | NA | NA | iOS 18+ | NA | NA | NA |
| `Background artwork` | NA | NA | iOS 27+ | NA | NA | iOS 27+ |
| `Footer image` | NA | NA | NA | NA | NA | NA |

#### Add an Icon

An icon needs to be a square 38-by-38-pixel image, appears on every type of pass style, and typically represents your brand or app.

![An image of the Icon section of the Pass Designer tool.](https://docs-assets.developer.apple.com/published/6d525adf439edde8dbb1619d9209a4e5/pass-designer-images-icon%402x.png)

Your icon also appears in Lock Screen banners, in Mail, and on passes in the Wallet app. If your pass has an associated app, your icon can represent your app icon. When someone taps on an icon in the Wallet app, it either opens your app or the App Store page for your app. To see a preview, build your pass and view it in the Wallet app on iPhone.

#### Add a Logo

The logo appears in the top left of your pass design and can be anything from a symbol representing your brand to text representing your brand identity.

![An image of the Logo section of the Pass Designer tool.](https://docs-assets.developer.apple.com/published/d018db18633e36fbda5f9d2c4aa9e256/pass-designer-images-logo%402x.png)

The logo appears on the following pass styles: boarding passes (before iOS 26), generic passes (all versions), coupons (all versions), event passes (before iOS 18), and store cards (all versions).

![An image of a coupon pass with a callout for the logo section of the pass.](https://docs-assets.developer.apple.com/published/002e6d8c34ad225fa154716ea9afa69d/pass-designer-images-logo-anatomy%402x.png)

The logo needs to be 50 pixels tall and can be anywhere from 50 to 160 pixels wide at the maximum. For design guidance on creating your logo see [`Pass styles`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/wallet#Pass-styles) in the Human Interface Guidelines.

#### Add a Primary Logo

The primary logo appears in the top left of your pass design and can be anything from a symbol representing your brand to text representing your brand identity.

![A screenshot of the Primary Logo section of the Pass Designer tool.](https://docs-assets.developer.apple.com/published/77bb309df9de7ced9a4ba3bf26cf3431/pass-designer-images-primary-logo%402x.png)

The primary logo needs to be 30 pixels tall and can be any width from 30 to 126 pixels.

The primary logo appears on the following pass styles: boarding passes (iOS 26 and later) and event passes (iOS 18 and later). Even though you may design your pass for the latest OS, remember that not every person views the pass on the same software. Be sure to include a logo as well for instances when the pass displays on previous software versions.

#### Add a Secondary Logo

The secondary logo is a mark that appears in the bottom right of an event pass beginning in iOS 18.

![An image of the secondary logo.](https://docs-assets.developer.apple.com/published/65c7faba9d95eabb0d4d9be208a69000/pass-designer-images-secondary-logo%402x.png)

You can use the secondary logo to represent information like the event venue, the brand logo of a ticket seller that the person purchased their ticket through, or other branding related to the event itself.

![An example of an event pass secondary logo.](https://docs-assets.developer.apple.com/published/8256b337a7f3b7a9c43175b86d158316/pass-designer-images-secondary-logo-anatomy%402x.png)

The secondary logo can range from a square 12-by-12-pixel icon up to a rectangular 12-by-135-pixel icon. Choose what shape and size suits your logo best.

#### Add a Strip Image

Strip images appear as a narrow band on coupons and store cards, providing space where you can include imagery to help tie in your brand or offer.

![An example of a strip image](https://docs-assets.developer.apple.com/published/ced220c84aba5537dd578edd4e782382/pass-designer-images-strip%402x.png)

The strip image needs to be 375 by 144 pixels. Be mindful that you can place text over strip images in your pass design, so ensure there’s good readability and contrast between your text and the strip image.

![An example of a strip image for a food truck.](https://docs-assets.developer.apple.com/published/64d1f56792ac6c564c9bde9dc0e8ca79/pass-designer-images-strip-image-anatomy%402x.png)

The primary field and strip image are in the same place on the pass. If you add any text in a primary field, it automatically appears over the strip image. For design guidance on creating the most effective strip image, refer to the Human Interface Guidelines section on [`Wallet coupons`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/wallet#Coupons).

#### Add a Thumbnail Image

Thumbnails are small images that appear on generic passes and nonposter event tickets.

![An example of the thumbnail component in Pass Designer.](https://docs-assets.developer.apple.com/published/8510f7c79b590408efa39e67d56497b9/pass-designer-images-thumbnail%402x.png)

They can be used for anything from helping to identify the type of event in an event pass to showing an image that helps the user identify the pass in a generic pass design. The thumbnail needs to be 90 pixels tall and can be anywhere between 60 and 90 pixels wide.

![An example of a thumbnail for a gym membership.](https://docs-assets.developer.apple.com/published/1453a4addfc55c759daf731a3b86cd9f/pass-designer-images-thumbnail-anatomy%402x.png)

#### Add a Background Image and Background Artwork

Background images offer an effective way to make your pass design feel unique and immersive. Backgrounds appear blurred with nonposter event tickets and unblurred on poster event tickets and poster generic passes.

If your background has important elements, be mindful that they don’t get covered up by any of the safe areas of the pass overlays. For more guidance on designing background images, see the Human Interface Guidelines page on [`Event tickets`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/wallet#Event-tickets).

#### Add a Footer Image

The footer image is available for airline boarding passes starting in iOS 26 and later. This thin image appears at the bottom of a pass, and you can use it for ancillary information.

#### Configure the Barcodes and Nfc

Barcodes are an essential part of designing a useful Wallet pass, from letting people easily scan their boarding pass at an airport to using a coupon code at checkout. With Pass Designer, you can fully customize the type of barcode included on your pass as well as how it’s displayed.

You can provide all barcode information directly in the Pass Designer app, and the barcodes generate automatically, with no need to provide any barcodes as images.

![An image of the Barcode & NFC section of the Pass Designer tool.](https://docs-assets.developer.apple.com/published/1158e64db6f33c996e04536aa7dc2671/pass-designer-barcode-and-nfc-overview%402x.png)

The types of barcodes available are QR, PDF417, Aztec, Code128, Code 39, Codabar, EAN-13, and Interleaved 2 of 5 (ITF). When designing your pass, take into consideration how the barcode placement affects elements like background images. If you’re including a background image, ensure the barcode doesn’t cover important visual areas of your image. Don’t include any barcodes in images. For design guidance on pass layout, see the Human Interface Guidelines page on [`Designing passes`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/wallet#Designing-passes).

**Aztec**:

![An image of an airline boarding pass with an Aztec barcode.](https://docs-assets.developer.apple.com/published/5239c1a7077f20e3f62cb401388cab15/pass-designer-barcode-types-aztec%402x.png)

**Code128**:

![An image of an airline boarding pass with a Code128 barcode.](https://docs-assets.developer.apple.com/published/6bbf77803afa392fe50edeb882ed994e/pass-designer-barcode-types-code128%402x.png)

**QR**:

![An image of an airline boarding pass with a QR code.](https://docs-assets.developer.apple.com/published/f7f0da3e3200e7bf8a0ce33d16f33951/pass-designer-barcode-types-qr%402x.png)

**PDF417**:

![An image of an airline boarding pass with a PDF417 barcode.](https://docs-assets.developer.apple.com/published/9d9517ac637b2d8a9ade2371ec1b0d91/pass-designer-barcode-types-pdf417%402x.png)

**Code 39**:

![An image of an airline boarding pass with a Code 39 barcode.](https://docs-assets.developer.apple.com/published/5ca892d8647fb981d2cbfe899851f773/pass-designer-barcode-types-code-39%402x.png)

**Codabar**:

![An image of an airline boarding pass with a Codabar barcode.](https://docs-assets.developer.apple.com/published/456c4a887929ecba59b0bbf056678236/pass-designer-barcode-types-codabar%402x.png)

**EAN-13**:

![An image of an airline boarding pass with a EAN-13 barcode.](https://docs-assets.developer.apple.com/published/a925e0188a2de772fc117caa0b41e133/pass-designer-barcode-types-ean-13%402x.png)

**Interleaved 2 of 5 (ITF)**:

![An image of an airline boarding pass with a Interleaved 2 of 5 barcode.](https://docs-assets.developer.apple.com/published/b97c06dad0e9c311c126878c9c73c9c2/pass-designer-barcode-types-interleaved%402x.png)

#### Add Semantic Tags

Semantic tags are information fields that you provide and that Pass Designer automatically lays out on your pass design. Simply provide the information and the app prioritizes where to put each piece of information. Semantic tags are available for Boarding Passes (in iOS 27 and later) and Event Passes (in iOS 18 and later).

![A screenshot of semantic tags component in Pass Designer.](https://docs-assets.developer.apple.com/published/276f1bcbcb7be5103ce1f5eabd822882/pass-designer-semantic-tags-overview%402x.png)

The type of information you provide as semantic tags differs depending on the pass styles. For example, a boarding pass may have semantic tags for things like flight details, airports, and seating, whereas an event pass for a sporting event might include semantic tags for team information, match details, and seating location.

Semantic tags can also display additional pass actions that the system displays when someone views the pass in the Wallet app on iPhone. These quick actions make it easy for someone viewing your pass to find related information, such as the bag policy for an event or hotel booking information, when looking at their membership card.

For more guidance on using semantic tags, see [`Add semantic tags`](defining-the-metadata-of-your-wallet-pass#Add-semantic-tags.md).

#### Text Fields

Text fields allow you to enter information in the fields of your pass. Text fields have fixed sections where field types appear. For more information on the layout of pass fields, see [`Defining the metadata of your Wallet Pass`](defining-the-metadata-of-your-wallet-pass.md).

When designing a semantic pass, be sure to also provide text fields to ensure backward compatibility. Pass Designer automatically populates the relevant text fields when you select a specific type of pass template. If you include more fields than the pass can display, the additional fields don’t appear on the pass face, but are still  included in the pass information when viewed in the Wallet app.

![A screenshot of the text field component in Pass Designer.](https://docs-assets.developer.apple.com/published/33c65c2ac88deadedbb0a73ee9d56f1f/pass-designer-text-fields-overview%402x.png)

Semantic boarding passes and event passes are backward-compatible and fall back to using text fields. For more information, see [`Ensure backward compatibility`](creating-an-airline-boarding-pass-using-semantic-tags#Ensure-backward-compatibility.md) and [`Provide content for your pass fields`](defining-the-metadata-of-your-wallet-pass#Provide-content-for-your-pass-fields.md).

#### Upload Your Pass Bundle to Pass Builder

After you finish designing your pass, save the pass. Pass Designer creates a `.pkpasstemplate` bundle that you use to build, sign, and distribute your pass.

Pass Builder is a Swift on Server package with which you can programmatically create and distribute passes for Apple Wallet. The server package provides a type-safe API for building and signing Wallet Passes. Download the  Pass Builder package and documentation on [`GitHub`](https://developer.apple.comhttps://github.com/apple/pass-builder).

If your distribution model isn’t suitable for Pass Builder, you can decompress the contents of the `.pkpasstemplate` bundle and sign and build them using the method described in [`Building a Pass`](building-a-pass.md).

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/creating-a-pass-with-pass-designer)*