# Giving hints to help learners solve problems

**Framework**: Swift Playgrounds

Add hints, spoilers, and solutions to a page to help teach the material.

#### Overview

Learners sometimes become stuck when working through a challenge or learning assessment. Try to anticipate where learners are likely to become stuck when going through your playground book, and provide hints to help them.

Hints are disclosed after the learner taps the Hint button in a page’s live view.

![A screenshot highlighting the Hint button in the bottom-right corner of a playground page’s live view.](https://docs-assets.developer.apple.com/published/ea261f418891119731edd16743d7e990/giving-hints-to-help-learners-solve-problems-1%402x.png)

##### Add Hints By Using a Property List

Add hints to your playground page by creating a property list at the following path, alongside the rest of the resources for the page:

`.playgroundbook/Contents/``.playgroundchapter/Pages/``.playgroundpage/PrivateResources/Hints.plist`

The root key for the hints property list is named `Hints`, and it must contain an array of dictionaries. Hints are shown in Swift Playgrounds in the same order as they appear in this array.

##### Add Keys to the Dictionaries

Add the following keys in each dictionary in the hints array:

Don’t include both the `Content` and `FileReference` keys in the same dictionary. You can use either one, but not both, because they both serve the role of provider of the hint text.

You can use markup to format hint text. For more information, see [`Markup Formatting Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_markup_formatting_ref/index.html#//apple_ref/doc/uid/TP40016497).

##### Create Hints for Various Contexts

Create hints, spoilers, and solutions to suit the needs of each of your playground pages. The example below shows each of the forms a hint can take.

```javascript
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Hints</key>
    <array>
        <dict>
            <key>Content</key>
            <string>Look at the `characters` property of `String`.</string>
        </dict>
        <dict>
            <key>Content</key>
            <string>This hint is initially hidden by a spoiler button.</string>
            <key>SpoilerButtonTitle</key>
            <string>Show Spoiler</string>
        </dict>
        <dict>
            <key>FileReference</key>
            <string>OutOfBandHint.txt</string>
        </dict>
        <dict>
            <key>FileReference</key>
            <string>OutOfBandHintWithSpoilerButton.txt</string>
            <key>SpoilerButtonTitle</key>
            <string>Show Spoiler</string>
        </dict>
    </array>
</dict>
</plist>
```

Here’s how the hints property list looks when displayed as a popover in the playground page’s live view:

![A screenshot showing three hints. The top hint uses the “Content” key, the middle hint uses a spoiler sheet to hide the hint initially, and the bottom hint uses text from a file.](https://docs-assets.developer.apple.com/published/fea67cbe8a6a18414895a56be83b4c98/giving-hints-to-help-learners-solve-problems-2%402x.png)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift-playgrounds/giving-hints-to-help-learners-solve-problems)*