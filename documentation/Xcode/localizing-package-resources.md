# Localizing package resources

**Framework**: Xcode

Ensure that your Swift package provides localized resources for many locales.

#### Overview

Localizing the resources in your Swift package ensures its usefulness for as many developers as possible. Adopt localized resources early to avoid additional development costs later.

##### Declare a Default Localization

To localize your package’s resources, pass the optional [`defaultLocalization`](https://developer.apple.com/documentation/PackageDescription/Package/defaultLocalization) parameter to the package initializer in your package manifest. This example provides English as the default localization:

```swift
let package = Package(
    name: "MyLibrary",
    defaultLocalization: "en",
    platforms: [
    ],
    products: [
        // Products define the executables and libraries a package produces, and make them visible to other packages.
    ],
    dependencies: [
        // Dependencies declare other packages that this package depends on.
        // .package(url: /* package url */, from: "1.0.0"),
    ],
    targets: [
        // Targets are the basic building blocks of a package. A target can define a module or a test suite.
        // Targets can depend on other targets in this package, and on products in packages this package depends on.
)
```

When you declare a value for `defaultLocalization` in the package manifest, Xcode requires the package to contain localized resources.

> ❗ **Important**: When declaring a supported language, or naming directories that contain localized resources, use two-letter ISO 639-1 or three-letter ISO 639-2 language codes with optional region or script designators. See [`CFBundleDevelopmentRegion`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleDevelopmentRegion) for more information.

When declaring a supported language, or naming directories that contain localized resources, use two-letter ISO 639-1 or three-letter ISO 639-2 language codes with optional region or script designators. See [`CFBundleDevelopmentRegion`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleDevelopmentRegion) for more information.

##### Add Resources to Language Specific Directories

To use Xcode’s default localization mechanism, place localized resources in language-specific directories. A language-specific directory has a name that uses an ISO 639 language code and optional designators, followed by the `.lproj` suffix, and doesn’t contain subdirectories. For example, resources in the English language as it’s used in the United Kingdom reside in a directory named `en-GB.lproj`. By placing package resources in directories that end in `.lproj` and using ISO 639 language codes, Xcode can infer the language automatically.

Place your `.lproj` directories in a parent directory named `Resources` so you’ll recognize that it contains package resources.

When you build your Swift package, Xcode validates the package’s localized resources and displays warnings or errors to help prevent issues at runtime. For example, Xcode detects:

- Subdirectories within a `.lproj` directory.
- Missing resources for a locale.
- Duplicate, conflicting, or inaccessible resources.

The following screenshot shows the structure of a Swift package with localized resources.

![Screenshot of an expanded Swift package in Xcode’s Project navigator with localized resource directories residing in a parent directory named Resources.](https://docs-assets.developer.apple.com/published/5f537126d363d23c91d9f7c4ccca00f3/localizing-package-resources-1%402x.png)

##### Localize Storyboards and Interface Builder Files

If the Swift package includes storyboards or Interface Builder files as resources, adopt base internationalization to relieve localizers of the need to modify these files directly. To have Xcode automatically recognize base localization in the Swift package:

1. Declare a value for [`defaultLocalization`](https://developer.apple.com/documentation/PackageDescription/Package/defaultLocalization) in the package manifest.
2. Create a directory named, for example, `Resources,` for your localized resources.
3. Create a subdirectory named `Base.lproj` and place the package’s storyboards and Interface Builder files in it.
4. Place the `.lproj` directories for all supported languages in the `Resources` directory.

If you prefer to explicitly declare a resource for base internationalization, use the process rule and pass [`Resource.Localization.base`](https://developer.apple.com/documentation/PackageDescription/Resource/Localization/base) to it. For example, use the following to declare a `.xib` file that supports base internationalization:

`.process(”path/to/MyViewController.xib”, localization: .base)`

For more information about base internationalization, see [`Internationalizing the User Interface`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/InternationalizingYourUserInterface/InternationalizingYourUserInterface.html#//apple_ref/doc/uid/10000171i-CH3-SW2).

##### Access Localized Resources

Xcode recognizes localized resources in `.lproj` directories and automatically creates resource bundles. As a result, you can access localized resource files in your package’s code with APIs you may already know from app development. For example, use [`Foundation`](https://developer.apple.com/documentation/Foundation) to access a localized string at runtime:

`let localizedString = NSLocalizedString(”a_localized_string”, bundle: Bundle.module, comment: “a comment”)`.

Similarly, you can access localized image resources with [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage):

`UIImage(named: “image name”, in: .module, with: nil)`.

For more information, see [`Access a resource in code`](bundling-resources-with-a-swift-package#Access-a-resource-in-code.md).

## See Also

- [Creating a standalone Swift package with Xcode](creating-a-standalone-swift-package-with-xcode.md)
  Bundle executable or shareable code into a standalone Swift package.
- [Bundling resources with a Swift package](bundling-resources-with-a-swift-package.md)
  Add resource files to your Swift package and access them in your code.
- [Distributing binary frameworks as Swift packages](distributing-binary-frameworks-as-swift-packages.md)
  Make binaries available to other developers by creating Swift packages that include one or more XCFrameworks.
- [Developing a Swift package in tandem with an app](developing-a-swift-package-in-tandem-with-an-app.md)
  Add your published Swift package as a local package to your app’s project and develop the package and the app in tandem.
- [Organizing your code with local packages](organizing-your-code-with-local-packages.md)
  Simplify maintenance, promote modularity, and encourage reuse by organizing your app’s code into local Swift packages.
- [PackageDescription](../PackageDescription/PackageDescription.md)
  Create reusable code, organize it in a lightweight way, and share it across your projects and with other developers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/localizing-package-resources)*