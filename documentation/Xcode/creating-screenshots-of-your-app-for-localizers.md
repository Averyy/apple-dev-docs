# Creating screenshots of your app for localizers

**Framework**: Xcode

Share screenshots of your app with localizers to provide context for translation.

#### Overview

When running UI tests of your localizations, you can generate screenshots to include in the exported localization folders that you give to localizers. The screenshots provide context for the localizable strings and resources in the interface. You can generate screenshots from your project’s test plans or Test scheme.

To include the screenshots in the Xcode Localization Catalog (a folder with a `.xcloc` file extension), see [`Exporting localizations`](exporting-localizations.md).

##### Create a Test Plan

If you add many localizations to your project, test plans are ideal for generating screenshots because you can create a configuration for each. A test plan (a file with a `.xctestplan` file extension) specifies which tests to run and how to run them one or more times.

You can use an existing test plan or create a new one. To add a test plan, choose Product > Test Plan > New Test Plan in Xcode. Enter a name for the test plan and click Create.

If you want to convert your project from using schemes to test plans, choose Product > Scheme > Convert Scheme to use Test Plans, select “Create Test Plan from scheme”, then click Convert. In the next dialog, you can change the name of the test plan, then click Save. The test plan appears in the editor area.

##### Add Localization Configurations

Add a configuration for each localization to your test plan. In the Project navigator, select the test plan, then click Configurations. On the left, click the Add button (+) at the bottom. Select the new configuration that appears and enter a name for the localization.

Edit the configuration file for the localization test. Under Localization, set the Application Language and Application Region settings to the corresponding language and region for the localization. Under UI Testing, switch Localization Screenshots from Off to On.

![Screenshot of the project editor with a test plan selected in the navigator and a configuration called Right-to-Left selected in the detail area, showing the location of the Application Language and Application Region under Localization.](https://docs-assets.developer.apple.com/published/1539767c41a46cd1bd0afbb817c4c0a8/creating-screenshots-of-your-app-for-localizers-1%402x.png)

##### Run Tests to Generate Screenshots

Next time you run your tests (choose Product > Test), Xcode saves the screenshots for each localization to disk. In the Test navigator, next to every screenshot, Xcode includes a property list (Localizable Strings Info) that maps the strings to the frame where the string appears in the screenshot. The property list includes the string IDs (that appear in the exported XLIFF file) and frame locations.

##### Generate Screenshots Using Schemes

Alternatively, if you don’t use test plans, you can make similar edits to the Test scheme to generate screenshots. In Xcode, choose Product > Scheme > Edit Scheme, click the Test scheme, then click Options. Choose the language and region from the pop-up menus, then select “Gather screenshots for localization.”

## See Also

- [Exporting localizations](exporting-localizations.md)
  Provide the localizable files from your project to localizers.
- [Editing XLIFF and string catalog files](editing-xliff-and-string-catalog-files.md)
  Translate or adapt the localizable files for a language and region that you export from your project.
- [Importing localizations](importing-localizations.md)
  Import the files that you translate or adapt for a language and region into your project.
- [Locking views in storyboard and XIB files](locking-views-in-storyboard-and-xib-files.md)
  Prevent changes to your Interface Builder files while localizing human-facing strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/creating-screenshots-of-your-app-for-localizers)*