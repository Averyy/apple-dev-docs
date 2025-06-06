# Creating width and device variants of strings

**Framework**: Xcode

Change a localized string for different interface widths and devices.

#### Overview

> ❗ **Important**: In Xcode 15 and later, string catalogs are the recommended way to create width and device variants of strings. In earlier versions of Xcode, use strings and `stringsdict` files. For more information about string catalogs, see [`Localizing and varying text with a string catalog`](localizing-and-varying-text-with-a-string-catalog.md).

In Xcode 15 and later, string catalogs are the recommended way to create width and device variants of strings. In earlier versions of Xcode, use strings and `stringsdict` files. For more information about string catalogs, see [`Localizing and varying text with a string catalog`](localizing-and-varying-text-with-a-string-catalog.md).

You can use a `.stringsdict` file to provide variants of a string for different view widths and for different devices. For example, display a different string for an iOS device in landscape or in portrait mode, or display a different string when your iPad app built with Mac Catalyst runs on a Mac.

A `.stringsdict` file is a property list that defines plural, width, and device variants of localizable strings. The `.stringsdict` file contains a dictionary of key-value pairs where the values are either a plural, width, or device rule.

The key for a rule is the string that you pass to [`Text`](https://developer.apple.com/documentation/SwiftUI/Text) structures, the [`NSLocalizedString`](https://developer.apple.com/documentation/Foundation/NSLocalizedString) macro, and similar APIs in your code. The rule can be a plural, width, or device rule that determines which formatted string the macro returns.

To create plural variants for formatted strings that contain amounts, see [`Localizing strings that contain plurals`](localizing-strings-that-contain-plurals.md).

##### Add a Strings Dictionary File to Your Project

To add a `.stringsdict` file to your project, choose File > New > File. In the sheet that appears, select the platform, enter `strings` in the Filter field, select Stringsdict File, and click Next. In the dialog that appears, enter a name for the file, choose a location, and click Create.

##### Provide String Variants for Different Widths

A  specifies variants for different available widths in the user interface. It contains a single dictionary with a single key-value pair. The key in the dictionary is `NSStringVariableWidthRuleType` and the value is another dictionary with key-value pairs for each variant. The key for a variant is a width and the value is a string.

In the following `.stringsdict` file, for the `hello `string in the code,` `the width variations are `1`, `22`, and `53`, and the values are `Hi`, `Hello`, and `Greetings and Salutations`:

```other
<plist version="1.0">
    <dict>
        <key>hello</key>
        <dict>
            <key>NSStringVariableWidthRuleType</key>
            <dict>
                <key>1</key>
                <string>Hi</string>
                <key>22</key>
                <string>Hello</string>
                <key>53</key>
                <string>Greetings and Salutations</string>
            </dict>
        </dict>
    </dict>
</plist>

```

For [`UILabel`](https://developer.apple.com/documentation/UIKit/UILabel) objects, the width is in em units that fit across the app window; otherwise, the width doesn’t have an associated unit.

The width rule defines variants for a range of widths:

- If the width is between two numerically sequential keys, the API returns the variant with the smaller key.
- If the width is less than all keys, the API returns the variant for the smallest key.

In the code above, if the width is `2`, the macro returns `Hi`. If the width is `55`, the macro returns `Hello`.

To get a variant for a specific width in your code, see the [`variantFittingPresentationWidth(_:)`](https://developer.apple.com/documentation/foundation/nsstring/1413104-variantfittingpresentationwidth) method.

##### Provide Device Specific String Variants

A  specifies a different string depending on the device. For example, your universal app may present different instructions to the user when running on an iOS device than when running on a Mac.

A device rule contains a single dictionary with a single key-value pair. The key is `NSStringDeviceSpecificRuleType` and the value is a dictionary with the following optional key-value pairs:

| Key | Description |
| --- | --- |
| appletv | The string to use on Apple TV. |
| applevision | The string to use on Apple Vision Pro. |
| applewatch | The string to use on Apple Watch. |
| ipad | The string to use on iPad. |
| iphone | The string to use on iPhone. |
| ipod | The string to use on iPod. |
| mac | The string to use on Mac. |

In the following `.stringsdict` file, when you pass `UserInstructions` as the string in your code, it returns `Tap here` when the app runs on an iPhone, `Click here` when it runs on a Mac, and `Press here` when it runs on an Apple TV:

```other
<plist version="1.0">
<dict>
    <key>UserInstructions</key>
    <dict>
        <key>NSStringDeviceSpecificRuleType</key>
        <dict>
            <key>iphone</key>
            <string>Tap here</string>
            <key>mac</key>
            <string>Click here</string>
            <key>appletv</key>
            <string>Press here</string>
        </dict>
    </dict>
</dict>
</plist>
```

## See Also

- [Localizing strings that contain plurals](localizing-strings-that-contain-plurals.md)
  Use a strings dictionary file to ensure correct localization of strings that contain language plurals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/creating-width-and-device-variants-of-strings)*