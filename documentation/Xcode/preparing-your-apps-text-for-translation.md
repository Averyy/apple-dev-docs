# Preparing your app’s text for translation

**Framework**: Xcode

Use localizable APIs to populate string catalogs automatically with your app’s user-facing text.

#### Overview

Wrap all user-facing text in localizable APIs that look up translations for strings based on the Language & Region settings on the device. Xcode also finds strings in localizable APIs and adds them to string catalog files for you at build time. Optionally, pass comments to localizable APIs to give localizers additional context. You can also pass table names to organize strings into separate string catalogs.

For more information on string catalogs, see [`Localizing and varying text with a string catalog`](localizing-and-varying-text-with-a-string-catalog.md).

##### Localize Text in Your View Hierarchy

When you use SwiftUI, all string literals of type [`LocalizedStringKey`](https://developer.apple.com/documentation/swiftui/localizedstringkey) within a view are automatically localizable.

For example, Xcode adds the following string literals in this code snippet to the default string catalog:

```swift
// Text made localizable with LocalizedStringKey.
Text("Title")
Label("Thanks for shopping with us!", systemImage: "bag")
    .font(.title)
HStack {
    Button("Clear Cart") {}
    Button("Checkout") {}
}
```

##### Create Localizable Strings

Use the [`init(localized:)`](https://developer.apple.com/documentation/swift/string/init(localized:)) initializer when creating [`String`](https://developer.apple.com/documentation/swift/string) and [`AttributedString`](https://developer.apple.com/documentation/foundation/attributedstring) objects that contain text you want to localize.

```swift
// General localizable text.
String(localized: "Add a description for your collection here.")
```

The initializer uses the string that you pass as the key to look up the translation based on the device settings.

To create localizable strings with different keys and values, use the  [`init(localized:defaultValue:options:table:bundle:locale:comment:)`](https://developer.apple.com/documentation/swift/string/init(localized:defaultvalue:options:table:bundle:locale:comment:)) initializer. Xcode uses the first parameter as the key and the second parameter as the default source string.

```swift
// Localizable string with a different key and value.
String(localized: "LIGHTING_KEY", defaultValue: "Lightbulbs")
```

For additional initializer options, see [`String`](https://developer.apple.com/documentation/swift/string). For apps targeting older platforms, use the [`NSLocalizedString`](https://developer.apple.com/documentation/foundation/nslocalizedstring) instead.

##### Add Comments to Your Localizable Strings

Add comments to give context and assist localizers when translating your text.

In SwiftUI, use the [`init(_:tableName:bundle:comment:)`](https://developer.apple.com/documentation/swiftui/text/init(_:tablename:bundle:comment:)) initializer of your [`Text`](https://developer.apple.com/documentation/swiftui/text) view and provide a comment with additional details.

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

In Swift, use the [`init(localized:table:bundle:locale:comment:)`](https://developer.apple.com/documentation/swift/string/init(localized:table:bundle:locale:comment:)) initializer:

```swift
// Localizable text with comments.
Text("Edit", comment: "The text label on a button to switch to editor mode.")
String(localized: "North America", comment: "The name of a continent.")
```

Alternatively, let Xcode generate comments for you from the context of your code. For more information, see [`Generate comments automatically`](localizing-and-varying-text-with-a-string-catalog#Generate-comments-automatically.md).

##### Organize Localizable Strings Into Tables

If the number of translations in your string catalog grows too large, consider using multiple string catalogs in one project. Then, when you build your app, Xcode adds the localizable strings to the catalog that you specify with a name.

In your code, choose which string catalog to use for each translation by passing the string catalog name to the localizable API using the `tableName` or `table` parameter.

```swift
// A SwiftUI localization example pointing to a specific string catalog.
Text("Explore", tableName: "Navigation")

// A general text localization example pointing to a specific string catalog.
String(localized: "Gorgeous mountain peaks!", table: "LandmarkCollectionData")
```

Use `String(localized:)` and `AttributedString(localized:)` initializers to initialize UIKit and AppKit controls as well.

##### Pass Localizable Strings with a Localizable Type

When defining or passing localizable text in your views, use the recommended type for passing strings in Swift [`LocalizedStringResource`](https://developer.apple.com/documentation/foundation/localizedstringresource).

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

##### Load Localizable Strings That Reside Outside of the Main Bundle

When localizable strings reside in another module, framework, or Swift Package, pass the [`bundle()`](https://developer.apple.com/documentation/foundation/bundle()) macro as the `bundle` parameter in localizable APIs to tell the system to look up the translation in the bundle associated with that target.

```swift
    // Localizable string within a framework.
    String(localized: "Songs", bundle: #bundle)
```

If you invoke this code in the app target, the macro returns the main bundle. Or you can explicitly pass `Bundle.main` which is also the default bundle.

Alternatively, you can create a bundle from a specific class that resides in that target using the [`init(for:)`](https://developer.apple.com/documentation/foundation/bundle/init(for:)) initializer and pass that as the `bundle` parameter to localizable APIs. For example, you can use this initializer in the framework code where the `BirdSongs` class resides.

```swift
// Localizable string within a framework.
String(localized: "Songs", bundle: Bundle(for: (BirdSongs.self)))
```

> ❗ **Important**: Avoid looking up strings from bundles you don’t own. Doing so may prevent automatic string extraction from properly working in the string catalog.

## See Also

- [Preparing your interface for localization](preparing-your-interface-for-localization.md)
  Find text in your app that needs translation and verify that your interface adapts to translated text.
- [Preparing dates, currencies, and numbers for translation](preparing-dates-numbers-with-formatters.md)
  Ensure that dates, currencies, and numbers display correctly across multiple languages and locales by using formatters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/preparing-your-apps-text-for-translation)*