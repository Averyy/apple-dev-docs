# Preparing your interface for localization

**Framework**: Xcode

Find text in your app that needs translation and verify that your interface adapts to translated text.

#### Overview

Before you localize your app, use Xcode to identify nonlocalized strings in your interface and to verify whether your interface adjusts to the characteristics of localized strings.

##### Find Nonlocalized Strings

Nonlocalized strings are text that appears in your interface that Xcode won’t include in exported files. To find nonlocalized strings in your app, choose Product > Scheme > Edit Scheme in Xcode. In the sheet that appears, select the Run scheme action in the left column, and click Options on the right. Then select “Show non-localized strings” under Localization Debugging and click Close.

When you run your app, the nonlocalized strings appear in all caps.

![Screenshot of the Xcode Scheme editor with the Run scheme selected and showing the App Language and App Region menus in the detail area.](https://docs-assets.developer.apple.com/published/2f16e334b21b1b262df18b3d6a8e0f0b/preparing-your-interface-for-localization-1%402x.png)

##### Run Your App Using Pseudolanguages

You can test your interface with samples of text that exhibit the characteristics of different types of languages. In Xcode, choose Product > Scheme > Edit Scheme. In the sheet that appears, select the Run scheme action in the left column, and click Options on the right. Choose one of the pseudolanguages at the bottom of the App Language pop-up menu and click Close in the sheet.

| Pseudolanguage | Description |
| --- | --- |
| Double-Length Pseudolanguage | Doubles the length of localizable strings to test whether views adjust their size and position. |
| Right-to-Left Pseudolanguage | Simulates a right-to-left writing direction to test whether views flip accordingly. |
| Emotional Pseudolanguage | Simulates emojis in a string. |
| Accented Pseudolanguage | Adds accents to localizable strings to test whether views adjust to languages that have high and low ascenders. |
| Bounded String Pseudolanguage | Wraps strings to identify places where localized strings may appear truncated. |
| Right-to-Left Pseudolanguage With Right-to-Left Strings | Simulates a right-to-left writing direction, using right-to-left strings. |

## See Also

- [Preparing your app’s text for translation](preparing-your-apps-text-for-translation.md)
  Make your app’s text translatable by leveraging the localization APIs in the Foundation framework.
- [Preparing dates, currencies, and numbers for translation](preparing-dates-numbers-with-formatters.md)
  Ensure that dates, currencies, and numbers display correctly across multiple languages and locales by using formatters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/preparing-your-interface-for-localization)*