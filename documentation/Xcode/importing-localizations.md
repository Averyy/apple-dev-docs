# Importing localizations

**Framework**: Xcode

Import the files that you translate or adapt for a language and region into your project.

#### Overview

After you localize the contents of a catalog, import the localizations back into your project. When you import localizations, Xcode updates the strings files in your project from the localized versions in the XLIFF file in the catalog.

##### Import Localizations Using Xcode

In the Project navigator, select the project, then choose Product > Import Localizations. In the import dialog that appears, select the Xcode Localization Catalog folder, and click Import. Xcode ingests the files and warns you if there are untranslated files.

In the sheet that appears, review the warnings and errors. In the left column, click the Issues View button in the toolbar, then select a message that appears below. In the comparison editor on the right, the imported catalog version of the file appears on the left and the current project file appears on the right.

![Screenshot of an import localization sheet where you review changes and errors.](https://docs-assets.developer.apple.com/published/8efcb565b78fd33c9aa7a05aeeceb1ba/importing-localizations-1%402x.png)

To review all the changes, click the File View button in the toolbar, and select a file in the navigator below. When you’re ready to import the files, click Import. Xcode updates the strings and `.stringsdict` files from the localized versions in the catalog. Xcode also updates any localizable resources and assets in an asset catalog.

##### Import Localizations Using Commands

You can also import the catalog with the `xcodebuild` command using the `-importLocalizations` argument:

`xcodebuild -importLocalizations -project <projectname> -localizationPath <dirpath>`

Be sure to test your app for the languages and regions in your project.

## See Also

- [Creating screenshots of your app for localizers](creating-screenshots-of-your-app-for-localizers.md)
  Share screenshots of your app with localizers to provide context for translation.
- [Exporting localizations](exporting-localizations.md)
  Provide the localizable files from your project to localizers.
- [Editing XLIFF and string catalog files](editing-xliff-and-string-catalog-files.md)
  Translate or adapt the localizable files for a language and region that you export from your project.
- [Locking views in storyboard and XIB files](locking-views-in-storyboard-and-xib-files.md)
  Prevent changes to your Interface Builder files while localizing human-facing strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/importing-localizations)*