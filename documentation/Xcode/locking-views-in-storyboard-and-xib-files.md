# Locking views in storyboard and XIB files

**Framework**: Xcode

Prevent changes to your Interface Builder files while localizing human-facing strings.

#### Overview

Before you export localizations, optionally lock the views in your storyboard and XIB files so you don’t inadvertently change localizable properties while you’re waiting for translations. Use this feature if you want to continue developing your app and avoid conflicts when importing localizations later. You can choose a locking level that controls the set of editable properties for each view.

##### Lock Views

You can set the locking level for a single view or for the entire user interface file. By default, views inherit their lock attribute from their parent view, and top-level views inherit their lock attribute from the user interface file. If you set a view’s lock attribute, it sets the lock attribute for all its descendant views.

To lock a single view, select the user interface file (files with a `.storyboard` or `.xib` filename extension) in the Project navigator, then select the view in Interface Builder. In the Identity inspector, choose a locking level from the Lock pop-up menu under Document:

![Screenshot of a view inspector showing the location of the Lock pop-up menu.](https://docs-assets.developer.apple.com/published/ec4a9d070923ee61715dc39ffd8f3d42/locking-views-in-storyboard-and-xib-files-1%402x.png)

For example, choose Localizable Properties while waiting for translations from localizers. If you import localizations and don’t want to make other changes inadvertently, choose Non-localizable Properties.

To lock all views, select the user interface file in the Project navigator, then choose a locking level from the Editor > Localization Locking menu.

##### Unlock Views

To unlock all views after you import localizations, select the user interface file in the Project navigator, then choose Editor > Localization Locking > Reset Locking Controls. To prevent any edits in a user interface file that would impact localized strings files, choose Editor > Localization Locking > Reset Locking Controls and then choose Editor > Localization Locking > Localizable Properties.

## See Also

- [Creating screenshots of your app for localizers](creating-screenshots-of-your-app-for-localizers.md)
  Share screenshots of your app with localizers to provide context for translation.
- [Exporting localizations](exporting-localizations.md)
  Provide the localizable files from your project to localizers.
- [Editing XLIFF and string catalog files](editing-xliff-and-string-catalog-files.md)
  Translate or adapt the localizable files for a language and region that you export from your project.
- [Importing localizations](importing-localizations.md)
  Import the files that you translate or adapt for a language and region into your project.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/locking-views-in-storyboard-and-xib-files)*