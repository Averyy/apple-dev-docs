# Bundling resources with a Swift package

**Framework**: Xcode

Add resource files to your Swift package and access them in your code.

#### Overview

If you declare a Swift tools version of 5.3 or later in your package manifest, you can bundle resources with your source code as Swift packages. For example, Swift packages can contain asset catalogs, storyboards, and so on.

##### Add Resource Files

Similar to source code, Xcode scopes resources to a target. Place resource files into the folder that corresponds with the target they belong to. For example, any resources for the `MyLibrary` target need to reside in `Sources/MyLibrary`. However, consider using a subfolder for resources to distinguish them from source files. For example, put all resource files into a directory named `Resources`, resulting in all of your resource files residing at `Sources/MyLibrary/Resources`.

To add resources to a Swift package, do any of the following:

- Drag them into the Project navigator in Xcode.
- From the File menu in Xcode, choose Add Files to .
- Use Finder or the Terminal app.

When you add a resource to your Swift package, Xcode detects common resource types for Apple platforms and treats them as a resource automatically. For example, you don’t need to make changes to your package manifest for the following resources:

- Interface Builder files; for example, XIB files and storyboards
- Core Data files; for example, `xcdatamodeld` files
- Asset catalogs
- `.lproj` folders you use to provide localized resources

If you add a resource file that Xcode doesn’t treat as a resource by default, you must configure it in your package manifest, as described in the next section.

##### Explicitly Declare or Exclude Resources

To add a resource that Xcode can’t handle automatically, explicitly declare it as a resource in your package manifest. The following example assumes that `text.txt` resides in `Sources/MyLibrary` and you want to include it in the `MyLibrary` target. To explicitly declare it as a package resource, you pass its file name to the target’s initializer in your package manifest:

```swift
targets: [
    .target(
        name: "MyLibrary",
        resources: [
            .process("text.txt")]
    ),
]
```

Note how the example code above uses the [`process(_:localization:)`](https://developer.apple.com/documentation/PackageDescription/Resource/process(_:localization:)) function. When you explicitly declare a resource, you must choose one of these rules to determine how Xcode treats the resource file:

If a file resides inside a target’s folder and you don’t want it to be a package resource, pass it to the target initializer’s `exclude` parameter. The next example assumes that `instructions.md` is a Markdown file that contains documentation, resides at `Sources/MyLibrary` and shouldn’t be part of the package’s resource bundle. This code shows how you can exclude the file from the target by adding it to the list of excluded files:

```swift
targets: [
    .target(
        name: "MyLibrary",
        exclude:["instructions.md"]
    ),
]
```

In general, avoid placing files that aren’t resources in a target’s source folder. If that’s not feasible, avoid excluding every file individually, place all files you want to exclude in a directory, and add the directory path to the array of excluded files.

##### Access a Resource in Code

When you build your Swift package, Xcode treats each target as a Swift module. If a target includes resources, Xcode creates a resource bundle and an internal static extension on [`Bundle`](https://developer.apple.com/documentation/Foundation/Bundle) to access it for each module. Use the extension to locate package resources. For example, use the following to retrieve the URL of a property list you bundle with your package:

`let settingsURL = Bundle.module.url(forResource: "settings", withExtension: "plist")`

> ❗ **Important**: Always use `Bundle.module` when you access resources. A package shouldn’t make assumptions about the exact location of a resource.

If you want to make a package resource available to apps that depend on your Swift package, declare a public constant for it. For example, use the following to expose a property list file to apps that use your Swift package:

`let settingsURL = Bundle.module.url(forResource: "settings", withExtension: "plist")`

## See Also

- [Creating a standalone Swift package with Xcode](creating-a-standalone-swift-package-with-xcode.md)
  Bundle executable or shareable code into a standalone Swift package.
- [Localizing package resources](localizing-package-resources.md)
  Ensure that your Swift package provides localized resources for many locales.
- [Distributing binary frameworks as Swift packages](distributing-binary-frameworks-as-swift-packages.md)
  Make binaries available to other developers by creating Swift packages that include one or more XCFrameworks.
- [Developing a Swift package in tandem with an app](developing-a-swift-package-in-tandem-with-an-app.md)
  Add your published Swift package as a local package to your app’s project and develop the package and the app in tandem.
- [Organizing your code with local packages](organizing-your-code-with-local-packages.md)
  Simplify maintenance, promote modularity, and encourage reuse by organizing your app’s code into local Swift packages.
- [PackageDescription](../PackageDescription/PackageDescription.md)
  Create reusable code, organize it in a lightweight way, and share it across your projects and with other developers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/bundling-resources-with-a-swift-package)*