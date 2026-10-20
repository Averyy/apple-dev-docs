# package

**Framework**: Uniform Type Identifiers  
**Kind**: property  
**Role**: Type Property

A base type that represents a packaged directory.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static var package: UTType { get }
```

#### Discussion

Bundles differ from packages in that a bundle has an internal file hierarchy that [`CFBundle`](../../CoreFoundation/cfbundle.md) can read, while packages display to the user as if they were regular files. A single file system object can be a package and a bundle.

The identifier for this type is `com.apple.package`.

This type conforms to [`UTTypeDirectory`](../uttypedirectory.md).

## See Also

### Apple system base types
- [static var item: UTType](./item.md)
  A generic base type for most objects, such as files or directories.
- [static var content: UTType](./content.md)
  A base type that represents anything containing user-viewable content.
- [static var compositeContent: UTType](./compositecontent.md)
  A base type that represents a content format supporting mixed embedded content.
- [static var data: UTType](./data.md)
  A base type that represents any sort of byte stream, including files and in-memory data.
- [static var resolvable: UTType](./resolvable.md)
  A base type that represents a resolvable reference, including symbolic links and aliases.
- [static var bundle: UTType](./bundle.md)
  A base type that represents a directory that conforms to one of the bundle layouts.
- [static var pluginBundle: UTType](./pluginbundle.md)
  A base type that represents a bundle-based plug-in.
- [static var application: UTType](./application.md)
  A base type that represents a macOS, iOS, iPadOS, watchOS, and tvOS app.
- [static var sourceCode: UTType](./sourcecode.md)
  A base type that represents source code of any programming language.
- [static var bookmark: UTType](./bookmark.md)
  A base type that represents bookmark data.
- [static var log: UTType](./log.md)
  A base type that represents console log data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/package)*