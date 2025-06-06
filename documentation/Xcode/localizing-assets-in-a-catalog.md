# Localizing assets in a catalog

**Framework**: Xcode

Use asset catalogs to localize colors, images, symbols, watch complications, and more.

#### Overview

You use  to organize and manage different types of assets, such as images, sprites, textures, stickers, and data. Most types of assets can have multiple variations to support different device characteristics, including variations for the language and region settings.

You can localize certain types of asset catalogs and add localized versions of those assets directly to the catalog in Xcode.

The localizable asset types include:

- Color sets
- Image sets
- Symbol sets
- Watch complications
- Apple TV image stacks
- Sprite atlases

##### Add Asset Catalogs to Localizations

In the Project navigator, select the asset catalog, then select the asset you want to localize in the outline view of the editor area. Under Localization in the Attributes inspector, click Localize. Select the localizations you want to add the asset to. Xcode displays corresponding placeholder spaces in the editor area.

![Screenshot of the project editor showing the language wells of an asset catalog with a Color set selected.](https://docs-assets.developer.apple.com/published/6cf24ee3cb769c02575470cbdc19024c/localizing-assets-in-a-catalog-1%402x.png)

Either drop the localized assets in the spaces for localizations, or export the localizations and let the localizers add the assets later.

## See Also

- [Adding resources to localizations](adding-resources-to-localizations.md)
  Include more resources in the localizations you add to your project.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/localizing-assets-in-a-catalog)*