# Preparing your app’s text for translation

**Framework**: Xcode

Make your app’s text translatable by leveraging the localization APIs in the Foundation framework.

#### Overview

Before the system can translate your app’s text, you need to prepare your app’s strings for translation by creating localizable versions of these strings using the `String(localized:)` and `AttributedString(localized:)` APIs found in the Foundation framework.

Localizable strings are user-facing strings you present to people at runtime. These strings signal to the system that they should be considered for translation, and thus added to your string catalog file. You then export those strings from your string catalog and send them to a localizer for translation or you edit the string catalog yourself and enter the translations directly there.

##### Make Your String Literals Localizable

String literals — strings created only with double quotes — aren’t localizable by themselves.

```swift
// An example of a nonlocalizable string literal.
let name = "Lightbulbs"
```

There’s no way for the system to know whether the string literal is a user-facing string in need of translation or simply a print statement there for debugging.

To make a string localizable, create a [`String`](https://developer.apple.com/documentation/Swift/String) object using the [`init(localized:)`](https://developer.apple.com/documentation/Swift/String/init(localized:)) initializer.

```swift
// Localizable string with the same key and value.
String(localized: "Lightbulbs")
```

This initializer takes the string literal passed in as a [`LocalizedStringResource`](https://developer.apple.com/documentation/Foundation/LocalizedStringResource) and assigns it to a key equal to the value of the string literal itself. Your string catalog uses this key to look up translations based on the language and locale of the user’s device, and then returns the translated value associated with that key. With this initializer, the key and underlying string value are the same. This means you can use the text of your development language as the keys for your translations.

To create localizable strings with different keys and values, use the  [`init(localized:defaultValue:options:table:bundle:locale:comment:)`](https://developer.apple.com/documentation/Swift/String/init(localized:defaultValue:options:table:bundle:locale:comment:)) initializer. This initializer assigns the first string literal as the string’s key and makes the second parameter the default string value.

```swift
// Localizable string with a different key and value.
String(localized: "LIGHTING_KEY", defaultValue: "Lightbulbs")
```

If someone else translates your strings, consider adding helpful comments to your string initializers to provide additional context about how and when the string displays.

```swift
// Localizable string with a comment providing additional context.
String(localized: "Lightbulbs", comment: "Label: The icon name displayed on the control screen")
```

If the number of translations in your string catalog grows too large, consider breaking the default catalog up into several smaller catalogs. Then specify which catalog a translation comes from using the `table` parameter in the [`init(localized:defaultValue:options:table:bundle:locale:comment:)`](https://developer.apple.com/documentation/Swift/String/init(localized:defaultValue:options:table:bundle:locale:comment:)) initializer.

```swift
// Localizable string referenced from the Greetings.xcstrings string catalog file.
String(localized: "Welcome", table: "Greetings")
```

Use `String(localized:)` and `AttributedString(localized:)` initializers to initialize UIKit and AppKit controls as well as general Swift structures containing variables of type [`String`](https://developer.apple.com/documentation/Swift/String).

```swift
struct Accessory {
     // Nonlocalizable string literal.
     let name: String
}
// Made localizable using the String(localized:) initializer.
Accessory(name: String(localized: "Welcome"))

// Localizable string passed into a UIKit control.
let label = UILabel()
label.text = String(localized: "Welcome")

// Localizable string passed into a AppKit UI control.
let textField = NSTextField()
textField.stringValue = String(localized: "Welcome")
```

##### Localize Text Automatically in Swiftui

SwiftUI views that accept string literals of type [`LocalizedStringKey`](https://developer.apple.com/documentation/SwiftUI/LocalizedStringKey) are automatically considered localizable. For example, the following strings are all automatically considered localizable in SwiftUI:

```swift
// Text made localizable with LocalizedStringKey.

Label("Thanks for shopping with us!", systemImage: "bag")
    .font(.title)
HStack {
    Button("Clear Cart") {}
    Button("Checkout") {}
}
```

To help translators better understand the context for a localized string, use the [`init(_:tableName:bundle:comment:)`](https://developer.apple.com/documentation/SwiftUI/Text/init(_:tableName:bundle:comment:)) initializer of your [`Text`](https://developer.apple.com/documentation/SwiftUI/Text) view and provide a comment with additional details.

```swift
// Provide additional localizable data with a `TextView`.

Stepper {
    Text("Increase or decrease the item quantity", comment: "Lets the shopper increase or decrease the quantity for an item in their shopping cart")
} onIncrement: {
    // ...
} onDecrement: {
    // ...
}
```

##### Pass Localizable Strings with a Localizable Type

When defining or passing localizable text in your views, use the recommended type for passing strings in Swift [`LocalizedStringResource`](https://developer.apple.com/documentation/Foundation/LocalizedStringResource).

```swift
// Localizable strings in SwiftUI.

struct CardView: View {
    let title: LocalizedStringResource
    let subtitle: LocalizedStringResource
    
    var body: some View {
        ZStack {
            Rectangle()
            VStack {
                Text(title)
                Text(subtitle)
            }
            .padding()
        }
    }
}

CardView(title: "Recent Purchases", subtitle: "Items you've ordered in the past week")
```

This type not only supports initialization using string literals, it also supports adding a comment, table name, or default value that’s different from the string key.

`LocalizedStringResource` also works for strings defined in general Swift code. For example, here’s a structure that defines a title of type `LocalizedStringResource`, which is then instantiated using a string literal and an instance of `LocalizedStringResource`, both localizable.

```swift
struct UserAction {
   let title: LocalizedStringResource
}

// Localizable text created with a string literal.
let action = UserAction(title: "Order items")

// Localizable text created with a `LocalizedStringResource`.
let actionWithComment = UserAction(title: LocalizedStringResource("Order items", comment: "Action title displayed in button"))
```

##### Define and Load Localizable Strings From Within Your Framework

If you define the strings that you want to localize in another module, framework, or Swift Package, use the `bundle` argument in their definition. For example, say you want to modularize your project and you create a framework called `BirdFinderUtilities`. To look up a localizable string from within that framework:

1. Identify the name of a class within the framework (in this case, `BirdSongs`).
2. Pass that class into an instance of [`Bundle`](https://developer.apple.com/documentation/Foundation/Bundle) using the [`init(for:)`](https://developer.apple.com/documentation/Foundation/Bundle/init(for:)) initializer.
3. Use that `Bundle` to look up the localizable string.

```swift
// Localizable string within a framework.
String(localized: "Songs", bundle: Bundle(for: (BirdSongs.self)))

// Localizable string within a framework in SwiftUI.
Text("Songs", bundle: Bundle(for: (BirdSongs.self)))

// Localizable string within a framework for a `LocalizedStringResource`.
LocalizedStringResource("Songs", bundle: .forClass(BirdSongs.self), comment: "Headline above the name of the song currently playing.")
```

> ❗ **Important**: Avoid looking up strings from bundles you don’t own. Doing so may prevent automatic string extraction from properly working in the string catalog.

## See Also

- [Preparing your interface for localization](preparing-your-interface-for-localization.md)
  Find text in your app that needs translation and verify that your interface adapts to translated text.
- [Preparing dates, currencies, and numbers for translation](preparing-dates-numbers-with-formatters.md)
  Ensure that dates, currencies, and numbers display correctly across multiple languages and locales by using formatters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/preparing-your-apps-text-for-translation)*